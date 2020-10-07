# list
print("======List======")
squares = [1, 4, 9, 16, 25]
print(squares[0])  # first element of list
print(squares[-1])  # first element of list reverse order
print(squares[-5])  # going through revers
print(squares + [36, 49, 64, 81, 100])  # concatenation
print(squares[3:])  #
print(squares[-3:])  #

cubes = [1, 8, 27, 65, 125]
print(4 ** 3)
cubes[3] = 64
print(cubes)
cubes.append(216)
print(cubes)
cubes.append(7 ** 3)
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']  # get slice(subset) from 2 to 4
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []  # clear the list by replacing all the elements with an empty list
print(letters)
print("======Data Structures======")
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting a position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()  # pull out the last element from the list
print(fruits)
print("======= Using Lists as Stacks ========")
stack = [3, 4, 5]
stack.append(6)  # Add item at top of stack
stack.append(7)  # Add item at top of stack
print(stack)
stack.pop()  # pull out the element from the top of stack
stack.pop()  # pull out the element from the top of stack
print(stack)
print("======= Using Lists as Queues ========")
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
squares2 = []
for x in range(10):
    squares2.append(x ** 2)
print(squares2)

