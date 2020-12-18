# Movimento das traças

mothPosition = input()
lightPosition = input()

if(int(mothPosition) <= int(lightPosition)):
    print(int(mothPosition))
    mothVelocity = 0
    instances = 0
    while(int(mothPosition) < int(lightPosition)):
        while(instances < 2):
            mothPosition = int(mothPosition) + mothVelocity
            instances = instances + 1
            if(int(mothPosition) < int(lightPosition)):
                print(int(mothPosition))
        instances = 0
        mothVelocity = mothVelocity + 1
    print(int(lightPosition))
