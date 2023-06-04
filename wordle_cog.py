import discord
from discord.ext import commands
import re


class WordleCog(commands.Cog):
    
  def _init_(self, client):
    self.client = client
  
  @commands.command()
  async def game(self, ctx):
    await ctx.reply("`Guess: The Number I am Thinking Of!`")

test = "123abc123ABCabc"
pattern = re.compile(r"abc")
matches = pattern.finditer(test)
#match = returns first
#search = 
for match in matches:
  print(match)

  




  
def setup(client): #PLS WOKRKR3IGJO
  client.add_cog(WordleCog(client))


