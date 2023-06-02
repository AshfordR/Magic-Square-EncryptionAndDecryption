import numpy as np  # For working with matrices
import random
import os  # To greet the user
from tabulate import tabulate


def is_magic_square(square):
    # Check if all rows, columns, and diagonals have the same sum
    target_sum = sum(square[0])
    
    # Check rows
    for row in square:
        if sum(row) != target_sum:
            return False
    
    # Check columns
    for col in range(3):
        column_sum = 0  # Initialize the sum of the current column
        for row in range(3):
            column_sum += square[row][col]  # Add the element at the current row and column to the sum
        if column_sum != target_sum:
            return False

    
    # Check diagonals
    if square[0][0] + square[1][1] + square[2][2] != target_sum:
        return False
    if square[0][2] + square[1][1] + square[2][0] != target_sum:
        return False
    
    return True

def generate_magic_squares():
    # List to store all magic squares
    magic_squares = []
    
    # Generate all possible permutations of numbers from 1 to 9
    numbers = list(range(1, 10))
    permutations = []
    for a in numbers:
        for b in numbers:
            if b != a:
                for c in numbers:
                    if c not in [a, b]:
                        for d in numbers:
                            if d not in [a, b, c]:
                                for e in numbers:
                                    if e not in [a, b, c, d]:
                                        for f in numbers:
                                            if f not in [a, b, c, d, e]:
                                                for g in numbers:
                                                    if g not in [a, b, c, d, e, f]:
                                                        for h in numbers:
                                                            if h not in [a, b, c, d, e, f, g]:
                                                                for i in numbers:
                                                                    if i not in [a, b, c, d, e, f, g, h]:
                                                                        permutation = [a, b, c, d, e, f, g, h, i]
                                                                        permutations.append(permutation)
      
    # print(permutation)
    # Check each permutation if it forms a magic square
    for perm in permutations:
        square = [[perm[0], perm[1], perm[2]],
                  [perm[3], perm[4], perm[5]],
                  [perm[6], perm[7], perm[8]]]
        
        if is_magic_square(square):
            magic_squares.append(square)
            
    print("All possible 3x3 Magic squares:")  # Display a magic square on the screen
    for choice in magic_squares:
        print(tabulate(choice, tablefmt="fancy_grid"))
            
    result = random.choice(magic_squares)   
    return result


def find_in_matrix(value, input_matrix):
    """ The function of searching in which row and column the element is located in the matrix """
    size = len(input_matrix)
    for i in range(size):
        for j in range(size):
            if input_matrix[i][j] == value:
                return [i, j]

    return [-1, -1]


def string_to_magic_square(string, magic_square):
    n = len(magic_square)
    string = string + " " * (n * n - len(string))
    res = [[" " for x in range(n)] for y in range(n)]
    for i in range(len(string)):
        i_pos, j_pos = find_in_matrix(i + 1, magic_square)
        res[i_pos][j_pos] = string[i]
    return res


def magic_square_to_string(crypt_square, magic_square):
    string = ""
    for i in range(len(crypt_square)**2):
        i_pos, j_pos = find_in_matrix(i + 1, crypt_square)
        string += magic_square[i_pos][j_pos]
    return string


print("Hello, " + os.environ.get("USERNAME") + "!\nThis code is to encrypt and decrypt string using 3x3 Magic Square\n\nEnter your string:")
input_string = str(input())
print("\nLength of text: " + str(len(input_string)) + " symbols\n")

size_of_matrix = int(np.ceil(np.sqrt(len(input_string))))  # Calculation of the size of the magic 

if(size_of_matrix > 3):
    print("Message is too long to encrypt")
else:
    magic = generate_magic_squares()  # Generation of the magic square obtained above dimensionally
    print("\nSelected Magic Square:")
    print(tabulate(magic, tablefmt="fancy_grid"))
    matrix = string_to_magic_square(input_string, magic)  # Encrypting strings
    print("\nEncrypted string in matrix:\n", matrix)  # Output of an encrypted string, which now has the form of a two-dimensional
    print(tabulate(matrix, tablefmt="fancy_grid"))
    string = magic_square_to_string(magic, matrix)  # Inverse conversion to string
    print("\nDecrypted string:\n", string)  # Output of the original strings