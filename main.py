import json

#Open yer file
f = open('test.tfstate')

data = json.load(f)

#ansible hosts
hosts = []

for i in data['resources']:
    if i['type'] == "aws_instance":
        for j in i['instances']:
            hosts.append(j['attributes']['private_dns'])
    # for j in i['instances']:
    #     if "tags" in j['attributes']:
    #         print(j['attributes']['tags'])
    #     # if j['tags_all']['Managed'] == "Ansible":
    #     #     print("yaaa")
    #     # print(i['name'])

print(hosts[0])

f.close()