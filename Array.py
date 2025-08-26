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
    
    def append(self, value):
        self.size += 1
        if self.size > self.capacity:
            self.resize()
        switch = False
        for i in range(self.capacity):
            if self.array[i] is None and switch == False:
                self.array[i] = value
                switch = True

    # Adjusts capacity if full, this is what makes a dynamic array dynamic
    def resize(self):
        self.capacity += 4
        newArray = [] * self.capacity
        for i in range(self.len()):
            newArray[i] = self.array[i]
        self.array = newArray

    def __getitem__(self, index):
        if self.inBounds(index):
            return self.array[index]

    def __setitem__(self, index, value):
        if self.inBounds(index):
            self.array[index] = value

    def insert(self, index, value):
        
        
    def delete(self, index):
        if self.inBounds(index):
            self.size -= 1
            switch = 0
            newArray = [] * self.capacity
            for i in range(self.len()):
                if i == index:
                    switch = 1
                newArray[i] = self.array[i + switch]

    def pop(self):
        if self.size == 0:
            return "There are no elements to pop"
        popped = self.array[0]
        newArray = [] * self.capacity
        for i in range(1, self.len()):
            newArray[i] = self.array[i]
        self.array = newArray[i]
        return popped

    def inBounds(self, index):
        return index < 0 or index >= self.size - 1
    
    def printArray(self):
        toPrint = "["
        print(f"self.len(): {self.len()}")
        for i in range(self.len()):
            if i != self.len() - 1:
                toPrint = toPrint + f"{self.array[i]}, "
            else:
                toPrint = toPrint + f"{self.array[i]}]"
        return toPrint

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
        self.check(popped == 20 and len(arr) == 1,
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
