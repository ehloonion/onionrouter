OnionRouter
===========


.. image:: https://img.shields.io/pypi/v/onionrouter.svg
        :target: https://pypi.python.org/pypi/onionrouter

.. image:: https://img.shields.io/travis/ehloonion/onionrouter.svg
        :target: https://travis-ci.org/ehloonion/onionrouter

.. image:: https://readthedocs.org/projects/onionrouter/badge/?version=latest
        :target: https://onionrouter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ehloonion/onionrouter/shield.svg
     :target: https://pyup.io/repos/github/ehloonion/onionrouter/
     :alt: Updates


Python Onion Routed Mail Deliveries

* Free software: GNU General Public License v3
* Documentation: https://onionrouter.readthedocs.io.

What is this ?
--------------

This python script implements dynamic SRV lookups to be fed to postfix as TCP transport map replies. More information on mail delivery over onion services can be found at https://github.com/ehloonion/onionmx.

An alternative implementation in Go can be found at https://git.autistici.org/ale/postfix-onion-transport


Features
--------
* Interactive/Client/Daemon/Debug modes
* Configurable SRV lookup string
* Domain whitelisting
* Lazy rerouting using static mappings

How to run
----------

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

Configuration and other options
-------------------------------
* Copy or update the onionrouter.ini file and with your settings (reference file is in onionrouter/configs folder if you cloned the git repo or in /etc/onionrouter/ if you installed the package)
* Edit the configuration file
    * Under the **DOMAIN** section replace the value of the **hostname** key with your local domain to be whitelisted from lookups. To add multiple local domains, separate them with comma ','
    * Under the **RESOLVER** section put in the **resolver_ip** field your preferred resolver (default is 127.0.0.1). To use multiple resolvers, separate them with comma ','
    * Under the **RESOLVER** section put in the **resolver_port** field the port that your resolver listens to (default is 53)

onionrouter by default queries the destination domain for a specific SRV record, *_onion-mx._tcp.* and if it finds a .onion address in the reply it gives it back to postfix to be used by the smtptor service defined in master.cf. If no valid SRV record is found the mail is passed to smtp service. This gives us dynamic SRV lookups that lead to SMTP over onion addresses!

* To change the SRV record the scripts looks for, edit the config file mentioned above and change under the **DNS** section the **srv_record** field with the SRV record you have setup (default is _onion-mx._tcp.)
* To change the service that will be used when a .onion address is found, edit the config file mentioned above and change under the **REROUTE** section the **onion_transport** field with the service you want to be used (default is smtptor)
* To *blacklist/ignore* domains in case you have a custom routing rule, or a black list of domains, add those domains under the **IGNORED** section in the **domains** field. For multiple domains, separate them with comma ','.

Execution options
-----------------
onionrouter by default runs in server mode and acts as a daemon waiting for connections.

Daemon mode can be configured with the following options:

* **--port PORT** or **-p PORT** to define port for daemon to listen (default 23000)
* **--host HOST** or **-l HOST** to define host for daemon to listen (default 127.0.0.1)

Other options are supported as well:

* **--mappings MAPPINGS** to define absolute path to static mappings folder (everything inside will be parsed as a yaml file) or yaml file
* **--config CONFIG** to define the absolute path to config folder (must contain a onionrouter.ini file inside) or config file
* **--client** or **-c** to connect to the daemon and interact with. Use the host and port options to define the options for the connection to the daemon
* **--debug** or **-d** to start the daemon in debug mode. In this mode, daemon will also print (besides replying) the queries and answers Use the host and port options to define the options for the daemon
* **--interactive** or **-i** to run onionrouter in interactive input mode for debugging or testing purposes without daemon

How to run
----------
Currently onionrouter runs in the foreground, so you need to either run it via a systemd unit file or through some other daemonizing method (eg screen/tmux/etc). An example systemd unit is included in the *contrib* directory, modify it to your liking.

.. code-block:: console

   $ ./onionrouter_run --config /srv/onionrouter/onionrouter/configs/onionrouter.ini --mappings /srv/onionrouter/onionrouter/configs/map.yml -p 23002 --debug
