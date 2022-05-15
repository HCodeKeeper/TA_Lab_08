from argparse import ArgumentError
from structures.LinkedList import MyLinkedList
from structures.RedBlackTree import MyRedBlackTree
from Person import *

class HashTableLinkedList:
    def __init__(self, table_size:int):
        self.size = table_size
        self.storage = [MyLinkedList() for _ in range(self.size)]

    def insert(self, key_person: Person, value):
        hash_code = key_person.generate_hashcode() % self.size
        self.storage[hash_code].append([key_person, value]) #Duplicates are possible

    def contain(self, key_person: Person):
        hash_code = key_person.generate_hashcode % self.size
        linked_list = self.storage[hash_code]
        head = linked_list.head
        if head.data != None:
            if head.data[0] == key_person:
                return True
            node = head
            while node.next != None:
                node = node.next_element
                if node.data[0] == key_person:
                    return True
        return False

    def update_size(self, new_size: int):
        if new_size < len(self.storage) and new_size >= 0:
            self.storage = self.storage[:new_size]
        elif new_size > len(self.storage):
            [self.storage.append(None) for _ in range(new_size - self.size)]
        else:
            raise ArgumentError(None, "Exception! Tried to extend size with a negative number")


class HashTableBT:
    def __init__(self):
        self.storage = MyRedBlackTree()

    #Unhandled Collsions
    
    def insert(self, key_person: Person, value):
        data = key_person.generate_hashcode()
        data.value = value
        self.storage.insert(data)

    #searches only for hashcode
    def contain(self, key_person: Person):
        return self.storage.contains(key_person.generate_hashcode())

