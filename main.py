import json

class Host:
    def ___init___(self, hostName, certPath = None):
        self.name = hostName
        self.cert = certPath

#Take in a list of hosts, output it to a file name "hosts" in the execution directory.
def output_hosts(hostList):
    hostFile = open("hosts", "w")

    for i in hostList:
        hostFile.write(i + "\n")

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
            hosts.append(j['attributes']['private_dns'])

output_hosts(hosts)

stateFile.close()