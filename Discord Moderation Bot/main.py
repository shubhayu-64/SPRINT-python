# Discord Moderation Bot by Shubhayu Majumdar
# Build for Clinify-Open-Sauce => SPRINT-python
# Github: shubhayu64
# Invite the bot in your server via: https://discord.com/api/oauth2/authorize?client_id=867299749438554134&permissions=8&scope=bot

import discord
from discord.ext import commands, tasks
import base64
import config

# The prefix set for the bot
client = commands.Bot(command_prefix='m.')


# Prints a message once bot becomes ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Sprint-Python"))
    print(f'{client.user} is running')


# Warn User
@client.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{member.mention} You are being warned for {reason}")


# Kick user
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{member.mention} kicked out for {reason}")
    await member.kick(reason=reason)


# Ban User
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{member.mention} banned for {reason}")
    await member.ban(reason=reason)

# Main function: Takes in token from config.py
if __name__ == "__main__":
    client.run(base64.b64decode(config.token).decode("ascii"))
