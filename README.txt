.. contents::

Introduction
============

This package extends the functionality of the templer code generation system. It
builds upon the functionality of templer.core_, and depends on that package.
This package provides basic support for creating buildouts and buildout recipes
using zc.buildout_. Included are packages for basic buildout skeletons and
buildout recipes.

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _zc.buildout: http://www.buildout.org/

Creating Packages
-----------------

As with the parent package, templer.core, creating packages using
templer.buildout templates is accomplished by using the ``templer`` script. The
script is invoked thus::

    templer basic_buildout

This will create a basic buildout skeleton, containing the zc.buildout 
bootstrap.py file and a buildout.cfg file which may be edited to taste.

Included Templates
------------------

basic_buildout
    This creates a basic skeleton for a buildout.

recipe
    This creates a skeleton for a buildout recipe for use with zc.buildout

Other Functions
---------------

The ``templer`` script provides a number of other functions, these are described
in full on the index page for templer.core_ at PyPI_

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _PyPI: http://pypi.python.org/pypi
