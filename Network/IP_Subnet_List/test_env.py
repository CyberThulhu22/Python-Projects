addr = [132, 32, 55, 56]
sublist = []

def netClass(ipaddr=addr[0]):
    if ipaddr in range(1,128):
    	return int(8)
    elif ipaddr in range(128,192):
    	return int(16)
    elif ipaddr in range(192,224):
    	return int(24)
    elif ipaddr in range(224,240):
    	return None
    elif ipaddr in range(240,255):
    	return None
        

cidr = netClass()
for ea in range(cidr,33):
    mask = [( ((1<<32)-1) << (32-ea) >> i ) & 255 for i in reversed(range(0, 32, 8))]
#    print(mask)

    netw = [addr[i] & mask[i] for i in range(4)]
            
#    print("Address: {0}".format('.'.join(map(str, addr))))
    if "{0}".format('.'.join(map(str, netw))) not in sublist:
        sublist.append("{0}".format('.'.join(map(str, netw))))

for ip in sublist:
    print("{0}".format(ip))
