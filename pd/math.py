dont_want = [24, 32.5, 43, 45, 66, 80, 83, 102.5, 108, 121, 136, 138, 157, 256, 269, 349, 415, 523, 618.5, 659, 762, 764.5]
my_list = [807, 830.5, 938.5, 988, 1109, 1141, 1182.5, 1397, 1421, 1480, 1523, 1569, 1637.5, 1818.5, 2096.5, 2250, 2538, 2877, 3003, 3184.5]
my_new_list = []
for item1, item2 in zip(my_list, my_list[1:]):
		new_item = item1 + item2
		my_new_list.append(new_item)
print(my_new_list)

my_new_list2 = []
for item1, item2 in zip(my_new_list, my_new_list[1:]):
		new_item = item1 + item2
		my_new_list2.append(new_item)
print(my_new_list2)

my_new_list3 = []
for item1, item2 in zip(my_new_list2, my_new_list2[1:]):
		new_item = item1 + item2
		my_new_list3.append(new_item)
print(my_new_list3)