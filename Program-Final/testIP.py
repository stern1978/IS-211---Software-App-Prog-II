import ipaddress

a = ipaddress.ip_network('192.168.0.1')
b = ipaddress.ip_interface('192.168.0.1/24')
print(a,b)
reserved = {'192.168.0.1'}

hosts_iterator = (host for host in a.hosts() if str(host) not in reserved)
for hosts in hosts_iterator:
    print (host)
