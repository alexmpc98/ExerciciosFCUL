# Numeros primos

num = input();
primeCounter = 0;

while(int(num) != 0):
    auxNum = int(num);
    prime = True;
    if(int(num) == 1):
        prime = False;
    while(auxNum > 1):
        auxAux = auxNum - 1;
        if(int(num) % auxAux == 0 and auxAux > 1):
            prime = False;
        auxNum = auxNum - 1;
    if(prime == True):
        primeCounter = primeCounter + 1;
        print(num + " é primo");
        num = input();
    else:
        print(num + " não é primo");
        num = 0;
        print("Introduziu " + str(primeCounter) + " primos");