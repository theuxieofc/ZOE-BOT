import discord
from discord.ext import commands

#developer theuxie
class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member_id: int):
        """Desbane um usuário utilizando o ID global."""
        try:
            user = await self.bot.fetch_user(member_id)
            await ctx.guild.unban(user)

            await ctx.send(f"🎉 {ctx.author.mention} Prontinho, o usuário foi desbanido! Só espero que ele não quebre as regras novamente né.")

        except discord.NotFound:
            await ctx.send(
                "@nevisk/off\n"
                "Eu procurei em todo o lugar, mas não encontrei nenhum usuário com esse ID!\n"
                "Lembre-se, eu procuro usuários por **IDs**, **menções** e **nomes**."
            )

        except discord.Forbidden:
            await ctx.send("⚠️ Não tenho permissão para desbanir esse usuário.")

        except discord.HTTPException:
            await ctx.send("❗ Ocorreu um erro ao tentar desbanir o usuário.")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("⚠️ Você não tem permissão para desbanir membros.")

        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Por favor, forneça um ID válido.")

        else:
            await ctx.send("❗ Ocorreu um erro inesperado.")

async def setup(bot):
    await bot.add_cog(UnbanCog(bot))
