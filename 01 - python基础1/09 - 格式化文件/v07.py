import json

# 这里student是一个dict格式内容，不是json
student = {
    "name":"lishasa",
    "age":"20",
    "QQ":"1670350470"
}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象: “{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)