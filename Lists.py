
item1= "bread"
item2= "pasta"
item3= "fruits"
items= ["bread","pasta","fruite","vegies"]
print(items)
print(items[0])
print(items[2])

items[0]='chips'
print(items)

print(items[0:2])
print(items[-1])

items= ["bread","pasta","fruite","vegies"]
items.append("butter")
print(items)

items= ["bread","pasta","fruite","vegies"]
print(items)
items.insert(1,'butter')
print(items)


food= ["bread","pasta","fruits"]
bathroom= ["shampoo","soap"]
items=food+bathroom
print(items)

print(len(items))

a="pasta" in items
print(a)