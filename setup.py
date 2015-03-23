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
    name='tornado_project_skeleton',
    packages=[
        'tornado_project_skeleton',
        'tornado_project_skeleton.tools',
        'tornado_project_skeleton.tests'
    ],
    package_dir={
        'tornado_project_skeleton': 'src/tornado_project_skeleton',
        'tornado_project_skeleton.tools': 'src/tornado_project_skeleton/tools',
        'tornado_project_skeleton.tests': 'src/tornado_project_skeleton/tests'
    },
    package_data={'': [
        'src/tornado_project_skeleton/main.ini'
    ]},
    data_files=[
        ('', [
            'src/tornado_project_skeleton/main.ini'
        ]),
    ],
    test_suite="tornado_project_skeleton.tests",
    include_package_data=True,
    install_requires=required,
    version='1.0',
    description='Tornado project skeleton',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='http://github.com/paoolo/tornado-project-skeleton',
    download_url='http://github.com/paoolo/tornado-project-skeleton',
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
