#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file, open('HISTORY.rst') as history_file:
    long_description = (readme_file.read() + "\n\n" + history_file.read())

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}
    'click>=6.0',
    {%- endif % }
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

{%- if cookiecutter.license != "Not open source" % }
    {%- set license = ('license' | pimport).find(cookiecutter.license) % }
{%- endif % }

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(),
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:main'
        ]
    },
    {%- endif %}
    include_package_data=True,
    install_requires=requirements,
    {%- if license is defined %}
    license="{{ license.python.split(':')[-1].strip() }}",
    {%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
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
    ],
    test_suite='tests',
    tests_require=test_requirements
)
