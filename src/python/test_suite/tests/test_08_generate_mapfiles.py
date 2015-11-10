import unittest

from tests import test_00_verify_empty

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1

class Test08VerifyGenerateMapfiles(test_00_verify_empty.Test00VerifyEmpty):

    # WHAT SHOULD WE DO HERE?
    pass

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test08VerifyGenerateMapfiles)
    unittest.TextTestRunner(verbosity=2).run(suite)
