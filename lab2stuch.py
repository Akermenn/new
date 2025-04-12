import numpy as np
#level 1  task 1
arr = np.array([1, 2, 3, 4, 5, 6], dtype=float)
sum_arr = np.sum(arr)
arr /= sum_arr

print("Результат задания 1 уровень 1:")
print(arr, '\n')


#level 1  task 2

arr = np.array([-1, 2, -3, 4, 5, -6, 7, 8], dtype=float)
positive_elements = arr[arr > 0]
mean_positive = np.mean(positive_elements)
arr[arr > 0] = mean_positive

print("Результат задания 2 уровень 1:")
print(arr, '\n')

#level 1  task 3

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
sum_arr = arr1 + arr2
diff_arr = arr1 - arr2

print("Результат задания 3 уровень 1:")
print("Сумма массивов:", sum_arr)
print("Разность массивов:", diff_arr, '\n')

#level 2 task 1

arr = np.array([5, 3, 8, 1, 9, 2])
min_index = np.argmin(arr)
arr[min_index] *= 2

print("Результат задания 1 уровень 2:")
print(arr, '\n')

#level 2 task 2

arr = np.array([5, 3, 8, 1, 9, 2])
max_index = np.argmax(arr)
sum_before_max = np.sum(arr[:max_index])

print("Результат задания 2 уровень 2:")
print("Сумма элементов до максимального:", sum_before_max, '\n')


#level 2 task 3

arr = np.array([5, 3, 8, 1, 9, 2])
min_index = np.argmin(arr)
arr[:min_index] *= 2

print("Результат задания 3 уровень 2:")
print(arr, '\n')

#level 3 task 1

arr = np.array([5, 3, 8, 8, 9, 2, 9, 1])
max_value = np.max(arr)
max_indices = np.where(arr == max_value)[0]

print("Результат задания 1 уровень 3:")
print("Индексы максимальных элементов:", max_indices, '\n')

#level 3 task 6

arr = np.array([5, -3, 8, -1, 9, -2, 7, -4])
negative_elements = arr[arr < 0]
non_negative_elements = arr[arr >= 0]
result = np.concatenate((non_negative_elements, negative_elements))

print("Результат задания 6 уровень 3:")
print(result, '\n')


#level 3 task 12


arr = np.array([5, 3, 8, 5, 9, 2, 3, 1])
unique_elements = np.unique(arr)

print("Результат задания 12 уровень 3:")
print(unique_elements)