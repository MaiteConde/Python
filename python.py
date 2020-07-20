a = int(input("Write a number a"))
b = int(input("Write a number b"))
if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")
L = []
for i in range(10):
    print(i+1)
    L.append(i**2)
print(L)

S = {"apple", 3.5, "cherry"}
for x in S:
    print(x)
else:
    print("loop ended")
print ("out of the loop")

def printOk():
    print("Done")
    print("Nice!")
printOk()

def checkIfNoNumeric(*args):
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True
def addAllNumerics(*args):
    s = 0
    for x in args:
        s+=x
    return s


