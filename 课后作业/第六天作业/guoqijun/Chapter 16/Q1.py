from scapy_ping_one_new import scapy_ping_one
from multiprocessing.pool import ThreadPool
import ipaddress


def ping_scan(network):
    pool = ThreadPool(processes=150)
    net = ipaddress.ip_network(network)

    result_obj_dict = {}

    for ip in net:
        result_obj = pool.apply_async(scapy_ping_one, args=(str(ip),))
        result_obj_dict[str(ip)] = result_obj

    pool.close()
    pool.join()

    active_ip = []

    for ip, obj in result_obj_dict.items():
        if obj.get()[1] == 1:
            active_ip.append(ip)

    return active_ip


if __name__ == '__main__':
    import datetime
    import pickle

    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d_%H-%M-%S")
    scan_file_name = 'scan_save_pickle_' + otherStyleTime + '.pl'
    scan_file = open(scan_file_name, 'wb')
    pickle.dump(ping_scan('192.168.2.0/24'), scan_file)
    scan_file.close()
    scan_file = open(scan_file_name, 'rb')
    scan_result_list = pickle.load(scan_file)
    print(scan_result_list)