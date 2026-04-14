import threading
import requests
from bs4 import BeautifulSoup

urls=[
    "https://python.langchain.com/v0.2/docs/introduction/",

"https://python.langchain.com/v0.2/docs/concepts/",

"https://python.langchain.com/v0.2/docs/tutorials/"
]

def fetch_content(url):
    response=requests.get(url) #->to get the url
    soup=BeautifulSoup(response.content,'html.parser')  #to do web scraping
    #html.parser is used to get the data info 
    #from the webpages contentv thaat is written in html
    #print(f"soup.text")-> TO DISPLAY THE CONTENT
    print(f"FETCHED :{len(soup.text)} characters fron the {url}")

threads=[]
for url in urls :
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for i in threads:
    i.join()

