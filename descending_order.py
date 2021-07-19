class Node:
    def __init__(self, data):
        self.item = data
        self.previous_node = None
        self.next_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None

    def get_head_node(self):
        return self.head_node

    def insert_in_empty_list(self, data):
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
        else:
            print("list is not empty!")

    def insert_at_end(self, data):
        n = self.head_node
        while n.next_node is not None:
            n = n.next_node
        new_node = Node(data)
        n.next_node = Node(data)
        new_node.previous_node = n

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next_node = self.head_node
        self.head_node.previous_node = new_node
        self.head_node = new_node

    def insert_when_smaller(self, data):
        new_node = Node(data)
        n = self.head_node
        prev_node = n
        while int(new_node.item) < int(n.item) and n.next_node is not None:
            prev_node = n
            n = n.next_node
        if n.next_node is None and int(n.item) >= int(new_node.item):
            new_node.next_node = None
            new_node.previous_node = n
            n.next_node = new_node
        else:
            new_node.next_node = n
            new_node.previous_node = prev_node
            n.previous_node = new_node
            prev_node.next_node = new_node

    def dll_to_descending_order_integer(self):
        aux = ""
        if self.head_node is None:
            print("List has no elements!")
            return
        n = self.head_node
        while n is not None:
            aux += str(n.item)
            n = n.next_node
        return int(aux)


def descending_order(num):
    dll = DoublyLinkedList()
    str_num = str(num)
    for index in range(len(str_num)):
        if index == 0:
            dll.insert_in_empty_list(str_num[0])
        else:
            if int(str_num[index]) >= int(dll.get_head_node().item):
                dll.insert_at_start(str_num[index])
            else:
                dll.insert_when_smaller(str_num[index])

    return dll.dll_to_descending_order_integer()