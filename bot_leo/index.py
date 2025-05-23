import discord
from discord.ext import commands
import os

from extracao import extrair_campos
from preencher import preencher_modelo

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith(".pdf"):
                await message.channel.send("Recebido o PDF. Processando...")

                caminho_pdf = f"./{attachment.filename}"
                await attachment.save(caminho_pdf)

                try:
                    dados = extrair_campos(caminho_pdf)
                    caminho_docx = "preenchido.docx"
                    preencher_modelo("modelo.docx", caminho_docx, dados)

                    await message.channel.send(file=discord.File(caminho_docx))
                except Exception as e:
                    await message.channel.send(f"Erro: {e}")

                # Limpeza dos arquivos temporários
                if os.path.exists(caminho_pdf):
                    os.remove(caminho_pdf)
                if os.path.exists(caminho_docx):
                    os.remove(caminho_docx)

    await bot.process_commands(message)


bot.run(TOKEN)