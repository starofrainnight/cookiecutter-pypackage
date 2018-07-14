#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join(
            '{{ cookiecutter.project_slug }}', '__main__.py')
        remove_file(cli_file)

    if 'NOT_OPEN_SOURCE' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')

    # Generate namespace directory and move the package directory into namespace
    # directory.
    "{{ cookiecutter.project_is_namespace_package }}"
    "{{ cookiecutter.project_ns_namespace }}"
    "{{ cookiecutter.project_ns_package }}"
    if 'y' in '{{ cookiecutter.project_is_namespace_package.lower() }}':
        temp_dst = os.path.join(PROJECT_DIRECTORY, '__post_gen_ns_dir')
        src = os.path.join(
            PROJECT_DIRECTORY,
            '{{ cookiecutter.project_ns_package }}')
        ns_dir = os.path.join(
            PROJECT_DIRECTORY,
            '{{ cookiecutter.project_ns_namespace }}')

        dst = os.path.join(ns_dir, '{{ cookiecutter.project_ns_package }}')

        # In case the namespace same with package name.
        shutil.move(src, temp_dst)

        os.makedirs(ns_dir, exist_ok=True)

        shutil.move(temp_dst, dst)

        with open(os.path.join(ns_dir, '__init__.py'), 'w') as f:
            content = """__import__('pkg_resources').declare_namespace(__name__)\n"""
            f.write(content)
