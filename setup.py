from setuptools import find_packages, setup

release_version = '0.0.4'

setup(
    name = 'renku-r-tools',
    version = release_version,
    description = 'A toolbox to work with R projects on Renku',
    long_description = open('README.rst').read(),
    long_description_content_type = 'text/x-rst',
    license = 'Apache License 2.0',
    author = 'Laboratory of Integrative System Physiology (LISP) at EPFL',
    author_email = 'alexis.rapin@epfl.ch',
    url = 'https://github.com/auwerxlab/renku-r-tools',
    download_url = 'https://github.com/auwerxlab/renku-r-tools/archive/v' + release_version + '.tar.gz',
    packages = find_packages(),
    install_requires = [
        'click>=7.0',
    ],
    entry_points = {
        'console_scripts': [
            'renku-r = renku_r_tools.__main__:cli'
        ]
    },
)
