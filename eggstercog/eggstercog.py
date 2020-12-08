from redbot.core import bot, commands
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.mod import slow_deletion
import asyncio
import time
import discord

class Eggstercog(commands.Cog):   
    
    global buul 
    
    async def refreshBuul(self, a: bool): 
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
    async def dennis(self, ctx): 
        """yeet"""
        buul = True
        thang = True
        yikes = 0
        while yikes<5: 
            yikes +=1
            await ctx.send("this is dennis")
            time.sleep(3)
            thang = self.refreshBuul(self, thang)
#            thang = buul
            await ctx.send(thang)
            if thang == False: 
                await ctx.send("oke i stop")
                break
    
    
    
    @commands.command()
    async def whereegg(self, ctx):
        """wirft zwar keinen fehler mehr, aber halt doch."""
        
        x=0
        yeet = True
        
        while yeet and x < 10:
            try:
                #for guild in bot.guilds:
                
                 #   channel = guild.channels.cache.find('madster');
                for guild in bot.guilds:
                    _guild = bot.get_guild(int(guild))
                    await _guild.get_channel(696395792742613083)
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
            except Exception:
                await ctx.send("taht went wrong")
                break
            

            
    @commands.command()
    async def there(self, ctx): 
        buul=False
        await ctx.send("it is wrong now")
#        return buul
        
    @commands.command()
    async def eggboard(self, ctx): 
        """This is where the leaderboard is supposed to go."""
        await ctx.send("This is where the leaderboard ist supposed to go.")
        
    @commands.command()
    async def eggchannel(self, ctx): 
        """You should be able to set the channel with this. Eventually."""
        await ctx.send("This is where you'd be able to set the channel.")
