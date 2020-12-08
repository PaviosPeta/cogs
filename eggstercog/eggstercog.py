from redbot.core import commands
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.mod import slow_deletion
import asyncio
import time

class Eggstercog(commands.Cog):   
    
    global buul 
    buul = True
    
    def refreshBuul(a: boolean): 
        a = buul
        return a
    
    @commands.command()
    async def egg(self, ctx):
        """activates an egg"""
        msg = await ctx.send("What's that over there?")
        a = 0
        start_adding_reactions(msg, ["\N{EGG}"])
        pred = ReactionPredicate.with_emojis(["\N{EGG}"], msg)
        try:
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=10)
            a = 1
        except asyncio.TimeoutError:
            await slow_deletion([msg])
            await ctx.send("Someone destroyed the egg!")
        
        if not pred.result and a == 1:
            await ctx.send("You have found the egg!")
    
    @commands.command()
    async def whereegg(self, ctx):
        x=0
        await self.bot.wait_until_ready()
        yeet = True
        
        while yeet and x < 10:
            try:
                for guild in self.guildcache:
                    const channel = guild.channels.cache.find(channel => channel.name === 'madster');
#                        if random.randint(1, 2) == 2:
 #                           continue
  #                      _guild = self.bot.get_guild(int(guild))
   #                     if _guild is None:
    #                        continue
     #                   channel = _guild.get_channel(
      #                      int(random.choice(self.guildcache[guild]["activechannels"]))
       #                 )
                    if channel is None:
                         continue
                        
                    await ctx.send("Where egg?")
                await asyncio.sleep(2)
                x+=1
                yeet = refreshBuul(yeet)
            except Exception as exc:
                log.error("that went wrong: ", exc_info=exc)
                break
            

            
    @commands.command()
    async def thereegg(self, ctx): 
        buul=False
        
    @commands.command()
    async def eggboard(self, ctx): 
        """This is where the leaderboard is supposed to go."""
        await ctx.send("This is where the leaderboard ist supposed to go.")
        
    @commands.command()
    async def eggchannel(self, ctx): 
        """You should be able to set the channel with this. Eventually."""
        await ctx.send("This is where you'd be able to set the channel.")
