# Implement a class for a Least Recently Used (LRU) Cache. The cache should support inserting key / value pairs (the insertKeyValuePair() method), retrieving a key's value (the getValueFromKey() method), and retrieving the most recently "active" key (the getMostRecentKey() method); each of these methods should run in constant time. 

# When a key / value pair is inserted or a key's value is retrieved, the key in question should become the most recent key. Also, the LRUCache class should store a maxSize property set to the size of the cache, which is passed in as an argument during instantiation. This size represents the maximum number of key / value pairs that the cache can hold at once. 

# If a key / value pair is added to the cache when it has reached maximum capacity, the least recently used ("active") key / value pair should be evicted from the cache and no longer retrievable; the newly added key / value pair should effectively replace it. Inserting a key / value pair with an already existing key should simply replace the key's value in the cache with the new value and should not evict a key / value pair if the cache is full. Attempting to retrieve a value from a key that is not in the cache should return the None (null) value.

# Sample input: (for an LRU Cache of size 3)

# insertKeyValuePair("a", 1)
# insertKeyValuePair("b", 2)
# insertKeyValuePair("c", 3)
# getMostRecentKey()
# getValueFromKey("a")
# getMostRecentKey()
# insertKeyValuePair("d", 4)
# getValueFromKey("b")
# insertKeyValuePair("a", 1)
# getValueFromKey("a")

# Output:

# -
# -
# -
# c
# 1
# a
# -
# None
# -
# 5

class LRUCache:
	def __init__(self, maxSize):
		self.cache = {}
		self.maxSize = maxSize or 1
		self.currentSize = 0
		self.listOfMostRecent = DoublyLinkedList()
		
	def insertKeyValuePair(self, key, value):
		if key not in self.cache:
			if self.currentSize == self.maxSize:
				self.evictLeastRecent()
			else:
				self.currentSize += 1
			self.cache[key] = DoublyLinkedListNode(key, value)
		else:
			self.replaceKey(key, value)
		self.updateMostRecent(self.cache[key])
			
	def getValueFromKey(self, key):
		if key not in self.cache:
			return None
		self.updateMostRecent(self.cache[key])
		return self.cache[key].value
		
	def getMostRecentKey(self):
		return self.listOfMostRecent.head.key
		
	def evictLeastRecent(self):
		keyToRemove = self.listOfMostRecent.tail.key
		self.listOfMostRecent.removeTail()
		del self.cache[keyToRemove]
		
	def updateMostRecent(self, node):
		self.listOfMostRecent.setHeadTo(node)
		
	def replaceKey(self, key, value):
		if key not in self.cache:
			raise Exception("Invalid case")
		self.cache[key].value = value

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def setHeadTo(self, node):
		if self.head == node:
			return
		elif self.head is None:
			self.head = node
			self.tail = node
		elif self.head == self.tail:
			self.tail.prev = node
			self.head = node
			self.head.next = self.tail
		else:
			if self.tail == node:
				self.removeTail()
			node.removeNode()
			self.head.prev = node
			node.next = self.head
			self.head = node
	
	def removeTail(self):
		if self.tail is None:
			return
		if self.tail == self.head:
			self.head = None
			self.tail = None
			return
		self.tail = self.tail.prev
		self.tail.next = None
		
		
class DoublyLinkedListNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None
		
	def removeNode(self):
		if self.next is not None:
			self.next.prev = self.prev
		if self.prev is not None:
			self.prev.next = self.next
		self.prev = None
		self.next = None
		
		
import unittest


letterMaps = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def testLruOfSize(size, testContext):
    # Instantiate cache and insert first key.
    lru = LRUCache(size)
    testContext.assertEqual(lru.getValueFromKey("a"), None)
    lru.insertKeyValuePair("a", 99)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 99)
    # Add existing key when cache isn't full.
    lru.insertKeyValuePair("a", 0)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 0)
    # Add keys until cache reaches maximum capacity.
    for i in range(1, size):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache isn't full.
        for j in range(0, i):
            letter = letters[j]
            testContext.assertEqual(lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), None)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(lru.getValueFromKey(currentLetter), letterMaps[currentLetter])
    # Add keys now that cache is at maximum capacity.
    for i in range(size, len(letters)):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache is full.
        for j in range(i - size, i):
            letter = letters[j]
            testContext.assertEqual(lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        leastRecentLetter = letters[i - size]
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), None)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(lru.getValueFromKey(currentLetter), letterMaps[currentLetter])
        testContext.assertEqual(lru.getValueFromKey(leastRecentLetter), None)
    # Add existing keys when cache is full.
    for i in range(len(letters) - size, len(letters)):
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), letterMaps[currentLetter])
        lru.insertKeyValuePair(currentLetter, (letterMaps[currentLetter] + 1) * 100)
        testContext.assertEqual(lru.getValueFromKey(currentLetter), (letterMaps[currentLetter] + 1) * 100)


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        testLruOfSize(1, self)

    def test_case_2(self):
        testLruOfSize(2, self)

    def test_case_3(self):
        testLruOfSize(3, self)

    def test_case_4(self):
        testLruOfSize(4, self)

    def test_case_5(self):
        testLruOfSize(5, self)

    def test_case_6(self):
        testLruOfSize(6, self)

    def test_case_7(self):
        testLruOfSize(7, self)

    def test_case_8(self):
        testLruOfSize(8, self)

    def test_case_9(self):
        testLruOfSize(9, self)

    def test_case_10(self):
        testLruOfSize(10, self)


if __name__ == "__main__":
	unittest.main()