# genorate a number 1-10

from random import randint
answer = randint(1,10)

answer = randint(int(sys.argv[1]), sys.argv[2])


# input from user

# check that the input is a number 1-10

while true:
    try:
        print(answer)
        guess = int(input('guess a number 1-10'))

    if 0 < int (guess) <11:
        if (guess) == answer:
            print('you are a genius!')
            break
   print('all good')
   break
   else:
print ( 'hey , use 1-10')
except valueError:
print('please enter a number')
continue
# check that number is right guess. otherwise
# ask again



