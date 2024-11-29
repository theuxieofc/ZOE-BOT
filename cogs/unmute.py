import discord
from discord.ext import commands

#developer theuxie
class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unmute", help="Remove o castigo de um membro.")
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, ctx, membro: discord.Member):
        try:
            if not membro.timed_out_until:
                await ctx.reply(embed=self.error_embed("Este membro não está mutado."))
                return

            await membro.edit(timed_out_until=None)

            embed = discord.Embed(
                title=f"✅ Mute removido de {membro}",
                description="O membro não está mais mutado.",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Removido por {ctx.author}", icon_url=ctx.author.avatar.url)
            await ctx.reply(embed=embed)

            try:
                dm_embed = discord.Embed(
                    title="✅ Mute removido",
                    description=f"Seu mute foi removido no servidor **{ctx.guild.name}**.",
                    color=discord.Color.green()
                )
                await membro.send(embed=dm_embed)
            except discord.Forbidden:
                pass

        except discord.Forbidden:
            await ctx.reply(embed=self.error_embed("Eu não tenho permissão para remover o mute desse membro."))
        except Exception as e:
            await ctx.reply(embed=self.error_embed(f"Ocorreu um erro: {e}"))

    def error_embed(self, description):
        return discord.Embed(title="❌ Erro", description=description, color=discord.Color.red())


async def setup(bot):
    await bot.add_cog(Unmute(bot))



    #developer theuxie
    #developer theuxie
    #developer theuxie
    #developer theuxie
    #developer theuxie
    