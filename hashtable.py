from argparse import ArgumentError
from structures.LinkedList import MyLinkedList
from structures.RedBlackTree import MyRedBlackTree
from Person import *


class HashTableLinkedList:
    def __init__(self, table_size: int):
        self.size = table_size
        self.storage = [MyLinkedList() for _ in range(self.size)]

    def insert(self, key_person: Person, value):
        hash_code = key_person.generate_hashcode() % self.size
        self.storage[hash_code].append([key_person, value])  # Duplicates are possible

    def contain(self, key_person: Person):
        hash_code = key_person.generate_hashcode() % self.size
        linked_list = self.storage[hash_code]
        head = linked_list.head
        if head.data is not None:
            if head.data[0] is key_person:
                return True
            node = head
            while node.next_element is not None:
                node = node.next_element
                if node.data[0] is key_person:
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

    def insert(self, key_person: Person):
        data = key_person.generate_hashcode()
        node = self.storage.contains_node(data)
        if node is not None:
            node.key_value_pairs_list.append(key_person)
        else:
            self.storage.insert(data, key_person)

    def contain(self, key_person: Person):
        node = self.storage.contains_node(key_person.generate_hashcode())
        print(node.key_value_pairs_list.head.data)
        if node is not None:
            person_list = node.key_value_pairs_list
            if person_list.get_element_index(key_person) != -1:
                return True
        return False
