import json
from newstoday.models.getnews import getnews

class getappnews():
  def getname(self,country,language):
      colnames = getnews().getcolnames() 
      #print(colnames)
      for colname in colnames:
       #print (colname)
       if country in str(colname):     
        if language in str(colname): 
           return colname
        else:
            pass 

       else:
            pass 
  def getdata(self, col): 
     coldata = getnews().getcollectiondata(col) 
     return  coldata  
#col = getappnews().getname('india','telugu')
#print(col)
#for news in getappnews().getdata(col):
# print (news)
