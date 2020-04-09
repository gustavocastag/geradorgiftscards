from random import choice, randint
from time import sleep

ranbanner = randint(1,3)

count = 0

if ranbanner == 1 :

    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print ('-'*50)
    print ('       GIFT CARDS GENERATOR FOR GOOGLE PLAY ')
    print (' ')
    print ('                     ________ ')
    print ('                    | \033[33m |\ \033[m   |')
    print ('                    | \033[36m | \ \033[m  |')
    print ('                    | \033[36m |  \ \033[m |')
    print ('                    | \033[32m |  /  \033[m|')
    print ('                    | \033[32m | /  \033[m |')
    print ('                    | \033[31m |/  \033[m  |')
    print ('                    |————————|')
    print ('                    |  GIFT  |')
    print ('                    |________|')
    print (' ')
    print ('-'*50)
    
if ranbanner == 2 :
    
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print ('-'*50)
    print ('       GIFT CARDS GENERATOR FOR GOOGLE PLAY ')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print ('                  :) INTERFACE (:')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print ('-'*50)

if ranbanner == 3 :
    
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print ('-'*50)
    print ('       GIFT CARDS GENERATOR FOR GOOGLE PLAY ')
    print (' ')
    print ('   \033[34m      _       _ \033[m  \033[31m  ______  \033[m     ___   ')
    print ('   \033[34m     | |     | |\033[m  \033[31m /  ____| \033[m    / _ \  ')
    print ('   \033[34m     | |     | |\033[m  \033[31m|  |____  \033[m   / / \ \ ')
    print ('   \033[34m     | |     | |\033[m  \033[31m \____  \ \033[m  |  |_|  | ')
    print ('   \033[34m     \ \     / /\033[m  \033[31m  ____|  |\033[m  | _____ |  ')
    print ('   \033[34m      \ \___/ / \033[m  \033[31m |______/ \033[m  | |   | |  ')
    print ('   \033[34m       \_____/  \033[m              |_|   |_|  ')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print ('-'*50)

sleep(2)

print (' ')

num = int(input('First: How many random GOOGLE PLAY codes you want \nto generate: '))

sleep(1)

print (' ')

name = input('Second: Name or location of the file to be \ngenerated: ')

archive = open(name, 'w')

print (' ')

while count != num :

    a = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    b = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    c = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    d = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    e = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    f = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    g = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    h = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    i = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    j = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    k = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    l = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    m = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    n = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    o = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    p = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    q = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    u = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    v = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    w = choice('ABCDEFGHIJKLMNOSTPQUVWXYZ123456789')
    
    x = (' '+a+b+c+d+'-'+e+f+g+h+'-'+i+j+k+l+'-'+m+n+o+p+'-'+q+u+v+w+'\n')
    
    archive.write(x)
    
    count += 1
    
    print (count)

archive.close

print (' ')  
print ('Done!')
print (' ')
print ('Good Luck.')
