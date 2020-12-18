dim=int(input())
x=int(input())
velocidade=int(input())
loss=int(input())
speed=velocidade

while(velocidade>0):
    print(x)
    x=x+speed
    if(x>=dim):
        x=dim
        speed=speed-loss
        velocidade=speed
        speed=-speed
    elif(x<=-dim):
        x=-dim
        speed=speed+loss
        velocidade=-speed
        speed=-speed
if(velocidade<=0) :
    print(x)
    
    