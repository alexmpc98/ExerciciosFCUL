dim = input()
while(int(dim) <= 0):
    print("Value must be greater than 0")
    dim = input()

shockCarInitialPosition = input()
while(int(shockCarInitialPosition) <= int(dim)*-1 or int(shockCarInitialPosition) >= int(dim)):
    print("Position should be greater or smaller than dimension")
    shockCarInitialPosition = input()

initialVelocity = input()
while(int(initialVelocity) <= 0):
    print("Initial velocity must be greater than 0")
    initialVelocity = input()

speedReduction = input()
while(int(speedReduction) <= 0):
    print("Speed Reduction must be greater than 0")
    speedReduction = input()



while(int(initialVelocity) >= 0):
    while(int(shockCarInitialPosition) < int(dim)):
        print(int(shockCarInitialPosition))
        shockCarInitialPosition = int(shockCarInitialPosition) + int(initialVelocity)
    shockCarInitialPosition = int(dim)
    initialVelocity = int(initialVelocity) - int(speedReduction)
    while(int(shockCarInitialPosition) > int(dim)*-1):
        print(int(shockCarInitialPosition))
        shockCarInitialPosition = int(shockCarInitialPosition) - int(initialVelocity)
    shockCarInitialPosition = int(dim)*-1
    initialVelocity = int(initialVelocity) - int(speedReduction)
    print("Here -------")
    print(int(initialVelocity))
    print("-------------")






