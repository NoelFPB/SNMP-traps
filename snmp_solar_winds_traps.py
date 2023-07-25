from pysnmp.hlapi import *
from pysnmp.hlapi import OctetString, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, sendNotification, NotificationType, ObjectIdentity


# assign values to variables
AlertID = '127'
AlertMessage = '_Interface_DOWN was triggered.'
Day = '7/17/2023'
Time = '9:51:11 AM'
AlertName = '_Interface_DOWN'
NodeID = '1N-SW-INT-12732'
Caption = 'et-3/0/2 · Internal NAP - Hacia ON-NAP-03-MX10008 et-0/0/3'
Severity = 'Critical'

# define the template with placeholders for variable substitution
template = "[AlertID] {AlertID} [AlertMessage] {AlertMessage} [Day] {Day} [Time] {Time} [AlertName] {AlertName} [NodeID] {NodeID} [Caption] {Caption} [Severity] {Severity}"
message = template.format(AlertID=AlertID, AlertMessage=AlertMessage, Day=Day, Time=Time, AlertName=AlertName, NodeID=NodeID, Caption=Caption, Severity=Severity)
print(message)

errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification(
        SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget(('localhost', 162)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity('1.3.6.1.4.1.11307.10') 
        ).addVarBinds(
            ('1.3.6.1.6.3.1.1.4.3.0', ObjectIdentifier('1.3.6.1.4.1.11307')),
            ('1.3.6.1.4.1.11307.10.2', OctetString(str(Caption))),
            ('1.3.6.1.4.1.11307.10.3', IpAddress('10.12.28.1')),
            ('1.3.6.1.4.1.11307.10.4', OctetString('3')),
            ('1.3.6.1.4.1.11307.10.5', OctetString(str(Caption))),
            ('1.3.6.1.4.1.11307.10.6', OctetString('Interface')),
            ('1.3.6.1.4.1.11307.10.7', OctetString(str(NodeID))),
            ('1.3.6.1.4.1.11307.10.1', OctetString(str(message)))
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
