import discord
from discord.ext import commands
import traceback

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', description="Bane um usuário do servidor")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member_id: int = None, *, reason: str = "Nenhum motivo fornecido"):
        if member_id is None:
            await ctx.send("**Por favor, forneça o ID do usuário para banir!**")
            return

        if member_id == ctx.author.id:
            await ctx.send("**Você não pode se banir!**")
            return

        try:
            user = await self.bot.fetch_user(member_id)

            user_name = user.name if hasattr(user, "name") else "Usuário Desconhecido"
            user_discriminator = user.discriminator if hasattr(user, "discriminator") else "0000"

            await ctx.guild.ban(user, reason=reason)

            await ctx.send(f"🎉 | {ctx.author.mention}, o usuário {user.mention} foi banido com sucesso. Não quebrou as regras, né?")

        except discord.NotFound:
            await ctx.send("**Não encontrei nenhum usuário com esse ID.**")
        except discord.Forbidden:
            await ctx.send("**Eu não tenho permissão para buscar ou banir este usuário.**")
        except discord.HTTPException as e:
            await ctx.send(f"**Ocorreu um erro ao tentar processar o banimento: {e}**")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            traceback.print_exc()
            await ctx.send("**Ocorreu um erro inesperado, verifique os logs do bot para mais detalhes.**")

    @ban.error
    async def ban_error(self, ctx, error):
        print(f"Erro no comando ban: {str(error)}")
        traceback.print_exc()
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("**Você não tem permissão para banir membros.**")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("**Por favor, forneça um ID válido (somente números).**")
        else:
            await ctx.send("**Ocorreu um erro inesperado.**")

async def setup(bot):
    await bot.add_cog(Ban(bot))


#developer theuxie


#developer theuxie

#developer theuxie

#developer theuxie



#developer theuxie

#developer theuxie



