import discord
from discord.ext import commands
import random
client = discord.Client()


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
@client.event
async def on_message(message):
    no_no_words = ["bad"]
    for word in no_no_words:
        if str(message).lower() == word:
            await bot.delete_message(message)

client.run("NzI0OTk2OTA2OTIwNzA2MDY4.XvLXEA.KoBOJNsZhzF8bvc2XoZ1c46OKZs")
