import random

#function of random key
def randomize(z):
    global init_key, key
    init_key = ''
    key = [str(x) for x in range(1, z + 1)]
    random.shuffle(key) #permutation
    for _ in range(z): init_key += str(random.randint(0, 1)) #iv