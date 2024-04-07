from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from weather_api import get_bot
from simple_responses import get_response
from interactive_responses import start_timer, pause_timer, resume_timer, cancel_timer

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


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
@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user}. Ready to serve!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
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
    client.run(token=TOKEN)
    get_bot.run(token = TOKEN)


if __name__ == '__main__':
    main()