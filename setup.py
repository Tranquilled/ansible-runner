#!/usr/bin/env python

# Copyright (c) 2018 Red Hat, Inc.
# All Rights Reserved.
import re
import subprocess

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


def version(default):
    try:
        process = subprocess.check_output(['git', 'describe', '--tags'], text=True)
        commit = re.match(r'([\d\.]+)[\d-]*([a-g0-9-]*)', process)
        if commit:
            if len(commit.group(2)) > 0:
                return commit.group(2)[1:]
            else:
                return commit.group(1)
        else:
            return default
    except (SystemError, OSError):
        return default


setup(
    name="ansible-runner",
    version="2.0.0",
    author='Red Hat Ansible',
    url="https://github.com/ansible/ansible-runner",
    license='Apache',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'psutil',
        'pexpect>=4.5',
        'python-daemon',
        'PyYAML',
        'six',
    ],
    zip_safe=False,
    entry_points={
        'receptor.worker': 'ansible_runner = ansible_runner.receptor_plugin',
        'console_scripts': [
            'ansible-runner = ansible_runner.__main__:main'
        ]
    }
)
