name = str(input("What is your name?"))
print("Nice to meet you, "+name+"! I counted many demons:")
enemies=0
for i in range(10):
    print(i+1)
    enemies=i+1
killed=0
fight="RAGES ON"
while fight!="DONE":
    killed=killed+1
    print("Killed: "+str(killed))
    fight=str(input("IS IT DONE?"))
    print ("RIP 'N' TEAR UNTIL IT'S DONE!!!")
if killed<enemies:
    print("You haven't killed them all!")
elif killed==enemies:
    print("You have killed them all!")
else:
    print("You have found spectres! Congratulations!")
print("Your fight is Eternal!")

