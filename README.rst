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


Features
--------
* Interactive/Client/Debug/Daemon modes
* Configurable SRV lookup string
* Lazy rerouting using static mappings

How to run
----------
**If you clone the git repo**

::

    pip install -r requirements.txt
    python onionrouter_run.py --help

**If you install the package (pip or other way of installing the package)**

::

    onionrouter --help

Configuration and other options
-------------------------------
* Copy or update the onionrouter.ini file and with your settings (reference file is in config folder if you cloned the git repo or in /etc/onionrouter/ if you installed the package)
* Edit the config
  * under the DOMAIN section the hostname field with your local domain
  * under the RESOLVER section the resolver_ip field with your resolver (default is 127.0.0.1). To use multiple resolvers, seperate them with comma ,
  * under the RESOLVER section the resolver_port field with the port your resolver listens (default is 53)

The script queries the destination domain for a specific SRV record, _onion-mx._tcp. and if it finds a .onion address in the reply it gives it back to postfix to be used by the smtptor service defined in master.cf. If no valid SRV record is found the mail is passed to smtp service. This gives us dynamic SRV lookups that lead to SMTP over onion addresses!

* To change the SRV record the scripts looks for, edit the config file mentioned above and change under the DNS section the srv_record field with the SRV record you have setup (default is _onion-mx._tcp.)
* To change the service that will be used when a .onion address is found, edit the config file mentioned above and change under the REROUTE section the onion_transport field with the service you want to be used (default is smtptor)

Execution options

Onionrouter script by default runs in server mode and acts as a daemon waiting for connections

Daemon mode can be configured with the following options:

* **--port PORT** or **-p PORT** to define port for daemon to listen (default 23000)
* **--host HOST** or **-l HOST** to define host for daemon to listen (default 127.0.0.1)

Other options are supported as well:

* **--interactive** or **-i** to run onionrouter in interactive input mode for debugging or testing purposes without daemon
* **--client** or **-c** to connect to the daemon and ineract with. Use the host and port options to define the options for the connection to the daemon
* **--debug** or **-d** to start the daemon in debug mode. In this mode, daemon will also print (besides replying) the queries and answers Use the host and port options to define the options for the daemon
* **--config CONFIG** to define the absolute path to config folder (must contain a onionrouter.ini file inside) or config file
* **--mappings MAPPINGS** to define absolute path to static mappings folder (everything inside will be parsed as a yaml file) or yaml file


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
