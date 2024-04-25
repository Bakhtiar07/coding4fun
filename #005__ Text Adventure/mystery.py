print("The Mystery of Eldritch Manor")
print("You find yourself standing at the edge of a dense forest, the path behind you obscured by an unnatural fog. Before you lies Eldritch Manor, a once-magnificent estate now fallen into disrepair. Rumors speak of a priceless artifact hidden within its walls, guarded by puzzles, traps, and something far more sinister. Your task is to navigate the manor, uncover its secrets, and escape with the artifact... and your life.")
answer = input("Would you like to play this game? (y/n)")
if answer.lower() == 'y':
    print("Welcome to Eldritch Manor")
    start = True
    Inventory = ['Flashlight', 'Notepad', 'Pen']
else:
    print("Okay, some other time")
    
if start == True:
    print("As you approach the manor's heavy, oak door, you notice it's slightly ajar, creaking on its hinges. You have a few options to begin your exploration:")
    print("1. Enter through the main door. The direct approach, but potentially the most dangerous.")
    print("2. Look for another way in. Perhaps a less conspicuous entry exists that could offer the element of surprise.")
    print ("3. Examine the exterior. There might be more to learn before venturing inside.")
    C1=input("What do you choose to do? (1/2/3)")
    
    if C1.lower() == '3':
        third_choice = True
        print("You decide to take a moment to examine the exterior of Eldritch Manor, believing that understanding your surroundings could provide an advantage. The manor, ensnared by the gnarled fingers of ancient trees, whispers tales of forgotten glory through its cracked and weathered facade. To the left, you notice a series of broken windows, remnants of a greenhouse that nature has begun to reclaim. On the right, a dilapidated garden shed stands, its door hanging off one rusty hinge. The main entrance looms before you, imposing yet inviting in a way that sends shivers down your spine.")
        print("As you circle the manor, three areas catch your attention:")
        print("1. The Greenhouse: Nature's unbridled dominion over man's creation is on full display here. Could something useful be hidden among the flora overtaking the structure?")
        print("2. The Garden Shed: It's small and looks like it might collapse at any moment, but sheds often hold tools and other items that could be useful.")
        print("3. A Mysterious Well: Almost hidden by the overgrowth, you find an old well sealed with a heavy stone lid. It seems out of place and piques your curiosity.")
        C2=input("Where do you choose to investigate first?")
        
        if C2.lower() == '1':
            first_choice = True
            print("Drawn by the tangled allure of nature reclaiming civilization, you decide to explore the greenhouse first. As you step closer, the scent of damp earth and decay mixes with the fragrance of wildflowers that have pushed their way through broken panes and shattered tables. The structure, though on the verge of collapse, houses a variety of plants, both common and exotic, thriving in the chaos.")
            print("Inside, the light is dappled, filtered through the canopy of leaves above. Vines have woven themselves into the very fabric of the building, and it's clear that no human has set foot here for a long time. As you navigate through the overgrowth, you keep an eye out for anything that might be of use.")
            print("Your search yields:")
        
        