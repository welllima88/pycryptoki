"""
Test methods for .. 'hsm usage' set of commands.
"""
import logging
import os

import pytest

from . import config as hsm_config
from ...defines import CKR_SESSION_HANDLE_INVALID, \
    CKR_USER_NOT_AUTHORIZED
from ...key_usage import ca_clonemofn, ca_duplicatemofn
from ...return_values import ret_vals_dictionary


class TestAlgorithm(object):
    """Test algorithm class"""
    h_session = 0
    admin_slot = 0

    @pytest.fixture(autouse=True)
    def setup_teardown(self, auth_session):
        self.h_session = auth_session
        self.admin_slot = hsm_config["test_slot"]

    def test_clonemofn(self):
        """Test clone M of N"""
        ret = ca_clonemofn(self.h_session)
        assert ret == CKR_SESSION_HANDLE_INVALID, \
            "Return code should be " + \
            ret_vals_dictionary[CKR_SESSION_HANDLE_INVALID] + \
            " not " + ret_vals_dictionary[ret]

    @pytest.mark.xfail(reason="Not valid on PWD auth")
    def test_duplicatemofn(self):
        """Test duplicate M of N"""
        ret = ca_duplicatemofn(self.h_session)
        assert ret == CKR_USER_NOT_AUTHORIZED, \
            "Return code should be " + \
            ret_vals_dictionary[CKR_USER_NOT_AUTHORIZED] + \
            " not " + ret_vals_dictionary[ret]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    pytest.cmdline.main(args=['-v', os.path.abspath(__file__)])