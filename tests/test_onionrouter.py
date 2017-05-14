#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_onionrouter
----------------------------------

Tests for `onionrouter` module.
"""

import pytest


class TestOnionRouter(object):
    def test_multiple_hostnames_support(self, dummy_onionrouter):
        assert len(dummy_onionrouter.myname) > 1

    def test_hostname_is_upper(self, dummy_onionrouter):
        assert all(x.isupper() for x in dummy_onionrouter.myname) is True

@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


