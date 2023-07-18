from pysnmp.hlapi import *
from pysnmp.hlapi import OctetString, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, sendNotification, NotificationType, ObjectIdentity


AlertID = 'Your Alert ID'
AlertMessage = 'Your Alert Message'
Day = 'Your Day'
Time = 'Your Time'
AlertName = 'Your Alert Name'
NodeID = 'Your Node ID'
Caption = 'Your Caption'
Severity = 'Your Severity'


errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification(
        SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget(('localhost', 162)),
        ContextData(),
        'trap',
        NotificationType(
            #ObjectIdentity('1.3.6.1.6.3.1.1.4.1.0'),
            #ObjectIdentity('1.3.6.1.2.1.1.3.0'),
            #ObjectIdentity('1.3.6.1.6.3.1.1.4.3.0')
            ObjectIdentity('1.3.6.1.4.1.11307.10') 
        ).addVarBinds(
            ('1.3.6.1.6.3.1.1.4.3.0', ObjectIdentifier('1.3.6.1.4.1.11307')),
            ('1.3.6.1.4.1.11307.10.2', OctetString(hexValue='65742d332f302f3220b720496e7465726e616c204e4150202d204861636961204f4e2d4e')),
            ('1.3.6.1.4.1.11307.10.3', IpAddress('10.12.28.1')),
            ('1.3.6.1.4.1.11307.10.4', OctetString('3')),
            ('1.3.6.1.4.1.11307.10.5', OctetString(hexValue='65742d332f302f3220b720496e7465726e616c204e4150202d204861636961204f4e2d4e')),
            ('1.3.6.1.4.1.11307.10.6', OctetString('Interface')),
            ('1.3.6.1.4.1.11307.10.7', OctetString(str(NodeID))),
            ('1.3.6.1.4.1.11307.10.1', OctetString(hexValue='5b416c65727449445d20313237205b416c6572744d6573736167655d205f496e74657266'))
        )
    )
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
