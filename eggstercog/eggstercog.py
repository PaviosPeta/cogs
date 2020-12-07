from redbot.core import commands
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate

class Eggstercog(commands.Cog):

    @commands.command()
    async def yeetus(self, ctx):
        """this yeets"""
        msg = await ctx.send("yeetus yeetus what is this deletus")
        start_adding_reactions(msg, "\N{EGG}")
        pred = ReactionPredicate.with_emojis(cls, "\N{EGG}")
        await ctx.bot.wait_for("reaction_add", check=pred)
        
        if pred.result: 
            await ctx.send("You have found the egg!")
        
    
