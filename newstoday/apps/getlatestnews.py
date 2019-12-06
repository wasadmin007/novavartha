import json
from newstoday.models.getnews import getnews

class getappnews():
  def getname(self,country,language):
      colnames = getnews().getcolnames() 
      for colname in colnames:
       if country in str(colname):     
        if language in str(colname): 
           return colname
        else:
            return 'None' 

       else:
             return 'None'
  def getdata(self, col): 
     coldata = getnews().getcollectiondata(col) 
     return  coldata  

