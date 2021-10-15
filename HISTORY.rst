=======
History
=======

0.6.2 (2021-10-15)
------------------
* Bump pip version in setup.py to >=19.2 due to CVE-2019-20916
* Lift PyYAML restriction of < 6.0 and pin to 6.0 in test requirements and requirements.txt
* Add support for Python 3.10

0.6.1 (2020-10-29)
------------------

* Bump cryptography requirement to 3.2 due to CVE-2020-25659
* Fix systemd paths and add hardening options

0.6.0 (2020-10-29)
------------------

* Fix byte/string conversion errors
* Add support for python 3.7/3.8/3.9
* Drop support for EOL Python 2.7/3.3/3.4
* Use newer versions of dnspython and PyYAML

0.5.4 (2020-10-20)
------------------

* Send a newline when replying to postfiX

0.5.3 (2020-10-20)
------------------

* Last version that supports Python 2.7
* Fixes issue with renamed module that rendered 0.5.2 non-working
* Pins dnspython < 2.0.0 since 2.0.0 does not support Python 2.7

0.4.1 (2017-05-13)
------------------

* Fix "[Errno 98] Address already in use" error when restarting the daemon

0.4.0 (2017-03-20)
------------------

* Beta release on PyPI.

0.1.0 (2017-03-14)
------------------

* First release on PyPI.
