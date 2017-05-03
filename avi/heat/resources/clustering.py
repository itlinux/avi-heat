# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from common import *
from options import *


class ClusterNode(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of controller VM."),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    vm_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID on the controller VM"),
        required=False,
        update_allowed=True,
    )
    vm_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the controller VM"),
        required=False,
        update_allowed=True,
    )
    vm_mor_schema = properties.Schema(
        properties.Schema.STRING,
        _("Managed object reference of this controller VM"),
        required=False,
        update_allowed=True,
    )
    vm_hostname_schema = properties.Schema(
        properties.Schema.STRING,
        _("hostname assigned to this controller VM"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'ip',
        'vm_uuid',
        'vm_name',
        'vm_mor',
        'vm_hostname',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'ip': ip_schema,
        'vm_uuid': vm_uuid_schema,
        'vm_name': vm_name_schema,
        'vm_mor': vm_mor_schema,
        'vm_hostname': vm_hostname_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip': getattr(IpAddr, 'field_references', {}),
    }



class Cluster(AviResource):
    resource_name = "cluster"
    # all schemas
    version_schema = properties.Schema(
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
    virtual_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("A virtual IP address. This IP address will be dynamically reconfigured so that it always is the IP of the cluster leader."),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    nodes_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ClusterNode.properties_schema,
        required=True,
        update_allowed=False,
    )
    nodes_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=nodes_item_schema,
        required=False,
        update_allowed=True,
    )
    rejoin_nodes_automatically_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Re-join cluster nodes automatically in the event one of the node is reset to factory. (Default: True)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'version',
        'name',
        'virtual_ip',
        'nodes',
        'rejoin_nodes_automatically',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'version': version_schema,
        'name': name_schema,
        'virtual_ip': virtual_ip_schema,
        'nodes': nodes_schema,
        'rejoin_nodes_automatically': rejoin_nodes_automatically_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'nodes': getattr(ClusterNode, 'field_references', {}),
        'virtual_ip': getattr(IpAddr, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::Cluster': Cluster,
    }

