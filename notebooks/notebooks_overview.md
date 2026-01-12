# Notebooks

::::{grid} 1 2 2 3
:gutter: 2

{% for item in data %}

:::{grid-item-card} {{ item.name }}
:link: {{ item.website or item.notebook }}
:shadow: md

{{ item.summary }}

:::

{% endfor %}

::::