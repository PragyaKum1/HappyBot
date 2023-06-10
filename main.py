import discord
import os
import dotenv
dotenv.load_dotenv()

token = str(os.getenv("TOKEN"))


from discord.ext import commands

client = commands.Bot(
    command_prefix = "!",
    help_command=None,
    intents = discord.Intents.all()
)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if ("super idol") in message.content.lower():
    await message.delete()

  if message.content == "<@1110059888958246993>":
    await message.channel.send("Yo! My prefixes are `!`")

  await client.process_commands(message)



for filename in os.listdir("./cogs"):
  if filename.endswith("cog.py"):
    client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.getenv('TOKEN'))




    

