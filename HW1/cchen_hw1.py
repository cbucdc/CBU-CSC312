with open("TitanicNames.txt") as f:
    names = f.read().strip().split("\n")
print("Count:", len(names))
print("Longest:", max(names, key=len))
print("Jones?", any(map(lambda s: "Jones" in s, names)))
