import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

with open("bad.txt", 'r', encoding='utf8') as file: x = file.read().split('\n')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for i in x:
        if i in message.content.lower():
            await message.author.send(f"you have been banned for using cuss word: {i}")
            await message.author.ban(reason="Cussing", delete_message_seconds=600)
            await message.channel.send(f"{message.author} is banned for using cuss word: {i}")
            break


bot.run('token')
