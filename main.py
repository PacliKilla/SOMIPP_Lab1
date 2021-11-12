
x = input("Chose one: cowntdown, linecount, txtindir: ")

if x == "cowntdown":
    exec(open('cowntdown.py').read())
elif x == "linecount":
    exec(open('linecount.py').read())
elif x == "txtindir":
    exec(open('txtindir.py').read())

else: print("Something went wrong")
