from paramiko_ssh import qytang_ssh

if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'python Simple_SSH_Client -i ipaddress -u username -p password -c command'

    parser = ArgumentParser(usage=usage)

    parser.add_argument('-i','--ipaddress',dest='ipaddress',help='SSH Sever',default='192.168.220.129',type=str)
    parser.add_argument('-u','--username', dest='username', help='SSH Username', default='root', type=str)
    parser.add_argument('-p','--password', dest='password', help='SSH Password', default='Cisc0123', type=str)
    parser.add_argument('-c','--command', dest='command', help='Shell Command', default='ls', type=str)

    args = parser.parse_args()

    print(qytang_ssh(args.ipaddress,args.username,args.password,cmd=args.command))