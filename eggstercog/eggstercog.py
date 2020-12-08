from redbot.core import commands
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.mod import slow_deletion
import asyncio

class Eggstercog(commands.Cog):   

    @commands.command()
    async def egg(self, ctx):
        """activates an egg"""
        msg = await ctx.send("What's that over there?")
        
        start_adding_reactions(msg, ["\N{EGG}"])
        pred = ReactionPredicate.with_emojis(["\N{EGG}"], msg)
        try:
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=10)
        except asyncio.TimeoutError:
            slow_deletion(msg)
            await ctx.send("Someone destroyed the egg!")
        
        if not pred.result:
            await ctx.send("You have found the egg!")
    
    @commands.command()
    async def whereegg(self, ctx): 
        await ctx.send("Where's the egg?")
        
    @commands.command()
    async def eggboard(self, ctx): 
        """This is where the leaderboard is supposed to go."""
        await ctx.send("This is where the leaderboard ist supposed to go.")
        
    @commands.command()
    async def eggchannel(self, ctx): 
        """You should be able to set the channel with this. Eventually."""
        await ctx.send("This is where you'd be able to set the channel.")
