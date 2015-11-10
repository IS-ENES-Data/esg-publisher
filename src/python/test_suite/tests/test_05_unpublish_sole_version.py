import unittest

from tests import test_01_publish_d1v1

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1

class Test05VerifyUnpublishSoleVersion(test_01_publish_d1v1.Test01VerifyPublishSingleDatasetSingleVersion):

    def test_05_01_unpublish_from_solr_d1v1(self):
        self.tlog("Unpublishing from SOLR: %s" % ds1.id)
        publisher.unpublish_from_solr(ds1.id, ds1.files)

    def test_05_02_verify_unpublished_from_solr_d1v1(self):
        self.tlog("Verifying unpublished from SOLR: %s" % ds1.id)
        verify.verify_unpublished_from_solr(ds1.id, ds1.files)

    def test_05_03_unpublish_from_tds_d1v1(self):
        self.tlog("Unpublished from TDS: %s" % ds1.id)
        publisher.unpublish_from_tds(ds1.id, ds1.files)

    def test_05_04_verify_unpublished_from_tds_d1v1(self):
        self.tlog("Verifying unpublished from TDS: %s" % ds1.id)
        verify.verify_unpublished_from_tds(ds1.id, ds1.files)

    def test_05_05_unpublish_from_db_d1v1(self):
        self.tlog("Unpublished from db: %s" % ds1.id)
        publisher.unpublish_from_db(ds1.id, ds1.files)

    def test_05_06_verify_unpublished_from_db_d1v1(self):
        self.tlog("Verifying unpublished from db: %s" % ds1.id)
        verify.verify_unpublished_from_db(ds1.id, ds1.files)

    def test_05_07_verify_unpublished_d1v1(self):
        self.tlog("Verifying unpublished from all: %s" % ds1.id)
        verify.verify_dataset_unpublished(ds1.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test05VerifyUnpublishSoleVersion)
    unittest.TextTestRunner(verbosity=2).run(suite)