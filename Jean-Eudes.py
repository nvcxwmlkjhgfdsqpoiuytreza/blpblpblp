import random
import re
import os
import discord
from discord.ext import commands

# Infos bot

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot = commands.Bot(command_prefix='<3 ')

bot.run(os.getenv('TOKEN'))

# arrivées/départs

@bot.event
async def on_member_join(member):
    channel = member.server.get_channel("474646016004718593")
    regles = member.server.get_channel("557599004695724042")
    await bot.send_message(channel, member.mention + 'Hey! Salut toi! Bienvenue au repère du doublage! Ici tu pourras'
                                                     ' suivre les actualités de ma chaîne YouTube et mes futurs projets'
                                                     ' ! Une fois que tu auras pris connaissance des '
                                                     + regles.mention + 'de ce serveur, tu pourras commencer ton '
                                                      'périple ici ! Amuse toi bien et à bientôt! :smile: ' )

    role = discord.utils.get(member.server.roles, name="Abonnés ♥")
    await bot.add_roles(member, role)

@bot.event
async def on_member_remove(member):
    channel = member.server.get_channel("474646016004718593")
    await bot.send_message(channel, "**" + member.name + "** nous a quittés... on espère te revoir bientôt.")
