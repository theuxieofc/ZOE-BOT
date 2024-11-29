import discord
from discord.ext import commands
from discord.ui import Button, View
import logging
import traceback

#developer theuxie
logging.basicConfig(
    filename='erros.txt', 
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filemode='a'
)

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo')
    async def userinfo(self, ctx, member_id: str = None):
        try:
            if member_id is None:
                member = ctx.author
            else:
                try:
                    member = await self.bot.fetch_user(member_id)
                except discord.NotFound:
                    await ctx.send("Não foi possível encontrar o usuário com esse ID.")
                    return

            user_info_embed = discord.Embed(
                title="Informações do Usuário",
                color=discord.Color.blue()
            )
            user_info_embed.set_thumbnail(url=member.avatar.url)
            user_info_embed.add_field(name="<:wumpachu:1310301053279010877> Nick", value=member.name, inline=False)
            user_info_embed.add_field(name="<:ID:1310301999920709712> ID do Discord", value=member.id, inline=False)
            user_info_embed.add_field(name="<:7442users:1310302819638579280> Tag do Discord", value=f"@{member}", inline=False)
            user_info_embed.add_field(
                name="📅 Data de Criação da Conta", 
                value=member.created_at.strftime("%d/%m/%Y %H:%M:%S"), 
                inline=False
            )

            server_info_embed = None
            permissions_button = None
            if ctx.guild:
                member_in_guild = ctx.guild.get_member(member.id)
                if member_in_guild:
                    server_info_embed = discord.Embed(
                        title="Informações do Membro no Servidor",
                        color=discord.Color.green()
                    )

                    join_date = member_in_guild.joined_at.strftime("%d/%m/%Y %H:%M:%S") if member_in_guild.joined_at else "Desconhecida"
                    server_info_embed.add_field(name="📅 Data de Entrada no Servidor", value=join_date, inline=False)

                    highest_role = member_in_guild.top_role.mention if member_in_guild.top_role else "Nenhum"
                    server_info_embed.add_field(name="<:dwn_Staffs:1308967098382422119> Cargo Mais Alto", value=highest_role, inline=False)
                    server_info_embed.add_field(name="✅ Informações Adicionais", value="Verificação de Membro Concluída", inline=False)

                    permissions_button = Button(
                        label="Permissões do Membro",
                        style=discord.ButtonStyle.primary,
                        custom_id="permissions_button"
                    )

            avatar_button = Button(
                label="Ver Avatar Global", 
                style=discord.ButtonStyle.primary, 
                custom_id="avatar_button"
            )

            view = View()
            view.add_item(avatar_button)

            if permissions_button:
                view.add_item(permissions_button)

            if server_info_embed:
                await ctx.send(embeds=[user_info_embed, server_info_embed], view=view)
            else:
                await ctx.send(embeds=[user_info_embed], view=view)

            async def avatar_callback(interaction):
                try:
                    if interaction.data['custom_id'] == "avatar_button":
                        avatar_embed = discord.Embed(
                            title=f"🖼️{member.name}",
                            color=discord.Color.blue()
                        )
                        avatar_embed.set_image(url=member.avatar.url)

                        await interaction.response.send_message(embed=avatar_embed, ephemeral=True)

                except KeyError:
                    logging.error(f"Erro ao acessar 'custom_id' em avatar_callback para {member}: {traceback.format_exc()}")

            async def permissions_callback(interaction):
                try:
                    if interaction.data['custom_id'] == "permissions_button":
                        member_in_guild = ctx.guild.get_member(member.id)
                        if member_in_guild:
                            permissions = [perm[0].replace('_', ' ').title() for perm in member_in_guild.guild_permissions if perm[1]]
                            permissions_list = ', '.join(permissions) if permissions else "Sem permissões específicas"
                            
                            permissions_embed = discord.Embed(
                                title=f"Permissões de {member.name}",
                                color=discord.Color.purple()
                            )
                            permissions_embed.add_field(name="Permissões", value=permissions_list, inline=False)

                            roles = [role.mention for role in member_in_guild.roles if role.name != "@everyone"]
                            roles_list = ', '.join(roles) if roles else "Sem cargos"

                            permissions_embed.add_field(name="<a:z_pig:1310401867125358752> Cargos", value=roles_list, inline=False)

                            await interaction.response.send_message(embed=permissions_embed, ephemeral=True)
                        else:
                            await interaction.response.send_message("Não foi possível encontrar o membro no servidor.", ephemeral=True)

                except KeyError:
                    logging.error(f"Erro ao acessar 'custom_id' em permissions_callback para {member}: {traceback.format_exc()}")

            avatar_button.callback = avatar_callback
            if permissions_button:
                permissions_button.callback = permissions_callback

        except Exception as e:
            logging.error(f"Erro ao executar o comando 'userinfo' para {member}: {str(e)}\n{traceback.format_exc()}")

async def setup(bot):
    await bot.add_cog(UserInfo(bot))
