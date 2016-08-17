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
from cloud_objects import *


class VcenterDatastore(object):
    # all schemas
    datastore_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'datastore_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'datastore_name': datastore_name_schema,
    }




class CdpLldpInfo(object):
    # all schemas
    switch_info_type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LLDP', 'NOT_APPLICABLE', 'CDP']),
        ],
    )
    device_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    chassis_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    mgmtaddr_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    system_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'switch_info_type',
        'device',
        'chassis',
        'port',
        'mgmtaddr',
        'system_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'switch_info_type': switch_info_type_schema,
        'device': device_schema,
        'chassis': chassis_schema,
        'port': port_schema,
        'mgmtaddr': mgmtaddr_schema,
        'system_name': system_name_schema,
    }


