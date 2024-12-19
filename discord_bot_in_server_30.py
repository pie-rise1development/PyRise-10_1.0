import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents = intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name}: Душевный кризис был успешно пережит, можно дальше спокойно суетить свои дела! :-)))")

@bot.command()
async def piroschock(ctx): #/piroschock
    await ctx.send("Приветствую! Я ассистент создателя данного сервера на платформе Discord, бот...")

bot.run("")
