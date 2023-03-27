

#create a function to find if a number is prime or not.
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


#create a function to find median of two sorted lists in O(logn) time.
def find_median(list1, list2):
    if len(list1) > len(list2):
        list1, list2 = list2, list1
    x = len(list1)
    y = len(list2)
    low = 0
    high = x
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX
        maxLeftX = list1[partitionX - 1] if partitionX != 0 else float('-inf')
        minRightX = list1[partitionX] if partitionX != x else float('inf')
        maxLeftY = list2[partitionY - 1] if partitionY != 0 else float('-inf')
        minRightY = list2[partitionY] if partitionY != y else float('inf')
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
            