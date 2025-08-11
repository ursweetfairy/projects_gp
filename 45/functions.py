import math

def add(a,b):
    return a + b

def if_palindrom(word):
    return word == word[::-1]

def if_valid_triangle(a,b,c):
    return max(a,b,c) < a + b + c - max(a,b,c) if min(a,b,c) > 0 else False

def divide(a,b):
    try:
        print(a/b)
    except:
        print("Nie dziel przez 0")

def sort_strings_by_length(list_of_strings):
    list_of_strings.sort(key=len) 
    return list_of_strings  

def if_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False 
    return True  

def calculate_mean(list_of_int):
    try:
        return -1 if not len(list_of_int) else sum(list_of_int)/len(list_of_int) 
    except:
        return -2
