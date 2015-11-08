import unittest

from tests import test_0_verify_empty

import utils.verify as verify
import utils.datasets as datasets
import utils.wrap_esgf_publisher as publisher

ds1 = datasets.d1v1
ds2 = datasets.d1v2

class Test9VerifyParallelPublication(test_0_verify_empty.Test0VerifyEmpty):
    # All test numbers begin with 9

    all_datasets = (ds1, ds2)
    
    def test_901_put_files_on_disk_all(self):
        for ds in self.all_datasets:
            self.tlog("Putting files on disk: %s" % ds.id)
            publisher.put_files_on_disk(ds.id, ds.files)

    def test_902_verify_files_on_disk_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying files on disk: %s" % ds.id)
            verify.verify_files_on_disk(ds.id, ds.files)

    def test_903_parallel_publish_to_db(self):
        self.tlog("Publishing all to db in parallel")
        for ds in self.all_datasets:
            # PROBABLY USE subprocess to spawn them here
            pass

    def test_904_verify_published_to_db_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to db: %s" % ds.id)
            verify.verify_published_to_db(ds.id, ds.files)

    def test_905_parallel_publish_to_tds_all(self):
        self.tlog("Publishing all to TDS in parallel")
        for ds in self.all_datasets:
            # PROBABLY USE subprocess to spawn them here
            pass

    def test_906_verify_published_to_tds_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to TDS: %s" % ds.id)
            verify.verify_published_to_tds(ds.id, ds.files)

    def test_907_parallel_publish_to_solr_all(self):
        self.tlog("Publishing all to SOLR in parallel")
        for ds in self.all_datasets:
            # PROBABLY USE subprocess to spawn them here
            pass

    def test_908_verify_published_to_solr_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to SOLR: %s" % ds.id)
            verify.verify_published_to_solr(ds.id, ds.files)

    def test_909_verify_published_all(self):
        for ds in self.all_datasets:
            self.tlog("Verifying published to all: %s" % ds.id)
            verify.verify_dataset_published(ds.id)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(Test9VerifyParallelPublication)
    unittest.TextTestRunner(verbosity=2).run(suite)