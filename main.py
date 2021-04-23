import os
import discord
import requests
import json
import asyncio
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
client = discord.Client()

def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("http://stormy-atoll-92132.herokuapp.com/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"

    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = id

        id += 1

    return(qs, answer)


    

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):

    if message.content.lower() == "shinobi":
        await message.channel.send("https://tenor.com/view/hiding-the-simpsons-homer-simpson-bushes-disappearing-gif-8862897")
    if message.content.lower() == "shinobi bot":
        await message.channel.send("https://tenor.com/view/nope-baby-oops-not-here-gif-4671110")
    if message.content.lower() == "salut":
        await message.reply("Coucou :kissing_heart:")
    if message.content.lower() == "coucou":
        await message.reply("Hello :kissing_heart:")
    if message.content.lower() == "yo":
        await message.reply("Salutation :kissing_heart:")
    if message.content.lower() == "bonjour":
        await message.reply("Bonne journée :kissing_heart:")
    if message.content.lower() == "bonsoir":
        await message.reply("Bonne soirée :kissing_heart:")
    if message.content.lower() == "hello":
        await message.reply("Hi :kissing_heart:")
    if message.content.lower() == "hi":
        await message.reply("Hey :kissing_heart:")
    if message.content.lower() == "hey":
        await message.reply("Sup :kissing_heart:")
    if message.content.lower() == "sa ou fè":
        await message.reply("Sa ka maché :kissing_heart:")


    if message.content.lower() == '!quiz':
        qs, answer = get_question()
        await message.channel.send(qs)
    
        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send("Pfff.. t'es trop lent(e) :yawning_face: ")

        if int(guess.content) == answer:
            await message.reply("Bien joué ! :partying_face: ")
        else:
            await message.channel.send("Euh... Non :face_with_raised_eyebrow: ") 


client.run(os.getenv("TOKEN"))
