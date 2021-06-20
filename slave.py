import traceback
import urllib3
import xmltodict
import configparser
import io
def getRSS(urlIn):
    url = urlIn
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

def parseConfig():
    Config = configparser.ConfigParser()
    Config.read("slaveconfig.ini")
    #print(Config.sections())
    for rs in Config.sections():
        options = Config.options(rs)
        for option in options:
            try:
             #   print(Config.get(rs, option))
                getRSS(Config.get(rs, option))
            except:
                print("WTF")
parseConfig()
