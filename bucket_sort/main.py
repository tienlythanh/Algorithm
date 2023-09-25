import numpy as np
import time
import math

def insertion_sort(array):
    for index in range(1,len(array)): 
        value = array[index]
        j = index
        while j > 0 and array[j-1] > value:
            array[j] = array[j-1]
            j = j-1
        array[j] = value
    return array

def bucket_sort(array, num_of_buckets):
    result = []
    max_value = get_max_of_array(array)
    buckets = []

    for i in range(0,num_of_buckets):
        buckets.append([])

    for element in array:
        bucket_index = int(num_of_buckets*element/(max_value + 1))
        buckets[bucket_index].append(element)

    for bucket in buckets:
        bucket = insertion_sort(bucket)
        result.extend(bucket)

    return result

def get_max_of_array(array):
    max_element = array[0]
    for index in range(1,len(array)):
        if array[index] > max_element:
            max_element = array[index]

    return max_element


if __name__ == "__main__":
    num_of_test_case = 10
    log_file = open('log.txt', 'a')
    for i in range(num_of_test_case):
        array_length = np.random.randint(100000,999999)
        start_time = time.time()
        array = np.random.random(size=array_length)
        bucket_sort_array = bucket_sort(array,  int(math.sqrt(array_length)))
        end_time = time.time()
        
        print(bucket_sort_array)
        print(end_time - start_time)
        log_file.write(f"Test case {i + 1}\n")
        log_file.write(f"Array length {array_length}\n")
        log_file.write(f"Excute time: {end_time - start_time}s\n\n")
    
    log_file.close()