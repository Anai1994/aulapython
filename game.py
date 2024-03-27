import random
import os
import sys

def menu ():
    print ("0-sair")
    print ("1-megasena")
    print ("2-lotofacil")
    print ("3-gerar senha")
    r=int(input ("qual o jogo?"))
    return r

def megasena (): 
    os.system("cls")
    print ("megasena")
    r=int(input("quantos jogos?")) 
    for j in range (r):
        numeros=""
        for n in range(6):
            x=random.randrange (1,60+1)
            numeros=numeros +str(x)+ " "
        print(f"jogo {j+1}: {numeros} ")
    p=input("ENTER para novo jogo")
    os.system("cls")

def lotofacil (): 
    os.system("cls")
    print ("lotofacil")
    r=int(input("quantos jogos?")) 
    for j in range (r):
        numeros=""
        for n in range(15):
            x=random.randrange (1,25+1)
            numeros=numeros +str(x)+ " "
        print(f"jogo {j+1}: {numeros} ")
    p=input("ENTER para novo jogo")
    os.system("cls")

def gerarsenha(): 
    os.system("cls")
    print ("senha")
    
    numeros=""
    for n in range(6):
        x=random.randrange (1,10)
        numeros=numeros +str(x)
    print(f"  {numeros}")
    p=input("ENTER para nova senha")
    os.system("cls")


    while True:
        r=menu()
        if r ==0:
            sys.exit()
        if r==1:
            megasena()
        if r==2:
            lotofacil()
        if r==3:
            gerarsenha()