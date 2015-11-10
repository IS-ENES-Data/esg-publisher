import unittest

from tests import test_01_publish_d1v1

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1
ds2 = datasets.d1v2

class Test02VerifyPublishSingleDatasetTwoVersions(test_01_publish_d1v1.Test01VerifyPublishSingleDatasetSingleVersion):

    def test_02_01_publish_to_db_d1v2(self):
        self.tlog("Publishing to db: %s" % ds2.id)
        publisher.publish_to_db(ds2.id, ds2.files)

    def test_02_02_verify_published_to_db_d1v2(self):
        self.tlog("Verifying published to db: %s" % ds2.id)
        verify.verify_published_to_db(ds2.id, ds2.files)

    def test_02_03_publish_to_tds_d1v2(self):
        self.tlog("Publishing to TDS: %s" % ds2.id)
        publisher.publish_to_tds(ds2.id, ds2.files)

    def test_02_04_verify_published_to_tds_d1v2(self):
        self.tlog("Verifying published to TDS: %s" % ds2.id)
        verify.verify_published_to_tds(ds2.id, ds2.files)

    def test_02_05_publish_to_tds_d1v2(self):
        self.tlog("Publishing to SOLR: %s" % ds2.id)
        publisher.publish_to_solr(ds2.id, ds2.files)

    def test_02_06_verify_published_to_solr_d1v2(self):
        self.tlog("Verifying published to SOLR: %s" % ds2.id)
        verify.verify_published_to_solr(ds2.id, ds2.files)

    def test_02_07_verify_published_d1v2(self):
        self.tlog("Verifying published to all: %s" % ds2.id)
        verify.verify_dataset_published(ds2.id)

    def test_02_08_verify_consistency_d1v2(self):
        self.tlog("Verifying consistency of: %s" % ds2.id)
        verify.verify_consistency(ds2.id)

    def test_02_09_verify_published_to_tds_d1v1(self):
        self.tlog("Verifying published to TDS: %s" % ds1.id)
        verify.verify_published_to_tds(ds1.id, ds1.files)

    def test_02_10_verify_published_to_solr_d1v1(self):
        self.tlog("Verifying published to SOLR: %s" % ds1.id)
        verify.verify_published_to_solr(ds1.id, ds1.files)

    def test_02_11_verify_published_d1v1(self):
        self.tlog("Verifying published to all: %s" % ds1.id)
        verify.verify_dataset_published(ds1.id)

    def test_02_12_verify_consistency_d1v1(self):
        self.tlog("Verifying consistency of: %s" % ds1.id)
        verify.verify_consistency(ds1.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test02VerifyPublishSingleDatasetTwoVersions)
    unittest.TextTestRunner(verbosity=2).run(suite)
