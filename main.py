import discord
from discord.ext import commands
import wavelink



TOKEN = "ENTER BOT TOKEN HERE"

app = commands.Bot(
    command_prefix="-----",
    intents=discord.Intents.all(),
)

@app.event
async def on_ready():
    print("24/7 Radio is Ready")

app.load_extension('Cogs.radiomodule')


app.run(TOKEN)