# To create overlay configurations, we first need to set up the underlying infrastructure; for our first subnet:
ip addr add 10.0.0.10/30 dev eth0

# A unique virtual IP assignment to `lo` interface for BGP neighbour relationships to operate over the overlay;
ip addr add 1.1.1.4/32 dev lo

# The OSPF configuration required to ensure that BGP neighbour relationships are established via the unique virtual IP addresses we previously assigned to the "lo" interface, rather than via physical interfaces;
vtysh -c "
 # Switch vtysh from read mode to write mode
 configure terminal
 # Enter OSPF configuration mode
 router ospf
 # Notify OSPF of the network addresses assigned to this device
 network 1.1.1.4/32 area 0
 network 10.0.0.8/30 area 0
 # exit from OSPF configuration
 exit
 # exit from write mode
 exit
 # Write the all configurations
 write
"

# The BGP configurations required for Leaf to establish a dynamic relationship with RR;
vtysh -c "
 configure terminal
 # Switch to the BGP configuration with AS number 1
 router bgp 1
 # The IP address of the neighbor to be connected to and the AS number it belongs to are specified;
 neighbor 1.1.1.1 remote-as 1
 # This means Use my lo interface as the source IP when sending BGP messages to this neighbor (1.1.1.1).
 neighbor 1.1.1.1 update-source lo
 # In FRR, lines beginning with ! are treated as comments and are not execute. It acts as a separator.
 !
 # We re moving on to another internal configuration shell to instruct BGP to carry not only IPv4 routes but also MAC information;
 address-family l2vpn evpn
  # we re saying, Share EVPN information with RR.
  neighbor 1.1.1.1 activate
  # we re saying, Advertise all VXLAN IDs defined on this device via BGP EVPN.
  advertise-all-vni
  # Exit from internal address-family configuration env
  exit
 exit
 exit
 write
 "

# Create a virtual network interface named `vxlan10`, of type `vxlan`, with an ID of `10`, a destination port of 4789, and the `nolearning` parameter to prevent it from learning MAC addresses on the data plane;
ip link add vxlan10 type vxlan id 10 local 1.1.1.4 nolearning dstport 4789
# Up to `vxlan10` virtual interface from `DOWN` state
ip link set vxlan10 up
# Create a bridge interface named `br0`, of type `bridge`
ip link add br0 type bridge
# Up to `br0` bridge interface from `DOWN` state
ip link set br0 up
# Connect one end of the bridge to `vxlan10`
ip link set vxlan10 master br0
# Connect the other end of the bridge to `eth1`
ip link set eth1 master br0
