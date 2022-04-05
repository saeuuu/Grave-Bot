import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="prefix")

@bot.event
async def on_connect():
  print ("Bot Ready")

  
@bot.command()
async def commandname(ctx):
  await ctx.send("")

  
@bot.command()
async def commandname(ctx):
  await ctx.send("")

  
@bot.command()
async def commandname(ctx):
  await ctx.send("")

  
@bot.command()
async def commandname(ctx):
  await ctx.send("")
  
@bot.command()
async def commandname(ctx):
  await ctx.send("")

@bot.command()
async def commandname(ctx):
  await ctx.send("")

@bot.command()
async def commandname(ctx):
  await ctx.send("")

@bot.command()
async def commandname(ctx):
  await ctx.send("")

@bot.command()
async def commandname(ctx):
  await ctx.send("")

@bot.command()
async def commandname(ctx):
  await ctx.send("")

@bot.command()
async def commandname(ctx):
  await ctx.send("")

token=("TOKEN") 
bot.run(token)
