# wrap_esgf_publisher.py - used until real ESGF code is connected

import utils.datasets as datasets

## TODO: what other args should be added to these calls?
## When we connect this up to the real publisher code it will become self-explanatory
## We need to wrap the command-line calls.

def publish(dsid, file_list):
    """
    Call 3 stages of publishing:
     - publish to db
     - publish to TDS
     - publish to SOLR
    """
    pass

def publish_to_db(dsid, file_list):
    pass

def publish_to_tds(dsid, file_list):
    pass

def publish_to_solr(dsid, file_list):
    pass

def unpublish(dsid, file_list):
    """
    Call 3 stages of unpublishing:
     - unpublish from SOLR
     - unpublish from TDS
     - unpublish from db
    """
    pass

def unpublish_from_db(dsid, file_list):
    pass

def unpublish_from_tds(dsid, file_list):
    pass

def unpublish_from_solr(dsid, file_list):
    pass

def _get_test_datasets():
    """
    Returns a list of all test datasets
    """
    test_datasets = datasets.all_datasets
    return test_datasets

def delete_all():
    """
    Delete all the test data.
    """
    delete_all_from_db()
    delete_all_from_tds()
    delete_all_from_solr()

def delete_all_from_db():
    """
    DELETE will talk directly to the python code.
    The capability to delete from the db is excluded from the
    command-line API.
    """
    for ds in datasets.all_datasets:
        pass

def delete_all_from_tds():
    for ds in datasets.all_datasets:
        pass

def delete_all_from_solr():
    for ds in datasets.all_datasets:
        pass
