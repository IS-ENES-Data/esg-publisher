import unittest

from tests import test_02_publish_d1v2

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1
ds2 = datasets.d1v2

class Test06VerifyUnpublishLatestOfMultiVersions(test_02_publish_d1v2.Test02VerifyPublishSingleDatasetTwoVersions):

    def test_06_01_unpublish_from_solr_d1v2(self):
        self.tlog("Unpublishing from SOLR: %s" % ds2.id)
        publisher.unpublish_from_solr(ds2.id, ds2.files)

    def test_06_02_verify_unpublished_from_solr_d1v2(self):
        self.tlog("Verifying unpublished from SOLR: %s" % ds2.id)
        verify.verify_unpublished_from_solr(ds2.id, ds2.files)

    def test_06_03_verify_published_d1v1(self):
        self.tlog("Verifying published to all: %s" % ds1.id)
        verify.verify_dataset_published(ds1.id)

    def test_06_04_verify_consistency_d1v1(self):
        self.tlog("Verifying consistency of: %s" % ds1.id)
        verify.verify_consistency(ds1.id)

    def test_06_05_unpublish_from_tds_d1v2(self):
        self.tlog("Unpublished from TDS: %s" % ds2.id)
        publisher.unpublish_from_tds(ds2.id, ds2.files)

    def test_06_06_verify_unpublished_from_tds_d1v2(self):
        self.tlog("Verifying unpublished from TDS: %s" % ds2.id)
        verify.verify_unpublished_from_tds(ds2.id, ds2.files)

    def test_06_06_verify_published_d1v1(self):
        self.tlog("Verifying published to all: %s" % ds1.id)
        verify.verify_dataset_published(ds1.id)

    def test_06_07_verify_consistency_d1v1(self):
        self.tlog("Verifying consistency of: %s" % ds1.id)
        verify.verify_consistency(ds1.id)

    def test_06_08_unpublish_from_db_d1v2(self):
        self.tlog("Unpublished from db: %s" % ds2.id)
        publisher.unpublish_from_db(ds2.id, ds2.files)

    def test_06_09_verify_unpublished_from_db_d1v2(self):
        self.tlog("Verifying unpublished from db: %s" % ds2.id)
        verify.verify_unpublished_from_db(ds2.id, ds2.files)

    def test_06_10_verify_published_d1v1(self):
        self.tlog("Verifying published to all: %s" % ds1.id)
        verify.verify_dataset_published(ds1.id)

    def test_06_11_verify_consistency_d1v1(self):
        self.tlog("Verifying consistency of: %s" % ds1.id)
        verify.verify_consistency(ds1.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test06VerifyUnpublishLatestOfMultiVersions)
    unittest.TextTestRunner(verbosity=2).run(suite)
