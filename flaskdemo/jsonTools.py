import json


if __name__ == '__main__':
    with open("package.json",'r',encoding='utf-8') as f:
        # 得到继承关系树字典
        jsonDict = json.loads(f.read())
        print(jsonDict)
