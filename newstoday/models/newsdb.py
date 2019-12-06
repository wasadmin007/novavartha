import pymongo
import json
from bson import json_util
class conn():
  def dbconn(self,dbname="news"):
        dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
        newsdb = dbclient[dbname]
        return dbclient,newsdb
  def db(self,dbname):
      cl,newsdb=conn().dbconn()
      newsdb = cl[dbname] 
      return newsdb

  def insert(self,alldata,channel,language='telugu',country='india'):
      newsdb=conn().db("news")
      cols = newsdb.list_collection_names()
      if country in str(cols):
       if language in str(cols):
        for cl in cols:   
          #print (cl)
          allcol = newsdb[cl]
          for col in allcol.find():
            print(col.keys())
            if channel in col.keys():
              udata={"$set": alldata}
              allcol.update_many(col, udata)
            else:
               allcol.insert_many(alldata) 


#print (conn().insert({"sakshi": [{}]}))
#cl,dbname=conn().dbconn()
#newsdb=conn().db("news")
#print(cl.list_database_names())
#cols = newsdb.list_collection_names()
#print('sdafsd',cols)
#data={"$set": { "sakshi": [ "praveen", "35"]}}
#for cl in cols:
#  allcol = newsdb[cl]
#  for col in allcol.find():
#     if 'sakshi' in col.keys():
#        allcol.update_many(col, data)
