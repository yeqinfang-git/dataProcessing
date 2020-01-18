l1 = ["1"]
# l1 = l1[:] if
l2 = ["key",{}]
l3 = l1 + l2
print(l3)
# list2 = ["1", "2", "3", "{1}" ]
# print(list2[0:-1])
print('.'.join(l3[0:-1]), ':', l3[-1])