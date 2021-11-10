import json

#Open yer file
f = open('test.tfstate')

data = json.load(f)

for i in data['resources']:
    if i['type'] == "aws_instance":
        for j in i['instances']:
            print(j['attributes']['private_dns'])
    # for j in i['instances']:
    #     if "tags" in j['attributes']:
    #         print(j['attributes']['tags'])
    #     # if j['tags_all']['Managed'] == "Ansible":
    #     #     print("yaaa")
    #     # print(i['name'])

#print(data)

f.close()