import requests 
import sys
from newstoday.models.newsdb import conn
from bs4 import BeautifulSoup 
  
def news(): 
    # the target we want to open     
    url='http://eenadu.net/'
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        print("The news are as follow :-\n") 
        print (resp) 
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     
        # l is the list which contains all the text i.e news  
        l = soup.findAll("div", attrs={"class": "col-left"}) 
        #head='<html><head><title>India News Today &hellip;</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></head><body>'
        alldata = {}
        data = []
        for ld in l:
         for i in ld.findAll("a", href=True):
            #content = str(i)
            if 'http' in i['href']:
              urlheader = i['href']
              js='onmouseover="openInNewTab('+str(urlheader)+')"'
            else:
               urlheader = url+str(i['href'])
               js='onmouseover="openInNewTab('+str(urlheader)+')"'
            content = "<a "+js+" href="+str(urlheader)+">"+str(i.text)+"</a> <br>"
            data.append( { "url": str(urlheader), "text": str(i.text) ,"tab": "regular"})
        l = soup.findAll("nav")
        #now we want to print only the text part of the anchor.
        for ld in l:
         for i in ld.findAll("a", href=True):
            #content = str(i)
            if 'http' in i['href']:
              urlheader = i['href']
              js='onmouseover="openInNewTab('+str(urlheader)+')"'
            else:
               urlheader = url+str(i['href'])
               js='onmouseover="openInNewTab('+str(urlheader)+')"'
            content = "<a "+js+" href="+str(urlheader)+">"+str(i.text)+"</a> <br>"
            data.append( { "url": str(urlheader), "text": str(i.text) ,"tab": "nav"})
        alldata = {"eenadu": data}
        print (alldata)
        print(conn().insert(alldata,'eenadu',country='india',language='telugu') )

    else: 
        print("Error") 
          
news()
