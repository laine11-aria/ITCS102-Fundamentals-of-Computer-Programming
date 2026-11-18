#2d dimnesional list 
Naruto = ['Frog Kumite', 'Sage of 6 Path', 'Rasenshuriken']
Sasuke = ['Chidori', 'Amentojakara', 'Fire Release']
Sakura = ['Healing Ability', 'Cherry Blossom Impact', '']
Naruto_shippuden = [Naruto, Sasuke, Sakura]
luma = ["Dragon_ball", "One Piece", Naruto_shippuden, "Bleach"]
bago = ["Blue Lock", "Jujutsu Kaisen", "Demon Slayer"]
korean = ["Solo leveling"]

anime = {"Old School: ":luma, "New:":bago, "manhwa:":korean}

print(anime["Old School: "])
print(anime["Old School: "][0][-1])