class Queue(object):
	def __init__(self,size):
		self.size = size
		self.enstack = []
		self.destack = []
		self.deqflag = False
	def enq(self, value):
		if self.isFull():
			return "Q is full"
		elif self.deqflag == True:
			self.transfer(self.destack, self.enstack)
			self.deqflag = False
		self.enstack.append(value)
	def deq(self):
		if self.isEmpty():
			return "Q is empty"
		elif self.deqflag == False:
			self.transfer(self.enstack, self.destack)
			self.deqflag = True
		x = self.destack.pop()
		return x
	def isFull(self):
		if self.deqflag == True and len(self.destack) == self.size:
			return True
		elif len(self.enstack) == self.size:
			return True
		else:
			return False
	def isEmpty(self):
		if self.deqflag == True and len(self.destack) == 0:
			return True
		elif len(self.enstack) == 0:
			return True
		else:
			return False
	def transfer(self, source, destination):
		for i in range(len(source)):
			destination.append(source.pop())

if __name__ == "__main__":
	q = Queue(5)
	print q.enq(1)
	print q.enq(2)
	print q.enq(3)
	print q.deq()

