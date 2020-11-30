from random import randint
def generate(amount):
    for n in range(amount):
        a = randint(0,255)
        b = randint(0,255)
        c = randint(0,255)
        d = randint(0,255)
        f = open('ips.txt', 'a', encoding='utf-8')
        f.write(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+'\n')
        f.close()
    print('Success!')

def generation(amount):
    for n in range(amount):
        a = 77
        b = 221
        c = 153
        d = n
        f = open('ips.txt', 'a', encoding='utf-8')
        f.write(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+'\n')
        f.close()
    print('Success!')

