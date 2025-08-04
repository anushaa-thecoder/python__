import random

# 1. Random Numbers
print("Returns a random float number between 0.0 (inclusive) and 1.0 (exclusive):", random.random())
print("Returns a random float between a and b. Can return both endpoints (Both are inclusive):", random.uniform(10, 20))
print("Returns a random integer N such that a <= N <= b:", random.randint(1, 10))
print("Returns a randomly selected element from range(start, stop, step):", random.randrange(1, 10, 2))
 
# 2. Random Choices
my_list = ['apple', 'banana', 'cherry', 'date']
print("Random choice from list:", random.choice(my_list))
print("Returns a list of k random elements from the sequence with replacement:", random.choices(my_list, k=2))
print("Returns a list of k unique random elements from the sequence:", random.sample(my_list, 2))

# 3. Shuffle List
print("Original list:", my_list)
random.shuffle(my_list)
print("Shuffled list:", my_list)


