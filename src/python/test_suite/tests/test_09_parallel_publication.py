import unittest

from tests import test_00_verify_empty

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1
ds2 = datasets.d1v2

class Test09VerifyParallelPublication(test_00_verify_empty.Test00VerifyEmpty):

    all_datasets = (ds1, ds2)

    def test_09_03_parallel_publish_to_db(self):
        self.tlog("Publishing all to db in parallel")
        for ds in self.all_datasets:
            # PROBABLY USE subprocess to spawn them here
            pass

    def test_09_04_verify_published_to_db_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to db: %s" % ds.id)
            verify.verify_published_to_db(ds.id, ds.files)

    def test_09_05_parallel_publish_to_tds_all(self):
        self.tlog("Publishing all to TDS in parallel")
        for ds in self.all_datasets:
            # PROBABLY USE subprocess to spawn them here
            pass

    def test_09_06_verify_published_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to TDS: %s" % ds.id)
            verify.verify_published_to_tds(ds.id, ds.files)

    def test_09_07_parallel_publish_to_solr_all(self):
        self.tlog("Publishing all to SOLR in parallel")
        for ds in self.all_datasets:
            # PROBABLY USE subprocess to spawn them here
            pass

    def test_09_08_verify_published_to_solr_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to SOLR: %s" % ds.id)
            verify.verify_published_to_solr(ds.id, ds.files)

    def test_09_09_verify_published_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to all: %s" % ds.id)
            verify.verify_dataset_published(ds.id)

    def test_09_10_verify_consistency_all(self):
        for ds in self.datasets:
            self.tlog("Verifying consistency of: %s" % ds.id)
            verify.verify_consistency(ds.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test09VerifyParallelPublication)
    unittest.TextTestRunner(verbosity=2).run(suite)