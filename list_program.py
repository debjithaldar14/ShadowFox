
# 3. LIST

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

print("Number of members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

justice_league.remove("Superman")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("After separating Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)

justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New Leader (0th index):", justice_league[0])
