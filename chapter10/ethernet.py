
from .util import BitFormat
from .packet import Packet


class EthernetF0(Packet):
    """Ethernet data
    .. py:attribute:: count
    .. py:attribute:: ttb

        Time tag bits:

        * 0 - First bit of the frame destination address
        * 0 - Last bit of the frame check sequence
        * 0 - First bit of the frame payload data
        * 0 - Last bit of the frame payload data

    .. py:attribute:: format

        Should be 0 (IEEE 802.3 MAC frame)

    **Message Format**

    .. py:attribute:: ipts
    .. py:attribute:: length

        Payload length (bytes)

    .. py:attribute:: data_length_error
    .. py:attribute:: data_crc_error
    .. py:attribute:: network_id
    .. py:attribute:: crc_error
    .. py:attribute:: frame_error
    .. py:attribute:: content

        * 0 - Full MAC frame
        * 1 - Payload only (14 bytes from the destination address)

    .. py:attribute:: ethernet_speed

        * 0 - Auto
        * 1 - 10 Mbps
        * 2 - 100 Mbps
        * 3 - 1 Gbps
        * 4 - 10 Gbps
    """

    item_label = 'Ethernet Frame'
    csdw_format = BitFormat('''
        u16 count
        p9
        u3 ttb
        u4 format''')
    # Note: bitfields may need to be listed in reverse of expected
    # order.
    iph_format = BitFormat('''
        u64 ipts
        u14 length
        u1 data_length_error
        u1 data_crc_error
        u8 network_id
        u1 crc_error
        u1 frame_error
        u2 content
        u4 ethernet_speed''')


class EthernetF1(Packet):
    """ARINC-664

    .. py:attribute:: count
    .. py:attribute:: iph_length

        Fixed at 28

    **Message Format**

    .. py:attribute:: ipts
    .. py:attribute:: flags

        * 0 - Actual data
        * 1 - Simulated data

    .. py:attribute:: error
    .. py:attribute:: length

        Message length (bytes)

    .. py:attribute:: virtual_link

        Lower 16 bits of the destination MAC address

    .. py:attribute:: src_ip

        Source IP address from ARINC IP header

    .. py:attribute:: dst_ip

        Destination IP address from ARINC IP header

    .. py:attribute:: dst_port

        Destination port from the ARINC UDP header

    .. py:attribute:: src_port

        Source port from the ARINC UDP header
    """

    item_label = 'Ethernet Frame'
    csdw_format = BitFormat('''
        u16 count
        u16 iph_length''')
    iph_format = BitFormat('''
        u64 ipts
        u8 flags
        u8 error
        u16 length
        u16 virtual_link
        p16
        u32 src_ip
        u32 dst_ip
        u16 dst_port
        u16 src_port''')
