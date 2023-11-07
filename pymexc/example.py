import spot, futures

api_key = "mx0vgloVgKopMEGcYt"
api_secret = "a75e6b3ef0c34815abc1781d6ae51a3c"

def handle_message(message): 
    # handle websocket message
    print(message)


# FUTURES V1

# initialize HTTP client
spot_client = spot.HTTP(api_key = api_key, api_secret = api_secret)
# initialize WebSocket client
ws_futures_client = futures.WebSocket(api_key = api_key, api_secret = api_secret)

# make http request to api
print(spot_client.account_information())


# create websocket connection to public channel (sub.tickers)
# all messages will be handled by function `handle_message`
#ws_futures_client.tickers_stream(handle_message)
