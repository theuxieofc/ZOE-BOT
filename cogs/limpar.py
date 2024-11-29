import discord
from discord.ext import commands

class Moderacao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='limpar', help='Limpa uma quantidade específica de mensagens.')
    async def limpar(self, ctx, quantidade: int):
        if not ctx.author.guild_permissions.administrator and ctx.author != ctx.guild.owner:
            await ctx.send("Você não tem permissão para usar este comando.", delete_after=10)
            return
        
        if quantidade <= 0:
            await ctx.send(" A quantidade de mensagens deve ser maior que zero.", delete_after=10)
            return

        deleted = await ctx.channel.purge(limit=quantidade + 1)

        await ctx.send(f"<:emoji_143:1310404613299503105> {len(deleted) - 1} mensagens foram excluídas com sucesso.", delete_after=10)

async def setup(bot):
    await bot.add_cog(Moderacao(bot))

#developer theuxie

#developer theuxie

#developer theuxie


#developer theuxie
