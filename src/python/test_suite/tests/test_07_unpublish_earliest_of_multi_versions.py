import unittest

from tests import test_02_publish_d1v2

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1
ds2 = datasets.d1v2

class Test07VerifyUnpublishEarliestOfMultiVersions(test_02_publish_d1v2.Test02VerifyPublishSingleDatasetTwoVersions):

    def test_07_01_unpublish_from_solr_d1v1(self):
        self.tlog("Unpublishing from SOLR: %s" % ds1.id)
        publisher.unpublish_from_solr(ds1.id, ds1.files)

    def test_07_02_verify_unpublished_from_solr_d1v1(self):
        self.tlog("Verifying unpublished from SOLR: %s" % ds1.id)
        verify.verify_unpublished_from_solr(ds1.id, ds1.files)

    def test_07_03_verify_published_d1v2(self):
        self.tlog("Verifying published to all: %s" % ds2.id)
        verify.verify_dataset_published(ds2.id)

    def test_07_04_verify_consistency_d1v2(self):
        self.tlog("Verifying consistency of: %s" % ds2.id)
        verify.verify_consistency(ds2.id)

    def test_07_05_unpublish_from_tds_d1v1(self):
        self.tlog("Unpublished from TDS: %s" % ds1.id)
        publisher.unpublish_from_tds(ds1.id, ds1.files)

    def test_07_06_verify_unpublished_from_tds_d1v1(self):
        self.tlog("Verifying unpublished from TDS: %s" % ds1.id)
        verify.verify_unpublished_from_tds(ds1.id, ds1.files)

    def test_07_07_verify_published_d1v2(self):
        self.tlog("Verifying published to all: %s" % ds2.id)
        verify.verify_dataset_published(ds2.id)

    def test_07_08_verify_consistency_d1v2(self):
        self.tlog("Verifying consistency of: %s" % ds2.id)
        verify.verify_consistency(ds2.id)

    def test_07_09_unpublish_from_db_d1v1(self):
        self.tlog("Unpublished from db: %s" % ds1.id)
        publisher.unpublish_from_db(ds1.id, ds1.files)

    def test_07_10_verify_unpublished_from_db_d1v1(self):
        self.tlog("Verifying unpublished from db: %s" % ds1.id)
        verify.verify_unpublished_from_db(ds1.id, ds1.files)

    def test_07_11_verify_published_d1v2(self):
        self.tlog("Verifying published to all: %s" % ds2.id)
        verify.verify_dataset_published(ds2.id)

    def test_07_12_verify_consistency_d1v2(self):
        self.tlog("Verifying consistency of: %s" % ds2.id)
        verify.verify_consistency(ds2.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test07VerifyUnpublishEarliestOfMultiVersions)
    unittest.TextTestRunner(verbosity=2).run(suite)
