{% set is_open_source = cookiecutter.license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_short_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_short_name }}

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_name }}.svg
    :target: https://travis-ci.org/starofrainnight/{{ cookiecutter.project_short_name }}.html

.. image:: https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_name }}?svg=true
    :target: https://ci.appveyor.com/project/starofrainnight/{{ cookiecutter.project_short_name }}

{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* License: {{ cookiecutter.license }}
* Documentation: https://{{ cookiecutter.project_short_name | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `PyPackageTemplate`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`PyPackageTemplate`: {{ cookiecutter._template_url }}

