import requests
import discord
from discord.ext import commands

response = requests.get("https://dog.ceo/api/breeds/image/random").json()
print(response['message'])
img = response['message']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def dog(ctx):
    await ctx.send(img)

bot.run("MTEyMTUzNDI5NDUyODEwMjUzMQ.G0_SYw.GtKMRlnMjIJXvLzbHd4qEov_K45FeJXkw6FBfk")
