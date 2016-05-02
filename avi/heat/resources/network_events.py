# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *


class NetworkSubnetClash(object):
    # all schemas
    ip_nw_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    networks_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    networks_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=networks_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip_nw',
        'networks',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip_nw': ip_nw_schema,
        'networks': networks_schema,
    }


class SummarizedSubnetInfo(object):
    # all schemas
    cidr_prefix_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    network_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'cidr_prefix',
        'network',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'cidr_prefix': cidr_prefix_schema,
        'network': network_schema,
    }


class SummarizedInfo(object):
    # all schemas
    subnet_info_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SummarizedSubnetInfo.properties_schema,
        required=True,
        update_allowed=False,
    )
    subnet_info_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=subnet_info_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'subnet_info',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'subnet_info': subnet_info_schema,
    }
