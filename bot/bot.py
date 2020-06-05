import discord
import requests

client = discord.Client()

cmd1 = '$olc'
cmd2 = '$phrase'

@client.event
async def on_ready():
    print('Logged in successfully.')

@client.event
async def on_message(message):
    if message.content.startswith(cmd1):
        olc = message.content[len(cmd1):] # rest of code
        req = requests.get('http://localhost:8000/lookup_olc?olc=' + olc) # http://localhost:8000/lookup_olc?olc=849VCWC8+R9
        json = req.json()
        await message.channel.send(olc + "'s phrase is: " + '**' + json['phrase'] + '**')

    if message.content.startswith(cmd2):
        phrase = message.content[len(cmd2):] # rest of phrase
        req = requests.get('http://localhost:8000/lookup_phrase?phrase=white.horse.body.girl.stead') # http://localhost:8000/lookup_phrase?phrase=white.horse.body.girl.stead
        json = req.json()
        await message.channel.send(phrase + "'s OLC is: " + '**' + json['olc'] + '**')

client.run('INSERT-TOKEN-HERE')