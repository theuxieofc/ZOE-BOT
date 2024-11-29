import discord
from discord.ext import commands
from datetime import datetime

class Banner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='banner', description='Veja o banner de um usuário.')
    async def banner(self, ctx, user: discord.User = None):
        if user is None: 
            user = ctx.author 

        try:
            fetched_user = await self.bot.fetch_user(user.id)

            if fetched_user.banner:
                banner_url = fetched_user.banner.url
                embed = discord.Embed(title=f"{fetched_user.display_name}", color=discord.Color.blue())
                embed.set_image(url=banner_url)

                button = discord.ui.Button(label="Abrir no navegador", url=banner_url)

            else:
                embed = discord.Embed(title=f"{fetched_user.display_name} não tem um banner.", color=discord.Color.red())
                button = None

        except discord.HTTPException as e:
            embed = discord.Embed(title="Erro", description="Não consegui acessar o banner do usuário. Verifique se o usuário tem um banner e tente novamente.", color=discord.Color.red())
            print(f"Erro ao acessar o banner: {e}")
            button = None
        except Exception as e:
            embed = discord.Embed(title="Erro", description="Ocorreu um erro ao tentar acessar o banner.", color=discord.Color.red())
            print(f"Erro inesperado: {e}")
            button = None

        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        embed.set_footer(text=f"Comando executado por {ctx.author.display_name} em {current_time}")

        if button:
            view = discord.ui.View()
            view.add_item(button)
            await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Banner(bot))

#developer theuxie


#developer theuxie

#developer theuxie

#developer theuxie



#developer theuxie

#developer theuxie



