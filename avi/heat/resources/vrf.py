# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *


class BgpPeer(object):
    # all schemas
    remote_as_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Peer Autonomous System ID (Default: 1)"),
        required=False,
        update_allowed=True,
    )
    peer_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the BGP Peer"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    subnet_schema = properties.Schema(
        properties.Schema.MAP,
        _("Subnet providing reachability for Peer"),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=True,
    )
    md5_secret_schema = properties.Schema(
        properties.Schema.STRING,
        _("Peer Autonomous System Md5 Digest Secret Key"),
        required=False,
        update_allowed=True,
    )
    bfd_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable Bi-Directional Forward Detection. Only async mode supported. (Default: True)"),
        required=False,
        update_allowed=True,
    )
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Network providing reachability for Peer"),
        required=False,
        update_allowed=True,
    )
    advertise_vip_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Advertise VIP to this Peer (Default: True)"),
        required=False,
        update_allowed=True,
    )
    advertise_snat_ip_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Advertise SNAT IP to this Peer (Default: True)"),
        required=False,
        update_allowed=True,
    )
    advertisement_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Advertisement interval for this Peer (Default: 5)"),
        required=False,
        update_allowed=True,
    )
    connect_timer_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Connect timer for this Peer (Default: 10)"),
        required=False,
        update_allowed=True,
    )
    keepalive_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Keepalive interval for this Peer (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    hold_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Hold time for this Peer (Default: 180)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'remote_as',
        'peer_ip',
        'subnet',
        'md5_secret',
        'bfd',
        'network_uuid',
        'advertise_vip',
        'advertise_snat_ip',
        'advertisement_interval',
        'connect_timer',
        'keepalive_interval',
        'hold_time',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'remote_as': remote_as_schema,
        'peer_ip': peer_ip_schema,
        'subnet': subnet_schema,
        'md5_secret': md5_secret_schema,
        'bfd': bfd_schema,
        'network_uuid': network_uuid_schema,
        'advertise_vip': advertise_vip_schema,
        'advertise_snat_ip': advertise_snat_ip_schema,
        'advertisement_interval': advertisement_interval_schema,
        'connect_timer': connect_timer_schema,
        'keepalive_interval': keepalive_interval_schema,
        'hold_time': hold_time_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'subnet': getattr(IpAddrPrefix, 'field_references', {}),
        'peer_ip': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'subnet': getattr(IpAddrPrefix, 'unique_keys', {}),
        'my_key': 'peer_ip',
        'peer_ip': getattr(IpAddr, 'unique_keys', {}),
    }



class InternalGatewayMonitor(object):
    # all schemas
    gateway_monitor_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) The interval between two ping requests sent by the gateway monitor in milliseconds. If a value is not specified, requests are sent every second. (Units: MILLISECONDS) (Default: 1000)"),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_failure_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) The number of consecutive failed gateway health checks before a gateway is marked down. (Default: 10)"),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_success_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) The number of consecutive successful gateway health checks before a gateway that was marked down by the gateway monitor is marked up. (Default: 15)"),
        required=False,
        update_allowed=True,
    )
    disable_gateway_monitor_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Disable the gateway monitor for default gateway. They are monitored by default. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'gateway_monitor_interval',
        'gateway_monitor_failure_threshold',
        'gateway_monitor_success_threshold',
        'disable_gateway_monitor',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'gateway_monitor_interval': gateway_monitor_interval_schema,
        'gateway_monitor_failure_threshold': gateway_monitor_failure_threshold_schema,
        'gateway_monitor_success_threshold': gateway_monitor_success_threshold_schema,
        'disable_gateway_monitor': disable_gateway_monitor_schema,
    }



class GatewayMonitor(object):
    # all schemas
    gateway_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of next hop gateway to be monitored"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    gateway_monitor_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The interval between two ping requests sent by the gateway monitor in milliseconds. If a value is not specified, requests are sent every second. (Units: MILLISECONDS) (Default: 1000)"),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_fail_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The number of consecutive failed gateway health checks before a gateway is marked down. (Default: 10)"),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_success_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The number of consecutive successful gateway health checks before a gateway that was marked down by the gateway monitor is marked up. (Default: 15)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'gateway_ip',
        'gateway_monitor_interval',
        'gateway_monitor_fail_threshold',
        'gateway_monitor_success_threshold',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'gateway_ip': gateway_ip_schema,
        'gateway_monitor_interval': gateway_monitor_interval_schema,
        'gateway_monitor_fail_threshold': gateway_monitor_fail_threshold_schema,
        'gateway_monitor_success_threshold': gateway_monitor_success_threshold_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'gateway_ip': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'gateway_ip': getattr(IpAddr, 'unique_keys', {}),
    }



class StaticRoute(object):
    # all schemas
    prefix_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=True,
    )
    next_hop_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    if_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    route_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    disable_gateway_monitor_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Disable the gateway monitor for default gateway. They are monitored by default."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'prefix',
        'next_hop',
        'if_name',
        'route_id',
        'disable_gateway_monitor',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'prefix': prefix_schema,
        'next_hop': next_hop_schema,
        'if_name': if_name_schema,
        'route_id': route_id_schema,
        'disable_gateway_monitor': disable_gateway_monitor_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'prefix': getattr(IpAddrPrefix, 'field_references', {}),
        'next_hop': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'prefix': getattr(IpAddrPrefix, 'unique_keys', {}),
        'next_hop': getattr(IpAddr, 'unique_keys', {}),
        'my_key': 'route_id',
    }



class DebugVrf(object):
    # all schemas
    flag_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) "),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DEBUG_VRF_ALL', 'DEBUG_VRF_BGP', 'DEBUG_VRF_NONE']),
        ],
    )

    # properties list
    PROPERTIES = (
        'flag',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'flag': flag_schema,
    }

    unique_keys = {
        'my_key': 'flag',
    }



class BgpProfile(object):
    # all schemas
    local_as_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Local Autonomous System ID"),
        required=True,
        update_allowed=True,
    )
    ibgp_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("BGP peer type (Default: True)"),
        required=True,
        update_allowed=True,
    )
    peers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("BGP Peers"),
        schema=BgpPeer.properties_schema,
        required=True,
        update_allowed=False,
    )
    peers_schema = properties.Schema(
        properties.Schema.LIST,
        _("BGP Peers"),
        schema=peers_item_schema,
        required=False,
        update_allowed=True,
    )
    keepalive_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Keepalive interval for Peers (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    hold_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Hold time for Peers (Default: 180)"),
        required=False,
        update_allowed=True,
    )
    send_community_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.2) Send community attribute to all peers (Default: True)"),
        required=False,
        update_allowed=True,
    )
    community_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.2) Set the community attribute - 'internet', 'local-AS', 'no-advertise', 'no-export', <AS>:<Val> One or more of these can be configured with 1 <= AS,Val <= 65535"),
        required=True,
        update_allowed=False,
    )
    community_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.1.2) Set the community attribute - 'internet', 'local-AS', 'no-advertise', 'no-export', <AS>:<Val> One or more of these can be configured with 1 <= AS,Val <= 65535"),
        schema=community_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'local_as',
        'ibgp',
        'peers',
        'keepalive_interval',
        'hold_time',
        'send_community',
        'community',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'local_as': local_as_schema,
        'ibgp': ibgp_schema,
        'peers': peers_schema,
        'keepalive_interval': keepalive_interval_schema,
        'hold_time': hold_time_schema,
        'send_community': send_community_schema,
        'community': community_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'peers': getattr(BgpPeer, 'field_references', {}),
    }

    unique_keys = {
        'peers': getattr(BgpPeer, 'unique_keys', {}),
    }



class DebugVrfContext(object):
    # all schemas
    flags_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) "),
        schema=DebugVrf.properties_schema,
        required=True,
        update_allowed=False,
    )
    flags_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.1.1) "),
        schema=flags_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'flags',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'flags': flags_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'flags': getattr(DebugVrf, 'field_references', {}),
    }

    unique_keys = {
        'flags': getattr(DebugVrf, 'unique_keys', {}),
    }



class VrfContext(AviResource):
    resource_name = "vrfcontext"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    static_routes_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=StaticRoute.properties_schema,
        required=True,
        update_allowed=False,
    )
    static_routes_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=static_routes_item_schema,
        required=False,
        update_allowed=True,
    )
    bgp_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Bgp Local and Peer Info"),
        schema=BgpProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    gateway_mon_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("Configure ping based heartbeat check for gateway in service engines of vrf."),
        schema=GatewayMonitor.properties_schema,
        required=True,
        update_allowed=False,
    )
    gateway_mon_schema = properties.Schema(
        properties.Schema.LIST,
        _("Configure ping based heartbeat check for gateway in service engines of vrf."),
        schema=gateway_mon_item_schema,
        required=False,
        update_allowed=True,
    )
    internal_gateway_monitor_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Configure ping based heartbeat check for all default gateways in service engines of vrf."),
        schema=InternalGatewayMonitor.properties_schema,
        required=False,
        update_allowed=True,
    )
    debugvrfcontext_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Configure debug flags for VRF"),
        schema=DebugVrfContext.properties_schema,
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    cloud_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'static_routes',
        'bgp_profile',
        'gateway_mon',
        'internal_gateway_monitor',
        'debugvrfcontext',
        'description',
        'cloud_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'static_routes': static_routes_schema,
        'bgp_profile': bgp_profile_schema,
        'gateway_mon': gateway_mon_schema,
        'internal_gateway_monitor': internal_gateway_monitor_schema,
        'debugvrfcontext': debugvrfcontext_schema,
        'description': description_schema,
        'cloud_uuid': cloud_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'gateway_mon': getattr(GatewayMonitor, 'field_references', {}),
        'debugvrfcontext': getattr(DebugVrfContext, 'field_references', {}),
        'bgp_profile': getattr(BgpProfile, 'field_references', {}),
        'static_routes': getattr(StaticRoute, 'field_references', {}),
        'internal_gateway_monitor': getattr(InternalGatewayMonitor, 'field_references', {}),
    }

    unique_keys = {
        'gateway_mon': getattr(GatewayMonitor, 'unique_keys', {}),
        'debugvrfcontext': getattr(DebugVrfContext, 'unique_keys', {}),
        'bgp_profile': getattr(BgpProfile, 'unique_keys', {}),
        'static_routes': getattr(StaticRoute, 'unique_keys', {}),
        'internal_gateway_monitor': getattr(InternalGatewayMonitor, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::VrfContext': VrfContext,
    }

