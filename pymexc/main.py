
import discord
import random
from discord.ext import commands
from discord import Interaction
import spot, futures
import example
import numpy as np


api_key = ""
api_secret = ""

def handle_message(message): 
    # handle websocket message
    print(message)

spot_client = spot.HTTP(api_key = api_key, api_secret = api_secret)
text = spot_client.account_information()
print(text)

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Game(name="discord.gg/Af4WKYZ2Ms"))
    print('We have logged in as {0.user}'.format(client))




@client.tree.command()
async def ping(interaction: Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong!...{bot_latency}ms")


@client.tree.command()
async def marksix(interaction: Interaction):    
    num = list(range(1, 47+1))
    random.shuffle(num)
    await interaction.response.send_message(num[0:6])




# FUTURES V1


# initialize WebSocket client
ws_futures_client = futures.WebSocket(api_key = api_key, api_secret = api_secret)

@client.tree.command()
async def futures_amount(interaction: Interaction):  
# initialize HTTP client
    futures_client = futures.HTTP(api_key = api_key, api_secret = api_secret)
# make http request to api
    await interaction.response.send_message(futures_client.open_positions())




@client.tree.command()
async def spot_amount(interaction: Interaction):  
    await interaction.response.send_message(spot_client.account_information())



@client.command()
async def buy(ctx, *symbol): 
    result_ = np.array(symbol)
    a = result_[0]
    b = result_[1]
    try:
        spot_client.test_new_order(a, 'BUY', 'MARKET',0,b)
        await ctx.send("成功用"+ b + "U買了 "+ str(symbol))
    except:
        await ctx.send("買不到 "+"，可能是沒有錢或是沒有這個幣種")
        raise


@client.command()
async def sell(ctx, *symbol): 
    result_ = np.array(symbol)
    a = result_[0]
    b = result_[1]
    try:
        await ctx.send(spot_client.new_order(a, 'SELL', 'MARKET',b ))
        await ctx.send("成功出售"+b+"顆 "+str(symbol))
    except:
        await ctx.send("賣不掉 "+"，可能是沒有這個幣種")
        raise



    ws_futures_client.order_stream(handle_message)
    



client.run('')
