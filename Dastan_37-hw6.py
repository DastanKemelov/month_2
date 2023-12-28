def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(element, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


unsorted_list = [59, 23, 42, 17, 8, 91, 12]


sorted_list = bubble_sort(unsorted_list.copy())
print("Отсортированный список метод пузырьковой сортировки:", sorted_list)


element_to_search = 17
result = binary_search(element_to_search, sorted_list)
if result != -1:
    print(f"Элемент {element_to_search} найден на позиции {result}")
else:
    print(f"Элемент {element_to_search} не найден")
