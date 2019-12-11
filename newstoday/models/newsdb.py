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
      cl='news.'+country+'.'+language 
      print(cl)
      allcol = newsdb[cl]
      for col in allcol.find():
            print(col.keys())
            if channel in col.keys():
              #print (alldata)
              udata={"$set": alldata}
              allcol.update_many(col, udata)
            else:
               udata={"$set": alldata}
               print('Not existing key inserting')
               allcol.update_many(col, udata)


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
