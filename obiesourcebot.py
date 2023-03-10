#!venv/bin/python3

import sys, os
import config
import discord

token = config.BOT_TOKEN
#A list of all pronouns. The first indecy refers to a user. The second indicy will be of size 2 where 0 is the user id and 1 is the pronoun.
pronouns = []

bot = discord.Bot()

# ---------------------
# HELPER METHODS
# ---------------------

def initialize_pronouns(file_name):
    file = open(file_name)
    lines = file.readlines()
    for i in range (len(lines)):
        line = lines[i].split(" ")
        #appends a new array on to pronouns with the user id (stored in line[0]) and pronouns (stored in line[1])
        pronouns.append([line[0], line[1]])
        pronouns[i][1] = line[1]
    file.close()

def add_pronouns(file_name, user_ID, pronouns):
    #Opens the file in append mode
    file = open(file_name, "a+")
    file.writelines([f"{user_ID} {pronouns}\n"])
    file.close()

def change_existing_pronouns(file_name, user_ID, pronouns):
    #Opens the readable version of the file to get its lines
    file = open(file_name)
    lines = file.readlines()
    #Closes the readable version of the file and opens the writeable version
    #You cant read a file in writeable mode
    file.close()
    file = open(file_name, "w")

    for i in range (len(lines)):
        if lines[i].__contains__(user_ID):
            lines[i] = f"{user_ID} {pronouns}"
    file.writelines(lines)


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
    author_id = str(ctx.author.id)
    for i in range(len(pronouns)):
        if author_id == pronouns[i][0]:
            place_in_pronouns = i

    if place_in_pronouns == -1:
        pronouns.append([author_id, pronoun])
        add_pronouns("pronouns.txt", author_id, pronoun)
    else:
        pronouns[i][1] = pronoun
        change_existing_pronouns("pronouns.txt", author_id, pronoun)


    if pronoun == None:
        await ctx.respond("Your pronouns were set to None. I shall not refer to you.")
    else:
        await ctx.respond(f"Hello {ctx.author.name}!. I will refer to you as {pronoun}.")


initialize_pronouns("pronouns.txt")

bot.run(token)
