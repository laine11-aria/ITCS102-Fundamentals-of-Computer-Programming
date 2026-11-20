# ==============================================================================
# CLUE: HOW TO ADD A NEW ENTRY TO A DICTIONARY
# Pattern:  dictionary[new_key] = new_value
# If the key is new, Python ADDS it. If the key already exists,
# Python REPLACES its value. Remove the # to try each one.
# Add your entries HERE, before the loops, so the loops print them.
# ==============================================================================

# --- Add a new CHARACTER to an anime (level 3) ---
# Step 1: make the character list [description, power]
# sanji = ["Cook of the Straw Hat crew", "Black Leg Style"]
# Step 2: add it to the anime's dictionary
# one_piece["Sanji"] = sanji
# Same thing in one line, going through the main dictionary:
# anime["Old Anime"]["One Piece"]["Sanji"] = ["Cook of the Straw Hat crew", "Black Leg Style"]

# --- Add a new ANIME to a genre (level 2) ---
# jjk = {"Gojo": ["Strongest jujutsu sorcerer", "Limitless"]}
# shonen["Jujutsu Kaisen"] = jjk

# --- Add a new GENRE / CATEGORY (level 1) ---
# haikyuu = {"Hinata": ["Short but high-jumping spiker", "Quick attack"]}
# sports = {"Haikyuu!!": haikyuu}
# anime["Sports Anime"] = sports

# --- Change (update) a value that already exists --
# anime["Old Anime"]["One Piece"]["Luffy"][1] = "Gear Fifth"

# ===== LEVEL 4: each character is a list [description, power] =====

luffy = ["Captain of the Straw Hat Pirates", "Gum-Gum Fruit (rubber body)"]
zoro = ["Swordsman of the Straw Hat crew", "Three-Sword Style"]
nami = ["Navigator of the Straw Hat crew", "Clima-Tact (weather control)"]

naruto = ["Ninja who dreams of becoming Hokage", "Shadow Clone Jutsu"]
sasuke = ["Last of the Uchiha clan", "Sharingan"]
sakura = ["Medical ninja of Team 7", "Super strength"]

ichigo = ["Substitute Soul Reaper", "Bankai: Tensa Zangetsu"]
rukia = ["Soul Reaper of the 13th Division", "Sode no Shirayuki (ice)"]

subaru = ["Boy summoned to another world", "Return by Death"]
emilia = ["Half-elf candidate for the throne", "Ice magic"]
rem = ["Oni maid of the Roswaal mansion", "Oni power"]

rimuru = ["Reincarnated as a slime", "Predator and Great Sage"]
benimaru = ["Leader of the ogres", "Black flames"]

# ===== LEVEL 3: each anime is a dictionary of characters =====
one_piece = {"Luffy": luffy, "Zoro": zoro, "Nami": nami}
naruto_series = {"Naruto": naruto, "Sasuke": sasuke, "Sakura": sakura}
bleach = {"Ichigo": ichigo, "Rukia": rukia}
re_zero = {"Subaru": subaru, "Emilia": emilia, "Rem": rem}
slime = {"Rimuru": rimuru, "Benimaru": benimaru}

# ===== LEVEL 2: each genre is a dictionary of anime =====
shonen = {"One Piece": one_piece, "Naruto": naruto_series, "Bleach": bleach}
isekai = {"Re:Zero": re_zero, "That Time I Got Reincarnated as a Slime": slime}

# ===== LEVEL 1: the main dictionary =====
anime = {"Old Anime": shonen, "New Anime": isekai}

print("=== 1. Going down one level at a time ===")
print(anime["Old Anime"]["One Piece"]["Luffy"][1])

print()
print("=== 2. Loop level 1: categories ===")
for category in anime:
    print(category)

print()
print("=== 3. Loop levels 1-2: categories and titles ===")
for category, titles in anime.items():
    print(category)
    for title in titles:
        print("  -", title)

print()
print("=== 4. Loop ALL levels ===")
for category, titles in anime.items():
    print(category)
    for title, characters in titles.items():
        print("  " + title)
        for name, info in characters.items():
            print("    " + name)
            print("      Description:", info[0])
            print("      Power:", info[1])

print()
print("=== 5. Count every character ===")
count = 0
for titles in anime.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1
print("Total characters:", count)

print()
print("=== 6. Search for a character ===")
search = "Rem"
found = False
for category, titles in anime.items():
    for title, characters in titles.items():
        if search in characters:
            print(search, "is from", title, "(" + category + ")")
            print("Power:", characters[search][1])
            found = True
if found == False:
    print(search, "not found.")