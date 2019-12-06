import requests 
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
        l = soup.findAll("div") 
        f=open('eenadu.html','w') 
        #now we want to print only the text part of the anchor. 
        #find all the elements of a, i.e anchor 
        head='<html><head><title>India News Today &hellip;</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></head><body>'
        f.write(head)
        for ld in l:
         for i in ld.findAll("a", href=True):
            #content = str(i)
            if 'http' in i['href']:
              urlheader = i['href']
              js='onmouseover="openInNewTab('+urlheader+')"'
            else:
               urlheader = "http://sakshi.com"+i['href']
               js='onmouseover="openInNewTab('+urlheader+')"'
            content = "<a "+js+" href="+urlheader+">"+i.text+"</a> <br>"
            f.write(str(content)+'\n')
        f.write("</body></html>")


        f.close()
    else: 
        print("Error") 
          
news()
