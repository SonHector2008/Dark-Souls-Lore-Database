import json

lore_database = {
    "Artorias the Abysswalker": {
        "category": "Character",
        "description": ("Artorias was one of the Four Knights of Gwyn, known for his unbending will of steel. "
                        "He ventured into the Abyss to defeat the Darkwraiths, but was ultimately consumed by it. "
                        "His legacy lives on through his loyal companion, Sif."),
        "tags": ["Knight", "Abyss", "Boss"]
    },
    "Sif, the Great Grey Wolf": {
        "category": "Character",
        "description": ("Sif, the loyal companion of Artorias, guards his master's grave in the Darkroot Garden. "
                        "With Artorias' greatsword in its jaws, Sif stands as a final guardian against those who would disturb Artorias' rest."),
        "tags": ["Wolf", "Guardian", "Boss"]
    },
    "Gwyn, Lord of Cinder": {
        "category": "Character",
        "description": ("Gwyn, the Lord of Sunlight, led the gods to victory against the Dragons in the Age of Ancients. "
                        "He sacrificed himself to kindle the First Flame, prolonging the Age of Fire but becoming the Lord of Cinder, "
                        "a hollowed shell of his former self."),
        "tags": ["God", "Fire", "Boss"]
    },
    "Ornstein and Smough": {
        "category": "Enemy",
        "description": ("Dragon Slayer Ornstein and Executioner Smough are the last line of defense in Anor Londo. "
                        "Ornstein, one of Gwyn's Four Knights, is known for his speed and power, while Smough, the executioner, "
                        "wields immense strength and brutality."),
        "tags": ["Knight", "Guardian", "Boss"]
    },
    "Seath the Scaleless": {
        "category": "Character",
        "description": ("Seath the Scaleless is a traitorous dragon who allied with Gwyn during the war against the Everlasting Dragons. "
                        "His betrayal and research into immortality drove him mad, and he now resides in the Duke's Archives."),
        "tags": ["Dragon", "Madness", "Boss"]
    },
    "Manus, Father of the Abyss": {
        "category": "Character",
        "description": ("Manus, once a human, was transformed into a primeval entity by the unchecked spread of the Abyss. "
                        "His rage and despair gave birth to the Dark, and he is considered the progenitor of the Abyss."),
        "tags": ["Abyss", "Dark", "Boss"]
    },
    "Gravelord Nito": {
        "category": "Character",
        "description": ("Nito, the First of the Dead, holds command over death itself. "
                        "He is one of the beings who obtained a Lord Soul from the First Flame and is now entombed within the Tomb of the Giants."),
        "tags": ["Undead", "Death", "Boss"]
    },
    "The Four Kings": {
        "category": "Enemy",
        "description": ("The Four Kings once ruled over New Londo, but were corrupted by the Abyss. "
                        "Now, they reside in the Abyss, serving as dark lords who seek to consume all."),
        "tags": ["Kings", "Abyss", "Boss"]
    },
    "Ceaseless Discharge": {
        "category": "Enemy",
        "description": ("The Ceaseless Discharge is the last surviving child of the Witch of Izalith. "
                        "He is a massive lava-spewing demon who guards his sister's corpse in the Demon Ruins."),
        "tags": ["Demon", "Fire", "Boss"]
    },
    "Chaos Witch Quelaag": {
        "category": "Character",
        "description": ("Quelaag is a daughter of the Witch of Izalith who was transformed into a half-spider, half-human demon. "
                        "She resides in Blighttown, guarding the second Bell of Awakening and protecting her frail sister, the Fair Lady."),
        "tags": ["Demon", "Fire", "Boss"]
    },
    "Bed of Chaos": {
        "category": "Enemy",
        "description": ("The Bed of Chaos is the source of all demons, created by the Witch of Izalith's failed attempt to recreate the First Flame. "
                        "It is a corrupted and uncontrollable mass of fire and roots, residing deep within the Demon Ruins."),
        "tags": ["Demon", "Fire", "Boss"]
    },
    "Crossbreed Priscilla": {
        "category": "Character",
        "description": ("Priscilla is a half-dragon, half-god hybrid, residing in the Painted World of Ariamis. "
                        "She possesses the power of lifehunt, a deadly form of life drain. "
                        "Despite her power, she lives in isolation, wishing only to be left alone."),
        "tags": ["Dragon", "Isolation", "Boss"]
    },
    "Pinwheel": {
        "category": "Character",
        "description": ("Pinwheel is a necromancer who resides in the Catacombs. "
                        "He is a being composed of three fused bodies, seeking to revive his lost family. "
                        "Pinwheel controls the power of the Rite of Kindling."),
        "tags": ["Necromancer", "Undead", "Boss"]
    },
    "Gwyndolin, Dark Sun": {
        "category": "Character",
        "description": ("Gwyndolin, the last-born son of Gwyn, was raised as a daughter due to his affinity with the moon. "
                        "He guards the illusion of Anor Londo and leads the Darkmoon Blades, a covenant of retribution."),
        "tags": ["God", "Illusion", "Boss"]
    },
    "Capra Demon": {
        "category": "Enemy",
        "description": ("The Capra Demon is a lesser demon found in the Depths and Undead Burg. "
                        "It is known for its brutal strength and dual greatswords, often accompanied by lesser demons or dogs."),
        "tags": ["Demon", "Brutal", "Boss"]
    },
    "Gaping Dragon": {
        "category": "Enemy",
        "description": ("The Gaping Dragon was once a noble creature, a descendant of the Everlasting Dragons. "
                        "However, it was consumed by insatiable hunger, transforming into a grotesque, all-devouring beast."),
        "tags": ["Dragon", "Hunger", "Boss"]
    },
    "Taurus Demon": {
        "category": "Enemy",
        "description": ("The Taurus Demon is a formidable creature encountered on the Undead Burg's bridge. "
                        "It is a large, aggressive demon that attacks any who cross its path, wielding a massive axe."),
        "tags": ["Demon", "Aggressive", "Boss"]
    },
    "Moonlight Butterfly": {
        "category": "Enemy",
        "description": ("The Moonlight Butterfly is a magical creature created by Seath the Scaleless. "
                        "It floats serenely in the Darkroot Garden, attacking intruders with powerful sorcery."),
        "tags": ["Magical", "Sorcery", "Boss"]
    },
    "Iron Golem": {
        "category": "Enemy",
        "description": ("The Iron Golem is a massive sentinel guarding the entrance to Anor Londo. "
                        "It was created by the gods to protect their city and prevent unworthy adventurers from progressing."),
        "tags": ["Golem", "Guardian", "Boss"]
    },
    "Bell Gargoyles": {
        "category": "Enemy",
        "description": ("The Bell Gargoyles are twin stone guardians protecting the first Bell of Awakening atop the Undead Parish. "
                        "They come to life when threatened, wielding halberds and breathing fire."),
        "tags": ["Gargoyle", "Guardian", "Boss"]
    },
    "Stray Demon": {
        "category": "Enemy",
        "description": ("The Stray Demon is an ancient demon imprisoned in the Undead Asylum. "
                        "It is a larger and more powerful version of the Asylum Demon, with pyrokinetic abilities."),
        "tags": ["Demon", "Prisoner", "Boss"]
    },
    "Sanctuary Guardian": {
        "category": "Enemy",
        "description": ("The Sanctuary Guardian is a ferocious chimera that guards the entrance to the Oolacile Sanctuary. "
                        "It is swift and deadly, with the ability to poison and strike with lightning."),
        "tags": ["Guardian", "Chimera", "Boss"]
    },
    "Kalameet, Black Dragon": {
        "category": "Enemy",
        "description": ("Black Dragon Kalameet is an ancient and fearsome dragon residing in the Royal Wood. "
                        "He is known for his intelligence, strength, and the ability to invoke the power of the Abyss."),
        "tags": ["Dragon", "Abyss", "Boss"]
    },
    "Centipede Demon": {
        "category": "Enemy",
        "description": ("The Centipede Demon is a creature born from the Bed of Chaos, residing in the Demon Ruins. "
                        "It is a multi-limbed demon with the ability to manipulate lava, creating a perilous battlefield."),
        "tags": ["Demon", "Fire", "Boss"]
    },
    "Demon Firesage": {
        "category": "Enemy",
        "description": ("The Demon Firesage is a powerful sorcerer demon who guards the way to the Bed of Chaos. "
                        "It is an enhanced version of the Asylum Demon, with a mastery of fire sorcery."),
        "tags": ["Demon", "Sorcery", "Boss"]
    },
    "Asylum Demon": {
        "category": "Enemy",
        "description": ("The Asylum Demon is the first major boss encountered in Dark Souls, residing in the Northern Undead Asylum. "
                        "It is a large, brutish demon wielding a massive hammer, serving as the tutorial boss."),
        "tags": ["Demon", "Tutorial", "Boss"]
    },
    "Quelana of Izalith": {
        "category": "NPC",
        "description": ("Quelana is one of the Daughters of Chaos, a survivor of the Witch of Izalith's failed experiment. "
                        "She resides in Blighttown, teaching pyromancy to those she deems worthy."),
        "tags": ["Chaos", "Pyromancy"]
    },
    "Lautrec of Carim": {
        "category": "NPC",
        "description": ("Lautrec is a knight from Carim known for his treachery and pursuit of the goddess Fina. "
                        "He is a ruthless character who can be either an ally or an adversary, depending on the player's actions."),
        "tags": ["Knight", "Treachery"]
    },
    "Big Hat Logan": {
        "category": "NPC",
        "description": ("Logan is a master sorcerer who has devoted his life to studying magic. "
                        "He is known for his enormous hat and his quest for knowledge, which eventually leads him to madness."),
        "tags": ["Sorcerer", "Madness"]
    },
    "Havel the Rock": {
        "category": "NPC",
        "description": ("Havel was a close friend of Gwyn who opposed Seath the Scaleless. "
                        "He is known for his incredible strength and the thick stone armor he wears, earning him the title 'The Rock.'"),
        "tags": ["Knight", "Strength"]
    },
    "Oscar of Astora": {
        "category": "NPC",
        "description": ("Oscar is a knight from Astora who helps the player character escape from the Undead Asylum. "
                        "He provides the player with their first Estus Flask and the key to begin their journey."),
        "tags": ["Knight", "Ally"]
    },
    "Petrus of Thorolund": {
        "category": "NPC",
        "description": ("Petrus is a cleric from Thorolund who seeks to recover the Rite of Kindling. "
                        "He can be found in Firelink Shrine, where he teaches miracles to the player."),
        "tags": ["Cleric", "Miracle"]
    },
    "Gwynevere, Princess of Sunlight": {
        "category": "NPC",
        "description": ("Gwynevere is the daughter of Gwyn, Lord of Sunlight. "
                        "She resides in Anor Londo, offering the player the Lordvessel and guidance on their quest."),
        "tags": ["God", "Sunlight"]
    },
    "Hawkeye Gough": {
        "category": "Vendor",
        "description": ("Gough is one of Gwyn's Four Knights, known for his unparalleled skill with a greatbow. "
                        "He resides in Oolacile, blinded but still possessing immense strength and wisdom."),
        "tags": ["Knight", "Archery"]
    },
    "Solaire of Astora": {
        "category": "NPC",
        "description": ("Solaire is a warrior from Astora on a quest to find his own sun. "
                        "He is known for his unwavering optimism and is a key ally to the player throughout their journey."),
        "tags": ["Warrior", "Ally"]
    },
    "Andre of Astora": {
        "category": "Vendor",
        "description": ("Andre is a blacksmith from Astora who helps the player upgrade their weapons and armor. "
                        "He is one of the most reliable and trustworthy NPCs in the game."),
        "tags": ["Blacksmith", "Ally"]
    },
    "Shiva of the East": {
        "category": "NPC",
        "description": ("Shiva is a warrior from the East, known for his skill with curved swords. "
                        "He is the captain of the Forest Hunter covenant, residing in Darkroot Garden."),
        "tags": ["Warrior", "Forest"]
    },
    "Velka, Goddess of Sin": {
        "category": "Character",
        "description": ("Velka is a mysterious deity associated with sin, retribution, and the occult. "
                        "She is the patron of the Pardoners, who offer absolution to players."),
        "tags": ["Goddess", "Sin"]
    },
    "New Londo": {
        "category": "Location",
        "description": ("New Londo was once a thriving city, now flooded and filled with the restless spirits of its former inhabitants. "
                        "It is the home of the Darkwraiths, cursed beings that thrive in the Abyss."),
        "tags": ["Abyss", "Cursed"]
    },
    "Anor Londo": {
        "category": "Location",
        "description": ("Anor Londo is the city of the gods, a majestic and sprawling metropolis that serves as the seat of Gwyn's power. "
                        "It is a place of grandeur and light, but also of illusions and secrets."),
        "tags": ["Gods", "Illusions"]
    },
    "Blighttown": {
        "category": "Location",
        "description": ("Blighttown is a treacherous, poison-filled swamp located deep within Lordran. "
                        "It is a place of misery and decay, inhabited by toxic creatures and plagued by disease."),
        "tags": ["Poison", "Decay"]
    },
    "Firelink Shrine": {
        "category": "Location",
        "description": ("Firelink Shrine is the hub of the player's journey, a place of respite and connection to other areas. "
                        "It is the home of the Fire Keeper, who maintains the bonfire that the player can rest at."),
        "tags": ["Hub", "Bonfire"]
    },
    "Kiln of the First Flame": {
        "category": "Location",
        "description": ("The Kiln of the First Flame is the final area of the game, where the First Flame is located. "
                        "It is a desolate, ashen place where the player confronts Gwyn, Lord of Cinder."),
        "tags": ["Final Area", "Fire"]
    },
    "Estus Flask": {
        "category": "Item",
        "description": ("The Estus Flask is a mystical flask that stores healing energy, allowing the player to restore health. "
                        "It is filled at bonfires, which are linked to the First Flame."),
        "tags": ["Healing", "Bonfire"]
    },
    "Lordvessel": {
        "category": "Item",
        "description": ("The Lordvessel is a powerful artifact that allows the player to warp between bonfires and hold the power of the Lord Souls. "
                        "It is given to the player by Gwynevere in Anor Londo."),
        "tags": ["Artifact", "Warp"]
    },
    "The Chosen Undead": {
        "category": "Character",
        "description": ("The Chosen Undead is the player character in Dark Souls, an undead warrior destined to link the fire or usher in the age of darkness. As the protagonist, the Chosen Undead embarks on a perilous journey through Lordran, facing countless trials and powerful enemies. The character's story is deeply intertwined with the themes of fate, sacrifice, and the cyclical nature of the world, where they must make critical decisions that determine the future of the world."),
        "tags": ["Undead", "Fate", "Sacrifice", "Protagonist"]
    }
}

def display_help():
    print("\nHelp Menu:")
    print("1. Search - Search for lore entries by keyword, category, or tag.")
    print("2. Browse by Category - View all entries in a specific category.")
    print("3. Browse by Tag - View all entries with a specific tag.")
    print("4. Add Entry - Add a new lore entry to the database.")
    print("5. Edit Entry - Edit an existing lore entry.")
    print("6. Delete Entry - Remove a lore entry from the database.")
    print("7. Export - Save the database to a JSON file.")
    print("8. Import - Load a database from a JSON file.")
    print("9. Help - Display this help menu.")
    print("10. Exit - Exit the program.")

def search_lore(keyword, category=None, tag=None):
    results = {}
    for title, entry in lore_database.items():
        if keyword.lower() in title.lower() or keyword.lower() in entry['description'].lower():
            if (category is None or entry['category'].lower() == category.lower()) and \
               (tag is None or tag.lower() in entry['tags']):
                results[title] = entry
    return results

def browse_entries(by):
    results = {}
    if by == "category":
        categories = set(entry['category'] for entry in lore_database.values())
        print("\nAvailable Categories:")
        for cat in categories:
            print(f"- {cat}")
        category = input("\nEnter the category to browse: ").strip()
        results = {title: entry for title, entry in lore_database.items() if entry['category'].lower() == category.lower()}
    elif by == "tag":
        tags = set(tag.lower() for entry in lore_database.values() for tag in entry['tags'])
        print("\nAvailable Tags:")
        for tag in tags:
            print(f"- {tag}")
        tag_input = input("\nEnter the tag to browse: ").strip().lower()  # Convert to lowercase for consistent matching
        results = {title: entry for title, entry in lore_database.items() if tag_input in [tag.lower() for tag in entry['tags']]}
    
    if results:
        print(f"\nFound {len(results)} result(s):")
        for title in results:
            print(f"- {title}")
        selected_title = input("\nEnter the title of the lore entry you'd like to view (or type 'back' to return to the main menu): ").strip()
        if selected_title.lower() == 'back':
            return
        if selected_title in results:
            entry = results[selected_title]
            print(f"\nTitle: {selected_title}")
            print(f"Category: {entry['category']}")
            print(f"Description: {entry['description']}")
            print(f"Tags: {', '.join(entry['tags'])}")
        else:
            print("Invalid selection. Please try again.")
    else:
        print("No results found. Please try again.")

def add_lore_entry():
    title = input("\nEnter the title of the lore entry: ").strip()
    if title in lore_database:
        print("This title already exists. Please choose a different title.")
        return
    category = input("Enter the category of the lore entry: ").strip()
    description = input("Enter the description of the lore entry: ").strip()
    tags = input("Enter tags for the lore entry (comma-separated): ").strip().split(',')
    tags = [tag.strip().lower() for tag in tags]
    lore_database[title] = {
        'category': category,
        'description': description,
        'tags': tags
    }
    print(f"Lore entry '{title}' added successfully.")

def edit_lore_entry():
    title = input("\nEnter the title of the lore entry to edit: ").strip()
    if title not in lore_database:
        print("This title does not exist. Please try again.")
        return
    category = input("Enter the new category of the lore entry (leave blank to keep current): ").strip()
    description = input("Enter the new description of the lore entry (leave blank to keep current): ").strip()
    tags = input("Enter new tags for the lore entry (comma-separated, leave blank to keep current): ").strip()
    if category:
        lore_database[title]['category'] = category
    if description:
        lore_database[title]['description'] = description
    if tags:
        lore_database[title]['tags'] = [tag.strip().lower() for tag in tags.split(',')]
    print(f"Lore entry '{title}' updated successfully.")

def delete_lore_entry():
    title = input("\nEnter the title of the lore entry to delete: ").strip()
    if title in lore_database:
        del lore_database[title]
        print(f"Lore entry '{title}' deleted successfully.")
    else:
        print("This title does not exist. Please try again.")

def export_database():
    filename = input("\nEnter the filename to save the database (e.g., 'lore_database.json'): ").strip()
    with open(filename, 'w') as file:
        json.dump(lore_database, file, indent=4)
    print(f"Database exported to '{filename}'.")

def import_database():
    filename = input("\nEnter the filename to load the database from (e.g., 'lore_database.json'): ").strip()
    try:
        with open(filename, 'r') as file:
            global lore_database
            lore_database = json.load(file)
        print(f"Database imported from '{filename}'.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

def main():
    print("Welcome to the Dark Souls 1 Lore Database!")
    while True:
        print("\nMain Menu:")
        print("1. Search Lore")
        print("2. Browse by Category")
        print("3. Browse by Tag")
        print("4. Add Lore Entry")
        print("5. Edit Lore Entry")
        print("6. Delete Lore Entry")
        print("7. Export Database")
        print("8. Import Database")
        print("9. Help")
        print("10. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            keyword = input("Enter a keyword to search for: ").strip()
            category = input("Enter a category to filter by (or leave blank): ").strip()
            tag = input("Enter a tag to filter by (or leave blank): ").strip()
            results = search_lore(keyword, category if category else None, tag if tag else None)
            if results:
                print(f"\nFound {len(results)} result(s):")
                for title in results:
                    print(f"- {title}")
                selected_title = input("\nEnter the title of the lore entry you'd like to view: ").strip()
                if selected_title in results:
                    entry = results[selected_title]
                    print(f"\nTitle: {selected_title}")
                    print(f"Category: {entry['category']}")
                    print(f"Description: {entry['description']}")
                    print(f"Tags: {', '.join(entry['tags'])}")
                else:
                    print("Invalid selection. Please try again.")
            else:
                print("No results found. Please try again.")
        elif choice == "2":
            browse_entries("category")
        elif choice == "3":
            browse_entries("tag")
        elif choice == "4":
            add_lore_entry()
        elif choice == "5":
            edit_lore_entry()
        elif choice == "6":
            delete_lore_entry()
        elif choice == "7":
            export_database()
        elif choice == "8":
            import_database()
        elif choice == "9":
            display_help()
        elif choice == "10":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
