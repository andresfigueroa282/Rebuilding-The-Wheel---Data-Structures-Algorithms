# --------------------------------------------------------------------------------------------------------------------------------
# The TestArray Class is NOT MY WORK I used ChatGPT to create tests for me becuase I am unfamiliar with how to create tests and I want to focus more on the implementation.

from Array import Array

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

        # ----------------
        # BASIC OPERATIONS
        # ----------------
        arr.append(10)
        self.check(arr[0] == 10, "Append inserts correctly", expected=10, actual=arr[0])

        arr.append(20)
        arr.insert(1, 15)
        self.check(arr[1] == 15 and arr[2] == 20,
                   "Insert shifts elements correctly",
                   expected=[10, 15, 20],
                   actual=[arr[i] for i in range(arr.len())])

        arr.delete(1)
        self.check(arr[1] == 20,
                   "Delete removes element and shifts",
                   expected=20,
                   actual=arr[1])

        popped = arr.pop()
        self.check(popped == 20 and arr.len() == 1,
                   "Pop returns and removes last element",
                   expected=(20, 1),
                   actual=(popped, arr.len()))

        arr[0] = 99
        self.check(arr[0] == 99,
                   "Set item works correctly",
                   expected=99,
                   actual=arr[0])

        try:
            _ = arr[10]
            self.check(False, "Out of range index raises IndexError")
        except IndexError:
            self.check(True, "Out of range index raises IndexError")

        try:
            arr.delete(10)
            self.check(False, "Invalid delete index raises IndexError")
        except IndexError:
            self.check(True, "Invalid delete index raises IndexError")

        # ----------------
        # SEARCHING TESTS
        # ----------------
        arr2 = Array()
        for val in [5, 3, 8, 3, 10]:
            arr2.append(val)

        # Linear search
        idx = arr2.linearSearch(8)
        self.check(idx == 2,
                   "Linear search finds correct index",
                   expected=2,
                   actual=idx)

        idx = arr2.linearSearch(42)
        self.check(idx == -1,
                   "Linear search returns -1 if not found",
                   expected=-1,
                   actual=idx)

        # Binary search (assumes sorted array)
        arr_sorted = Array()
        for val in [1, 3, 5, 7, 9]:
            arr_sorted.append(val)

        idx = arr_sorted.binarySearch(7)
        self.check(idx == 3,
                   "Binary search finds correct index in sorted array",
                   expected=3,
                   actual=idx)

        idx = arr_sorted.binarySearch(4)
        self.check(idx == -1,
                   "Binary search returns -1 if element not found",
                   expected=-1,
                   actual=idx)

        # ----------------
        # SORTING TESTS
        # ----------------
        arr3 = Array()
        for val in [64, 25, 12, 22, 11]:
            arr3.append(val)

        # Bubble sort
        arr3.bubbleSort()
        self.check([arr3[i] for i in range(arr3.len())] == [11, 12, 22, 25, 64],
                   "Bubble sort sorts array correctly",
                   expected=[11, 12, 22, 25, 64],
                   actual=[arr3[i] for i in range(arr3.len())])

        # Selection sort
        arr4 = Array()
        for val in [29, 10, 14, 37, 14]:
            arr4.append(val)

        arr4.selectionSort()
        self.check([arr4[i] for i in range(arr4.len())] == [10, 14, 14, 29, 37],
                   "Selection sort sorts array correctly",
                   expected=[10, 14, 14, 29, 37],
                   actual=[arr4[i] for i in range(arr4.len())])

        # Insertion sort
        arr5 = Array()
        for val in [5, 2, 9, 1, 5, 6]:
            arr5.append(val)

        arr5.insertionSort()
        self.check([arr5[i] for i in range(arr5.len())] == [1, 2, 5, 5, 6, 9],
                   "Insertion sort sorts array correctly",
                   expected=[1, 2, 5, 5, 6, 9],
                   actual=[arr5[i] for i in range(arr5.len())])

        # ----------------
        # SUMMARY
        # ----------------
        print("\n📊 Test Summary:")
        print(f"Total: {self.total_tests}, Passed: {self.tests_passed}, Failed: {self.tests_failed}")

        score = (self.tests_passed / self.total_tests) * 100
        print(f"🏆 Final Score: {score:.2f}%")