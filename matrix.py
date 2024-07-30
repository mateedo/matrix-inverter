import numpy as np

def isSquare(arr):
    if arr.shape[0] == arr.shape[1]:
        return True
    
    return False


def determinant(arr):
    if arr.shape[0] == 2:
        return (arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0])
    

    sum = 0
    for i in range(len(arr)):

        temp = arr
        temp = np.delete(temp, i, 1)
        temp = np.delete(temp, 0, 0)
        if i % 2 == 0:
            sum+= arr[0][i] * determinant(temp)
        else:
            sum-= arr[0][i] * determinant(temp)

    return sum

def Identity(n):

    identity = []
    for i in range(n):
        identity.append(n * [0])


    for i in range(n):
        identity[i][i] = 1

    return np.array(identity, dtype = float)

def dotProduct(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i] * v2[i]


    return sum


def matrixMultiply(arr1, arr2):
    temp = []
    if arr1.shape[1] != arr2.shape[0]:
        print("Not compatible")

    for i in range(arr1.shape[0]):
        row1 = []
        for j in range(arr2.shape[1]):
            

            row1.append(dotProduct(arr1[i], arr2[:,j]))
        
        temp.append(row1)


    return np.array(temp).T




def calculateInverse(temp):
    arr = temp
    arr = np.array(arr, dtype=float)

    if not isSquare(arr):
        print("Not square.")
        return
    
    if determinant(arr) == 0:
        print("Non-zero Determinant")
        return
    

    n = arr.shape[0]
    identity = Identity(n)

    for i in range(n):

        for j in range(i):
            if arr[i][j] == 0:
                continue
            else:
                identity[i] = identity[i] / arr[i][j] - identity[j]
                arr[i] = arr[i] / arr[i][j] - arr[j]


        identity[i] = identity[i] / arr[i][i]
        arr[i] = arr[i] / arr[i][i]


    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            identity[j] = identity[j] - identity[i] * arr[j][i]
            arr[j] = arr[j] - arr[i] * arr[j][i]
    # print(arr)
    return identity





arr = np.array([[5, 3, 2, 0], [0, 10, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

inverse_arr = calculateInverse(arr)

print("Matrix A", "\n", arr, "\n")
print("A-inverse", "\n", inverse_arr, "\n")
print(matrixMultiply(inverse_arr, arr))
# print(matrixMultiply(calculateInverse(arr), arr))

# print(arr, determinant(arr))