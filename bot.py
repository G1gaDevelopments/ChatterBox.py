# --- IMPORTS --- #
import discord
from discord.ext import commands
from discord.ext import tasks
import random

# --- MULTIPLE PREFIX SETUP --- #
def getprefix(bot,msg):
    prefixes = ["cb!","%","cb%"]
    if not msg.guild: # only allow cb! to be used in dms
        return "cb!"
    return commands.when_mentioned_or(*prefixes)(bot, msg)

# --- BOT SETUP --- #
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=getprefix,intents=intents)
bot.remove_command("help") # remove default help command

ext_names = ["cogs.testcog","cogs.colour","cogs.util"] # add all cog/extension names here
for ext in ext_names:
    print(f"LOADING EXT {ext}")
    bot.load_extension(ext) # load every ext
    print(f"LOADED EXT {ext}")

@tasks.loop(seconds = 12.0)
async def refresh_status():
    act = random.choice(["cb!help","with colours | cb!help","[WEBSITE HERE] | cb!help","the fool | cb!help"])
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.playing, name = act))

# --- STARTING SEQUENCE --- #
@bot.event
async def on_ready():
    print("BOT TOKEN PROCESSED")
    refresh_status.start()
    print("RPC CHANGING")

f = open("token.txt","r")
TOKEN = f.read()
print("READING BOT TOKEN")
bot.run(TOKEN)
