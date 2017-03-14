from collections import defaultdict

class DJNode:
	def __init__(self,value):
		self.value = value
		self.next = None
class DJSet:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
	def add(self,node):
		self.size += 1
		if (not self.head):
			self.head = node
		if (not self.tail):
			self.tail = node
		else: 
			self.tail.next = node
			self.tail = node
	def remove(self,value):
		prev = None
		cur = self.head
		while (cur != None):
			#Found
			if cur.value == value:
				if (prev):
					prev.next = cur.next
				if (cur == self.head):
					self.head = cur.next
				if (cur == self.tail):
					self.tail = prev
				self.size -= 1
				return
			prev = cur
			cur = cur.next
	def find(self,value):
		cur = self.head
		while (cur != None):
			if cur.value == value:
				return True
			cur = cur.next
		return False
	def union(self, set2):
		self.tail.next = set2.head
		self.tail = set2.tail
	def printValues(self):
		cur = self.head
		if (cur):
			print('[',end='')
			while (cur.next != None):
				print(cur.value,end='-->')
				cur = cur.next
			print(cur.value,end=']\n')
		else:
			print("[]")


class DisjointSet:
	def __init__(self):
		self.sets = defaultdict(int)
	def addSet(self,index):
		if not self.sets[index]:
			self.sets[index] = DJSet()
		else:
			print("Set " + str(index) + " already exists!")
	def addToSet(self,index,value):
		if self.sets[index]:
			self.sets[index].add(DJNode(value))
		else:
			print("Set " + str(index) + " does not exist")
			del self.sets[index]

	def union(self,set1,set2):
		if self.sets[set1] and self.sets[set2]:
			self.sets[set1].union(self.sets.pop(set2))
		elif self.sets[set1] and not self.sets[set2]:
			print("Set " + str(set2) + " does not exist")
			del self.sets[set2]
		elif self.sets[set2] and not self.sets[set1]:
			print("Set " + str(set1) + " does not exist")
			del self.sets[set1]
		else:
			print("Neither set " + str(set1) + " nor set " + str(set2) + " exist")
			del self.sets[set1]
			del self.sets[set2]
	def find(self,value):
		for k,v in self.sets.items():
			if v.find(value):
				return k
		return None
	def printSets(self):
		for k,v in self.sets.items():
			print("Set " + str(k) + ": ",end='')
			v.printValues()
	def removeSet(self, index):
		del self.sets[index] #Doesn't check if set exists

	def getSize(self, index):
		if (self.sets[index]):
			return self.sets[index].size
		else:
			print("Set " + str(index) + " does not exist")
			del self.sets[index]


