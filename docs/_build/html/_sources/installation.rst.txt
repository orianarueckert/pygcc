Installation
================

pygcc is available on `PyPi <https://pypi.org/project/pygcc/>`_, and can be downloaded with pip:

.. code-block:: bash

   pip install --user pygcc


.. note:: With pip, a user-level installation is generally recommended (i.e. using the
          :code:`--user` flag), especially on systems which have a system-level
          installation of Python (including `*.nix`, WSL and MacOS systems); this can
          avoid some permissions issues and other conflicts. For detailed information
          on other pip options, see the relevant
          `docs <https://pip.pypa.io/en/stable/user_guide>`__.
          pygcc is not yet packaged for Anaconda, and as such
          :code:`conda install pygcc` will not work.


Upgrading pygcc
--------------------

New versions of pygcc are released frequently. You can upgrade to the latest edition
on `PyPi <https://pypi.org/project/pygcc/>`_ using the :code:`--upgrade` flag:

.. code-block:: bash

   pip install --upgrade pygcc



