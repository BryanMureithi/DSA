def binary_search(list, target):
    first = 0 #First value in the list
    last = len(list) - 1 #last value in the list

    while first <= last:
        midpoint = (first + last) // 2 #floor division rounds down to the nearest whole number

        if list[midpoint] == target:
            return midpoint
        
        elif list[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return None            

def verify(index):
     if index is not None:
          print("Target found at index:", index)
     else:
          print("Target not found in the list") 

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 10)
verify(result)