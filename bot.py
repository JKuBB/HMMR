import discord

client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild(ID)
    channels = ["commands"]
    valid_users = ["Ti#9298"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")

@client.event
async def on_message(message):
    blocked_words = ["retarded", "gay", "nigger", "nig", "faggot", "fag", "jew", "vagina"]
    for word in blocked_words:
        if message.content == word:
            await message.channel.purge(limit=1)

@client.event
async def on_message(message):
    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)

client.run("#")
