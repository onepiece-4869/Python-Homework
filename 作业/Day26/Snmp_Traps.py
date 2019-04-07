#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from GET_IP_netifaces import get_ip_address
from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
import pprint


def analysis(info):
    if '1.3.6.1.2.1.14.10.1.6' in info.keys():
        if info['1.3.6.1.2.1.14.10.1.6']['integer-value'] == '1':
            print('OSPF Neighbor {0} down'.format(info['1.3.6.1.2.1.14.10.1.1']['ipAddress-value']))
        elif info['1.3.6.1.2.1.14.10.1.6']['integer-value'] == '8':
            print('OSPF Neighbor {0} full'.format(info['1.3.6.1.2.1.14.10.1.1']['ipAddress-value']))
    # print(info)


def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(wholeMsg, asn1Spec=pMod.Message(),)
        print('Notification message from %s:%s ' % (transportDomain, transportAddress))
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                print('Enterprise: %s' % pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint())
                print('Agent Address: %s' % pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint())
                print('Generic Trap: %s' % pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint())
                print('Specific Trap:  %s' % pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint())
                print('Uptime: %s' % pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint())
                varBinds = pMod.apiTrapPDU.getVarBindList(reqPDU)
            else:
                varBinds = pMod.apiPDU.getVarBindList(reqPDU)

            result_dict = {}
            for x in varBinds:
                result = {}
                for x, y in x.items():
                    # print(x, y)
                    if x == 'name':
                        id = y.prettyPrint()
                    else:
                        bind_v = [x.strip() for x in y.prettyPrint().split(':')]
                        print(bind_v)
                        for v in bind_v:
                            if v == '_BindValue':
                                next
                            else:
                                result[v.split('=')[0]] = v.split('=')[1]
                result_dict[id] = result
            analysis(result_dict)
    return wholeMsg


def snmp_trap_receiver(ifname, port=162):
    if_ip = get_ip_address(ifname)
    transportDispatcher = AsynsockDispatcher()
    transportDispatcher.registerRecvCbFun(cbFun)

    transportDispatcher.registerTransport(udp.domainName, udp.UdpSocketTransport().openServerMode((if_ip, port)))
    transportDispatcher.jobStarted(1)
    print('SNMP Trap Receiver Started!!!')
    try:
        transportDispatcher.runDispatcher()
    except:
        transportDispatcher.closeDispatcher()
        raise


if __name__ == '__main__':
    snmp_trap_receiver('ens33')

