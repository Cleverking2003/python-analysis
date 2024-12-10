import numpy as np

def function1(int_list):
    n_list = np.array(int_list)
    n_list = np.where(n_list < 0, n_list - 3, n_list)
    n_list = np.where(n_list > 0, n_list * 3, n_list)
    n_list = np.where(n_list == 0, n_list + 1, n_list)
    return np.sum(n_list)


def function2(temperature1, temperature2):
    temp1 = np.array(temperature1)
    temp2 = np.array(temperature2)
    step2 = np.concatenate((temp1[::3],temp2[::3]))
    mas_temp = step2[step2 > 0]
    return int(np.min(mas_temp)) + int(np.max(mas_temp)) + int(np.average(mas_temp)) + int(np.std(mas_temp))

def function(a, b, c, d):
    A = np.array([
        [1, 0, 1, 0],
        [4, 0, 1, -2],
        [-4, 4, 0, 1],
        [a, b, c, d],
    ])
    B = np.array([2, 0, 5, -2]).T
    sol = np.linalg.inv(A) @ B
    return int(np.sum(sol))

print(function(12,12,1,1))
print(function(102,12,33,1))
