import discord
from discord.ext import commands
from datetime import timedelta

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mute", help="Aplica um castigo (mute) a um membro do servidor.")
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, membro: discord.Member, duration: int = None, *, motivo: str = None):
        if duration is None:
            await ctx.reply(embed=self.error_embed("Você precisa fornecer a duração do mute em segundos."))
            return

        if membro == ctx.author:
            await ctx.reply(embed=self.error_embed("Você não pode se mutar."))
            return
        if membro == self.bot.user:
            await ctx.reply(embed=self.error_embed("Eu não posso me mutar."))
            return

        try:
            until_time = discord.utils.utcnow() + timedelta(seconds=duration)
            await membro.edit(timed_out_until=until_time, reason=motivo)

            embed = discord.Embed(
                title=f"⚠️ {membro} foi mutado",
                description=f"Duração: {duration} segundos.",
                color=discord.Color.orange()
            )
            if motivo:
                embed.add_field(name="📜 Motivo", value=motivo, inline=False)
            embed.set_footer(text=f"Mutado por {ctx.author}", icon_url=ctx.author.avatar.url)
            await ctx.reply(embed=embed)

            try:
                dm_embed = discord.Embed(
                    title="⚠️ Você foi mutado",
                    description=f"Você foi mutado no servidor **{ctx.guild.name}** por {duration} segundos.",
                    color=discord.Color.orange()
                )
                if motivo:
                    dm_embed.add_field(name="📜 Motivo", value=motivo, inline=False)
                await membro.send(embed=dm_embed)
            except discord.Forbidden:
                pass

        except discord.Forbidden:
            await ctx.reply(embed=self.error_embed("Eu não tenho permissão para mutar esse membro."))
        except Exception as e:
            await ctx.reply(embed=self.error_embed(f"Ocorreu um erro: {e}"))

    def error_embed(self, description):
        return discord.Embed(title="❌ Erro", description=description, color=discord.Color.red())

async def setup(bot):
    await bot.add_cog(Mute(bot))

#developer theuxie
#developer theuxie


#developer theuxie
#developer theuxie
#developer theuxie

#developer theuxie
#developer theuxie
