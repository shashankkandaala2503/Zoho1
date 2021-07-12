import ipaddress
def convert_method(ip4):
    while True:
       
        try:
            ip4 = ipaddress.IPv4Address(ip4)
        except ValueError:
            print("invalid ip address. Try, again")
       
        ans = bin(int(ip4))
        ans1 = hex(int(ip4))

        ans = ans[2:]
        bin_ans = ''
        for i in range(len(ans)):
            if i%8==0 and i!=0:
                bin_ans = bin_ans + '.' + ans[i]
            else:
                bin_ans += ans[i]

        ans1 = ans1[2:]
        hex_ans = ''
        for i in range(len(ans1)):
            if i%4==0 and i!=0:
                hex_ans = hex_ans + '.' + ans1[i]
            else:
                hex_ans += ans1[i]            
        print(bin_ans,hex_ans)

        return bin_ans,hex_ans


def convert_method2(ip4str, netmask ):

    while True:
       
        try:
            ip4 = ipaddress.IPv4Address(ip4str)
        except ValueError:
            print("invalid ip address. Try, again")
        else:
            break 
   

    x=sum(bin(int(x)).count('1') for x in netmask.split('.'))
    ip4str= ip4str+'/'+str(x)
    print(ip4str)

    return ip4str

def convert_method1(ip, mask):
    ipv4 = ip
    while True:
       
        try:
            ipv4 = ipaddress.IPv4Address(ip)
        except ValueError:
            print("invalid ip address. Try, again")
        else:
            break 
    
    network = ''
    iOctets = ip.split('.')
    mOctets = mask.split('.')
    network = str( int( iOctets[0] ) & int(mOctets[0] ) ) + '.'
    network += str( int( iOctets[1] ) & int(mOctets[1] ) ) + '.'
    network += str( int( iOctets[2] ) & int(mOctets[2] ) ) + '.'
    network += str( int( iOctets[3] ) & int(mOctets[3] ) )
    print(network)

    return network
        