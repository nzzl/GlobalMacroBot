import urllib, json, threading

current1 = "https://pro-data.btcc.com/data/pro/ticker?market=BPICNY"
response = urllib.urlopen(current1)
current1 = json.loads(response.read())
currentPrice = current1['ticker']['Last']
currentQuant = current1['ticker']['LastQuantity']
lastTradeTime = current1['ticker']['Timestamp']
tradeVolume = current1['ticker']['Volume']
deltaTime = 0

print 'Initial Values: ', currentPrice, ', ', currentQuant, ', ', tradeVolume, ',', lastTradeTime

def proTicker():

    global currentPrice, currentQuant, lastTradeTime, tradeVolume, deltaTime

    data = "https://pro-data.btcc.com/data/pro/ticker?market=BPICNY"
    threading.Timer(0.1, proTicker).start()
    response = urllib.urlopen(data)
    data = json.loads(response.read())

    # if data['ticker']['Last'] != currentPrice \
    #         or data['ticker']['LastQuantity'] != currentQuant\
    #         and data['ticker']['Timestamp'] != lastTradeTime:

    if data['ticker']['Last'] != currentPrice and data['ticker']['Last'] != ' ':
        #print 'Price:', currentPrice, ', Quantity:', currentQuant, ', Volume:', tradeVolume,', Delta Time:', deltaTime

        print currentPrice

        # print 'Price:', currentPrice
        # print 'Quantity:', currentQuant
        # print 'Volume:', tradeVolume
        # print 'Delta Time:', deltaTime

    currentPrice = data['ticker']['Last']
    # currentQuant = data['ticker']['LastQuantity']
    # tradeVolume = data['ticker']['Volume']
    # deltaTime = data['ticker']['Timestamp']
    # tradeVolume = data['ticker']['Volume']

proTicker()