# An example of a variable
myvar = "This variable is a string"
numvar = 10 # This is an example number variable

newList = []
spltlst = myvar.split()
for ea in myvar:
    newea = ea.upper()
    newList.append(newea)

anotherList = []
for i in spltlst:
    newi = i.capitalize()
    anotherList.append(newi)

print("".join(newList))
print(" ".join(anotherList))