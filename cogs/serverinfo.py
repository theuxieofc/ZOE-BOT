import discord
from discord.ext import commands
import logging
import traceback


# developer by uxie
logging.basicConfig(
    filename='erros.txt', 
    level=logging.ERROR,  
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filemode='a'  
)

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        try:
            guild = ctx.guild

            nome_servidor = guild.name
            servidor_id = guild.id
            shard_id = guild.shard_id

            dono = guild.owner
            if dono:
                dono_nome = f"{dono.name}#{dono.discriminator}"
                dono_id = dono.id
            else:
                dono_nome = "Desconhecido"
                dono_id = "Desconhecido"
                logging.error(f"Não foi possível obter o dono do servidor {guild.name} (ID: {guild.id})")

            total_canais = len(guild.text_channels) + len(guild.voice_channels)
            canais_texto = len(guild.text_channels)
            canais_voz = len(guild.voice_channels)

            data_criacao = guild.created_at.strftime("%d %b %Y, %H:%M")
            data_entrada = ctx.message.author.joined_at.strftime("%d %b %Y, %H:%M")

            total_membros = guild.member_count

            embed = discord.Embed(title=f"Informações do servidor: {nome_servidor}", color=discord.Color.blue())
            embed.set_thumbnail(url=guild.icon.url if guild.icon else None)  
            embed.add_field(name="💻 ID", value=str(servidor_id), inline=True)
            embed.add_field(name="💻 Shard ID", value=str(shard_id), inline=True)
            embed.add_field(name="👑 Dono", value=f"{dono_nome} ({dono_id})", inline=False)
            embed.add_field(name="💬 Canais", value=f"{total_canais} canais", inline=False)
            embed.add_field(name="📝 Texto", value=str(canais_texto), inline=True)
            embed.add_field(name="🗣 Voz", value=str(canais_voz), inline=True)
            embed.add_field(name="📅 Criado em", value=data_criacao, inline=False)
            embed.add_field(name="🌟 Entrei aqui em", value=data_entrada, inline=False)
            embed.add_field(name="👥 Membros", value=str(total_membros), inline=False)

            await ctx.send(embed=embed)

        except Exception as e:
            logging.error(f"Erro ao executar o comando 'serverinfo' para o servidor {guild.name} (ID: {guild.id}): {str(e)}\n{traceback.format_exc()}")

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))


#developer theuxie

#developer theuxie
#developer theuxie
#developer theuxie

#developer theuxie
#developer theuxie
#developer theuxie
