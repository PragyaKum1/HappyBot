import discord
from discord.ext import commands

class ResponsesCog(commands.Cog):
    
  def _init_(self, client):
    self.client = client

    
  @commands.command()
  async def zhongli(self, ctx):
    await ctx.reply("He is the stronger Geo Character in da Game")
  
  @commands.command()
  async def sing(self, ctx):
    await ctx.reply("Yeet Yeet skrrt skrrt")

  @commands.command()
  async def hi(self, ctx):
    await ctx.reply("`hewoo`")
  

  @commands.command()
  async def beepity(self, ctx):
    await ctx.reply("boopity")

 
  @commands.command()
  async def happy(self, ctx):
    await ctx.reply("yep! I am very happy!")   
      

  @commands.command()
  async def guild_ID(self,ctx):
    await ctx.reply(ctx.guild.id)
    
  @commands.command()
  async def guild_name(self, ctx):
    await ctx.reply(ctx.guild.name)

  @commands.command()
  async def sad(self,ctx):
    await ctx.reply("`〒▽〒`")

  @commands.command()
  async def ily(self,ctx):
    await ctx.reply("(っ˘з(˘⌣˘ )")

  @commands.command()
  async def rage(self,ctx):
    await ctx.reply("`(ノಠ益ಠ)ノ彡┻━┻`")

  @commands. command()
  async def mald(self, ctx):
    await ctx.reply("`୧༼ ಠ益ಠ ༽୨`")

  @commands.command()
  async def rick(self, ctx):
    await ctx.reply("we are no strangers to love")
  
  @commands.command()
  async def grieve(self,ctx):
    await ctx.reply("ALL ALONE, HORRIFIED, TURN THE PAGE MY LITTLE DARK AGE")

  @commands.command()
  async def damn(self,ctx):
    await ctx.reply("( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)")

  @commands.command()
  async def happy(self,ctx):
    await ctx.reply("(≧▽≦)")

  @commands.command()
  async def hug(self,ctx):
    await ctx.reply("(⁠つ⁠≧⁠▽⁠≦⁠)⁠つ")
  




  
 
    



  
def setup(client): #PLS WOKRKR3IGJO
  client.add_cog(ResponsesCog(client))


