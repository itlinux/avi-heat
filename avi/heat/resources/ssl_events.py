# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *


class SSLRenewFailedDetails(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of SSL Certificate"),
        required=False,
        update_allowed=True,
    )
    error_schema = properties.Schema(
        properties.Schema.STRING,
        _("Error when renewing certificate"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'error',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'error': error_schema,
    }


class SSLExpireDetails(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of SSL Certificate"),
        required=False,
        update_allowed=True,
    )
    days_left_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of days until certificate is expired"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'days_left',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'days_left': days_left_schema,
    }


class SSLRenewDetails(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of SSL Certificate"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
    }


class SSLExportDetails(object):
    # all schemas
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request user"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'user',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'user': user_schema,
    }
