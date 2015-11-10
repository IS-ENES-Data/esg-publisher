import unittest

from tests import test_00_verify_empty

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1
ds2 = datasets.d1v2

class Test04VerifyPublishAllInReverse(test_00_verify_empty.Test00VerifyEmpty):

    all_datasets = (ds2, ds1)

    def test_04_01_publish_to_db_all(self):
        for ds in self.all_datasets:
            self.tlog("Publishing to db: %s" % ds.id)
            publisher.publish_to_db(ds.id, ds.files)

    def test_04_02_verify_published_to_db_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to db: %s" % ds.id)
            verify.verify_published_to_db(ds.id, ds.files)

    def test_04_03_publish_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Publishing to TDS: %s" % ds.id)
            publisher.publish_to_tds(ds.id, ds.files)

    def test_04_04_verify_published_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to TDS: %s" % ds.id)
            verify.verify_published_to_tds(ds.id, ds.files)

    def test_04_05_publish_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Publishing to SOLR: %s" % ds.id)
            publisher.publish_to_solr(ds.id, ds.files)

    def test_04_06_verify_published_to_solr_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to SOLR: %s" % ds.id)
            verify.verify_published_to_solr(ds.id, ds.files)

    def test_04_07_verify_published_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to all: %s" % ds.id)
            verify.verify_dataset_published(ds.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test04VerifyPublishAllInReverse)
    unittest.TextTestRunner(verbosity=2).run(suite)
