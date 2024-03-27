def crianca (x):
    if x < 12:
        return True
    else:
        return False 

def pre (x):
    if x > 11 and x < 16: 
        return True

    else:
        return False
def jovem (x):
    if x >15 and x < 25:
        return True
    else:
        return False
def adulto (x):
    if x > 24 and x <36:
        return True
    else:
        return False
def quase(x):
    if x > 35 and x < 66:
        return True
    else:
        return False
def idoso(x):
    if x > 65 and x <200: 
        return True
    else:
        return False        

a=int (input("qual a sua idade?"))

print("========")

if crianca (a) == True:
    print("você é uma criança")
else:
    if pre (a)== True:
        print("você é quase um adolescente")
    else: 
        if jovem (a)== True:
            print("você é um jovem") 
        else:
            if adulto (a)==True:
              print("você é um jovem adulto")
            else:
                if quase (a)== True:
                    print("você é um adulto")
                else:
                    if idoso (a)==True:
                        print("você é um idoso")
                    else: 
                      if adulto (a)== False:
                        print( "parabéns está no paraíso")
                    
        
                 
