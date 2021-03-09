import discord
from discord.ext import commands
from colorama import Fore, Style
from threading import Thread
import asyncio
import json
import requests
import os

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
reset = Fore.RESET
magenta = Fore.MAGENTA
cyan = Fore.CYAN
token = input(f"{reset}[{green}+{reset}] Token : ")
prefix = input(f"{reset}[{green}+{reset}] Prefix : ")
os.system('clear')
Ylum = commands.Bot(command_prefix=prefix,self_bot=True)

@Ylum.event
async def on_connect():
  os.system('clear')
  print(f""""
{red}──────────────────────────────────────

        {magenta}╦ ╦  ╦    ╦ ╦  ╔╦╗
        {magenta}╚╦╝  ║    ║ ║  ║║║
         {magenta}╩   ╩═╝  ╚═╝  ╩ ╩
      
{red}    Logged In As: {Ylum.user.name}#{Ylum.user.discriminator}
{red}    Guilds: {Ylum.user.guilds}

{red}──────────────────────────────────────""")

@Ylum.command()
async def edit(ctx, *, name):
  await ctx.guild.edit(name=name)
  print(f"{reset}[{green}+{reset}] Used Command Edit ")

  print(f"{reset}[{green}+{reset}] Edited From {ctx.guild.name} To {name}")

@Ylum.command()
async def mban(ban):
  try:
    for nigger in ban.guild.users:
      await nigger.ban(reason="Ylum Nuker")
      print(f"{reset}[{green}+{reset}] Banned {nigger}")
  except:
       print(f"{reset}[{green}+{reset}] Couldnt Ban {nigger}")
@Ylum.command()
async def mkick(kick):
  try:
    for nigger in kick.guild.users:
      await nigger.ban(reason="Ylum Nuker")
      print(f"{reset}[{green}+{reset}] Kicked {nigger}")
  except:
       print(f"{reset}[{green}+{reset}] Couldnt Kick {nigger}")       
       
@Ylum.command(aliases=["help", "commands", "nigger"])
async def cmd(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
 embed.set_author(name="; 😈 𝘠𝘓𝘜𝘔 𝘕𝘜𝘒𝘌𝘙 😈 ; ", icon_url=ctx.author.avatar_url)
 embed.add_field(name="edit", value="; Edits Server Name To What You Want", inline=False)
 embed.add_field(name="mban", value="; Bans All Users Below You ;", inline=False)
 embed.add_field(name="mkick", value="; Kicks All Users Below You ;",inline=False)
 embed.set_image(url="https://cdn.discordapp.com/attachments/817916070110691330/817920901231935518/38C0BE6D-F61C-4BBA-B5A4-5A8D5B306CAE.gif")
 embed.set_footer(text="Logged In As YlumV1")
 embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817916070110691330/817920901231935518/38C0BE6D-F61C-4BBA-B5A4-5A8D5B306CAE.gif")
 await ctx.send(embed=embed)
\

Ylum.run(token,bot=False) 
