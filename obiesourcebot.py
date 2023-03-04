#!venv/bin/python3

import sys, os
import config
import discord

token = config.BOT_TOKEN

bot = discord.Bot()

# --------------------
# COMMANDS
# --------------------

@bot.slash_command()
async def resources(ctx):
    await ctx.respond("resource stuff here")

@bot.slash_command()
async def hello(ctx, name: str = None, color: str = None):
    await ctx.respond(f"Hello, {name}! Your favorite color is {color}.")

@bot.slash_command()
async def pronoun_picker(ctx):
    await ctx.respond("Hello Person.")

bot.run(token)
