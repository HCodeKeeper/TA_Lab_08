import random
import time

from Person import Person
from hashtable import HashTableLinkedList, HashTableBT

c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
     'w', 'x', 'y', 'z']
names = []
for i in range(5000):
    name = ""
    name += c[random.randrange(0, len(c))].upper()
    for j in range(random.randrange(2, 12)):
        name += c[random.randrange(0, len(c))]
    names.append(name)
print("added names")
arr = []
# codes = []
for i in range(200000):
    arr.append(Person(names[random.randrange(1, len(names))], names[random.randrange(1, len(names))]))
    # codes.append(arr[i].generate_hashcode())

# table = HashTableLinkedList(250000)

table = HashTableBT()
time1 = time.perf_counter()
for i in range(1000):
    table.insert(arr[i])
time2 = time.perf_counter()
print((time2 - time1) * 1000)


for i in range(500, 1000):
    table.contain(arr[i])

#
# pers = Person("Danilo", "Berkovskyi")
# table.insert(pers, 1001)
# print("added in table")
# print(table.contain(pers))