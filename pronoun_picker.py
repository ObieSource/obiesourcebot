#!venv/bin/python3

import sys, os
import config
import discord
from discord.utils import get


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
            lines[i] = f"{user_ID} {pronouns}\n"
    file.writelines(lines)

# ---------------------
# Classes
# ---------------------

#This is a visual class that inherits from discord.ui.view
#It has a specific format and is required when working with dropdown menus
class PronounButtons(discord.ui.View):

    @discord.ui.select(
        placeholder = "Pick a pronoun", #The text displayed when nothing has been selected
        min_values = 1, #The minimum amount of items that can be selected
        max_values = 1, #The maximum amount of items that can be selected
        options = [
            discord.SelectOption(
                label="He/Him"
            ),
            discord.SelectOption(
                label="He/They"
            ),
            discord.SelectOption(
                label="They/He"
            ),
            discord.SelectOption(
                label="They/Them"
            ),
            discord.SelectOption(
                label="They/She"
            ),
            discord.SelectOption(
                label="She/They"
            ),
            discord.SelectOption(
                label="She/Her"
            )
        ]
    )

    #This is a specific method with a specific signature that runs when a dropdown menu option has been selected
    async def select_callback(self, select, interaction):
        pronoun = select.values[0]
         #This will be set to the users place in the pronoun list
        place_in_pronouns = -1
        author_id = str(interaction.user.id)
        for i in range(len(pronouns)):
            if author_id == pronouns[i][0]:
                place_in_pronouns = i

        if place_in_pronouns == -1:
            pronouns.append([author_id, pronoun])
            role = get(interaction.guild.roles, name=pronoun)
            if role:
                await interaction.user.add_roles(role.id)
            else:
                guild = interaction.guild
                await guild.create_role(name=pronoun)
                new_role = get(interaction.guild.roles, name=pronoun)
                await interaction.user.add_roles(new_role)
            
            add_pronouns("pronouns.txt", author_id, pronoun)
        else:
            #removes the previous pronoun associated with the user
            prev_role = get(interaction.guild.roles, name=(pronouns[place_in_pronouns][1]))
            if prev_role:
                await interaction.user.remove_roles(prev_role)
                
            pronouns[place_in_pronouns][1] = pronoun
            change_existing_pronouns("pronouns.txt", author_id, pronoun)

            #finds the pronoun in roles and adds it to a user
            role = get(interaction.guild.roles, name=pronoun)
            if role:
                await interaction.user.add_roles(role)
            else:
                guild = interaction.guild
                await guild.create_role(name=pronoun)
                new_role = get(interaction.guild.roles, name=pronoun)
                await interaction.user.add_roles(new_role)


        if pronoun == None:
            await interaction.response.send_message("Your pronouns were set to None. I shall not refer to you.")
        else:
            await interaction.response.send_message(f"Hello {interaction.user.name}!. I will refer to you as {pronoun}.")

#2 dimentional array. pronouns[][0] is the user ID and pronouns[][1]
pronouns = []
initialize_pronouns("pronouns.txt")
