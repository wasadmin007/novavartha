import json
import pymongo
import json
from bson import json_util
from newstoday.models.newsdb import conn

conn,db = conn().dbconn()
