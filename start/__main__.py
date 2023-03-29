#BATTLE

import discord
from discord.ext import commands
import random
from set_token import *

toke = token

bot = commands.Bot(command_prefix="b.",intents=discord.Intents.all())

E = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"

@bot.command()
async def howbattle(ctx):    
    await ctx.send("""Use b.roll, if 4- you start, if 4+ the "enemy" start, Then show your card, by abilities and HP you view who won.""")

@bot.command()
async def roll(ctx):
    if fight == "yes":
     await ctx.send(random.choice(E))

@bot.event
async def on_ready():
    print("hi world")

@bot.command()
async def fight(message, ctx):
    await message.channel.send("You fight {ctx.message.mentions[1].id}")
    fight = "yes"

bot.run(toke)