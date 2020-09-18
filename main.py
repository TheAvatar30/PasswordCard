import random as rnd

def main():
    #generateWithSeed(60, 20, "")
    generate(60, 20)
    #printCard()

def generate(x: int, y: int):
    file = open("PCard.txt", "w")
    file.write("    ")
    for i in range(x):
        if((i%10) == 9):
            file.write(f"{int(i/10)+1} ")
        else:
            file.write("  ")
    file.write("\n    ")
    for i in range(x):
        file.write(f"{(i+1)%10} ")
    file.write("\n\n")

    for j in range(y):
        s = ""
        for i in range(x):
            tmp = rnd.randint(33, 126)
            c = chr(tmp)
            s += c + " "
        file.write(f"{(j+1)%10}   "+s + "\n")

def generateWithSeed(x: int, y: int, seed: str):
    rnd.seed(seed, 2)
    file = open("PCard.txt", "w")
    file.write("    ")
    for i in range(x):
        file.write(f"{(i+1)%10} ")
    file.write("\n\n")

    for j in range(y):
        s = ""
        for i in range(x):
            tmp = rnd.randint(33, 126)
            c = chr(tmp)
            s += c + " "
        file.write(f"{(j+1)%10}   "+s + "\n")

def printCard():
    file = open("PCard.txt")
    content = file.read()
    file.close()


    print(content+f"\n\nThe File's Size is {len(content)} Bytes")

if __name__ == '__main__':
    main()
