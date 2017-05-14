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

    def test_get_domain_multiple_at(self, dummy_onionrouter):
        with pytest.raises(RuntimeError):
            dummy_onionrouter.get_domain("lalla@lalala.com@lalal.net")

    def test_get_domain_no_email(self, dummy_onionrouter):
        with pytest.raises(RuntimeError):
            dummy_onionrouter.get_domain("lalla")

    def test_get_domain_correct_email(self, dummy_onionrouter):
        assert dummy_onionrouter.get_domain("lol@test.com") == "test.com"

    def test_reroute_local_domain(self, dummy_onionrouter):
        assert dummy_onionrouter.reroute("myself.net") == tuple(["200 :"])
