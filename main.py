import discord
from discord.ext import commands
import asyncio
import os

#developer theuxie
TOKEN = ""

intents = discord.Intents.all()

def get_prefix(bot, message):
    return ('+', ',')

bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=None)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f'Obrigada por me adicionar!')
            break

async def load_cogs():
    cogs_dir = 'cogs'
    for filename in os.listdir(cogs_dir):
        if filename.endswith('.py'):
            cog_name = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog_name)
                print(f"{cog_name} carregado com sucesso!")
            except Exception as e:
                print(f"Falha ao carregar {cog_name}: {e}")

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

async def main():
    await load_cogs()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
