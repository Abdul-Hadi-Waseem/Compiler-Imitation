import keyword
print("{")
for num,i in enumerate(keyword.kwlist):
    print(f"\"{i}\":{num},")
print("}")
