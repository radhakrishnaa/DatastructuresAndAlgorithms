class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.q = [None for i in range(k)]
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.tail = (self.tail + 1)%self.size
            #print self.tail
            self.q[self.tail] = value
            if self.head == -1:
                self.head += 1
            return True

        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        data = self.q[self.head]
        if self.head == self.tail:
            
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        print(data)
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return False
        else:
            print(self.q[self.head])
            return True

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return False
        else:
            print(self.q[self.tail])
            return True

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.head == -1:
            return True
        else:
            return False
        
    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if ((self.tail + 1) % self.size) == self.head:
            return True

if __name__ == '__main__':
    c = MyCircularQueue(2)
    print c.enQueue(2)
    print c.deQueue()
    print c.deQueue()
    print c.enQueue(3)
    print c.enQueue(4)
    print c.deQueue()
    print c.deQueue()