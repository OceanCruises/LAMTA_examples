# Notebooks

::::{grid} 1 2 2 3
:gutter: 2

{% set data = yaml_load_file("gallery.yml") %}
{% for item in data %}

:::{card}
:link: {{ item.website or item.notebook }}
{% if item.image %}:img-top: {{ item.image }}{% endif %}

**{{ item.name }}**

{{ item.summary }}

:::

{% endfor %}
::::
