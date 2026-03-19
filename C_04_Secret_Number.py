import random

low_num = 1
high_num = 3

# Generate a secret number between high and low
for item in range(0, 30):
    secret = random.randint(low_num,high_num)
    print(secret, end="\t")