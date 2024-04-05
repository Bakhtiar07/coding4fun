from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    # List of commands handled by interactive_responses.py
    interactive_commands = ['start timer', 'pause timer', 'resume timer', 'cancel timer']

    # Check if the user_input is an interactive command
    if any(command in lowered for command in interactive_commands):
        # If it is, return None or an empty string to indicate no response should be sent for this input
        return None
    
    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Up and running!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    elif 'you\'re awesome' in lowered or 'love you' in lowered or 'you\'re great' in lowered:
        return choice(["Oh, you're making me blush!", "Thanks, you're pretty awesome yourself!", "I appreciate that!"])
    elif 'tell me a joke' in lowered or 'make me laugh' in lowered or 'joke' in lowered:
        return choice(["Why don't scientists trust atoms? Because they make up everything!", 
                   "I told my computer I needed a break, and it said 'You seem to be working hard, try chilling with some ice-cream!'"])
    elif "i'm feeling down" in lowered or "need some motivation" in lowered or "cheer me up" in lowered:
        return choice(["Keep your head up. Tomorrow is another day!", 
                   "You're doing great, don't forget how far you've come!", 
                   "Every day is a second chance. You've got this!"])
    elif "tell me a fact" in lowered or "give me a fact" in lowered or "random fact" in lowered:
        return choice(["Did you know that octopuses have three hearts?", 
                   "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old but still perfectly edible!", 
                   "A group of flamingos is called a 'flamboyance'."])

# Add similar elif blocks for other responses

    else:
        return choice(['I\'m afraid I do not follow...',
                       'Can you rephrase that?'])



