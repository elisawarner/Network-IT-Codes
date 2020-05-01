import os
import re
import getpass

cmd = "scutil --dns | grep 'nameserver\[[0-9]*\]'"
cmd2 = "ipconfig getifaddr en0"

# Get DNS address
result = os.popen(cmd).read().strip()
DNS_address = re.findall('\d+.\d+.\d+.\d+',result)[0]
IP_address = os.popen(cmd2).read().strip()

print('IP:',IP_address)
print('DNS:',DNS_address)

password = getpass.getpass()
cmd = "echo %s | sudo -S tcpdump -i en0 -n host %s and port 53 -v | grep %s" % (password, DNS_address, IP_address)
cmd = os.system(cmd)

result_dict = {}
fhnd = open('history_concat.txt','w')
with open('history.txt') as f:
	packets = f.readlines()
	for p in packets:


		result = re.findall('[a-z]+\.[a-z.]+',p)

		if result:
			result_dict[result[0]] = result_dict.get(result[0], 0) + 1


keys = sorted(result_dict.keys(), key=lambda key : result_dict[key], reverse=True)

for key in keys:
	fhnd.write(key + ' ' + str(result_dict[key]) + '\n')
fhnd.close()

print("Complete.")
cmd = 'less history_concat.txt'
os.system(cmd)