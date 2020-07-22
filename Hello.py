# print('Hello')
# new = 10
# print(f'hello {new}')
# number = int(input("Enter a Number"))
# if number > 12:
#     print(f"Number is Greter tham 12")

# name = "Jonny"
# age = 45
#
# print('Hi '+name +',You are ' + str(age )+ ' old.')

# print(f'Hi {name}, you are {age} year\'s old')


# #String Index
# name_index = '812345'
# # [start:stop:stepover]
# print(name_index[::-1])


# # Boolean
# print(bool(1))
# print(bool(0))
# print(bool("Name"))
# print(bool(""))
# print(bool())
# print(bool(12))


# # 25.Excercise Password Checker
# user_name = input('What is your name???')
# password = input('What is your password???')
# pass_length = len(password)
# hidden_password = '*' * pass_length
# print(f'Your Username is {user_name} & Your password {hidden_password} is {pass_length}  character long.')


# # 26.Lists
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = [1,'a', 1.2, True]
# print(list3)


# # 27. List_Slicing
# amazon_cart = [
#     'notebooks',
#     'pen',
#     'toys',
#     'sunglasses',
#     'mobile',
#     'mouse',
#     'computer',
#     'gaps',
#     'apple',
#     'orange',
#     'guava'
# ]
# # print(amazon_cart[-2:2:-3])
# amazon_cart[0] = 'laptop'
# # print(amazon_cart[0:3])
#
# # new_cart = amazon_cart     #not copy ,Direct move.
# new_cart = amazon_cart[:]  #Copy list
# new_cart = amazon_cart.copy()  #Copy list
# new_cart[0] = 'desktop'
# print(new_cart)
# print(amazon_cart)

# # 28. Matrix
# matrix= [
#     [2,3,4,7],
#     [5,7,8],
#     [6,8,0]
# ]
# print(matrix[0][::-1])
# print(len(matrix[0]))

# # 29.List Method
# basket = [2,3,4,5,6,5,2,0,5,9,1]
# # basket.append(33)  ##Aded Data
# # basket.insert(2,55) ##inserting Data
# # basket.extend([122,456]) ##Extending Data
#
# # basket.pop()   ##Remove last Data or select index number
# # basket.remove(6)  ##Remove Direct provide value not index
# # basket.clear() #Clear total list

# print(basket.index(3))  #Find index number any Number or String
# print(basket.index(3,0,3))  ##Find index number on select start and stop range
# print(3 in basket)                              ##Output True or False value
# print("i" in "Find any number or character.")   ##Output True or False value
# print(basket.count(5))       ##Counting number
# #Basket.sort()  ##Sort direct list
# print(sorted(basket)) ## Dos'nt modified main list
# basket.reverse()  ## Reverse List
# print(basket)


# print(list(range(30)))

# sentence = "!"
# new_sentence = sentence.join(["Hello","How are you???"])
# print(new_sentence)

# # # List Unpacking
# a,b,c ,*other,d,e= [3,4,7,2,8,1,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)
# print(e)


# # # Dictionary # # #
#
#
#
# user = {
#     'basket': [1, 3, 5],
#     'greet': 'hello',
#     'age': 20
# }
# print(user['basket'])
# print(user.get('age',55))  # # here 55 is default value , user.get method didn't through err ,it passed None.

# user2 = dict({'basket': [1, 4, 7], 'age': 45})  # # Declare another style Dictionary
# print(user2)
#
# print('basket' in user)
# print('basket' in user.keys())  # # Search keys on  Dictionary #Through True or False
# print('basket' in user.value())  # # Search value on Dictionary #Through True or False
# print(user.item())  # # Returns  Dictionary item as a list(Tuple)
# user.clear() , # user.copy()
# print(user.update({'age' : 54}))  # # Update user age value


# # #  Tuples  # # #
#
#
# my_tuple = (2, 1, 2, 3, 5, 6)  # One kind of list But Immutable
# print(my_tuple)
# print(5 in my_tuple)
# print(sorted(my_tuple))
# new_tuple = my_tuple[1:5:2]  # # start: end: stepover
# print(new_tuple)
#
# x, y, z, *other = 1, 5, 3, 7, 5, 2, 4, 8
# print(other)


# # #  Sets # # #
#
#
# my_set = {3, 2, 5, 6, 21, 3, 4, 7}   # # Set is a unordered collection of object
# print(my_set)
# my_set.add(41)
# print(my_set)
# print(1 in my_set)
# print(len(my_set))
# print(list(my_set))
# new_set = my_set.copy()
# new_set.add(45)
# print(new_set)
#
#
# set_one = {1, 2, 3, 4, 5}
# set_two = {2, 4, 5, 6, 7, 9, 9, 5, 34, 56}
#
# print(set_one.difference(set_two))  # A/B
#
# set_one.discard(5)  # # Remove an item and modified  set_one directly
# print(set_one)
#
# set_one.difference_update(set_two) # # difference and new set return
# print(set_one)
#
# print(set_one.intersection(set_two))
#
# print(set_one.isdisjoint(set_two)) # # Check it separate set or disparate
# print(set_one.issubset(set_two))
# print(set_one.issuperset(set_two))
# print(set_one.union(set_two))


# # # Conditional logic # # #
#
#
# is_old = False
# is_licenced = True
#
# if is_old:
#     print('You are old enough to drive!')
# elif is_licenced:
#     print('You can drive now!')
# else:
#     print('checkCheck')
#
# # # Ternary Operator # # #
# condition_if_true if condition else condition if_False
#
# is_friend = True
# can_message = 'Message allowed' if is_friend else 'Not allowed to message'
# print(can_message)


# # # String to Binary
# byte_array = input('Enter Your Name : ').encode()
# binary_int = int.from_bytes(byte_array, "big")
# binary_string = bin(binary_int)
# print(binary_string)

# # # Loops # # #
#
#
# for item in 'Hello python!!!':
#     print(item)
#
# for number in [1, 2, 3, 4, 5]:
#     for item in ['a', 'b', 'c']:
#         print(number, item)
#
# user = {
#     'name': 'Sohan',
#     'age': 23,
#     'can_swim': True
# }
# for item in user.items():  # # item in user return only keys but use user.items() returns tuples
#     print(item)
# for item in user.values():  # # item in user return only keys but use user.values() returns value
#     print(item)
# for item in user.keys():  # # item in user return only keys but use user.keys() returns keys
#     print(item)
# for key, value in user.items():
#     print(f'{key} : {value}')
#
# # Counter  # #
#
# my_list = list(range(11))
# print(my_list)
# counter = 0
# for item in my_list:
#     counter = counter+item
# print(counter)

# # enumerate()     # # enumerate function returns index and value
# for i, char in enumerate('hello'):
#     print(i, char)


# # While loops # #
#
# i = 0
# while i < 10:
#     # print(i)
#     i += 1
#     print(i)
# else:
#     print('Done with all the work')
#
# my_list = ['a', 'b', 'c']
# for item in my_list:  # for loops
#     print(item)
#
# i = 0
# while i < len(my_list):  # while loops
#     print(my_list[i])
#     i += 1
#
# while True:
#     response = input('Say something : ')
#     if response == 'bye':
#         break


# # # *args & **kwargs
# def super_func(*args, **kwargs):
#     print(args)  # # args returns tuples
#     print(*args)  # # return Passing arg value
#     print(kwargs)  # # kwargs returns Dictionary
#     print(kwargs.values())  # # kwargs returns Dictionary
#
#
# print(super_func(2, 3, 54, name='sohan', age=33))


# # CLASS
#
# class PlayerCharecter:
#
#     def __init__(self, uname, age):
#         self.name = uname
#         self.aged = age
#
#     def run(self):
#         print('run')
#         return 'done'
#
#
# player1 = PlayerCharecter('Harry', 34)
# player2 = PlayerCharecter('Sohan', 45)
# print(player1.run())
# print(player2.aged)


# # # List , set & Dictionary comprehension  # # Short terms for loops
# new_list = []
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         new_list.append(i)
#
# print(new_list)
#
# new_list2 = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
# print(new_list2)
# new_set = {i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0}
# print(sorted(new_set))
#
# my_dict = {
#     'a': 1,
#     'b': 2
# }
#
# new_dict = {k:v * 2 for k,v in my_dict.items()}
# print(new_dict)


# # # Pure Function  # *Every time same result *No side effect
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list
#
#
# print(multiply_by2([2, 3, 4]))


# # # Map Function
# my_list = [2, 3, 5]
#
#
# def multiply_by2(item):
#     return item * 2
#
#
# print(list(map(multiply_by2, my_list)))
# print(my_list)

# # # Filter Function
# my_list = [2, 3, 4, 5, 6, 7, 6, 3, 9]
#
#
# def check_odd(item):
#     return item % 2 != 0
#
#
# print(list(filter(check_odd, my_list)))
# print(my_list)


# # # Zip Function
#
# list_one = [2,54,7,5,4]
# list_two = [3,4,6,2,9]
# list_three = (5,6,7,3,2)
# print(list(zip(list_one,list_two,list_three)))

# # # Reduce Function
#
# from functools import reduce
#
# my_list = [1, 2, 3]
#
#
# def accumulator(acc, item):
#     return acc + item
#
#
# print(reduce(accumulator, my_list, 10))


# # # Generator function
#
# def generator_function(num):
#     for i in range(num):
#         yield i
#
# for temp in generator_function(1000000000000000000000):
#     print(temp)


# # # Lambda Expression
#
# my_list = [3, 5, 1]
# new_list = list(map(lambda num: num ** 2, my_list))
# print(new_list)


# # # Regular expression
#
# import re
# # string = 'Search this inside of this text please!'
# # a = re.search('this',string)
# # print(a.start())
# # print(a.group())
# #
# search = input('Enter Your Word : ')
# pattern = re.compile(search) # #
# # pattern = re.compile(r"(^[a-zA-Z0-9$#@!])")  # # Regex
# string = 'Search this inside of this text please!'
#
# a = pattern.search(string)
# b = pattern.findall(string)  # # Return match and list
# c = pattern.fullmatch(string)  # # Match full
# d = pattern.match(string)  # # match 0 to . . .
# print(d)

# class Node:
#     def __init__(self, value):
#         self.next = None
#         self.prev = None
#         self.val = value
#
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def add(self, val):
#         node = Node(val)
#         if self.tail is None:
#             self.head = node
#             self.tail = node
#             self.size += 1
#         else:
#             self.head.next = node
#             node.prev = self.head
#             self.tail = node
#             self.size += 1
#
#     def __str__(self):
#         vals = []
#         while node is not None:
#             vals.append(node.val)
#             node = node.next
#         return f'[{}]'
#
#
# my_list = DoubleLinkedList

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # # #

# # # Single Linked List
#
class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print('List is empty')
            return
        else:
            print('List is : ')
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print('Numbers of nodes in the list = ', n)

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, ' is at position ', position)
                return True
            position += 1
            p = p.link
        else:
            print(x, ' not found in list')
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input('Enter the number of Nodes : '))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        pass

    def insert_before(self, data, x):
        pass

    def insert_at_position(self, data, k):
        pass

    def delete_node(self):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self, listStart):
        pass

    def _divide_list(self, p):
        pass


# #######################################################################
#
# n_list = SingleLinkedList()
# print(n_list.display_list())
# print(n_list.count_nodes())
# print(n_list.search(7))

n_list = SingleLinkedList()
# n_list.create_list()

while True:
    print('1. Display List')
    print('2. Count the Number of Nodes')
    print('3. Search for an element')
    print('4. Insert the empty list')
    print('5. Insert a node at the end of the list')
    print('6. Insert a Node after a specified node')
    print('7. Insert a Node Before a specified node')
    print('8. Insert a Node at a given position')
    print('9. Delete first node')
    print('10. Delete last node')
    print('11. Delete any node')
    print('12. Reverse the list')
    print('13. Bubble sort by exchanging data')
    print('14. Bubble sort by exchanging links')
    print('15. Merge sort')
    print('16. Insert cycle')
    print('17. Detect cycle')
    print('18. Remove cycle')
    print('19. Quit')

    option = int(input('Enter Your Choice : '))
    if option == 1:
        n_list.display_list()
    elif option == 2:
        n_list.count_nodes()
    elif option == 3:
        data = int(input('Enter the element to be search : '))
        n_list.search(data)
    elif option == 4:
        data = int(input('Enter the element to be inserted : '))
        n_list.insert_in_beginning(data)
    elif option == 5:
        data = int(input('Enter the element to be inserted : '))
        n_list.insert_at_end(data)
    elif option == 6:
        data = int(input('Enter the element to be inserted : '))
        x = int(input('Enter the element after which to insert : '))
        n_list.insert_after(data, x)
    elif option == 7:
        data = int(input('Enter the element to be inserted : '))
        x = int(input('Enter the element before which to insert : '))
        n_list.insert_before(data, x)
    elif option == 8:
        data = int(input('Enter the element to be inserted : '))
        x = int(input('Enter the position which to insert : '))
        n_list.insert_at_position(data, x)
    elif option == 9:
        n_list.delete_first_node()
    elif option == 10:
        n_list.delete_last_node()
    elif option == 11:
        data = int(input('Enter the element to be deleted : '))
        n_list.delete_node(data)
    elif option == 12:
        n_list.reverse_list()
    elif option == 13:
        n_list.bubble_sort_exdata()
    elif option == 14:
        n_list.bubble_sort_exlinks()
    elif option == 15:
        n_list.merge_sort()
    elif option == 16:
        data = int(input('Enter the element at which the cycle has to be inserted : '))
        n_list.insert_cycle(data)
    elif option == 17:
        if n_list.has_cycle():
            print('List has a cycle.')
        else:
            print('List does not have a cycle.')
    elif option == 18:
        n_list.remove_cycle()
    elif option == 19:
        break
    else:
        print('Wrong Option. Please try right Option.')
print()
