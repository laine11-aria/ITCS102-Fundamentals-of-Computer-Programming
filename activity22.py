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

#level 4 === Heroes Description or title ===

Aamon = ["After the late Duke Paxley was presumed dead, Aamon was not only left with the responsibilities of the entire family, but also his young brothers and sisters", "Head of House Paxley; Duke of Shards"]
Gus = ["House Paxley Cursed Child", "Holy Blade"]
Alu = ["Demon Hunter", "Lightborn: Striker"]

Dyr = ["Born as a prince of the Moniyan Empire", "Prince of the Abyss"]
Yz = ["Black Dragon", "Great Dragon's Successor"]
Zil = ["Great Dragon's Spear", "Faithful Warrior of Cadia"]

Tig = ["Warrior of Dawn", "Exalted Knight of Moniyan"]
Flor = ["Nature's Spirit", "Guardian of the Enchanted Forest"]
Rafa = ["Wings of Holiness", "Angel of Light"]

Claude = ["Growing up in such a place as an orphan, Claude soon learned how to fight, lie, gamble and steal: tricks of the trade he had to rely upon to survive", "Has a monkey as his parter in crime called Dexter"]
Lesley = ["Deadly Sniper", "Adopted Daughter of Vance Family"]
Granger = ["Death Chanter: plays poor violin music, use to distract enemies off guard before shooting them", "Demon Hunter of the Monastery"]

Nana = ["Sweet Leonin", "Feline Sorceress of the Forest"]
Valen = ["Prophetess of the Night", "The Former Duchess of House Paxley, the one who outlived her death"]
Luo_Yi = ["Yin-Yang Geomancer", "Master of Yin-Yang"]

Julian = ["Scarlet Raven", "Warrior of the Church"]
Guin = ["Ms. Violet", "Daughter of House Baroque"]
Saber = ["Wandering Sword", "Creation of Project S.A.B.E.R."]

#level 3 === Lanes or roles I use them ===
Jungler = {"Aamon" : Aamon, "Alucard" : Alu, "Gusion" : Gus}
Exp = {"Dyrroth" : Dyr, "Yu Zhong" : Yz, "Zilong" : Zil}
Roam = {"Tigreal" : Tig, "Rafaela" : Rafa, "Floryn" : Flor}
Mid = {"Nana" : Nana, "Valentina" : Valen, "Luo Yi" : Luo_Yi}
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
print("=== 3. Loop levels 1-2: Categories and lanes ===")
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
            print("    " + name)
         
