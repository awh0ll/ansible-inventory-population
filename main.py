import json

class Host:
    def __init__(self, hostName, certPath = None):
        self.name = hostName
        self.cert = certPath

#Take in a list of hosts, output it to a file name "hosts" in the execution directory.
def output_hosts(hostList):
    hostFile = open("hosts", "w")

    for i in hostList:
        temp = [i.name]
        if i.cert is not None:
            temp.append("ansible_ssh_private_key_file=" + i.cert)
        
        hostFile.write(" ".join(temp) + "\n")

    hostFile.close()

stateFile = open('test.tfstate')
data = json.load(stateFile)

#ansible hosts
hosts = []

#Iterate through the resources in tfstate
for i in data['resources']:
    #We only care about AWS instances
    if i['type'] == "aws_instance":
        for j in i['instances']:
            hosts.append(Host(j['attributes']['private_dns']))

output_hosts(hosts)
print(hosts)

stateFile.close()
