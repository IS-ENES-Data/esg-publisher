import unittest

from tests import test_00_verify_empty

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1
ds2 = datasets.d1v2

class Test03VerifyPublishAllInStages(test_00_verify_empty.Test00VerifyEmpty):

    all_datasets = (ds1, ds2)

    def test_03_01_publish_to_db_all(self):
        for ds in self.all_datasets:
            self.tlog("Publishing to db: %s" % ds.id)
            publisher.publish_to_db(ds.id, ds.files)

    def test_03_02_verify_published_to_db_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to db: %s" % ds.id)
            verify.verify_published_to_db(ds.id, ds.files)

    def test_03_03_publish_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Publishing to TDS: %s" % ds.id)
            publisher.publish_to_tds(ds.id, ds.files)

    def test_03_04_verify_published_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to TDS: %s" % ds.id)
            verify.verify_published_to_tds(ds.id, ds.files)

    def test_03_05_publish_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Publishing to SOLR: %s" % ds.id)
            publisher.publish_to_solr(ds.id, ds.files)

    def test_03_06_verify_published_to_solr_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to SOLR: %s" % ds.id)
            verify.verify_published_to_solr(ds.id, ds.files)

    def test_03_07_verify_published_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to all: %s" % ds.id)
            verify.verify_dataset_published(ds.id)

    def test_03_08_verify_consistency_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying consistency of: %s" % ds.id)
            verify.verify_consistency(ds.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test03VerifyPublishAllInStages)
    unittest.TextTestRunner(verbosity=2).run(suite)
