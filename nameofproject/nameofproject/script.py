#!/usr/bin/python3.8.10

# -*- coding: utf-8 -*-
import os
import sys
import locale
import postgresql
import pymongo
import datetime
from bson.binary import Binary as debin
import threading

start = datetime.datetime.now()
startTime = "%d:%d:%d" % (start.hour, start.minute, start.second)
print("#START in", startTime)

####### PROD ########
pgdb = postgresql.open('pq://centrum:DY5YfYkrF7@10.0.89.12:5432/centrum')
mgdb_pre = pymongo.MongoClient(
    'mongodb://centrum:n2dln2efwwg@10.0.124.202:27017/?authSource=photos&readPreference=primary&authMechanism=SCRAM-SHA-1')
mgdb_new = pymongo.MongoClient(
    'mongodb://centrum:n2dln2efwwg@10.0.89.165:27017/?authSource=photos&readPreference=primary&authMechanism=SCRAM-SHA-1')

print("#DBS ALL CONNECTED")
####### TEST ########
# pgdb = postgresql.open('pq://centrum:DY5YfYkrF7@10.0.85.196:5432/centrum')
# mgdb_pre = pymongo.MongoClient('mongodb://centrum:kV6gaSVxlT@10.0.85.197:27017/?authSource=photos&readPreference=primary&authMechanism=SCRAM-SHA-1')
# mgdb_new = pymongo.MongoClient('mongodb://momentum:zAdR5RgOl1@10.0.85.198:27017/?authSource=mphotos&readPreference=primary&authMechanism=SCRAM-SHA-1')

mgdb_pre = mgdb_pre['photos']
mgcoll_pre = mgdb_pre['photos']

mgdb_new = mgdb_new['photos']
mgcoll_new = mgdb_new['photos']

dfrom = '2021-01-01 00:00:00'
dto = '2021-02-01 00:00:00'
sql = "select source_camera_event_id from its_passage_event \
 where passage_date between '" + dfrom + "' and '" + dto + "' \
 and hcm_id in (select id from its_hcm h where h.road_id in (1,2,3,4,5,6,7,8));"
pgrs = pgdb.query(sql)

# # pgrs = pgdb.query("select recognized_event_id from its_correction_log \
# # where recognized_date > '2021-02-11 23:59:59' and is_corrected = false; \
# # ")

print("#TOTALY events ", len(pgrs))

pgdb.close()