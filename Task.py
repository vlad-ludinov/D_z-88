def binary_search(search_list: list, num: int) -> int:

    low = 0
    high = len(search_list) - 1

    while low <= high:
      
        mid = (low + high)//2
       
        if search_list[mid] == num:
            return mid
        elif search_list[mid] > num:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(binary_search([1, 2, 3, 6, 7, 9], 1))
print(binary_search([1, 2, 3, 6, 7, 9], 6))
print(binary_search([1, 2, 3, 6, 7, 9], 9))
print(binary_search([1, 2, 3, 6, 7, 9], 4))