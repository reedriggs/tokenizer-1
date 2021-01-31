#both of these now work on my iPhone

def checkNet():
  import requests
  try:
    response = requests.get("http://www.google.com")
    print("response code: " + str(response.status_code))
    return True
  except requests.ConnectionError:
    print("Could not connect")

checkNet()

def internet_on():
  import requests
  for timeout in [1,5,10,15]:
    try:
      response = requests.get('http://google.com', timeout=timeout)
      print("response code: " + str(response.status_code))
      return True
    except urllib2.URLError as err: pass
  return False
  print("Could not connect")

internet_on()

print("""HTTP status codes: 200 OK, 301 Moved Permanently, 302 Found (Moved Temporarily), 401 Unauthorized, 403 Forbidden, 404 Not Found, 410 Gone, 500 Internal Server Error, 503 Service Unavailable""")

#next steps:
#1. check if works on laptop computer
#2. first check if internet is connected
  #if so, check if corpus search returns results
    #if so, perform lemmatization and other analyses
#3. gui offers Chinese corpus database clickboxes
