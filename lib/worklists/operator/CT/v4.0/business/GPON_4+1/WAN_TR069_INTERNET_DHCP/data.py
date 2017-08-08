#coding:utf-8


# -----------------------------doc--------------------------
# 工单 描述
WORKLIST_DOC = """
功能描述：生成一个TR069混合上网新装工单.

    参数：
    | PVC_OR_VLAN            | PVC:0/32 | ADSL上行用PVC格式,LAN\GPON\VDSL则用VLAN格式,默认是ADSL的PVC |
    | X_CT_COM_LanInterface  | LAN1 | 绑定LAN端口,默认LAN1,可以为LAN1,LAN2,LAN3,LAN4,WLAN1,WLAN2,WLAN3,WLAN4 |     
    | WANEnable_Switch       | True | WAN连接使能与WAN连接参数是否一起下发,True表示一起下发.默认为True |
    
            
    
    *注意:此工单的脚本中固定是DHCP的WAN连接,X_CT-COM_ServiceList为"TR069,INTERNET",
    绑定端口则根据不同的CPE设备类型而不同.
    
    出厂默认TR069 WAN连接是DHCP的,必须用此工单才能实现将TR069改为TR069+INTERNET
"""


# -----------------------------args--------------------------
# 工单 参数
WORKLIST_ARGS = {
# PVC_OR_VLAN
"PVC_OR_VLAN":("PVC:0/32", "1"), 
"X_CT_COM_LanInterface":("LAN1", "2"),
# 最后的WAN连接使能动作是否单独下发
"WANEnable_Switch":("True", "3")
}

