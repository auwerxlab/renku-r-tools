==========================================
A toolbox to work with R projects on Renku
==========================================

.. image:: http://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: https://github.com/auwerxlab/renku-r-tools/blob/master/LICENSE
.. image:: https://img.shields.io/github/v/release/auwerxlab/renku-r-tools
   :target: https://github.com/auwerxlab/renku-r-tools/releases

Renku-r-tools is a small python package that provides a CLI to setup R projects on Renku.

Features:

- Link the packrat libraries of a R project to another location. This is useful when packrat libraries are located on the docker image.

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

renku-r ln_packrat_lib
----------------------

::

    Usage: renku-r ln-packrat-lib [OPTIONS]

      Link packrat libraries to another location.

    Options:
      -p, --proj_dir TEXT  R project main directory path. Use absolute path.
                           [required]
      -s, --source TEXT    Main directory path of the new packrat libraries
                           source. Use absolute path.  [default:
                           /home/rstudio/packrat; required]
      --help               Show this message and exit.


Example:

::

    $ renku-r ln_packrat_lib -p <your_R_project_main_directory_path> -s <your_new_packrat_library_path>

