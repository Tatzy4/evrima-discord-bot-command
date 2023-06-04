# -*- coding: utf-8 -*-

import discord
import socket
import time
import sys
import os
from discord.ext import commands

__author__ = "Tatzy"


TOKEN = 'bot token here'

ip = "140.40.240.240"
port = 88888
password = b"RCONpass123"
timeout = 5

intents = discord.Intents().all()
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("made by tatzy#2190")

@bot.command(name='evrima-announce')
@commands.has_role(nitro boost id rank)  # Add the role ID that is required to use the command
async def send_announcement(ctx, *, announcement):
    announce_packet = bytes('\x02', 'utf-8') + bytes('\x10', 'utf-8') + announcement.encode() + bytes('\x00', 'utf-8')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        s.send(announce_packet)
        time.sleep(1)  # Wait for the announcement to be sent (adjust the sleep duration if needed)

    await ctx.send("**`Everything went good (bot made by tatzy#2190)`**")

@send_announcement.error
async def send_announcement_error(ctx, error):
    if isinstance(error, commands.MissingRole):  # Handle the case where the user doesn't have the required role
        await ctx.send("**`U dont boost server `**")

bot.run(TOKEN)
