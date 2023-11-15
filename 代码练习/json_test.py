import json

# 列表转json
mylist = [{"name": "张三", "age": 13}, {"name": "李四", "age": 18}, {"name": "王五", "age": 14}]

my_json1 = json.dumps(mylist, ensure_ascii=False)
print(type(my_json1))
print(my_json1)

# 字典转json
myset = {"name": "张三", "age": 13}
my_json2 = json.dumps(myset, ensure_ascii=False)
print(type(my_json2))
print(my_json2)

# json字符串转列表
l=json.loads(my_json1)
print(type(l))
print(l)
l=json.loads(my_json2)
print(type(l))
print(l)

