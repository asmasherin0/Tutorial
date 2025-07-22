# import json
# json_str='{"name":"abc","age":1}'
# a=json.loads(json_str)
# print(a["name"])
# print(a)
# print(a["age"])



# import json
# person={"name":"abc","age":1}
# json_str=json.dumps(person)
# print(json_str)

# import json
# with open('data.json','r')as file:
#     content=json.load(file)
#     print(content)


# import json
# book={"name":"abc","num":10}
# a=json.dumps(book)
# print(a)


# import json
# book={"name":"abcd","num":10}
# s=json.dumps(book)
# with open("C:\\Users\\Administrator\\Desktop\\gal\\abc\\qweee.txt",'r') as file:
#     file.write(s)


import json
book='{"name":"abcd","num":10}'
print(type(book))
a=json.loads(book)
with open("data.json", "w") as file:
    json.dump(a,file)









































