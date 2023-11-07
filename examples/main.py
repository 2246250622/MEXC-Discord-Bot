
import discord
import random
from discord.ext import commands
from discord import Interaction
from pymexc import spot, futures

api_key = "mx0vgloVgKopMEGcYt"
api_secret = "a75e6b3ef0c34815abc1781d6ae51a3c"

def handle_message(message): 
    # handle websocket message
    print(message)

    spot_client = spot.HTTP(api_key = api_key, api_secret = api_secret)
    print(spot_client.exchange_info())

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Game(name="discord.gg/Af4WKYZ2Ms"))
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def contract(ctx): 
# initialize HTTP client
    futures_client = futures.HTTP(api_key = api_key, api_secret = api_secret)
# make http request to api
    await ctx.send(futures_client.open_positions())

@client.command()
async def spot(ctx): 
# initialize HTTP client
    spot_client = spot.HTTP(api_key = api_key, api_secret = api_secret)
# make http request to api
    await ctx.send(spot_client.account_information())

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

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
async def contract(interaction: Interaction):  
# initialize HTTP client
    futures_client = futures.HTTP(api_key = api_key, api_secret = api_secret)
# make http request to api
    await interaction.response.send_message(futures_client.open_positions())




@client.tree.command()
async def spot(interaction: Interaction):  
    spot_client = spot.HTTP(api_key = api_key, api_secret = api_secret)
    await interaction.response.send_message(spot_client.account_information())

# create websocket connection to public channel (sub.tickers)
# all messages will be handled by function `handle_message`

    ws_futures_client.order_stream(handle_message)
    


client.run('NjQ0MjA2NTI4Mjk5MTM5MDcy.Gl0NyF.BmM6IJ8gGKsSRrGhYAj-ci7LIoQniKB214qe-U')