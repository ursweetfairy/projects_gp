import numpy as np
from numpy import random


def print_array():  
    arr = np.array([[-1,2,-3],[4,5,6],[7,8,9]])
    
    print(f"Tablica \n {arr}")
    print(f"Pierwszy element tablicy {arr[0]}")
    print(f"Pierwszy zagniezdzony element {arr[0][0]}")
    print(f"Typ obiektu tablicy {type(arr)}")
    print(f"Ksztalt tablicy {arr.shape}")
    return arr

arr = print_array()

def shapeshifter(arr):
    print("Ksztalt tablicy 9x1")
    print(arr.reshape(9,1))
    print("Ksztalt tablicy 1x9")
    print(arr.reshape(1,9))
    print("Ksztalt tablicy 3x3")
    print(arr.reshape(3,3))
    print("Ksztalt tablicy ?x9")
    print(arr.reshape(-1,9))
    print("Ksztalt tablicy 3x?")
    print(arr.reshape(3,-1))
    print("Podzial tablicy na 3")
    newarr = np.array_split(arr.reshape(-1,9), 3)
    print(newarr)

shapeshifter(arr)


def data_format():

    try:
            arr = np.array([[1.1,2.2,3.3],["kot",12,"ola"],['a', 'h', '5']],dtype ="U")
            print(arr)
            print(type(arr))

    except Exception as e:
         print(e)

    arr = np.array([[1.1,2.2,3.3],[4.4,5.5,6.6],[7.7,8.7,9.9]],dtype ="U")
    print(arr)
    print(type(arr))

    arr = np.array([[1.1,2.2,3.3],[4.4,5.5,6.6],[7.7,8.7,9.9]],dtype ="i")
    print(arr)
    print(type(arr))

    arr = np.array([[1.1,2.2,3.3],[4.4,5.5,6.6],[7.7,8.7,9.9]],dtype ="f")
    print(arr)
    print(type(arr))

data_format()

def sorted_ndarray():
    arr = np.array([[5,2,9],[8,1,4],[3,7,6]])
    print(f"Tablica przed sortowaniem {arr}")
    print(f"Tablica po sortowaniu {np.sort(arr)}")

sorted_ndarray()

def generate_random_numbers():
    for _ in range(10):
        print(random.randint(100))
    for _ in range(10):
        print(random.rand())

generate_random_numbers()


def pick_random_numbers():
    print(random.rand(3, 5))
    print(random.choice([3, 5, 7, 9]))
    print(random.choice([3, 5, 7, 9], size=(3, 5)))
    x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
    print(x)

pick_random_numbers()


def shuffle_ndarray():
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Przed tasowaniem {arr}")
    print(f"Przetasowana tablica {random.shuffle(arr)}")
    print(f"Po tasowaniu {arr}")

    arr = np.array([1, 2, 3, 4, 5])
    print(f"Przed tasowaniem {arr}")
    print(f"Przetasowana tablica {random.permutation(arr)}")
    print(f"Po tasowaniu {arr}")

shuffle_ndarray()

def array_functions():
    arr = np.linspace(0,10,11)
    print(f"Tablica: {arr}")
    print(f"Suma elementow: {np.sum(arr)}")
    print(f"Najmniejszy element: {np.min(arr)}")
    print(f"Najwiekszy element: {np.max(arr)}")
    print(f"Srednia elementow: {np.mean(arr)}")
    print(f"Wariancja elementow: {np.var(arr)}")
    print(f"Odchylenie standardowe elementow: {np.std(arr)}")
    
array_functions()

def mathematical_functions():
    print(f"Liczba pi: {np.pi}")
    print(f"Liczba Eulera: {np.e}")
    print(f"Liczba Eulera do potegi x: {np.exp(2)}")
    print(f"Sin  pi/2: {np.sin(0.5*np.pi)}")
    print(f"Cos  pi/2: {np.round(np.cos(0.5*np.pi))}")
    print(f"Tan  pi/2: {np.round(np.tan(0.5*np.pi))}")
    print(f"Pi/2 to {np.degrees(0.5*np.pi)} stopni, a 360 stopni to {np.radians(360)} radianow")

mathematical_functions()
