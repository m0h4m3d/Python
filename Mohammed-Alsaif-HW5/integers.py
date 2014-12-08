import random

print("INTEGER DIVISIONS")
while True:
    data = []
    for i in range(0,2):
        a = random.randrange(10)
        data.append(a)
    if(data[1] != 0):
        val = int(data[0]/data[1])
        try:
            userVal = int(input(str(data[0])+"/"+str(data[1])+"="))
            if(val == userVal):
                print("CORRECT!")
            else:
                print("INCORRECT!")
        except:
            print("Please enter Integers Only!")
    
