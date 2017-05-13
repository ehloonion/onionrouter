.. highlight:: shell

There are two ways to install onionrouter, automatically using pip or cloning the repository and manually installing the needed packages on Debian. Currently onionrouter has only been tested on Debian Jessie.

Using pip
^^^^^^^^^
.. code-block:: console

   $ sudo pip install onionrouter

Test functionality
""""""""""""""""""
.. code-block:: console

   $ onionrouter --help

Manual installation on Debian Jessie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clone repository
"""""""""""""""""""""""
.. code-block:: console

   $ git clone https://github.com/ehloonion/onionrouter.git

Install Debian packages
"""""""""""""""""""""""
onionrouter has only been tested on Debian Jessie. Install the following packages:

.. code-block:: console

   $ sudo apt install python-dnspython python-yaml

Test functionality
""""""""""""""""""
.. code-block:: console

   $ cd onionrouter
   $ ./onionrouter_run --help


.. _Github repo: https://github.com/ehloonion/onionrouter
.. _tarball: https://github.com/ehloonion/onionrouter/tarball/master
