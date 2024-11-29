import discord
from discord.ext import commands

class UnlockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        overwrites = ctx.channel.overwrites_for(ctx.guild.default_role)
        if overwrites.send_messages is True:
            await ctx.send(f"<a:2lteas:1296880663848554538> | {ctx.author.mention} Este canal já está desbloqueado! Use `..lock` para travar!")
        else:
            overwrites.send_messages = True
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"🎉 | {ctx.author.mention} Canal desbloqueado com sucesso! Use `..lock` para travar!")

async def setup(bot):
    await bot.add_cog(UnlockCog(bot))


#developer theuxie


#developer theuxie

#developer theuxie
#developer theuxie
#developer theuxie
