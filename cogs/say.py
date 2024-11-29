import discord
from discord.ext import commands
#developer theuxie
class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say')
    async def say(self, ctx, *, message: str):
        embed = discord.Embed(
            description=message,
            color=discord.Color.random()
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        embed.timestamp = ctx.message.created_at #developer theuxie
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Say(bot))



#developer theuxie

#developer theuxie
#developer theuxie
#developer theuxie

#developer theuxie
#developer theuxie