from discord.ext import commands
import time

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#developer theuxie
    @commands.command()
    async def ping(self, ctx):
        
        start_time = time.monotonic()
        
        message = await ctx.send("🏓 **Aqui Esta Minha Latencia**")#developer theuxie
        
        websocket_latency = round(self.bot.latency * 1000)
        
        response_time = round((time.monotonic() - start_time) * 1000)
        
        await message.edit(content=f"🏓 **Pong! kkk**\nWebsocket: {websocket_latency}ms\nMensagem: {response_time}ms")

async def setup(bot):
    await bot.add_cog(PingCog(bot)) #developer theuxie




#developer theuxie
#developer theuxie

#developer theuxie
#developer theuxie
#developer theuxie

#developer theuxie
#developer theuxie
#developer theuxie