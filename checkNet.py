#quickly check internet connection through three common web browser links

def checkLink(link):
  import requests
  link_a = "http://www." + str(link) + ".com"
  try:
    response = requests.get(link_a)
    #print("response code: " + str(response.status_code))
    return True
  except requests.ConnectionError:
    status_code = ("response code: " + str(response.status_code) + "; ")
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
    import requests
    link_b = str(corpus_link)
    try:
      response = requests.get(link_b)
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
BLCU_corpus_site = """http://202.112.195.8:8089/ccir_login?input=*"""
sinica_ch = "https://www.sinica.edu.tw/ch"
CheckCorpusSite(sinica_ch)

def internet_on():
  import requests
  for timeout in [1,5,10,15]:
    try:
      response = requests.get('http://google.com', timeout=timeout)
      print("response code: " + str(response.status_code))
      return True
    except urllib2.URLError as err: pass
  return False
  print("Could not connect" + "\n" + "HTTP status codes: 200 OK, 301 Moved Permanently, 302 Found (Moved Temporarily), 401 Unauthorized, 403 Forbidden, 404 Not Found, 410 Gone, 500 Internal Server Error, 503 Service Unavailable")

#internet_on()

#print("\n" + "HTTP status codes: 200 OK, 301 Moved Permanently, 302 Found (Moved Temporarily), 401 Unauthorized, 403 Forbidden, 404 Not Found, 410 Gone, 500 Internal Server Error, 503 Service Unavailable")


#first check if internet is connected
  #if so, check if corpus search returns results
    #if so, perform lemmatization and other analyses

#gui offers Chinese corpus database clickboxes
