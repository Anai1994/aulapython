import hashlib

def initial():
    r=input ("qual a senha?")
    l=input ("digite a frase?")
    return r + "#" + l

def crypto(senha):
    x=hashlib.sha512(senha.encode('utf-8')).hexdigest()
    return x

def criptoinvert(senha):
    senha_invertida = senha[::-1]
    return senha_invertida
        

if __name__ == "__main__":
    while True:
        senha=initial()
        print(crypto(senha))
        print(criptoinvert(senha))

