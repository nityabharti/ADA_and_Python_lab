
from abc import ABC, abstractmethod, abstractproperty


class Sorting(ABC):

    @abstractproperty
    def data(self):  # property for storing values
        pass

    # method to sort the data
    @abstractmethod
    def sort(self):
        pass

    # method to display data
    @abstractmethod
    def display(self):
        pass


class BubbleSort(Sorting):
    def __init__(self, arr):
        self.arr = [x for x in arr]  # Deep copy

    @property
    def data(self):
        return self.arr

    def sort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-i-1):
                if self.arr[j] > self.arr[j+1]:
                    # Swapping if left side value is greater
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def display(self):
        for val in self.arr:
            print(val, end=" ")
        print()


class SelectionSort(Sorting):
    def __init__(self, arr):
        self.arr = [x for x in arr]  # Deep copy

    @property
    def data(self):
        return self.arr

    def sort(self):
        for i in range(len(self.arr)):
            min_val_idx = i
            for j in range(i, len(self.arr)):
                if self.arr[j] < self.arr[min_val_idx]:
                    min_val_idx = j
            # swapping with the smallest value
            self.arr[i], self.arr[min_val_idx] = self.arr[min_val_idx], self.arr[i]

    def display(self):
        for val in self.arr:
            print(val, end=" ")
        print()


if __name__ == "__main__":
    # taking user input
    array = [int(x) for x in input("Enter space seperated values: ").split()]

    # instantiating Bubble Sort class
    print("\n-----Bubble Sort-----")
    b = BubbleSort(array)
    print("Before sorting: ")
    b.display()
    b.sort()
    print("After sorting: ")
    b.display()

    # instantiating Selection Sort class
    print("\n-----Selection Sort-----")
    s = SelectionSort(array)
    print("Before sorting: ")
    s.display()
    s.sort()
    print("After sorting: ")
    s.display()

