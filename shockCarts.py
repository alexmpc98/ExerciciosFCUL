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

