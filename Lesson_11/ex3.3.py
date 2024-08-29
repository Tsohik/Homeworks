#.Write a python function, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers

def create_cubes_dict(N):
    return {i: i**3 for i in range(1, N + 1)}
N = 5
cubes_dict = create_cubes_dict(N)
print(cubes_dict)
