class Heap:
    def __init__(self):
        self.arr = []

    @staticmethod
    def parent(i):
        return i // 2

    @staticmethod
    def left(i):
        return i * 2 + 1

    @staticmethod
    def right(i):
        return i * 2 + 2

    def size(self):
        return len(self.arr)

    def get_min(self):
        return self.arr[0]

    def delete_min(self, v):
        if self.size() == 0:
            return None

        i = self.arr.index(v)
        self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
        head = self.arr.pop()
        if self.size() > 0:
            self.sift_down(i)
        return head

    def sift_up(self, i):
        while i > 0:
            parent = Heap.parent(i)
            if self.arr[i] < self.arr[parent]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent

    def sift_down(self, i):
        while True:
            min_child = self.min_child(i)
            if i == min_child:
                break
            self.arr[i], self.arr[min_child] = self.arr[min_child], self.arr[i]
            i = min_child

    def insert(self, e):
        self.arr.append(e)
        self.sift_up(self.size() - 1)

    def min_child(self, i):
        left = Heap.left(i)
        right = Heap.right(i)
        length = self.size()
        smallest = i
        if left < length and self.arr[i] > self.arr[left]:
            smallest = left
        if right < length and self.arr[smallest] > self.arr[right]:
            smallest = right
        return smallest

if __name__ == '__main__':
    n = int(input())
    heap = Heap()

    for _ in range(n):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            heap.insert(cmd[1])
        elif cmd[0] == 2:
            heap.delete_min(cmd[1])
        elif cmd[0] == 3:
            print(heap.get_min())