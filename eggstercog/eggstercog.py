from redbot.core import commands
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate

class Eggstercog(commands.Cog):

    @commands.command()
    async def yeetus(self, ctx):
        """this yeets"""
        msg = await ctx.send("yeetus yeetus what is this deletus")
#        start_adding_reactions(msg, "\N{EGG}")
 #       pred = ReactionPredicate.with_emojis("\N{EGG}", msg)
  #      try: 
   #         await ctx.bot.wait_for("reaction_add", check=pred, timeout = 60)
    #    except asyncio.TimeoutError: 
     #       await self._clear_react(msg)
      #  
       # if pred.result: 
        #    await ctx.send("You have found the egg!")
        
        start_adding_reactions(msg, "\N{EGG}")
        pred = ReactionPredicate.with_emojis(["\N{EGG}", "\N{WHITE HEAVY CHECK MARK}"], msg)
        try:
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=60)
        except asyncio.TimeoutError:
            await self._clear_react(msg)
        
        if pred.result:
            await ctx.send("yeet")
        
    
