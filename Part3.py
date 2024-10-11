def counting_sort(input_array):
    min_value = min(input_array)
    shifted_array = [num - min_value for num in input_array]
    k = max(shifted_array)
    count = [0] * (k + 1)
    output = [0] * len(shifted_array)
    for i in range(len(shifted_array)):
        count[shifted_array[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(shifted_array) - 1, -1, -1):
        count[shifted_array[i]] -= 1
        output[count[shifted_array[i]]] = shifted_array[i]
    sorted_array = [num + min_value for num in output]
    return sorted_array
input_array = [-5, -10, 0, -3, 8, 5, -1, 10]
sorted_array = counting_sort(input_array)
print("Sorted array:", sorted_array)


# RADIX SORT
def counting_sort_for_radix(input_array, exp):
    n = len(input_array)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (input_array[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (input_array[i] // exp) % 10
        count[index] -= 1
        output[count[index]] = input_array[i]
    for i in range(n):
        input_array[i] = output[i]
def radix_sort(input_array):
    max_num = max(input_array)
    exp = 1 
    while max_num // exp > 0:
        counting_sort_for_radix(input_array, exp)
        exp *= 10
input_array = [110, 45, 65,50, 90, 602, 24, 2, 66]   
radix_sort(input_array)
print("Sorted array:", input_array)

#BUCKET SORT

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        index = int(arr[i] * n)  
        buckets[index].append(arr[i])
    for bucket in buckets:
        insertion_sort(bucket)
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    return sorted_array
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
sorted_array = bucket_sort(arr)
print("Sorted array:", sorted_array)
