# list
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
