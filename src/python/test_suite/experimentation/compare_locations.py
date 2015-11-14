import read_esg_config
import read_filesystem
import read_database
import read_thredds
import read_index

mapfile_path = "/badc/cmip5/metadata/mapfiles/by_name/cmip5/output1/CSIRO-QCCCE/CSIRO-Mk3-6-0/historical/cmip5.output1.CSIRO-QCCCE.CSIRO-Mk3-6-0.historical.mon.land.Lmon.r5i1p1.v1"

conf = read_esg_config.Config()
rf = read_filesystem.ReadFilesystem(conf)

ds_fs = rf.dset_from_mapfile(mapfile_path)

name = ds_fs.name
version = ds_fs.version

print "As seen on filesystem:"
print ds_fs


db = read_database.ReadDB(conf)
ds_db, catalog_loc = db.get_dset(name, version)
print "As seen in database:"
print ds_db

assert ds_db == ds_fs

rt = read_thredds.ReadThredds(conf)
url_path = rt.url_path(catalog_loc)
local_path = rt.local_path(catalog_loc)
print local_path
ds_thredds_served = rt.parse_catalog(url_path)
ds_thredds_local = rt.parse_catalog(local_path)

print "As seen in THREDDS (local fs):"
print ds_thredds_local

assert ds_thredds_local == ds_fs

print "As seen in THREDDS (http from server):"
print ds_thredds_served

assert ds_thredds_served == ds_fs

ri = read_index.ReadIndex(conf)
ds_index = ri.get_dset(name, version)

print "As seen in index:"
print ds_index

assert ds_index == ds_fs
