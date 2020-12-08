# --- IMPORTS --- #
import discord
from discord.ext import commands
from discord.ext import tasks

# --- TEST COMMAND --- #
class TestCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def testcmd(self,ctx):
        await ctx.send("Hello World! The cogs are working!")

def setup(bot):
    bot.add_cog(TestCog(bot))