

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
        longer time than the code above. Here, I am just assigning the last value of the array, which should
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

    # Removing and returning the last element in the array    
    def pop(self):
        if self.size == 0:
            return "There are no elements to pop"
        
        popped = self.array[self.size - 1]
        self.array[self.size] = None
        self.size -= 1
        return popped
    '''Here, I am just getting the last value of the array, assigning 'popped' the value. Then, I would set the last value of the array to None as to remove it.'''
    
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

# --------------------------------------------------------------------------------------------------------------------------------
# The TestArray Class is NOT MY WORK I used ChatGPT to create tests for me becuase I am unfamiliar with how to create tests and I want to focus more on the implementation.

class TestArray:
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0
        self.total_tests = 0

    def check(self, condition, message, expected=None, actual=None):
        """Helper to check test results and print expected vs actual"""
        self.total_tests += 1
        if condition:
            print(f"✅ PASS: {message}")
            self.tests_passed += 1
        else:
            print(f"❌ FAIL: {message}")
            if expected is not None or actual is not None:
                print(f"   Expected: {expected}")
                print(f"   Actual:   {actual}")
            self.tests_failed += 1

    def run_tests(self):
        print("🚀 Running Array Tests...\n")

        arr = Array(capacity=5)

        # Test 1: Append
        arr.append(10)
        self.check(arr[0] == 10, "Append inserts correctly", expected=10, actual=arr[0])

        # Test 2: Insert
        arr.append(20)
        arr.insert(1, 15)
        self.check(arr[1] == 15 and arr[2] == 20,
                   "Insert shifts elements correctly",
                   expected=[10, 15, 20],
                   actual=[arr[i] for i in range(arr.len())])

        # Test 3: Delete
        arr.delete(1)
        self.check(arr[1] == 20,
                   "Delete removes element and shifts",
                   expected=20,
                   actual=arr[1])

        # Test 4: Pop
        popped = arr.pop()
        self.check(popped == 20 and arr.len() == 1,
                   "Pop returns and removes last element",
                   expected=(20, 1),
                   actual=(popped, arr.len()))

        # Test 5: Set item
        arr[0] = 99
        self.check(arr[0] == 99,
                   "Set item works correctly",
                   expected=99,
                   actual=arr[0])

        # Test 6: Get item (IndexError)
        try:
            _ = arr[10]
            self.check(False, "Out of range index raises IndexError")
        except IndexError:
            self.check(True, "Out of range index raises IndexError")

        # Test 7: Delete invalid index
        try:
            arr.delete(10)
            self.check(False, "Invalid delete index raises IndexError")
        except IndexError:
            self.check(True, "Invalid delete index raises IndexError")

        # Summary
        print("\n📊 Test Summary:")
        print(f"Total: {self.total_tests}, Passed: {self.tests_passed}, Failed: {self.tests_failed}")

        score = (self.tests_passed / self.total_tests) * 100
        print(f"🏆 Final Score: {score:.2f}%")

if __name__ == "__main__":

    tester = TestArray()
    tester.run_tests()
