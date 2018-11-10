#for x in range(10,20):
#    print(x)

#words = ["Peanut","Butter","Jelly","Time","Is","Now"]
#for word in words:
#    print(word)

random_list = ["A",1,"Hello",4.5]
#for x in random_list:
#    print(x,type(x))

for i in range(len(random_list)):
    print(i,random_list[i],type(random_list[i]))

new_list = []

new_list.append("A")
new_list.append("1")
new_list.append("Hello")
new_list.append("4.5")

print(new_list)

new_list.remove("4.5")

print(new_list)

new_list.pop(-1)

print(new_list)

print(new_list.index("A"))