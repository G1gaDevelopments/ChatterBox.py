# --- IMPORTS --- #
import discord
from discord.ext import commands
from discord.ext import tasks

# --- COLOURS --- #
class ColourMain(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # --- UTIL FUNCTIONS --- #
    async def clearnl(self,content):  # this function gets rid of newlines
        s_content = str(content) # converts to string in case it is a different object type for some reason
        p_content = s_content.replace('\r', ' ').replace('\n', ' ') # clears newlines and carrage returns
        return p_content

    async def clearspaces(self,content,replacement="_"): # this replaces spaces with a given character
        s_content = str(content) # converts to string in case it is a different object type for some reason
        p_content = s_content.replace(' ', replacement) # replaces whitespace
        return p_content

    # --- COLOUR COMMANDS --- #
    @commands.command()
    async def red(self,ctx,*,content):
        content = await self.clearnl(content)
        await ctx.send("```diff"+"\n"+
                       f"- {content}"+"\n"+
                       "```")

    @commands.command()
    async def blue(self,ctx,*,content):
        content = await self.clearnl(content)
        await ctx.send("```ini"+"\n"+
                       f"[ {content} ]"+"\n"+
                       "```")

    @commands.command()
    async def green(self,ctx,*,content):
        content = str(content)
        await ctx.send("```css"+"\n"+
                       content+"\n"+
                       "```")

    @commands.command()
    async def orange(self,ctx,*,content):
        content = await self.clearnl(content)
        await ctx.send("```asciidoc"+"\n"+
                       f"[ {content} ]"+"\n"+
                       "```")

    @commands.command()
    async def yellow(self,ctx,*,content):
        content = str(content)
        await ctx.send("```fix"+"\n"+
                       content+"\n"+
                       "```")

    @commands.command(aliases=["teal"])
    async def cyan(self,ctx,*,content):
        content = await self.clearnl(content)
        await ctx.send("```py"+"\n"+
                       f"\" {content} \""+"\n"+
                       "```")

    @commands.command(aliases=["grey"])
    async def gray(self,ctx,*,content):
        await ctx.send("```cpp"+"\n"+
                       f"/* {content} */"+"\n"+
                       "```")

    @commands.command(aliases=["tex"])
    async def highlight(self,ctx,*,content):
        await ctx.send("```tex"+"\n"+
                       f"$ {content}"+"\n"+
                       "```")

# --- ADDING EXT --- #
def setup(bot):
    bot.add_cog(ColourMain(bot))