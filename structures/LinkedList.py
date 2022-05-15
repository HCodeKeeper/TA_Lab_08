from .ICollection import ICollection


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next_element = None


class MyLinkedList(ICollection):

    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, data):
        if self.head is None:
            self.head = LinkedListNode(data)
            self.count += 1
            return

        current_el = self.head

        while current_el.next_element is not None:
            current_el = current_el.next_element
        current_el.next_element = LinkedListNode(data)
        self.count += 1

    def prepend(self, data):
        new_head = LinkedListNode(data)

        new_head.next_element = self.head
        self.head = new_head
        self.count += 1

    def add_middle(self, position, data):
        if position >= self.count or position < 0:
            return "Position can not be less and equal or more and equal than length of the list"

        if position == 0:
            self.prepend(data)
            return
        elif position == self.count:
            self.append(data)

        if self.head is None:
            self.head = LinkedListNode(data)
            return

        current_el = self.head
        local_count = 0
        while local_count < position - 1:
            current_el = current_el.next_element
            local_count += 1
        new_node = LinkedListNode(data)
        new_node.next_element = current_el.next_element
        current_el.next_element = new_node
        self.count += 1

    def delete_start(self):
        if self.head is None:
            return
        self.head = self.head.next_element
        self.count -= 1

    def delete_end(self):
        if self.head is None:
            return

        current_el = self.head

        while current_el.next_element.next_element is not None:
            current_el = current_el.next_element
        current_el.next_element = None
        self.count -= 1

    def delete_middle(self, position):
        if position >= self.count or position < 0:
            return "Position can not be less and equal or more and equal than length of the list"

        if position == 0:
            self.delete_start()
            return
        elif position == self.count:
            self.delete_end()

        if self.head is None:
            return

        current_el = self.head
        local_count = 0
        while local_count < position - 1:
            current_el = current_el.next_element
            local_count += 1
        current_el.next_element = current_el.next_element.next_element
        self.count -= 1

    def print_list(self):
        current_el = self.head
        print(current_el.data)
        while current_el.next_element is not None:
            current_el = current_el.next_element
            print(current_el.data)

    def get_element_index(self, value):
        if self.head is None:
            return

        local_index = 0
        current_el = self.head
        while current_el.next_element is not None:
            if current_el.data == value:
                return local_index
            current_el = current_el.next_element
            local_index += 1
        return -1
