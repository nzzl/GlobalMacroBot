import urllib, json, threading, time, datetime

bitMEX_instruments = "https://www.bitmex.com/api/v1/instrument"

def getStats(instruments):

    response = urllib.urlopen(instruments)
    instruments = json.loads(response.read())

    symbols = ['XBT24H', 'XBT48H', 'XBT7D', 'XBTM16', 'XBTU16']
    indexer = list()

    for i in range(0, len(symbols)):
        for j in range(0, len(instruments)):
            if symbols[i] == instruments[j]['symbol']:
                indexer.append(j)

    def printOut():
        threading.Timer(3600, printOut).start()
        ts = time.time()
        print datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        for k in indexer:
            print \
            instruments[k]['symbol'], ',', \
            instruments[k]['timestamp'].replace("T00:00:00.000Z", "")[0:10], ',', \
            instruments[k]['lastPrice'], ',', \
            instruments[k]['volume24h'], ',', \
            instruments[k]['turnover24h'], ',', \
            instruments[k]['turnover']
    printOut()

getStats(bitMEX_instruments)