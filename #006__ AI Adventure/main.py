from astrapy import DataAPIClient
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import time

load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_KEYSPACE = os.environ.get("ASTRA_DB_KEYSPACE")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ASTRA_DB_SECURE_BUNDLE_PATH = os.environ.get("ASTRA_DB_SECURE_BUNDLE_PATH")

session = Cluster(
    cloud={"secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH},
    auth_provider=PlainTextAuthProvider("token", ASTRA_DB_APPLICATION_TOKEN),
).connect()

# Initialize the client
client = DataAPIClient(ASTRA_DB_APPLICATION_TOKEN)
db = client.get_database_by_api_endpoint(
 ASTRA_DB_API_ENDPOINT,
    namespace=ASTRA_DB_KEYSPACE,
)
  
print(f"Connected to Astra DB: {db.name()}")

message_history = CassandraChatMessageHistory(
    session_id="game",
    session=session,
    keyspace=ASTRA_DB_KEYSPACE,
    ttl_seconds=3600 #store all this for a maximum of 60 minutes
)

message_history.clear()
time.sleep(5)

cass_buff_memory = ConversationBufferMemory(
    memory_key="chat_history",
    # chat_memory=message_history
)

template = """
You are the guardian of tales, and it is your duty to guide a wanderer through their chosen adventure.
Today, a new seeker has arrived, eager to carve out a story of their own making.
First, please ask the seeker to choose a name for their character.
This name will be used throughout the journey to personalize their experience.
Next, ask them to select a genre from the following options: fantasy, sci-fi, mystery, or horror.
The chosen genre will shape the world and the challenges they encounter.
Once the character's name and genre are established, begin narrating their adventure.
Throughout the journey, use this format to guide the interaction.

Here are some guidelines to ensure a dynamic and engaging experience:

1. You will start by asking the player to choose name that will be used later in the game.
2. After getting the name start the journey by asking player's genre.
3. Design several paths within the chosen genre that lead to different outcomes, some successful and others perilous.
4. Some paths should lead to death. If the character dies, provide a detailed account of what led to this end and conclude with the phrase: "The End." This will signal the conclusion of the game.
5. Don't make any response for human

Here is the chat history, use this to understand what to say next: {chat_history}
Answer the following human query/followup.
Human: {human_input}
AI:
"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template 
)

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=cass_buff_memory
)

choice = ""
import sys
while True:
    response = llm_chain.predict(human_input=choice)
    for c in response.strip():
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)
    print("\n")

    if "The End.".lower() in response.lower():
        break

    choice = input("Your reply: ")
