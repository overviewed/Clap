import discord, os, threading, requests, sys, time, random, urllib.request
from pystyle import Colors, Colorate
from discord.ext import commands
from itertools import cycle
from colorama import Fore
from colored import fg

p1 = fg('#8c00ff')
r1 = '\x1b[38;5;196m'
proxies = []
rotating = cycle(proxies)
client = commands.Bot(command_prefix = "clap", intents = discord.Intents.all())

def clear():
  if sys.platform.startswith("win"):
    os.system('cls')
  elif sys.platform == 'linux' or 'darwin':
    os.system('clear')

def Spinner():
  os.system(f'cls & mode 85,20 & title Clap by Loopy - Loading')
  l = ['|', '/', '-', '\\', '|']
  for i in l+l+l:
    sys.stdout.write(f'\r{p1}I solemnly swear im up to no good...'+i)
    sys.stdout.flush()
    time.sleep(0.2)
Spinner()

p1 = fg('#8c00ff')
r1 = '\x1b[38;5;196m'
b1 = '\033[34m'

clear()
os.system(f'cls & mode 85,20 & title Clap by Loopy - Login')
print(Colorate.Horizontal(Colors.blue_to_purple, 
"""
 ▄▄· ▄▄▌   ▄▄▄·  ▄▄▄·
▐█ ▌▪██•  ▐█ ▀█ ▐█ ▄█
██ ▄▄██▪  ▄█▀▀█  ██▀·
▐███▌▐█▌▐▌▐█ ▪▐▌▐█▪·•
·▀▀▀ .▀▀▀  ▀  ▀ .▀

"""))
prox = input(f"{p1}[?] Do you want to use proxies during this session <yes/no>: ")
while prox != 'yes' and prox != 'no':
  print(f"{r1}[!] Invalid option...")
  prox = input(f"{p1}[?] Do you want to use proxies during this session <y/n>: ")
  
tokentype = input(f"{p1}[?] Are you using a Bot or User token <bot/user>: ")
while tokentype != "bot" and tokentype != "user":
  print(f"{r1}[!] Invalid option...")
  tokentype = input(f"{p1}[?] Are you using a Bot or User token <bot/user>: ")
  
token = input(f'{p1}[?] Enter token: ')
if tokentype == "bot":
  type = "Bot"
  headers = {'Authorization': f'Bot {token}'}
elif tokentype == "user":
  type = "Human"
  headers = {'Authorization': f'{token}'}

async def Exit():
  os.system(f'cls & mode 85,20 & title Clap by Loopy - Bye Bye')
  await client.close()
  print(f"{p1}Bye bye >_<")
  time.sleep(2)
  os._exit(0)

def Ban(guild_id, member):
  if prox == 'yes':
    while True:
      r = requests.put(f"https://discord.com/api/v{random.randint(6,9)}/guilds/{guild_id}/bans/{member}", headers=headers, proxies={"http": 'http://' + next(rotating)})
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{p1}[+] Banned {member.strip()}\n")
      if r.status_code == 429:
        print(f"{r1}[!] Rate limited sleeping for {r.json()['retry_after']}")
        time.sleep(int(r.json()['retry_after']))
        Ban(guild_id, member)
      if r.status_code == 403:
        print(f"{r1}[!] Missing permissions")
      if r.status_code == 404:
        print(f"{r1}[!] Error || Most likely removed from guild")
        pass
  if prox == 'no':
    while True:
      r = requests.put(f"https://discord.com/api/v{random.randint(6,9)}/guilds/{guild_id}/bans/{member}", headers=headers)
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{p1}[+] Banned {member.strip()}\n")
      if r.status_code == 429:
        print(f"{r1}[!] Rate limited sleeping for {r.json()['retry_after']}")
        time.sleep(int(r.json()['retry_after']))
        Ban(guild_id, member)
      if r.status_code == 403:
        print(f"{r1}[!] Missing permissions")
      if r.status_code == 404:
        print(f"{r1}[!] Error || Most likely removed from guild")
        pass
  else:
    os._exit(0)

def Kick(guild_id, member):
  if prox == 'yes':
    while True:
      r = requests.delete(f"https://discord.com/api/v{random.randint(6,9)}/guilds/{guild_id}/members/{member}", headers=headers, proxies={"http": 'http://' + next(rotating)})
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{p1}[+] Kicked {member.strip()}\n")
      if r.status_code == 429:
        print(f"{r1}[!] Rate limited sleeping for {r.json()['retry_after']}")
        time.sleep(int(r.json()['retry_after']))
        Kick(guild_id, member)
      if r.status_code == 403:
        print(f"{r1}[!] Missing permissions")
      if r.status_code == 404:
        print(f"{r1}[!] Error || Most likely removed from guild")
        pass
  if prox == 'no':
    while True:
      r = requests.delete(f"https://discord.com/api/v{random.randint(6,9)}/guilds/{guild_id}/members/{member}", headers=headers)
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{p1}[+] Kicked {member.strip()}\n")
      if r.status_code == 429:
        print(f"{r1}[!] Rate limited sleeping for {r.json()['retry_after']}")
        time.sleep(int(r.json()['retry_after']))
        Kick(guild_id, member)
      if r.status_code == 403:
        print(f"{r1}[!] Missing permissions")
      if r.status_code == 404:
        print(f"{r1}[!] Error || Most likely removed from guild")
        pass
  else:
    os._exit(0)

async def MassBan():
  clear()
  while True:
    try:
      guild_id = int(input(f'{r1}[?] Guild ID: '))
      break
    except ValueError:
      print(f"{r1}Invalid Value")
      continue
  for guild in client.guilds:
    if guild.id == guild_id:
      print(f"{p1}{guild.name} has been targeted")
      members = open('members.txt')
      for member in members:
        threading.Thread(target=Ban, args=(guild_id, member,)).start()
      members.close()

async def MassKick():
  clear()
  while True:
    try:
      guild_id = int(input(f'{r1}[?] Guild ID: '))
      break
    except ValueError:
      print(f"{r1}Invalid Value")
      continue
  for guild in client.guilds:
    if guild.id == guild_id:
      print(f"{p1}{guild.name} has been targeted")
      members = open('members.txt')
      for member in members:
        threading.Thread(target=Kick, args=(guild_id, member,)).start()
      members.close()

async def Scrape():
  clear()
  while True:
    try:
      guild_id = int(input(f'{p1}[?] Guild ID: '))
      break
    except ValueError:
      print(f"{r1}Invalid Value")
      continue
  for guild in client.guilds:
    if guild.id == guild_id:
      print(f"{p1}Scraping {guild.name}...")
      members_ = 0
      f = open("members.txt", "a+")
      for member in guild.members:
        f.write(f"{member.id}\n")
        members_ += 1
      print(f"{r1}Scraped {members_} Members from {guild.name}")
      return

async def ProxyScrape():
  clear()
  req = urllib.request.Request("http://free-proxy-list.net/")
  req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")
  prox = urllib.request.urlopen(req)
  part = str(prox.read())
  part = part.split("<tbody>")
  part = part[1].split("</tbody>")
  part = part[0].split("<tr><td>")
  proxylist = ""
  for proxy in part:
    proxy = proxy.split("</td><td>")
    try:
      proxylist=proxylist + proxy[0] + ":" + proxy[1] + "\n"
    except:
      pass
  print(f"{p1}Proxies Scraped")
  out_file = open("proxies.txt","w")
  out_file.write(proxylist)
  out_file.close()


async def clap():
  os.system(f'cls & mode 85,20 & title Clap by Loopy/Raze - Clap Menu')
  print(Colorate.Horizontal(Colors.blue_to_purple, 
"""
 ▄▄· ▄▄▌   ▄▄▄·  ▄▄▄·
▐█ ▌▪██•  ▐█ ▀█ ▐█ ▄█
██ ▄▄██▪  ▄█▀▀█  ██▀·
▐███▌▐█▌▐▌▐█ ▪▐▌▐█▪·•
·▀▀▀ .▀▀▀  ▀  ▀ .▀

"""))
  print(Colorate.Horizontal(Colors.blue_to_purple, 
f'''
Logged in as {client.user}                           
╔══════════════════════════╗
║  [1] Mass Ban            ║ 
║  [2] Mass Kick           ║
║  [3] Scrape              ║
║  [4] Proxy Scrape        ║
║  [5] Credits             ║ 
║  [6] Exit                ║
╚══════════════════════════╝
'''))
  select = input(f'''{p1}┌──{p1}({Fore.WHITE}root@Clap{p1}){p1}[{Fore.WHITE}?{Fore.WHITE}{p1}]{p1}:
└─{p1}{p1}${p1}{Fore.RESET}: ''')
  if select == '1':
    await MassBan()
    time.sleep(2)
    input(f"{p1}Tasks Complete press enter to continue")
    clear()
    await clap()
  if select == '2':
    await MassKick()
    time.sleep(2)
    input(f"{p1}Tasks Complete press enter to continue")
    clear()
    await clap()
  if select == '3':
    await Scrape()
    time.sleep(2)
    input(f"{p1}Tasks Complete press enter to continue")
    clear()
    await clap()
  if select == '4':
    await ProxyScrape()
    time.sleep(2)
    input(f"{p1}Tasks Complete press enter to continue")
    clear()
    await clap()
  if select == '5':
    input(f"{p1}Clap was created by Loopy\nIf you skid this u like getting fucked by fat gay men in the ass and eating stale honey buns with ur great grandpas cum on it\nPress enter to continue")
    clear()
    await clap()
  if select == '6':
    await Exit()
  else:
    input(f"{r1}Invalid option...")
    clear()
    await clap()

@client.event
async def on_ready():
  clear()
  await clap()

if type == "Human":
  try:
    client.run(token, bot=False)
  except discord.errors.LoginFailure as e:
    print(f"{r1}[!] Invalid Token: {e}")
  except Exception as e:
    print(f"{r1}[!] An error occured: {e}")
    
elif type == "Bot":
  try:
    client.run(token, bot=True)
  except discord.errors.LoginFailure as e:
    print(f"{r1}[!] Invalid Token: {e}")
  except Exception as e:
    print(f"{r1}[!] An error occured: {e}")