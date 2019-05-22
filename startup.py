import discord
from discord.ext import commands

TOKEN = "NTgwMzAxODU3Mjk4MTg2MjYw.XOPfoA.TlAY-5q1YryNWSuJ2iulPe8MROE"

class MyClient(discord.Client):
    MyClient = commands.Bot(command_prefix = '.')
    async def on_ready(self):
        print('--------------')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('--------------')
        await client.change_presence(activity=discord.Game(name="Minecraft", type='2'))

    async def on_message(self, message):
        author = message.author
        content = message.content
        server = message.guild
        print('{}: {} snet on {}'.format(author, content, server))
        # we do not want the bot to reply to itself
        if message.content.startswith('.help'):
            await message.channel.send('This Contains Commands That Can Be Used.'.format(message))
        
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))


    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
        print(f'{member} has joined {server}!')

    async def on_member_left(member):
        print(f'{member} has left {server}.')

client = MyClient()
client.run(TOKEN)
