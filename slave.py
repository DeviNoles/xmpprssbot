import traceback
import urllib3
import xmltodict

def getChinaRSS():
    url = ""	
    http = urllib3.PoolManager()

    response = http.request('GET', url)
    #print(response)
    try:
        data = xmltodict.parse(response.data)
        titles = data
        #print(data['feed']['entry'][0]['title']['#text'])
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    
   # print(titles['feed']['entry'][0]['title']['#text'])
    for x in titles['feed']['entry']:
        print(x['title']['#text'])
    return data

getChinaRSS()
