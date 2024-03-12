# x = 100
# for i in range(100,0,-1):
#     while x>i:
#         print(i, x)
#         x-=1


*_, (first, *rest) = [range(1,5)]*5

print(_)
print(first)
print(rest)

