young = {'speed1' : 1,'vision1' : 80,'distance1' : 600, 'time1' : 600}
print (young[])
old = {'speed2' : 1, 'vision2' : 40,'distance' : 600, 'time1' : 600}
print (old[])

jfrom random import randint
secret_num = randint(0, 300)
user_num = -1
try_count = 1
while secret_num != user_num:
    print("%d try: " % try_count, end='')
    user_num = int(input())
    if user_num < secret_num:
        print("Too less")
    elif user_num > secret_num:
        print("Too much")
    else:
        print("You guessed it!")
    try_count += 1
