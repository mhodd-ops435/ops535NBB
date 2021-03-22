# Authors: Mackenzie Hodd, Justin Stewart
# all credit goes to Justin Stewart
import sys
file_Location = 'C:\\Users\\Mackenzie\\Documents\\test.txt' #Enter your file path here. You'll have to edit the slash direction if you running on linux
nmclicmds = ['nmcli con modify ens192 +ipv4.routes 192.168.1.0/24 172.20.1.1 100','nmcli con modify ens192 +ipv4.routes 192.168.2.0/24 172.20.2.1 100','nmcli con modify ens192 +ipv4.routes 192.168.3.0/24 172.20.3.1 100']
restartCmds = ['nmcli con down ens192', 'nmcli con up ens192']
count = 3
netnum = 0
while True:
    newstring = 'nmcli con modify ens192 +ipv4.routes 192.168.' + str(count) + '.0/24 172.20.' + str(count) + '.1 100'
    nmclicmds.append(newstring)
    count = count + 1
    if count == 44:
        break

r = open(file_Location, 'w')
for item in nmclicmds:
    newline = item + '\n'
    r.write(newline)
for cmds in restartCmds:
    lines = cmds + '\n'
    r.write(lines)
r.close()

print("Done")
