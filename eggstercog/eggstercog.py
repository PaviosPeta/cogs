from redbot.core import commands
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate

class Eggstercog(commands.Cog):   
    
#    async def random_spawn(self):
#        await self.bot.wait_until_ready()
#        while True:
#            try:
#                for guild in self.guildcache:
#                    if (
#                        self.guildcache[guild]["toggle"]
#                        and self.guildcache[guild]["activechannels"]
#                    ):
#                        if random.randint(1, 2) == 2:
#                            continue
#                        _guild = self.bot.get_guild(int(guild))
#                        if _guild is None:
#                            continue
#                        channel = _guild.get_channel(
#                            int(random.choice(self.guildcache[guild]["activechannels"]))
#                        )
#                        if channel is None:
#                            continue
#                        await self.spawn_pokemon(channel)
#                await asyncio.sleep(2400)
#            except Exception as exc:
#                log.error("Exception in pokemon auto spawning: ", exc_info=exc)
#
#                
#    async def spawnchance(self, ctx, _min: int, _max: int):
#        """Change the range of messages required for a spawn."""
#        if _min < 15:
#            return await ctx.send(_("Min must be more than 15."))
#        if _max < _min:
#            return await ctx.send(_("Max must be more than the minimum."))
#        await self.config.spawnchance.set([_min, _max])
#        await self.update_spawn_chance()
#        await ctx.tick()

    @commands.command()
    async def yeetus(self, ctx):
        """this yeets"""
        msg = await ctx.send("ai caramba")
        
        start_adding_reactions(msg, ["\N{EGG}"])
        pred = ReactionPredicate.with_emojis(["\N{EGG}"], msg)
        try:
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=60)
        except asyncio.TimeoutError:
            await self._clear_react(msg)
        
        if not pred.result:
            await ctx.send("You have found the egg!")
    
    @commands.command()
    async def egg(self, ctx): 
        await ctx.send("Where's the egg?")
