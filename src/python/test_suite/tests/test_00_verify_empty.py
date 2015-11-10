import unittest
import utils.verify as verify
from tests.base_tests import PublishBaseTest

class Test00VerifyEmpty(PublishBaseTest):

    def test_00_01_verify_empty(self):
        self.tlog("Verifying empty before we begin")
        verify.verify_empty()

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test00VerifyEmpty)
    unittest.TextTestRunner(verbosity=2).run(suite)