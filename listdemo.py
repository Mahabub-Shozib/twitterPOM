
#
# def storeValues(list):
#     length = len(list)
#     for i in range(length):
#         print(list[i])
#
# followList = []
# total = int(input("Enter the length of list: "))
# print("Write followers name: ")
# for i in range(total):
#     followers = str(input())
#     followList.append(followers)
# print(followList)
# storeValues(followList)

name = "@TamaraWhitee"
print('Follow '+str(name))

l = "//div[@aria-label='Follow "+name+"']"
print(l)