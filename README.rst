==========================================
A toolbox to work with R projects on Renku
==========================================

.. image:: https://img.shields.io/badge/license-apache2-brightgreen.svg
   :target: https://github.com/auwerxlab/renku-r-tools/blob/master/LICENSE

.. image:: https://img.shields.io/github/v/release/auwerxlab/renku-r-tools
   :target: https://github.com/auwerxlab/renku-r-tools/releases

.. image:: https://img.shields.io/pypi/v/renku-r-tools
   :target: https://pypi.python.org/pypi/renku-r-tools

.. image:: https://readthedocs.org/projects/renku-r-tools/badge/?version=latest
   :target: https://renku-r-tools.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Renku-r-tools is a small python package that provides a CLI to setup R projects on Renku.

Features:

- Link the packrat libraries of a R project to another location. This is particularly useful when packrat libraries are located on the docker image.

Installation
============

The latest release is available on PyPI and can be installed using ``pip``:

::

    $ pip install renku-r-tools

Isolated environments using ``pipx``
------------------------------------

Install and execute renku-r-tools in an isolated environment using ``pipx``.

`Install pipx <https://github.com/pipxproject/pipx#install-pipx>`_
and make sure that the ``$PATH`` is correctly configured.

::

    $ python3 -m pip install --user pipx
    $ pipx ensurepath

Once ``pipx`` is installed use following command to install ``renku-r-tools``.

::

    $ pipx install renku-r-tools
    $ which renku-r-tools
    ~/.local/bin/renku-r-tools

Usage
=====

The latest documentation is available on `https://readthedocs.org <https://renku-r-tools.readthedocs.io/en/latest/>`_.