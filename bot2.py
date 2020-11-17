from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord
from discord.ext import commands
x = 1

bot = ChatBot('Norman')
trainer = ChatterBotCorpusTrainer(bot)
client = commands.Bot("$", self_bot = True)

if x < 15:
    trainer.train(
    "chatterbot.corpus.english"
)   
    x =+ 1
trainer = ChatterBotCorpusTrainer(bot)



@client.event
async def on_ready():
    print("bot is ready")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(""):
        response = bot.get_response(message.content)
        
        print(message.content)
        print(response)
        await message.channel.send(response)
client.run("Nzc4MDUyMjgyNzc5Njk3MTcy.X7MarA.2LWntOhBR7ZPDDvClkEBMMqqayA", bot=False)        
    
