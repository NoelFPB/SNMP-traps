from pysnmp.hlapi import *
from pysnmp.hlapi import OctetString, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, sendNotification, NotificationType, ObjectIdentity

# Replace these with actual values
values = {
    'AlertID': 'Your Alert ID',
    'AlertMessage': 'Your Alert Message',
    'Day': 'Your Day',
    'Time': 'Your Time',
    'AlertName': 'Your Alert Name',
    'NodeID': 'Your Node ID',
    'Caption': 'Your Caption',
    'Severity': 'Your Severity'
}
trap_oid = '1.3.6.1.4.1.11307.10'
var_binds = [(trap_oid + '.' + str(i+1), OctetString(str(value))) for i, value in enumerate(values.values())]

errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification(
        SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget(('localhost', 162)),
        ContextData(),
        'trap',   
        NotificationType(ObjectIdentity('1.3.6.1.4.1.11307.10')).addVarBinds(*var_binds)
    )
)

if errorIndication:
    print(errorIndication)

