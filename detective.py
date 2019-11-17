import discord
from discord.ext import commands, tasks
import math
import random
from itertools import cycle
from discord.ext.commands import CommandNotFound
import asyncio
import sys
import traceback
from async_timeout import timeout
from functools import partial 
import json 
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get

#-------------------------------------------------------------------
# Variables, Constants, Files, and Dictionaries are all defined here
#-------------------------------------------------------------------

howgay_rate   = [10, 69, 15, 13, 32, 23, 75, 26, 45, 92, 87, 78, 65, 2, 14, 53, 90, 43]
INCREMENT     = [10, 42, 64, 23, 21, 4, 61, 53, 35, 12, 15, 14, 19, 24, 49, 18, 25, 63]
START_BAL     = 100 
BALANCES_FILE = 'balances.json'
balances      = {} 

bot = commands.Bot(command_prefix='$')
status = cycle(['$help'])

#---------------------------------------
# These are the main events in this code
#---------------------------------------

@bot.event
async def on_ready():
  change_status.start() 
  global balances, INCREMENT, houses 
  try: 
    with open(BALANCES_FILE, 'r') as fp: 
      balances = json.load(fp) 
  except FileNotFoundError: 
    print(f'In on_ready(): File {BALANCES_FILE} not found. Starting off with an empty balances dictionary.') 
    balances = {} 

  print(f'In on_ready(): INCREMENT = {INCREMENT}')
  print(f'In on_ready(): START_BAL = {START_BAL}')
  print(f'In on_ready(): balances = {balances}')
  print('---------------------------------------------------') 
  print(f'{bot.user.name} ready for duty! ({bot.user.id})')
  print('---------------------------------------------------') 

@bot.event
async def on_member_join(ctx, member: discord.Member):
  await bot.send_message(member, "Welcome to your newest server. Remember to have fun here")

@bot.event
async def on_message(message):
  if message.content.startswith('pray'):
    msg = "JESUS"
    await bot.send_message(message.channel, msg)
    return

@tasks.loop(seconds=20)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

#--------------------------------------
# The encryption and decryption strings
#--------------------------------------

def encrypt_char(c): 
  return chr(ord(c)+1) 

def decrypt_char(c): 
  return chr(ord(c)-1) 

def encrypt_string(s): 
  return ''.join([encrypt_char(c) for c in s]) 

def decrypt_string(s): 
  return ''.join([decrypt_char(c) for c in s]) 

#-------------------
# The memey commands
#-------------------

@bot.command()
async def robotify(ctx, *, words):
  await ctx.send(f'```{words}```')

@bot.command()
async def randomrob(ctx):
  rob = [
    "You tried robbing the bank but the bank robbed you lol",

    "You tried robbing the meme headquarters but got YEETED",

    "You tried robbing Apple but the iPhone u stole whooped your ass"
  ]
  await ctx.send(random.choice(rob))

@bot.command(name = 'enc')
async def encrypt2(ctx, *args): 
  print(f"Encryption Log: {len(args)} argument(s): {', '.join(args)}") 

  if len(args) < 1: 
    print(f'Encryption Log: No arguments found! Proper use: "$encrypt <text>"')
    response = 'hey dud, try giving me something to encrypt lmao' 
  else: 
    source = ' '.join(args)
    print(f'Encryption Log: Encrypting <{source}>...') 
    response = f'Here\'s the encrypted text: {encrypt_string(source)}' 
  print(f'Encryption Log: Sending response = <{response}>')
  await ctx.send(response) 

@bot.command(name = 'dec')
async def decrypt2(ctx, *args): 
  print(f"Decryption Log: {len(args)} argument(s): {', '.join(args)}") 

  if len(args) < 1: 
    print(f'Decryption Log: No arguments found! Proper use: "$decrypt <text>"')
    response = 'hey dud, try giving me something to decrypt lmao' 
  else: 
    source = ' '.join(args)
    print(f'Decryption Log: Decrypting <{source}>...') 
    response = f'Here\'s the decrypted text: {decrypt_string(source)}' 

  print(f'Decryption Log: Sending response = <{response}>')
  await ctx.send(response) 

@bot.command()
async def encrypt(ctx):
  await encrypt2.invoke(ctx)

@bot.command()
async def decrypt(ctx):
  await decrypt2.invoke(ctx)

@bot.command()
async def powerofgod(ctx):
  await ctx.send("god rejects ur stupid ass boi")

@bot.command()
async def tryme(ctx):
  await ctx.send("i have the power of god and anime on my side u can't beat me")
  await asyncio.sleep(2)
  await ctx.send("LOSER")

@bot.command()
async def avatar(ctx, member: discord.Member):
  await ctx.send('{}'.format(member.avatar_url))

@bot.command()
async def uptime(ctx):
  embed = discord.Embed(title="Detective Dank's Uptime", description="Uptime is the time a bot is online", color=0xeee657)

  embed.add_field(name="Weekdays", value="7:00 P.M to 9:00 P.M", inline=False)
  
  embed.add_field(name="Weekends", value="10:00 A.M to 7:00 A.M", inline=False)

  await ctx.send(embed=embed)

@bot.command()
async def howgay(ctx):
  embed = discord.Embed(title="gay boi determiner", description=f"You are {random.choice(howgay_rate)}% gay", color=0xeee657)
  await ctx.send(embed=embed)

@bot.command()
async def justdoit(ctx):
  await ctx.send("Lower your volume lmao")
  await ctx.send("R.I.P headphone users")
  await ctx.send("https://www.youtube.com/watch?v=e1mvrXB7k0A")

@bot.command()
async def meme(ctx):
  meme_generator = [

    "https://imgflip.com/i/2xt9op",

    "https://imgflip.com/i/3fromx",

    "https://imgflip.com/i/3ffiq7",

    "https://imgflip.com/i/3f4b9t",

    "https://imgflip.com/i/3fkhhv",

    "https://imgflip.com/i/3fhbuj",

    "https://imgflip.com/i/3fcqsw",

    "https://imgflip.com/i/3fmtla",

    "https://imgflip.com/i/3fcum2",

    "https://imgflip.com/i/3frpkv",

    "https://imgflip.com/i/3fnxiz",

    "https://imgflip.com/i/25pypz",

    "https://imgflip.com/i/3fkzwn",

    "https://imgflip.com/i/3fcshx",

    "https://imgflip.com/i/3fgnlj",

    "https://imgflip.com/i/3filv4",

    "https://imgflip.com/i/3fl2tm",

    "https://imgflip.com/i/2y09tm",

    "https://imgflip.com/i/2hp9ev",

    "https://imgflip.com/i/3fglhy",

    "https://imgflip.com/i/3ftez0"
  
  ]
  await ctx.send(random.choice(meme_generator))

@bot.command()
async def roast(ctx):
  roast_generator = [
    "You're fat, don't sugarcoat it or you'll eat that too",
    " If your brain was dynamite, there wouldn’t be enough to blow your hat off",
    "Sorry, can't roast plastic",
    "I would slap you, but sh*t splatters",
    "Your mom got fined for littering when she dropped you off at school"
  ]
  await ctx.send(random.choice(roast_generator))

@bot.command()
async def dank(ctx):
  await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command(name='8ball')
async def magic_eight_ball(ctx, *args):
  response =[
    '8 Ball says: Without a doubt.', 
    '8 Ball says: Outlook good.', 
    '8 Ball says: Better not tell you now.', 
    '8 Ball says: Cannot predict now.',
    '8 Ball says: My reply is no.', 
    '8 Ball says: Outlook not so good.',
  ]
  if len(args) < 1:
    await ctx.send("8 Ball: Gimme something to predict big brain")
  else:
    await ctx.send(random.choice(response))

@bot.command()
async def echo(ctx, *args):
  print(f"Echo log: {len(args)} argument(s): {','.join(args)}")

  if len(args) < 1:
    print(f"Echo Log: No arguments found! Proper use: '$echo <text>'")
    response = "boi, i cant repeat a word without anything  to repeat dummy"
    await ctx.send(response)
  else:
    response = ' '.join(args)
    print(f'Echo Log: Echoing <{response}>...')
    await ctx.send(response)

@bot.command()
async def doggo(ctx):
  doggo_generator = [
    "https://imgflip.com/i/3d6wiu",

    "https://imgflip.com/i/3eot1b",

    "https://imgflip.com/i/36pd9u"
  ]

  await ctx.send(random.choice(doggo_generator))
  
@bot.command()
async def robyeebank(ctx):
  await ctx.send("You tried to rob the bank but the cops busted your ass. Now you're in jail")
  await asyncio.sleep(4)
  await ctx.send("BITCH")

#----------------------------
# The bot's currency commands
#----------------------------

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
  user = str(ctx.message.author.id)
  global balances, START_BAL
  if user not in balances:
    await ctx.send(f"oi you don't got a bank account so i made you one with a bonus of ${START_BAL}")
  else:
    embed = discord.Embed(title="**500** coins were placed in your bank account", description="Every 24 hours you can get 500 free coins, and try out our other commands")

    await ctx.send(embed=embed)
    balances[user] += 500

@bot.command(pass_context=True)
async def transfer(ctx, amount: int, member: discord.Member):
  user = str(ctx.message.author.id)
  global balances, START_BAL
  if user not in balances:
    await ctx.send(f"hey you don't have an account so i started you off with one with a ${START_BAL}")
    balances[user] = START_BAL
  elif member not in balances:
    await ctx.send("The other party does not have an account")
  elif balances[user] < amount:
    await ctx.send("You cannot afford this transaction")
  else:
    balances[user] -= amount
    balances[member] += amount
    await ctx.send(f"You gave {amount} to @{member}")

@bot.command()
async def donate(ctx):
  await transfer.invoke(ctx)

@bot.command()
async def give(ctx):
  await transfer.invoke(ctx)

@bot.command(name = 'plead')
@commands.cooldown(1, 60, commands.BucketType.user)
async def plead(ctx):
  global balances, INCREMENT, START_BAL 
  user = str(ctx.message.author.id) 
  print(f'In plead(): Author Id = {ctx.message.author.id}, Author Name = {user}')

  if user in balances: 
    print(f'In beg(): Found record for {user}. Incrementing balance by {random.choice(INCREMENT)}')
    responses = [
      f"**Detective Dank** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**David Dobrik** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**Pewdiepie** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**Kylie Jenner** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**Ur Mom** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**Kanye West** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**Markiplier** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**Mojang** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!",
      f"**Jesus** donated {random.choice(INCREMENT)} coins to {ctx.message.author.mention}!"
    ]
    await ctx.send(random.choice(responses))
    balances[user] += INCREMENT

  else: 
    print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
    balances[user] = START_BAL 
    await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
   with open(BALANCES_FILE, 'w') as fp: 
    json.dump(balances, fp) 
  except FileNotFoundError: 
   print(f'In beg(): File {BALANCES_FILE} not found! Not sure what to do here!') 

@bot.command(name = 'bal')
async def bal(ctx): 
  global balances, INCREMENT, START_BAL 
  user = str(ctx.message.author.id) 
  print(f'In balance(): Author Id = {ctx.message.author.id}, Author Name = {user}')

  if user in balances: 
    print(f'In balance(): Found record for {user}. User balance = {balances[user]}') 
    embed = discord.Embed(title=f":moneybag: {ctx.message.author}'s balance", description=f"**Bank Account**: {balances[user]}/ꝏ", color=0xeee657)

    await ctx.send(embed=embed)

  else: 
    print(f'In balance(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
    balances[user] = START_BAL 
    await ctx.send(f'hey you don\'t have an account yet. I just created one for you and started you off with ${START_BAL}. To register type in `$plead`') 

  print(f'In balance(): balances = {balances}')

@plead.error
async def plead_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Slow down dude", description="Stop pleading so much, you look like a big baby.\nYou can have more coins in **{} seconds**.\n The default cooldown for pleading is `1m`.".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

@daily.error
async def daily_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Chill tf out dude", description="Keep asking for money and you'll look like a baby.\nYou can have more coins in {} seconds".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

@bot.command()
async def balance(ctx):
  await bal.invoke(ctx)

#-----------------------
# The fast food commands 
#-----------------------

@bot.command()
async def fastfood(ctx):
  embed = discord.Embed(title="Fast food", description="it's finger lickin' good", color=0xeee657)

  embed.add_field(name="to buy food type in $buy(food)", value="ex\ buydonut", inline=False)

  embed.add_field(name=":doughnut: Donut; Price: $100", value="Gives you a good luck boost of 69%/", inline=False)

  embed.add_field(name=":fries: Fries; Price: $50", value="Gives you $1. No scam guaranteed", inline=False)

  embed.add_field(name=":taco: Tacos; Price: $75", value="overdose of hot sauce and meat? why not?", inline=False)

  await ctx.send(embed=embed)

@bot.command(name = 'buydonut')
async def buydonut(ctx):
  global balances, START_BAL
  user = str(ctx.message.author)
  print(f'In buyDonut(): Author Id = {ctx.message.author.id}, Author Name = {user}')

  if user not in balances:
    await ctx.send(f'hey you didn\'t have an account but i created one for you with a ${START_BAL} bonus')
    balances[user] = START_BAL
  elif balances[user] < 100:
    await ctx.send("oi u don\'t got enough money, don\'t try and scam me mate")
  else:
    await ctx.send("you bought a donut and now you have a good luck boost of 69%")  
    balances[user] -= 100

@bot.command()
async def buyfries(ctx):
  global START_BAL, balances
  user = str(ctx.message.author)
  if user not in balances:
    await ctx.send(f'hey you didn\'t have an account but i created one for you with a ${START_BAL} bonus')
    balances[user] = START_BAL
  elif balances[user] < 50:
    await ctx.send("oi u don\'t got enough money, don\'t try and scam me mate")
  else:
    await ctx.send("you bought some fries and got a buck xd")  
    balances[user] -= 49

@bot.command()
async def buytaco(ctx):
  global START_BAL, balances
  user = str(ctx.message.author)
  if user not in balances:
    await ctx.send(f'hey you didn\'t have an account but i created one for you with a ${START_BAL} bonus')
    balances[user] = START_BAL
  elif balances[user] < 75:
    await ctx.send("oi u don\'t got enough money, don\'t try and scam me mate")
  else:
    await ctx.send("you choked on hot sauce and sued the taco truck. i pray for that poor man")  
    balances[user] -= 75

#--------------------
# Calculator commands
#--------------------

@bot.command()
async def add(ctx, a: int, b: int, *args):
  await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
  await ctx.send(a*b)

@bot.command()
async def divide(ctx, a: int, b: int):
  await ctx.send(a/b)

@bot.command()
async def subtract(ctx, a: int, b: int):
  await ctx.send(a-b)

@bot.command()
async def exponent(ctx, a: int, b: int):
  await ctx.send(a**b)

@bot.command()
async def greet(ctx):
  await ctx.send("wuttup loser")

#----------------------------------
# These are the moderation commands
#----------------------------------

@bot.command()
async def userinfo(ctx, member: discord.Member, *args):
  roles = [role for role in member.roles]

  embed=discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

  embed.set_author(name=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

  embed.add_field(name="ID:", value=member.id)
  embed.add_field(name="Guild name:", value=member.display_name)
  embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
  embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
  embed.add_field(name="Top role:", value=member.top_role.mention)

  embed.add_field(name="Bot?", value=member.bot)
  embed.add_field(name="Idiot?", value="True")

  await ctx.send(embed=embed)

@bot.command()
async def addrole(ctx, role: discord.Role = None, *, member: discord.Member):
  if role is None: 
    await ctx.send("You haven't specified a role!")
  elif member is None:
    await ctx.send("You haven't specified a member!")
  elif role not in ctx.message.guild.roles:
    await ctx.send("This role doesn't exist what are you doing")
  elif member not in ctx.message.guild:
    await ctx.send("The member you specified either doesn't exist or he/she is not in your server")
  else:
    await bot.add_roles(member, role)
    await ctx.send(f'{member} has earned the role: {role}')

@bot.command()
@commands.has_any_role("Moderator")
async def kick(ctx, member: discord.Member=None, *, reason=None):
  if member == None or member == ctx.message.author:
    await ctx.send("oi stupid ya can\'t kick yourself")
    return
  if reason == None:
    reason = "No reason given"
  await member.kick(reason=reason)
  await ctx.send(f"```{member} was kick for {reason}```")

@bot.command()
@commands.has_any_role("Moderator")
async def ban(ctx, member: discord.Member=None, *, reason=None, guild: discord.Guild):
  if member == None or member == ctx.message.author:
    await ctx.send("oi stupid ya can\'t ban yourself")
    return
  elif reason == None:
    reason = "No reason given"
    await member.ban(reason=reason)
    await ctx.send(f"```{member} was banned for {reason}```")
  else:
    await member.ban(reason=reason)
    await ctx.send(f"```{member} was banned for {reason}```")

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def bomb(ctx, limit: int):
  user = ctx.message.author
  if limit > 200:
    await ctx.send("```You can't clear that many messages unless you want your server to die```")
  else:
    await ctx.channel.purge(limit=limit)
    await ctx.send(f"```{limit} message(s) cleared by {user}```", delete_after=3)

@bot.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, reason=None):
  if member == None:
    await ctx.send("oi dum dum give me a member to warn and not yourself")
  elif member == ctx.message.author:
    await ctx.send("Hate to break it to ya but you can't warn yourself")
  elif reason == None:
    reason = "No reason given"
    await ctx.send(f"```@{member} was warned\nReason: {reason}```")
  else:
    await ctx.send(f"```@{member} was warned\nReason: {reason}```")
    await ctx.send(member, "You were warned in {guild}, try not to do it again")


@bot.command(pass_context=True)
async def purge(ctx):
  await bomb.invoke(ctx)

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def mute(ctx, member: discord.Member):
  if member == None or member == ctx.message.author:
    await ctx.send("oi stupid ya can't mute yourself")
    return
  else:
    role = discord.utils.get(member.guild.roles, name="Muted")
    await member.add_roles(member, role)

#---------------------------
# The help and info commands
#---------------------------

bot.remove_command('help')

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Detective Dank's list of commands",description="Type in `$help`'category' to learn more about it", color=0xeee657)

  embed.add_field(name=":joy: Memey", value="`$helpmemey`")

  embed.add_field(name=":hammer_pick: Moderation", value="`$helpmoderation`")

  embed.add_field(name=":fax: Calculation", value="`$helpcalc`")

  embed.add_field(name=":pager: Encryption", value="`$helpencrypt`")

  embed.add_field(name=":money_mouth: Currency", value="`$helpcurrency`")

  embed.add_field(name=":shopping_cart: Shopping", value="`$helpshop`")

  await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
  embed = discord.Embed(title="Detective Dank", description="he protecc, he attacc, but he also perfecc", color=0xeee657)

  embed.add_field(name="Creator", value="diabetic seagull#4741")

  embed.add_field(name="Email The Creator", value="minecraftdoge534@gmail.com", inline=False)

  embed.add_field(name="Server count", value=f"{len(bot.guilds)}", inline=False)

  embed.add_field(name="Language written in", value="Python 3.7")

  embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=630958730644553729&permissions=0&scope=bot")

  await ctx.send(embed=embed)

@bot.command()
async def helpencrypt(ctx):
  embed = discord.Embed(title="Encryption and fun text commands", description="Send secret messages or echo messages")

  embed.add_field(name="`encrypt` , `decrypt` , `echo`", value="Remeber to use `$` before each command!")

  await ctx.send(embed=embed)

@bot.command()
async def helpmoderation(ctx):
  embed = discord.Embed(title="Moderation Commands", description="`kick` , `ban` , `warn` , `bomb` , `purge`")

  embed.add_field(name="lol", value="The role needed for these actions are either `Moderator` , `MODERATOR` , or `MOD`")

  await ctx.send(embed=embed)

@bot.command()
async def helpmemey(ctx):
  embed = discord.Embed(title=":joy:Memey Commands", description="`powerofgod` , `tryme` , `meme` , `avatar` , `justdoit` , `roast` , `dank` , `8ball` , `doggo` , `howgay` , `randomrob`")

  await ctx.send(embed=embed)

@bot.command()
async def helpcurrency(ctx):
  embed = discord.Embed(title="Currency Commands", description="`balance` , `plead`")

  await ctx.send(embed=embed)

bot.run('NjMwOTU4NzMwNjQ0NTUzNzI5.XdF_6g.7CX3nDwBfaWCNnTodSW1TIOoL5U')
