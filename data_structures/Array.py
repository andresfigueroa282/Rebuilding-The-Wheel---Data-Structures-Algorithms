"""
====================================
Author: Andres Figueroa
Email: andresfigueroa282@brandeis.edu

Description:
    This file implements a custom Array class along with 
    different operations (insert, delete, search, sort, etc.).

How to Run:
    Option 1: Run directly (if this file is standalone):
        python Array.py

    Option 2: Run as a module (if using project structure):
        python -m data_structures.Array
====================================
"""
class Array:

    capacity = 0 # The total number of slots available in memory (The number of seats that exist)
    array = [] # The memory
    size = 0 # The number of actual elements stored in the array (The number of seats that are filled)

    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.array = [None] * capacity

    # Return the number of stored elements, not capacity of the array
    def len(self):
        return self.size
    
    # Adds values to the end of an array
    def append(self, value):
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1 # To tell us/adjusts how many elements are in the array

        #print(f"@ append() {self.printArray()}")
    ''' What I was doing previously was copying every value from one array to a new one then copying. While it did work, it was overly complicated and took a much
        longer time than the code above. Here, I am just assigning the upper value of the array, which should
        be a free open space in memory, to the value.'''

    # Adjusts capacity if full, this is what makes a dynamic array dynamic
    def resize(self):
        self.capacity += 4
        newArray = [None] * self.capacity
        for i in range(self.len()):
            newArray[i] = self.array[i]
        self.array = newArray
    '''Here, I am adding +4 memory to the array to add more elements. I am then copying the contents of the older array to the new one'''

    # Getting an item at a specified index
    def __getitem__(self, index):
        if self.inBounds(index):
            return self.array[index]

    # Setting the value at a specified index to the value given
    def __setitem__(self, index, value):
        if self.inBounds(index):  
            self.array[index] = value

    # Inserting a value at a specified index
    def insert(self, index, value):
        if self.inBounds(index):
            if self.size + 1 == self.capacity:
                self.resize()
            
            newArray = [None] * self.capacity
            for i in range(index):
                newArray[i] = self.array[i]
            newArray[index] = value
            for i in range(index, self.size):
                newArray[i + 1] = self.array[i]

            self.array = newArray
            self.size += 1

            #print(f"@ insert {self.printArray()}")
    '''Insert was really frusturating. Previously, I was conducting all operations in one loop. When the specified index was reached, I would then shift the values.
        This is essentially the same idea. Copy paste, just two seperate for-loops. What made this so frusturating was that 'printArray' gave me the expected output.
        Then, the actual array would have a bunch of 'None' values and one actual element. What made this really frusturating was that I needed to look at a solution
        online. There is definitely a prettier solution than the one above, but I wanted these solutions to be my own! I am just annoyed with having to rely on an
        online solution.'''
    
    # Deleting the value at the specified index
    def delete(self, index):
        if self.inBounds(index) and self.size != 0:
            newArray = [None] * self.capacity
            for i in range(index):
                newArray[i] = self.array[i]
        
            for i in range(index, self.size + 1):
                newArray[i] = self.array[i + 1]

            self.array = newArray
            self.size -= 1

            #print(f"@ delete {self.printArray()}")
    ''''delete()' was a lot easier after having figured out how to implement 'insert()'. In one for-loop, I essentially copied the values till index was reached. Then
        in the second, I am copying and skipping over the index.'''

    # Removing and returning the upper element in the array    
    def pop(self):
        if self.size == 0:
            return "There are no elements to pop"
        
        popped = self.array[self.size - 1]
        self.array[self.size] = None
        self.size -= 1
        return popped
    '''Here, I am just getting the upper value of the array, assigning 'popped' the value. Then, I would set the upper value of the array to None as to remove it.'''
    
    # Checks whether an index is within the bounds of the array and not  memory
    def inBounds(self, index):
        if 0 <= index and index < self.size:
            return True
        else:
            raise IndexError
    '''If the index is between 0 and the length of the array, then the index is valid'''


    def printArray(self):
        toPrint = "["
        for i in range(self.len()):
            if i != self.len() - 1:
                toPrint = toPrint + f"{self.array[i]}, "
            else:
                toPrint = toPrint + f"{self.array[i]}]"
        return toPrint
    '''This wasn't required, but helped me understand what was happening in each function. There were aalso a lot more print statements.'''

    def linearSearch(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1
    '''Goes through the array until the value is found and returns that index'''
    
    def binarySearch(self, value):
        lower = 0
        upper = self.size - 1
        print(f"lower: {lower}")
        print(f"upper: {upper}")
        run = 0
        while lower < upper:
            run += 1
            midpoint = lower + (upper - lower) // 2
            #print(f"midpoint on run {run}: {midpoint}")
            if self.array[lower] == value:
                return lower
            if self.array[upper] == value:
                return upper
            if self.array[midpoint] == value:
                return midpoint
            if value < self.array[midpoint]:
                upper = midpoint - 1
            if value > self.array[midpoint]:
                lower = midpoint + 1 
            #print(f"lower on run {run}: {lower}")
            #print(f"upper on run {run}: {upper}")
        
        return -1
    '''Halves the search each iteration(O(log n)). REQUIRES A SORTED ARRAY. Finds a midpoint, then determines if the value is greater or less than the given value.
        If the value is greater than the midpoint, then we search the right half of the array, else the left half if less than the midpoint. This continues till the
        search is reduced to a single value, hopefully the value we are looking for'''
    
    def recursiveBinarySearch(self, array, target, left, right):
        if left > right:
            return -1
        midpoint = (left + right) // 2

        if array[midpoint] == target:
            return midpoint

        elif array[midpoint] > target:
            return self.recursiveBinarySearch(array, target, left, midpoint - 1)
        
        else:
            return self.recursiveBinarySearch(array, target, midpoint + 1, right)
    '''Binary Search done recursively'''
    
    def bubbleSort(self):
        for i in range(self.len()):
            for j in range(0, self.len() - i - 1):
                if self.array[j] > self.array[j + 1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = temp
    '''Elements next to each other are swapped. Comparing neighbors.'''

    def selectionSort(self):
        for i in range(self.len()):
            curr = i
            for j in range(1 + i, self.len()):
                if self.array[j] < self.array[curr]:
                    curr = j
            temp = self.array[i]
            self.array[i] = self.array[curr]
            self.array[curr] = temp
    '''The smallest element is swapped and sent to the front in an ordered manner. Finding the smallest value for the rest of the array and swapping with the current value.'''

    def insertionSort(self):
        for i in range(1, self.len()):
            curr = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > curr:
                self.array[j + 1] = self.array[j]
                j -= 1
            
            self.array[j + 1] = curr
    '''Inserting an element in the "right place", shifting larger elements to the right'''
        
    

if __name__ == "__main__":
    from tests.TestArray import TestArray
    tester = TestArray()
    tester.run_tests()