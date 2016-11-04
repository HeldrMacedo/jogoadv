print("bem vindo")
num = 0

while num != 5:
    num = int(input("Digite um numero"))     
    if num == 5:
        print("you win ")
    elif num > 5:
        print("Too High ")
    else:
        print("too low ")

print("Game over ")
