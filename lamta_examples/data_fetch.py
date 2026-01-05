from pathlib import Path
import os
import tarfile
import pooch

BASE_URL = "https://github.com/OceanCruises/LAMTA_examples/releases/download/data-v0.1/"
CACHE_NAME = "lamta_examples"

REGISTRY = {
    "bathymetry_etopo_medsea.tar.gz":
        "sha256:4C98D6BCC1E0E04D5E877BC020A5E685197A031FE55FAEBF19DA9BE266AD1C66",
    "sst_ostia_slstr_samples.tar.gz":
        "sha256:D1D7D0F9E88A765727C664445DDEF8B86E4A4FF6B375E5445CF3A9F0DC1F7D68",
    "altimetry_cmems_duacs_europe_20230606-20230608.tar.gz":
        "sha256:7185E4E482E6AF18362D9A8E150F14F8A00AA8C6EDFB8EDC874F82DA1006B60D",
    "altimetry_nrt_europe_202305.tar.gz":
        "sha256:E85C2A8160E9F39139E8FC530603ED1BB0D89194290602C8649DAEA5992A9EF0",
    "altimetry_nrt_global_20220909-20220929.tar.gz":
        "sha256:45E6BBDB0A35452E0E2D7B085FD314CCD0A24489A0EB6DD4D7490644B1062EF6",
    "swot_l3_lr_ssh_expert_20230606-20230609.tar.gz":
        "sha256:F1CAD06C7E03861EB392B434FE84E9A9BE5DE05C2BDF186BC7CDE9F5E9DF00B4",
}


def _cache_dir():
    if os.environ.get("READTHEDOCS") == "True":
        return Path(".cache") / CACHE_NAME
    return Path(pooch.os_cache(CACHE_NAME))

def repo_root() -> Path:
    # lamta_examples/ is at repo_root/lamta_examples/
    return Path(__file__).resolve().parents[1]


def ensure_dataset(asset: str, data_dir: Path | None = None) -> Path:
    if data_dir is None:
        data_dir = repo_root() / "data"
    data_dir.mkdir(exist_ok=True)

    sentinel = data_dir / f".{asset}.ready"
    if sentinel.exists():
        return data_dir

    p = pooch.create(
        path=_cache_dir(),
        base_url=BASE_URL,
        registry=REGISTRY,
    )

    archive = Path(p.fetch(asset))

    with tarfile.open(archive, "r:gz") as tf:
        tf.extractall(path=data_dir)

    sentinel.write_text("ok\n")
    return data_dir
