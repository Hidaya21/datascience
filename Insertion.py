def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key["gpa"] < arr[j]["gpa"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Test case
import random
def main():

    # Generate 10 random integers in the range [50, 100] using list comprehension
    #numbers = []
    #for i in range (10):
        #numbers.append(random.randint(50, 100))
    students=[{"name":"Alic","age":20,"gpa":3.9},
         {"name":"Bob","age":20,"gpa":3.7},
         {"name":"Charlie","age":21,"gpa":4.0},
         {"name":"David","age":19,"gpa":3.5},
         ]

  
    print("Original dictionary:")
    for s in students:
        print(s)
    print("--------------------------------")
    insertion_sort(students)
    print("Sorted dictionary:")

    for s in students:
        print(s)    
    #print("Sorted dictionary:", students)
main()
