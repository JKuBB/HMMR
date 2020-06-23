from discord.ext import commands

TOKEN = "NzI0OTk2OTA2OTIwNzA2MDY4.XvIYnA.hfWtzbb0oVOriht5QMYP0-m3-E0"
GUILD = "test_server"

bot = commands.Bot(command_prefix='!')

@bot.command(name='j')
async def join_queue(ctx):
    pass
bot.run(TOKEN)
