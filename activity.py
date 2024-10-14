products = [
{
"id": 1,
"name": "IPHONE 13",
"category": "Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 2,
"name": "IPHONE 15",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 3,
"name": "IPHONE 16",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
}
]
print(products)
products[2]["name"] = "IPHONE 16 PROMAX"


#TODO ACCESS STOCK OF products[2]

print("Product[2] stocks:", products[2]["stock"])

#TODO ACCESS INDEX 3 STOCK OF products[2]
#sir 2 index(2 dictionary) lang po ung nasa stock :3

print("Product[2] index 2 of stocks:", products[2]["stock"][1])

#TODO CHANGE black small quantity - products[2]

products[2]["stock"][1]["black-small"] = 10

print("New Stock of Product[2] black-small:", products[2]["stock"][1]["black-small"])