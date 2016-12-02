import json

filename = "sample.json"
fh = open(filename,"r")
data = fh.read() #fetch data from link

# print data
data = data.replace("true","True")
data = data.replace("false","False")

# print data
dict_data = eval(json.loads(json.dumps(data)))

#1

# print dict_data["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["application"]["service"][0]["protocol"]
dict_data["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["application"]["service"][0]["protocol"] = "udp"


#2
# print dict_data["vnics"]["vnics"][2]["portgroupName"]
dict_data["vnics"]["vnics"][2]["portgroupName"] = "EXT_VLAN_201b"

#3
# print dict_data["featureConfigs"]["features"][5]["ospf"]["enabled"]
dict_data["featureConfigs"]["features"][5]["ospf"]["enabled"] = True

#4
print len(dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"])
for i in range(len(dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"])):
    # print dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i]["holdDownTimer"]
    # print dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i]["keepAliveTimer"]
    dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i]["holdDownTimer"] +=dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i]["keepAliveTimer"]
    # print dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i]["holdDownTimer"]

fh.close()

fh = open(filename,"w")
fh.write(str(dict_data))
fh.close()

