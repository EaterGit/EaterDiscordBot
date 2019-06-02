import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import random
from itertools import cycle
import time

BOT_PREFIX = '.'
user = input('Enter Bot Discord ID and Name ID : ')
TOKEN = "NTgwMzAxODU3Mjk4MTg2MjYw.XOuoIA.0yz8XAVBC49gTl5ukxEB4r_X5No"

bot = commands.Bot(command_prefix=",", activity=discord.Game(name="Booting..."))
bot.remove_command('help')
t = str(len(bot.guilds))
act = cycle(['Do ,help', 'Development Ongoing', 'Minecraft', 'Mobile Legends: Bang Bang', 'Python', 'Javascript', 'Discord', "On {} Servers".format(t)])


# # Successfuly Launched # #
@bot.event
async def on_ready():
    botowner = (await bot.application_info()).owner
    change_status.start()
    print("=" * 45 + "\n")
    print("Ready To Go!" + "\n")
    print("Owned and Programmed By : Kaizer / Eater \n")
    print("Logged In As {0.user}\n".format(bot))
    print("Currently running in : {} servers. \n".format(len(bot.guilds)))
    print("Bot's Prefix : , \n")
    print("=" * 45 + "\n")
    print("Bot Owner is " + botowner.name + "#" + botowner.discriminator + "\n")
    print("Current Discord.py Version : {}\n".format(discord.__version__))
    print("{}\n".format(discord.version_info))
    print("=" * 45 + "\n")


    
# # Change Status # #
@tasks.loop(seconds=9.5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(act)))



# # AutoRole / On Joined# #
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Community")
    channel = bot.get_channel(582810265238896651)
    await channel.send("Welcome {member.mention} To Eater's Official")
    await bot.add_roles(member, role)



# # Left # #
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(582810265238896651)
    await channel.send("{0.mention} Left Eater's Official".format(member))


    
# # Reciever # #
@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    guild = message.guild
    print("{} : {} sent on {}".format(author, content, guild))
    await bot.process_commands(message)



# # Help Module # #
@bot.command()
async def help(ctx):
        embed = discord.Embed(

        colour = discord.Colour.blue()

        )

        embed.add_field(name="Add Me  To Your Server : \n ", value="http://bit.ly/eaterbot \n",inline=False)
        embed.add_field(name="\n General Commands", value="\n")
        embed.add_field(name="help", value="Shows The List Of s", inline=False)
        embed.add_field(name="ping", value="Sends The Latency Of The Bot", inline=False)
        embed.add_field(name="quote", value="Sends A Quote To Enlighten Your Day", inline=False)
        embed.add_field(name="info", value="Gets The User Info Using This ", inline=False)
        await ctx.author.send(embed=embed)
        


# # Ping Module # #
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"Your ping is {ping}ms")



# # Quotes Module # #
@bot.command()
async def quote(ctx):
        author = ctx.message.author
        respo = [
        "You’re off to great places, today is your day. Your mountain is waiting, so get on your way.",
        "You always pass failure on the way to success.",
        "No one is perfect - that’s why pencils have erasers.",
        "You’re braver than you believe, and stronger than you seem, and smarter than you think.",
        "It always seems impossible until it is done.",
        "Keep your face to the sunshine and you cannot see a shadow.",
        "Once you replace negative thoughts with positive ones, you’ll start having positive results.",
        "If you can forgive you can forget.",
        "Positive thinking will let you do everything better than negative thinking will.",
        "In every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact.",
        "The only time you fail is when you fall down and stay down.",
        "Just be happy and everything will be fine!",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "Creativity Is Intelligence Having Fun.",
        "Your limitation—it’s only your imagination",
        "Push yourself, because no one else is going to do it for you.",
        "Sometimes later becomes never. Do it now.",
        "Great things never come from comfort zones.",
        "Dream It. Wish It. Do It.",
        "Everything happens for a reason.",
        "Dream Big. Do Bigger!",
        "Little things make big days.",
        "It’s going to be hard, but hard does not mean impossible.",
        "Don’t wait for opportunity. Create it.",
        "The key to success is to focus on goals, not obstacles.",
        "Dream It. Believe It. Build It.",
        "Do one thing every day that scares you.",
        "You never have to change anything you got up in the middle of the night to write.",
        ]
        await ctx.send(random.choice(respo))
        await ctx.send("{0.mention} Hope This Quote Helps You! \n".format(author))



# # Info Command # #
@bot.command(aliases=['user', 'userinfo'])
async def info(ctx, user: discord.Member):
    desktop = user.desktop_status
    web = user.web_status
    mobile = user.mobile_status
    embed = discord.Embed(title="User info for {name}#{discriminator}".format(name=user.name, discriminator=user.discriminator), color=0x68e887)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Name on server", value="{nick}".format(nick=user.display_name if user.display_name is not user.name else "None"), inline=True)
    embed.add_field(name="ID", value="{id}".format(id=user.id), inline=True)
    embed.add_field(name="On Client", value="{client}".format(client="Desktop" if desktop is desktop.online or desktop is desktop.idle or desktop is desktop.dnd else "Web" if web is web.online or web is web.idle or web is web.dnd else "Mobile" if mobile is mobile.online or mobile is mobile.idle or mobile is mobile.dnd else "None")) 
    embed.add_field(name="Status", value="{status}".format(status=user.status), inline=True)
    embed.add_field(name="Playing/Activity", value="{}".format(user.activity), inline=True)
    embed.add_field(name="Join Date", value="{}".format(user.joined_at), inline=True)
    embed.add_field(name="Highest Role", value="{}".format(user.top_role), inline=True)
    embed.add_field(name="Account Created", value="{}".format(user.created_at), inline=True)
    await ctx.send(embed=embed)


## Error On Info ##
@info.error
async def info_handler(ctx, error):
    if error.param.name == 'user':
        await ctx.send("{sender} Which user did you want to get the info of?".format(sender=ctx.message.author.mention))



# # Owner # #
@bot.command()
async def botowner(ctx):
    botowner = (await bot.application_info()).owner
    await  ctx.send("The Owner Of This Bot Is {}.\n Message him if you have any suggestions.".format(botowner))


# # Clear command # #
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int=None):
            channel = bot.get_channel(58425827681172224)
            chsent = ctx.message.channel
            if amount is None:
                await ctx.send("Do ,clear (amount)")
            else:
                await ctx.channel.purge(limit=amount)
                await channel.send("Cleared (amount) Messages on {}".format(chsent))



## Error On Clear ##
@clear.error
async def clear_handler(ctx, error):
    sender = ctx.message.author
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You Don't Have Permission To Use This Command!".format(sender.mention))



# # Shut Down The Bot # #
@bot.command(aliases=['shutdown'])
async def stop(ctx):
    Owner = [
        397944315407761410 
    ]
    sender = ctx.message.author
    bot = ctx.bot
    if sender.id in Owner:
        await ctx.send(":wave: Bye!")
        print("{}#{} Shuts down the bot.".format(sender.name, sender.discriminator))
        await bot.logout()
    else:
        await ctx.send("Sorry {}  Only the hosts or the bot owner can do this.".format(sender.mention))



@bot.command(aliases=['print', 'printtoconsole', 'saytoconsole', 'say'])
async def printconsole(ctx, *, args):
    sender = ctx.message.author
    Owner = [
        397944315407761410 
    ]
    if sender.id in Owner:
        print("{name}#{discrim}: {msg}".format(name=sender.name, discrim=sender.discriminator, msg=args))
    else:
        await ctx.send("{} || Only the bot's Owner can do that.".format(sender.mention))


@printconsole.error
async def printconsole_handler(ctx, error):
    sender = ctx.message.author
    if isinstance(error, commands.MissingRequiredArgument):
        if error.param.name == 'args':
            await ctx.send("{} Can't send something blank to the server's console.".format(sender.mention))



bot.run(TOKEN)
