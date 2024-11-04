import random
randomizer_num = [1,6,8,3,5,4,3123,2,5,67,4,3,2,4,6,8,123,67,4,59,98]
randomizer_word = ["a","b", "casdwd", "oihfehou", "dki"]
word = random.choice(randomizer_word)
num = random.choice(randomizer_num)
password = print(f"Password is: {word}{num}")