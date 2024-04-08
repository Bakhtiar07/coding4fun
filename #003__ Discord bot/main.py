from typing import Final
import os
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Client, Message
from simple_responses import get_response
from interactive_responses import start_timer, pause_timer, resume_timer, cancel_timer

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
api_key: Final[str] = os.getenv('API_KEY')
base_url = "http://api.openweathermap.org/data/2.5/weather?"


# STEP 1: BOT SETUP
intents: Intents = discord.Intents.default()
intents.message_content = True  # NOQA
intents.message_content = True
client: Client = Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
# @client.event 
# async def on_ready() -> None:
#     print(f'Logged in as {client.user}. Ready to serve!')
    
@bot.event
async def on_ready() -> None:
    print(f'Logged in as{bot.user}.')


# STEP 4: HANDLING INCOMING MESSAGES

@bot.command()
async def weather(ctx, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    #channel = ctx.message.channel
    
    #Check if city name is valid
    if x["cod"] != "404":
        #async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            
            await ctx.send(embed=embed)
    else:
            await ctx.send(f"There was no results about this place!")

@bot.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return # Avoid bot responding to itself
    if message.content.lower().startswith('start timer'):
        await start_timer(message)
    elif message.content.lower().startswith('pause timer'):
        await pause_timer(message)
    elif message.content.lower().startswith('resume timer'):
        await resume_timer(message)
    elif message.content.lower().startswith('cancel timer'):
        await cancel_timer(message)
    if message.content.lower().startswith('!weather'):
        city_name = message.content[len('!weather'):].strip()
        await weather(message, city_name)
    
        
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    bot.run(token=TOKEN)
    #client.run(token=TOKEN)


if __name__ == '__main__':
    main()