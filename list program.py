names = ["muthu", "celin", "stephen", "rajarajan"]

names1 = []

while names:
    smallest = min(names)
    names1.append(smallest)
    names.pop(names.index(smallest))
print(names1)
