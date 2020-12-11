# --- IMPORTS --- #
import discord
from discord.ext import commands
from discord.ext import tasks

# --- TEST COMMAND --- #
class UtilCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=["status","latency"])
    async def ping(self,ctx):
        ping = client.latency * 1000
        ping = round(ping)

        if ping < 300:
            c = discord.Colour.green()
            status_msg = "Online"
        elif ping < 700:
            c = discord.Colour.gold()
            status_msg = "Slowing Down"
        else:
            c = discord.Colour.red()
            status_msg = "OH GOD THE LAG"

        embed = discord.Embed(title = "ChatterBox.py",colour=c)
        embed.add_field(name="Pong!", value = f":ping_pong: My latency is {ping}ms!", inline = False)
        embed.add_field(name="Version",value="1.0",inline = True)
        embed.add_field(name="Status",value=status_msg,inline = True)
        embed.add_field(name="Experiencing problems?", value = "DM macpherson#1415 for help!", inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title = "Need Help?", colour = discord.Colour.green(),
                              description = ":page_facing_up: A list of commands can be found [here](https://github.com/Errorcrafter/ChatterBox.py/blob/main/commandlist.md)!\n\n"+
                              ":open_file_folder: This bot is open source! Find it on Github [here](https://github.com/Errorcrafter/ChatterBox.py).\n\n"+
                              ":question: Still lost? Join our [support server](https://www.example.com)!")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UtilCog(bot))