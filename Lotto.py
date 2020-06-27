import random

chosen = []
randoms = []
a=-1
play = "y"
while play=="y":
    for i in range(6):
        a=int(input("Choose number "+str(i+1)+" : "))
        while a in chosen:
            print("You have already chosen this number. Choose another.")
            a=int(input("Choose "+str(i+1)+" number: "))
        chosen.append(a)
        a=random.randint(1,40)
        while a in randoms:
            a=random.randint(1,40)
        randoms.append(a)
    ok = 0
    for j in chosen:
        for k in randoms:
            if j==k:
                ok=ok+1
    print("Matching numbers: "+str(ok))
    print("Randoms: ")
    for i in randoms:
        print(i)
    chosen.clear()
    randoms.clear()
    play = input("Would you like to play again? (y if yes)")
