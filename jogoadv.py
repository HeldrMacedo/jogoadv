from random import randint
print("bem vindo")
secreto = randint(1, 10)
num = 0

while num != secreto:
    num = int(input("Digite um numero "))     
    if num == secreto:
        print("you win ")
    elif num > secreto:
        print("Too High ")
    else:
        print("too low ")

print("Game over ")
