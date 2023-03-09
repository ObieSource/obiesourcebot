#!venv/bin/python3

import sys, os
import config
import discord

token = config.BOT_TOKEN
#A list of all pronouns. The first indecy refers to a user. The second indicy will be of size 2 where 0 is the username and 1 is the pronoun.
pronouns[0][0]
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
async def pronoun_picker(ctx, pronoun: str = None):
    #This will be set to the users place in the pronoun list
    place_in_pronouns = -1

    for i in range(len(pronouns)):
        if ctx.author.name == pronouns[i][0]:
            place_in_pronouns = i

    if place_in_pronouns == -1:
        pronouns.append({ctx.author.name, pronoun})

    if pronoun == None:
        await ctx.respond("Your pronouns were set to None. I shall not refer to you.")
    else:
        await ctx.respond(f"Hello {ctx.author.name}!. I will refer to you as {pronoun}")

bot.run(token)


def initialize_pronouns(file_name):
    file = open(file_name)
    lines = file.readlines()
    for i in range (len(lines)):
        line = lines[i].split(" ")
        pronouns[i][0] = line[0]
        pronouns[i][1] = line[1]
    file.close()