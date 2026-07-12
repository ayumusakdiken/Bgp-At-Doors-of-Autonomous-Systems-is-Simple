##################### Group 1: Dynamic BGP configuration for EVPN overlay
# To create overlay configurations, we first need to set up the underlying infrastructure; for our first subnet:
ip addr add 10.0.0.1/30 dev eth0

# for second subnet:
ip addr add 10.0.0.5/30 dev eth1

# for third subnet:
ip addr add 10.0.0.9/30 dev eth2

# A unique virtual IP assignment to `lo` interface for BGP neighbour relationships to operate over the overlay;
ip addr add 1.1.1.1/32 dev lo

# The OSPF configuration required to ensure that BGP neighbour relationships are established via the unique virtual IP addresses we previously assigned to the "lo" interface, rather than via physical interfaces. Switch to the CLI environment for FRR configurations (BGP, OSPF, etc.);
vtysh -c "
 # Switch vtysh from read mode to write mode
 configure terminal
 # Enter OSPF configuration mode
 router ospf
 # Notify OSPF of the network addresses assigned to this device
 network 1.1.1.1/32 area 0
 network 10.0.0.0/30 area 0
 network 10.0.0.4/30 area 0
 network 10.0.0.8/30 area 0
 # exit from OSPF configuration 
 exit
 # exit from write mode
 exit
 # Write the all configurations
 write
 "

# Dynamic relationship BGP configuration;
vtysh -c "
 configure terminal
 # Switch to the BGP configuration with AS number 1
 router bgp 1
 # This means create a group called VTEP-GROUP. Any settings applied to the group are applied to all members.
 neighbor VTEP-GROUP peer-group
 # This means that all neighbours in this group are in AS 1.
 neighbor VTEP-GROUP remote-as 1
 # It means communicate with neighbours in this group via loopback.
 neighbor VTEP-GROUP update-source lo
 # This means automatically accepting BGP neighbour requests from the 1.1.1.0/24 block and adding them to the VTEP-GROUP group.
 bgp listen range 1.1.1.0/24 peer-group VTEP-GROUP
 # In FRR, lines beginning with ! are treated as comments and are not execute. It acts as a separator.
 !
 # We’re moving on to another internal configuration shell to instruct BGP to carry not only IPv4 routes but also MAC information. 
 address-family l2vpn evpn
  # We say, Share the EVPN information with VTEP-GROUP members as well. 
  neighbor VTEP-GROUP activate
  # This means VTEP-GROUP members are the clients in my EVPN address family.
  neighbor VTEP-GROUP route-reflector-client
  # Exit from internal address-family configuration env
  exit
 exit
 exit
 write
"

################# Static BGP configuration for EVPN overlay
# ip addr add 10.0.0.1/30 dev eth0
# ip addr add 10.0.0.5/30 dev eth1
# ip addr add 10.0.0.9/30 dev eth2
# ip addr add 1.1.1.1/32 dev lo
# vtysh -c "
# configure terminal
# router ospf
# network 1.1.1.1/32 area 0
# network 10.0.0.0/30 area 0
# network 10.0.0.4/30 area 0
# network 10.0.0.8/30 area 0
# exit
# exit
# write
# "
#vtysh -c "
# configure terminal
# router bgp 1
# neighbor 1.1.1.2 remote-as 1
# neighbor 1.1.1.3 remote-as 1
# neighbor 1.1.1.4 remote-as 1
# neighbor 1.1.1.5 remote-as 1
# neighbor 1.1.1.2 update-source lo
# neighbor 1.1.1.3 update-source lo
# neighbor 1.1.1.4 update-source lo
# neighbor 1.1.1.5 update-source lo
# !
# address-family l2vpn evpn
#  neighbor 1.1.1.2 activate
#  neighbor 1.1.1.3 activate
#  neighbor 1.1.1.4 activate
#  neighbor 1.1.1.5 activate
#  neighbor 1.1.1.2 route-reflector-client
#  neighbor 1.1.1.3 route-reflector-client
#  neighbor 1.1.1.4 route-reflector-client
#  neighbor 1.1.1.5 route-reflector-client
#  exit
# exit
# exit
# write
#"


