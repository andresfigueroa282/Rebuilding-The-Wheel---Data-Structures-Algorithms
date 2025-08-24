class Array:
    capacity = 0
    array = []
    size = 0

    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.array = [None] * capacity

    def len(self):
        return self.size
    
    def append(self, value):
        if self.freeSpaceCheck():
            switch = False
            for i in range(self.len()):
                if self.array[i] is None and switch == False:
                    self.array[i] == value
                    switch = True
        
        else:
            self.size += 1
            newArray = [self.size]
            for i in range(self.len()):
                newArray[i] = self.array
            newArray[self.size] = value

    def __getitem__(self, index):
        if index < 0 or index >= self.len():
            return "Index Out of Bounds Error"
        else:
            return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.len():
            return "Index Out of Bounds Error"
        else:
            self.array[index] = value

    def insert(self, index, value):
        if index < 0 or index >= self.len():
            return "Index Out of Bounds Error"
        if self.array[index] is None:
            self.array[index] = value
        else:
            switch = False
            self.size += 1
            newArray = [None] * self.size
            for i in range(self.size):
                if switch == False:
                    newArray[i] == self.array[i]
                    if i == index:
                        switch = True
                        newArray[i] == value
                else:
                    newArray[i] == self.array[i - 1]
                    


    def delete(self, index):
        if index < 0 or index >= self.len():
            return "Index Out of Bounds Error"
        else:
            switch = False
            self.size -= 1
            newArray = [None] * self.size
            for i in range(self.size):
                if i < index:
                    newArray[i] == self.array[i]
                if i > index:
                    newArray[i] == self.array[i - 1]

    def freeSpaceCheck(self):
        for i in range(self.len() + 1):
              if self.array[i] is None:
                   return True
        return False
    
    def print(self):
        arrayString = "["
        for i in range(self.len() - 1):
            arrayString = arrayString.join(self.array[i], ", ")
        arrayString = arrayString.join(self.array[self.len()], "]")
        print(arrayString)


    
class TestArray:
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0
        self.total_tests = 0

    def check(self, condition, message):
        """Helper to check test results"""
        self.total_tests += 1
        if condition:
            print(f"✅ PASS: {message}")
            self.tests_passed += 1
        else:
            print(f"❌ FAIL: {message}")
            self.tests_failed += 1

    def run_tests(self):
        print("🚀 Running Array Tests...\n")

        arr = Array(capacity=5)

        # Test 1: Append
        arr.append(10)
        self.check(arr[0] == 10, "Append inserts correctly")

        # Test 2: Insert
        arr.append(20)
        arr.insert(1, 15)
        self.check(arr[1] == 15 and arr[2] == 20, "Insert shifts elements correctly")

        # Test 3: Delete
        arr.delete(1)
        self.check(arr[1] == 20, "Delete removes element and shifts")

        # Test 4: Pop
        popped = arr.pop()
        self.check(popped == 20 and len(arr) == 1, "Pop returns and removes last element")

        # Test 5: Set item
        arr[0] = 99
        self.check(arr[0] == 99, "Set item works correctly")

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


    array = [1, 2, 3, 4]
    for i in array:
        print(i)

    tester = TestArray()
    tester.run_tests()
