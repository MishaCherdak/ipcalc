import ipaddress

IP = input('ip: ')
MASK = input('mask: ')

host = ipaddress.IPv4Address(IP)
net = ipaddress.IPv4Network(IP + '/' + MASK, False)
print('IP:', IP)
print('Mask:', MASK)
print('Subnet:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Host:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Broadcast:', net.broadcast_address)
