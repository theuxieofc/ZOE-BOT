import discord
from discord.ext import commands
from discord.ui import Button, View

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='av', help='Mostra o avatar do usuário.')
    async def avatar(self, ctx, member: discord.Member = None):

        if member is None:
            member = ctx.author

        button = Button(label="Abrir no navegador", url=member.avatar.url)

        view = View()
        view.add_item(button)

        avatar_embed = discord.Embed(
            title=f"{member.name}",
            color=discord.Color.blue()
        )
        avatar_embed.set_image(url=member.avatar.url)

        await ctx.send(embed=avatar_embed, view=view)

async def setup(bot):
    await bot.add_cog(Avatar(bot))
 #developer theuxie


#developer theuxie

#developer theuxie

#developer theuxie



#developer theuxie

#developer theuxie



