from discord.ext import commands
import random

TOKEN = "NzI0OTk2OTA2OTIwNzA2MDY4.XvI0mw.4KoAYG1K8qvZJ_voA6qGLtcJuTw"
GUILD = "test_server"

bot = commands.Bot(command_prefix='!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run(TOKEN)
