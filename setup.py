# coding=utf-8
# !/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    print 'No setuptools installed, use distutils'
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='python_project_skeleton',
    packages=[
        'python_project_skeleton',
        'python_project_skeleton.tools',
        'python_project_skeleton.tests'
    ],
    package_dir={
        'python_project_skeleton': 'src/python_project_skeleton',
        'python_project_skeleton.tools': 'src/python_project_skeleton/tools',
        'python_project_skeleton.tests': 'src/python_project_skeleton/tests'
    },
    package_data={'': [
        'src/python_project_skeleton/main.ini'
    ]},
    data_files=[
        ('', [
            'src/python_project_skeleton/main.ini'
        ]),
    ],
    test_suite="python_project_skeleton.tests",
    include_package_data=True,
    install_requires=required,
    version='1.0',
    description='python project skeleton',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='http://github.com/paoolo/python-project-skeleton',
    download_url='http://github.com/paoolo/python-project-skeleton',
    keywords=[
        'skeleton'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description='''\
'''
)
