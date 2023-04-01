#!venv/bin/python3

import sys, os
import config
import pronoun_picker as pro_pick
import discord

token = config.BOT_TOKEN

bot = discord.Bot()


@bot.slash_command(description="Replies with a drop down menu that allows you to choose your pronouns!")
async def pronoun_picker(ctx):
    button_view = pro_pick.PronounButtons()
    await ctx.respond("Choose your pronouns!", view=button_view)

@bot.slash_command()
async def resources(ctx):
    await ctx.respond("resource stuff here")

@bot.slash_command()
async def hello(ctx, name: str = None, color: str = None):
    await ctx.respond(f"Hello, {name}! Your favorite color is {color}.")

bot.run(token)
