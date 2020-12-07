from redbot.core import commands
from redbot.core.utils.menus import start_adding_reactions

class Eggstercog(commands.Cog):

    @commands.command()
    async def yeetus(self, ctx):
        """this yeets"""
        msg = await ctx.send("yeetus yeetus what is this deletus")
        start_adding_reactions(msg, "\N{EGG}")
        
        
    
