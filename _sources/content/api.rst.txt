API Documentation
-----------------

In the following sections, we demonstrate how to use the ``sphinx.ext.autodoc``
extension to import the docstrings from a Python module into this documentation
page.

Utilities
~~~~~~~~~

First, we can pull in the module level docstring for :class:`agu_oss.utilities`
with the following command::

  .. automodule:: agu_oss.utilities

.. automodule:: agu_oss.utilities

Then we can auto include the dosctrings for specific functions in that module
such as::

  .. autofunction:: agu_oss.divide

  .. autofunction:: agu_oss.moving_average

.. autofunction:: agu_oss.divide

.. autofunction:: agu_oss.moving_average


Cleaning
~~~~~~~~

.. automodule:: agu_oss.clean_data

.. autofunction:: agu_oss.open_and_clean
