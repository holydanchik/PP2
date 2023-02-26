import json
s=open('C:/Users/tuzel/OneDrive/Рабочий стол/only/pp2/lab4/json/sample-data.json','r')
okay=s.read()
obj=json.loads(okay)
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for i in range(len(obj["imdata"])):
    dn=(obj["imdata"][i]['l1PhysIf']["attributes"]["dn"])
    description=(obj["imdata"][i]['l1PhysIf']["attributes"]["descr"])
    speed=(obj["imdata"][i]['l1PhysIf']["attributes"]["speed"])
    mtu=(obj["imdata"][i]['l1PhysIf']["attributes"]["mtu"])
    print("{:<49}{:<23}{:<7}  ".format(dn,description,speed), mtu )