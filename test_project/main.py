# def search(arr, target):
 
#     for i in range(len(arr)):
 
#         if arr[i] == target:
#             return i
 
#     return None


# arr=[10,20,30,40,50,60]
# print(search(arr,5))


# def binary_search(arr,target):
#     low = 0
#     high = len(list)-1
#     while low <= len(list)-1:
#         mid = (low +high)//2
#         guess = list[mid]
#         if guess == target:
#            return mid
#         if guess > target :
#            high = mid -1
    
#         else:
#            low = mid +1
    
#     else:
#         return None
    
# arr=[10,20,30,40,50,60]
# print(search(arr,50))
# print(binary_search(arr,50))
   
# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self) -> bool:
#         return len(self.items) == 0

#     def push(self, item) -> None:
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             item = self.items.pop()
#             print(f'Popped {item}')
#         return 'Stack is empty!'

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         return 'Stack is empty!'

#     def size(self) -> int:
#         return len(self.items)
    

    



# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push('apple')
# stack.push('banana')
# print(stack.items)


from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
            return
        return 'Queue is empty ! '

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
        return 'Queue is empty ! '

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
print(queue.enqueue)

