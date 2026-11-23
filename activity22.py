#2d dimnesional list 
#Naruto = ['Frog Kumite', 'Sage of 6 Path', 'Rasenshuriken']
#Sasuke = ['Chidori', 'Amentojakara', 'Fire Release']
#Sakura = ['Healing Ability', 'Cherry Blossom Impact', '']
#Naruto_shippuden = [Naruto, Sasuke, Sakura]
#luma = ["Dragon_ball", "One Piece", Naruto_shippuden, "Bleach"]
#bago = ["Blue Lock", "Jujutsu Kaisen", "Demon Slayer"]
#korean = ["Solo leveling"]

#anime = {"Old School: ":luma, "New:":bago, "manhwa:":korean}

#print(anime["Old School: "])
#print(anime["Old School: "][0][-1])


# characters = Heroes
# anime title = Role/lane
# Release date = map Path
# anime = MLbb

#Heroes I use in MLBB

#level 4 === Heroes Lore and Title ===

Aamon = ["After the late Duke Paxley was presumed dead, Aamon was not only left with the responsibilities of the entire family, but also his young brothers and sisters.", "Head of House Paxley; Duke of Shards"]
Gus = ["Born into the prestigious House Paxley, Gusion was expected to follow his family's traditions of magic. However, he rejected their rigid expectations and chose to combine light magic with swordsmanship. His rebellious nature often put him at odds with his family, particularly his older brother Aamon.", "Holy Blade"]
Alu = ["After losing his father during a disastrous battle against demons, Alucard devoted himself to demon hunting. He trained at the Monastery of Light and became an Arbiter of Light. However, after discovering the truth surrounding his father's disappearance and the Church's treatment of him, he abandoned the institution and continued hunting demons independently.", "Demon Hunter"]

Dyr = ["Born as the young prince of the Moniyan Empire, Dyrroth was kidnapped by the forces of the Abyss as an infant. Raised by Alice and the Abyss, he eventually became the Prince of the Abyss and one of its most formidable warriors, standing against the empire he was originally born to inherit.", "Prince of the Abyss"]
Yz = ["Once the Black Dragon's reincarnation, Yu Zhong sought to reclaim the power of the Black Dragon and restore his position in Cadia Riverlands. Through his ambition, manipulation, and pursuit of the Dragon Altar's power, he became a formidable force determined to reshape the region.","Black Dragon"]
Zil = ["Born in the Cadia Riverlands, Zilong was chosen by the Great Dragon and raised in the Dragon Altar. He received the mission of traveling across the Land of Dawn to restore balance and protect those in need, becoming one of the Great Dragon's most trusted warriors.", "Spear of Dragon"]

Tig = ["A distinguished knight of the Moniyan Empire, Tigreal rose through the ranks of the Light's Order through courage and dedication. Despite suffering a devastating defeat during an expedition to the Northern Vale, he returned to the empire and continued serving as one of its greatest military commanders.", "Warrior of Dawn"]
Flor = ["Floryn was brought into existence through Belerick's efforts to create the Oasis in the Agelta Drylands. After discovering the suffering caused by the desert's harsh environment, she left her home with Dew, a magical creature born from the seed containing Belerick's power. Together, they travel to restore greenery and bring hope to the desert.", "Budding Hope"]
Rafa = ["An angel of the Monastery of Light, Rafaela was born with the power to heal and bring peace. She dedicates herself to helping the wounded and protecting humanity from evil. She is also the twin sister of Argus, whose fall from grace placed them on opposing sides.", "Wings of Holiness"]


Claude = ["Growing up in such a place as an orphan, Claude learned to survive through stealing and deception. He eventually became a notorious thief, accompanied by his partner Dexter. His reputation grew through daring heists and his rivalry with the authorities, particularly Bruno.", "Partners in crime"]
Lesley = ["Lesley was raised in the Vance family after her father, who served the family, was killed. She eventually became the family's guardian and assassin, protecting Harley, the young heir of the Vance household. Despite her cold and professional nature, she cares deeply for her adopted family.", "Deadly Sniper"]
Granger = ["Granger's childhood was destroyed when demons attacked his hometown and killed his parents. The trauma left him haunted by the sounds of their final moments. After finding temporary comfort through music at the Monastery of Light, he became a demon hunter. Following the death of the priest who helped him, Granger embraced his role as a hunter and turned every battle into a requiem for those he lost.", "Death Chanter"]

Xav = ["Born into a family that served the Monastery of Light, Xavier was expected to become a devoted follower of the Church. However, he grew disillusioned with its rigid doctrines and eventually joined the Forsaken Light. He became a powerful wielder of light magic, fighting for his own understanding of justice and freedom.", "Defier of Light"]
Valen = ["The one who outlived her death: A Former Duchess of House Paxley in the Moniyan Empire who turned to dark magic to revive her fallen husband, Irlan, after being betrayed during a battle against the Abyss.", "Prophetess of the Night"]
Luo_Yi = ["A practitioner of Yin-Yang magic from Cadia Riverlands, Luo Yi was once involved in the conflict surrounding the Great Dragon and the Black Dragon. She became Yu Zhong's devoted follower after recognizing his identity as the Black Dragon's reincarnation, helping him pursue his ambitions.", "Yin-Yang Geomancer"]

Julian = ["Julian was raised by the Church of Light after being abandoned as a child. He was trained as one of its Scarlet Shadows, carrying out missions alongside Xavier and Melissa. However, after discovering the truth about his past and the Church's secrets, he turned against the institution that had raised him.", "Scarlet Raven"]
Guin = ["Born into the prestigious Baroque family, Guinevere displayed exceptional talent for magic from a young age. Her family intended to arrange her marriage to strengthen their political influence, but Guinevere refused to let others dictate her future. She pursued her own path and developed a close friendship with Lancelot and other companions.", "Ms. Violet"]
Saber = ["Originally a human from the technologically advanced city of Eruditio, Saber was kidnapped and subjected to experiments that transformed him into a powerful cyborg swordsman. After escaping the organization responsible for his transformation, he wandered the Land of Dawn, seeking freedom and answers about his past.", "Wandering Sword"]

#level 3 === Lanes or roles I use them ===
Jungler = {"Aamon" : Aamon, "Alucard" : Alu, "Gusion" : Gus}
Exp = {"Dyrroth" : Dyr, "Yu Zhong" : Yz, "Zilong" : Zil}
Roam = {"Tigreal" : Tig, "Rafaela" : Rafa, "Floryn" : Flor}
Mid = {"Xavier" : Xav, "Valentina" : Valen, "Luo Yi" : Luo_Yi}
Gold = {"Lesley" : Lesley, "Claude" : Claude, "Granger" : Granger}
Flex = {"Julian" : Julian, "Guinevere" : Guin, "Saber" : Saber}

#level 2 === One lane only vs Rotating the whole map ===
one_lane = {"Exp Lane" : Exp, "Mid Lane" : Mid, "Gold Lane" : Gold}
Rot = {"Jungle" : Jungler, "Roamer" : Roam, "Role fill" : Flex}



print("HEROES THAT I MAIN IN PARTICULAR ROLES ON MOBILE LEGENDS BANG BANG")


#level 1 main dictionary
MLbb = {"Heroes I use with fixed lane": one_lane, "Heroes I use rotating the whole map": Rot}

print()
print("=== 1. Going down one level at a time ===")
print(MLbb["Heroes I use rotating the whole map"]["Jungle"]["Aamon"][1])

print()
print("=== 2. Loop level 1: Categories ===")
for category in MLbb:
    print(category)

print()
print("=== 3. Loop levels 1-2: roles and lanes ===")
for category, lanes in MLbb.items():
    print(category)
    for lane in lanes:
        print("  -", lane)

print()
print("=== 4. Loop all levels ===")
for category, lane in MLbb.items():
    print(category)
    for lane, heroes in lanes.items():
        print("  " + lane)
        for name, info in heroes.items():
            print()
            print("    " + name)
            print("      Lore:", info[0])
            print("      Title:", info[1])
            print()

print()
print("=== 5. Count every hero ===")
count = 0
for lanes in MLbb.values():
    for heroes in lanes.values():
        for name in heroes:
            count = count + 1
print("Total heroes:", count)

print()
print("=== 6. Search for a hero ===")
search = "Aamon"
found = False
for category, lanes in MLbb.items():
    for lane, heroes in lanes.items():
        if search in heroes:
            print(search, "is under", lane, "(" + category + ")")
            print("Title:", heroes[search][1])
            found = True
if found == False:
    print(search, "not found.")


print()
print()
