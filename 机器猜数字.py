from random import randint
answer =randint(0,10000)
guess_number=None
guess_count=1
while guess_number != answer:
    guess_number =randint(0,10000) 
    guess_count+=1
    print(f"第{guess_count}次猜测，猜测数字是；{guess_number}")