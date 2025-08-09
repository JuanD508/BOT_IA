import discord
from discord.ext import commands
from modelo import detect_dog
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot iniciado como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            os.makedirs("images", exist_ok=True)
            img_path = f"./images/{archivo.filename}"
            await archivo.save(img_path)

            resultado = detect_dog(img_path)
            await ctx.send(resultado)
    else:
        await ctx.send("No ingresaste ninguna imagen.")

bot.run("TU_TOKEN_AQUI")
