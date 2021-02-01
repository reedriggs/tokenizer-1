"""
Goals: 
    - Create a list from text on a corpus website following a search
    - inform user of problems at which step of connectivity to corpus site
Steps:
    - first check if internet is connected via Bing, Yahoo, Duckduckgo
    - if so, check if corpus search returns results
    - if so, create a list for various analyses
Next steps: 
    - check if and which corpus sites block webscraping
    - gui offers Chinese corpus database cptions via clickboxes
"""

import requests
#import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

#quickly check internet connection through three common web browser links

def checkLink(link):
  link_a = "http://www." + str(link) + ".com"
  try:
    requests.get(link_a)
    #print("response code: " + str(response.status_code))
    return True
  except requests.ConnectionError:
    print("Could not connect" + "\n" + "HTTP status codes: 200 OK, 301 Moved Permanently, 302 Found (Moved Temporarily), 401 Unauthorized, 403 Forbidden, 404 Not Found, 410 Gone, 500 Internal Server Error, 503 Service Unavailable")
    return False

def CheckConnect():
  #Bing showed the fastest response relative to Yahoo! and Duckduckgo, so checking Bing first should return the fastest response
  if checkLink("bing") == True:
    #print("Connected")
    return True
  elif checkLink("yahoo") == True:
    #print("Connected")
    return True
  elif checkLink("duckduckgo") == True:
    #print("Connected")
    return True
  else:
    print("Problem Connecting to Internet")
    return False

def CheckCorpusSite(corpus_link):
  if CheckConnect() == True:
    link_b = str(corpus_link)
    try:
      response = requests.get(link_b)
      #status_code = ("response code: " + str(response.status_code) + "; ")
      print("response code: " + str(response.status_code))
      print("Connected to " + str(corpus_link))
      return True
    except requests.ConnectionError:
      print("Could not connect to corpus site")
      return False
  else:
    print("Problem Connecting to Internet")
    return False

#first test to see if the operations above will work and in in their intended order
#BLCU_corpus_site = """http://202.112.195.8:8089/ccir_login?input=*"""
sinica_ch = "https://www.sinica.edu.tw/ch"
CheckCorpusSite(sinica_ch)

searchTerm = "有"
link = "https://corpora.uni-leipzig.de/de/res?corpusId=zho-simp_news_2010&word=" + searchTerm
#f = urllib.urlopen(link)
#response = urlopen(link)
#content = response.read()
#print(content)

headers = "{'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'}"

source = requests.get(link, headers).text
element = '/html/body/div[1]/div[1]/div/div[1]/div[4]/div/div[2]/ul[1]/li[1]'
html = "html5lib"

soup = BeautifulSoup(source, html)

target_text = soup.find(element)
output = target_text.text
print(output)


