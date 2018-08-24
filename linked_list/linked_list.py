class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class linkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def search(self, data):
        current = self.head
        found = False
        while current != None and found == False:
            if current.data == data:
                found = True
            else:
                current = current.next
        if found == True:
            return True
        else:
            return False

    def remove(self, data):
        current = self.head
        prev = None

        while current != None:
            if current.data == data:
                break
            else:
                prev = current
                current = current.next
        if current == None:
            return "could not find the element"
        elif prev == None:
            self.head = current.next
        else:
            prev.next = current.next

    def traverse(self):
        current = self.head
        while current != None:
            print str(current.data) + "-->",
            current = current.next

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += str(p.data)
                s += "->"
                p = p.next
            s += str(p.data)
        return s

mylist = linkedList()
mylist.add(9)
mylist.add(10)
mylist.add(11)
mylist.add(12)

#mylist.traverse()

print mylist

mylist.remove(10)

print mylist



