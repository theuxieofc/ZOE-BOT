import discord
from discord.ext import commands

class LockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        overwrites = ctx.channel.overwrites_for(ctx.guild.default_role)
        if overwrites.send_messages is False:
            await ctx.send(f" | {ctx.author.mention} Este canal já está bloqueado! Use `&unlock` para destravar!")
        else:
            overwrites.send_messages = False
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"🎉 | {ctx.author.mention} Canal bloqueado com sucesso! Use `&unlock` para destravar!")

async def setup(bot):
    await bot.add_cog(LockCog(bot))


#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
