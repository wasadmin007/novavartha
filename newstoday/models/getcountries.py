import json
import pymongo
import json
from bson import json_util
from newstoday.models.newsdb import conn

conn,db = conn().dbconn()
class getcountries():
   def getcountries(self):
       col = db["countries"]
       coldata = col.find()
       countries = []
       for info in coldata:
        for country in info['countries']:
          countries.append((country,country,)) 
       return countries
   def getlanguages(self,country):
       col = db["languages"]
       coldata = col.find()
       for info in coldata:
        if info['country'] == country:
           languages = info['languages']
       return languages 
   def getlanguagech(self,country):
       col = db["languages"]
       coldata = col.find()
       languages = []
       for info in coldata:
        if info['country'] == country:
           for language in info['languages']:
             languages.append((language,language,))
       return languages

countries=getcountries().getcountries()
print (countries)
lan=getcountries().getlanguages('USA')
print(lan)
