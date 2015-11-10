import unittest

from tests import test_00_verify_empty

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1

class Test01VerifyPublishSingleDatasetSingleVersion(test_00_verify_empty.Test00VerifyEmpty):

    def test_01_01_publish_to_db_d1v1(self):
        self.tlog("Publishing to db: %s" % ds1.id)
        publisher.publish_to_db(ds1.id, ds1.files)

    def test_01_02_verify_published_to_db_d1v1(self):
        self.tlog("Verifying published to db: %s" % ds1.id)
        verify.verify_published_to_db(ds1.id, ds1.files)

    def test_01_03_publish_to_tds_d1v1(self):
        self.tlog("Publishing to TDS: %s" % ds1.id)
        publisher.publish_to_tds(ds1.id, ds1.files)

    def test_01_04_verify_published_to_tds_d1v1(self):
        self.tlog("Verifying published to TDS: %s" % ds1.id)
        verify.verify_published_to_tds(ds1.id, ds1.files)

    def test_01_05_publish_to_tds_d1v1(self):
        self.tlog("Publishing to SOLR: %s" % ds1.id)
        publisher.publish_to_solr(ds1.id, ds1.files)

    def test_01_06_verify_published_to_solr_d1v1(self):
        self.tlog("Verifying published to SOLR: %s" % ds1.id)
        verify.verify_published_to_solr(ds1.id, ds1.files)

    def test_01_07_verify_published_d1v1(self):
        self.tlog("Verifying published to all: %s" % ds1.id)
        verify.verify_dataset_published(ds1.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test01VerifyPublishSingleDatasetSingleVersion)
    unittest.TextTestRunner(verbosity=2).run(suite)
