# Discord Bot

This Discord bot is designed to interact with users by responding to messages sent in channels where the bot is present or directly to the bot in a private message. It's built using Python and leverages the Discord API for message interactions.

## Features

- **Message Handling**: Responds to both public and private messages. Private messages are prefixed with a `?`.
- **Environment Variables**: Uses environment variables for secure storage of the Discord token.
- **Error Handling**: Includes basic error handling for response generation failures.

## Prerequisites

Before you start, ensure you have the following installed:
- Python 3.6 or higher
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Additionally, you'll need a Discord token. Follow [Discord's official guide](https://discord.com/developers/docs/intro) on setting up a bot and obtaining your token.

## Setup

1. Clone this repository to your local machine.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Create a .env file in the root directory and add your Discord token:
    ```bash
    DISCORD_TOKEN=your_token_here
    ```
4. Run the bot:
    ```bash
    python main.py
    ```
## Usage
After starting the bot, it will listen to messages in any channel it has been added to. To interact with the bot, simply send a message. For private responses, prefix your message with ?.
