import json
import pymongo
import json
from bson import json_util
from newstoday.models.newsdb import conn 

conn,db = conn().dbconn() 
class getnews():
    def getcolnames(self):
       cols = db.collection_names()
       return cols
    def getcollectiondata(self,col):
       
       col = db[col]
       coldata = col.find()
       return coldata
	
