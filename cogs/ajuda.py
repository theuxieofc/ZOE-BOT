import discord
from discord.ext import commands
from discord.ui import Select, View

class UtilidadeDropdown(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Utilidade", description="Comandos úteis diversos", emoji="⚙️"),
            discord.SelectOption(label="Administração", description="Comandos de administração", emoji="🛠️"),
        ]
        super().__init__(placeholder="Selecione uma categoria", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Utilidade":
            embed = discord.Embed(
                title="⚙️ Comandos de Utilidade",
                description="`[] = Obrigatório / () = Opcional`\n\n" + 
                            "**uuserverinfo**\n- Veja as informações sobre um usuário.\n\n" +
                            "**uavatar**\n- Veja o avatar do usuário.\n\n" +
                            "**ubanner**\n- Veja o banner do usuário.\n\n" +
                            "**uping**\n- Veja as informações da Uxie.\n\n" +
                            "**uservericon**\n- Veja o ícone do servidor.\n\n" +
                            "**uajuda**\n- Mostra o painel de comandos/ajuda.\n\n" +
                            "**ulock**\n- Tranca um canal.\n\n" +
                            "**uunlock**\n- Destranca um canal.\n\n",
                color=discord.Color.green()
            )
            embed.set_footer(text="Categoria: Utilidade")
        
        elif self.values[0] == "Administração":
            embed = discord.Embed(
                title="🛠️ Comandos de Administração",
                description="`[] = Obrigatório / () = Opcional`\n\n" +
                            "**uban <usuário> <motivo>**\n- Desbane um usuário do servidor.\n\n" +
                            "**uunban <usuário>**\n- Reverte um desbanimento.\n\n" +
                            "**umute <usuário> <tempo> <motivo>**\n- Silencia um usuário por um tempo determinado.\n\n" +
                            "**uunmute <usuário>**\n- Remove o mute de um usuário.",
                color=discord.Color.red()
            )
            embed.set_footer(text="Categoria: Administração")

        await interaction.response.edit_message(embed=embed)

class UtilidadeView(View):
    def __init__(self):
        super().__init__()
        self.add_item(UtilidadeDropdown())

class Ajuda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ajuda")
    async def ajuda(self, ctx):
        embed = discord.Embed(
            title="Ajuda | ZOE",
            description=f"Bem-vindo(a) {ctx.author.mention}, este é o painel de ajuda do bot!",
            color=discord.Color.purple()
        )
        embed.add_field(
            name="Selecione a categoria abaixo",
            value="para ver os comandos disponíveis.",
            inline=False
        )
        embed.set_footer(text=f"Comando executado por: {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed, view=UtilidadeView())

async def setup(bot):
    await bot.add_cog(Ajuda(bot))


#developer theuxie


#developer theuxie

#developer theuxie

#developer theuxie



#developer theuxie

#developer theuxie



