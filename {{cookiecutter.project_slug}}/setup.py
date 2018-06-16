#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file, open('HISTORY.rst') as history_file:
    long_description = (readme_file.read() + "\n\n" + history_file.read())

install_requires = [
{%- if cookiecutter.command_line_interface|lower == 'click' %}
    'click>=6.0',
{%- endif %}
    # TODO: put package requirements here
]

setup_requires = [
{%- if cookiecutter.use_pytest == 'y' %}
    'pytest-runner',
{%- endif %}
    # TODO({{ cookiecutter.github_username }}): put setup requirements (distutils extensions, etc.) here
]

tests_requires = [
{%- if cookiecutter.use_pytest == 'y' %}
    'pytest',
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
    'click>=6.0',
{%- endif %}
    # TODO: put package test requirements here
]

{%- if cookiecutter.license != "NOT_OPEN_SOURCE" %}
    {%- set license = ('license' | pimport).find(cookiecutter.license) %}
{%- endif %}

setup(
    name='{{ cookiecutter.project_short_name }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_name }}',
    packages=find_packages(),
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_short_name }}={{ cookiecutter.project_slug }}.__main__:main'
        ]
    },
    {%- endif %}
    include_package_data=True,
    install_requires=install_requires,
    {%- if license is defined %}
    license="{{ license.python.split(':')[-1].strip() }}",
    {%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }},{{ cookiecutter.project_short_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        {%- if license is defined %}
        '{{ license.python }}',
        {%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=tests_requires,
    setup_requires=setup_requires,
)
