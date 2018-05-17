import tweepy
import discord
from urllib.parse import urlparse
from credentials import *


client = discord.Client()



auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!t'):
        msg = message.content
        #await client.send_message(message.channel, msg[2:])
        await api.update_status(status=msg[2:])
    
    if message.content.startswith('!r'):
        msg = message.content[3:]
        domain = urlparse(msg).hostname.split('.')[0]
        if domain == 'twitter':
            path = urlparse(msg).path.split('/')
            tID = path[3]
            api.retweet(tID)

    if message.content.startswith('!l'):
        msg = message.content[3:]
        domain = urlparse(msg).hostname.split('.')[0]
        if domain == 'twitter':
            path = urlparse(msg).path.split('/')
            tID = path[3]
            api.create_favorite(tID)

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(TOKEN)