import discord
from discord.ext import commands
from discord import app_commands

class ServerIconCog(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command(name="servericon")
    async def servericon_prefix(self, ctx):
        server_icon_url = ctx.guild.icon.url if ctx.guild.icon else None
        if server_icon_url:
            embed = discord.Embed(
                title="❤️ zoe",
                description=f"Baixar o ícone de {ctx.guild.name}",
                color=discord.Color.blue()
            )
            embed.set_image(url=server_icon_url)
            embed.set_footer(text=f"Comando solicitado por {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("Este servidor não possui um ícone.")

    @app_commands.command(name="servericon", description="Mostra o ícone do servidor.")
    async def servericon_slash(self, interaction: discord.Interaction):
        server_icon_url = interaction.guild.icon.url if interaction.guild.icon else None
        if server_icon_url:
            embed = discord.Embed(
                title="❤️ zoe",
                description=f"Baixar o ícone de {interaction.guild.name}",
                color=discord.Color.blue()
            )
            embed.set_image(url=server_icon_url)
            embed.set_footer(text=f"Comando solicitado por {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
            
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Este servidor não possui um ícone.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ServerIconCog(bot))


#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie
#developer theuxie

#developer theuxie