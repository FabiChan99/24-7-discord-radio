import discord
from discord.ext import commands
import wavelink
import asyncio
import sys

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.volume = 20
        self.refresh = 600 #Auto Reconnect in seconds
        self.channel = 861905485815873566 #Input Voice Channel ID Here
        self.port = 2333 #Put lavalink server port here
        self.server = 750365461945778209 # Input Discord Guild ID
        self.host = '127.0.0.1' #Put lavalink address here
        self.password = 'nicepassword'
        self.radio = "https://juka-kpop.stream.laut.fm/juka-kpop?pl=m3u&t302=2021-07-06_23-45-13&uuid=949425c3-ae7f-4196-b0ad-239bbe5e032a" #Input Stream URL Here
        self.restore = 3
        self.autoconnect = True
        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)
        self.bot.loop.create_task(self.start_nodes())


    async def start_nodes(self):
        await self.bot.wavelink.initiate_node(host=self.host, port=self.port, password=self.password, rest_uri=f"http://{self.host}:{self.port}", identifier='Main', region='europe')
        self.bot.loop.create_task(radio(self))

# 24/7 radio player
async def radio(self):
    while True:
        channel = self.bot.get_channel(self.channel)
        player = self.bot.wavelink.get_player(self.server)
        if not player.is_connected or not self.bot.user in channel.members or not player.is_playing:
            await player.set_volume(self.volume)
            await player.connect(channel.id)
            await self.bot.get_guild(self.server).change_voice_state(channel=channel, self_deaf=True)
            tracks = await self.bot.wavelink.get_tracks(self.radio)
            await player.play(tracks[0])
        await asyncio.sleep(self.refresh)



def setup(bot):
    bot.add_cog(Music(bot))
