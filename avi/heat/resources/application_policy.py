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
from match import *
from action import *
from rate import *


class HTTPSecurityAction(object):
    # all schemas
    action_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of the security action to perform"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HTTP_SECURITY_ACTION_SEND_RESPONSE', 'HTTP_SECURITY_ACTION_REDIRECT_TO_HTTPS', 'HTTP_SECURITY_ACTION_RATE_LIMIT', 'HTTP_SECURITY_ACTION_ALLOW', 'HTTP_SECURITY_ACTION_CLOSE_CONN']),
        ],
    )
    status_code_schema = properties.Schema(
        properties.Schema.STRING,
        _("HTTP status code to use for local response"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HTTP_LOCAL_RESPONSE_STATUS_CODE_403', 'HTTP_LOCAL_RESPONSE_STATUS_CODE_429', 'HTTP_LOCAL_RESPONSE_STATUS_CODE_200', 'HTTP_LOCAL_RESPONSE_STATUS_CODE_404']),
        ],
    )
    https_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Secure SSL/TLS port to redirect the HTTP request to"),
        required=False,
        update_allowed=True,
    )
    file_schema = properties.Schema(
        properties.Schema.MAP,
        _("File to be used for generating HTTP local response"),
        schema=HTTPLocalFile.properties_schema,
        required=False,
        update_allowed=True,
    )
    rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit profile to be used to rate-limit the flow"),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'action',
        'status_code',
        'https_port',
        'file',
        'rate_limit',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'action': action_schema,
        'status_code': status_code_schema,
        'https_port': https_port_schema,
        'file': file_schema,
        'rate_limit': rate_limit_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rate_limit': getattr(RateProfile, 'field_references', {}),
        'file': getattr(HTTPLocalFile, 'field_references', {}),
    }

    unique_keys = {
        'rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'file': getattr(HTTPLocalFile, 'unique_keys', {}),
    }



class HTTPPolicies(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the virtual service HTTP policy collection"),
        required=True,
        update_allowed=True,
    )
    http_policy_set_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the virtual service HTTP policy collection You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'http_policy_set_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'http_policy_set_uuid': http_policy_set_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'http_policy_set_uuid': 'httppolicyset',
    }

    unique_keys = {
        'my_key': 'index',
    }



class HTTPRequestRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the rule"),
        required=True,
        update_allowed=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the rule"),
        required=True,
        update_allowed=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the rule (Default: True)"),
        required=True,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add match criteria to the rule"),
        schema=MatchTarget.properties_schema,
        required=False,
        update_allowed=True,
    )
    redirect_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP redirect action"),
        schema=HTTPRedirectAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    hdr_action_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP header rewrite action"),
        schema=HTTPHdrAction.properties_schema,
        required=True,
        update_allowed=False,
    )
    hdr_action_schema = properties.Schema(
        properties.Schema.LIST,
        _("HTTP header rewrite action"),
        schema=hdr_action_item_schema,
        required=False,
        update_allowed=True,
    )
    rewrite_url_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP request URL rewrite action"),
        schema=HTTPRewriteURLAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    switching_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Content switching action"),
        schema=HTTPSwitchingAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log HTTP request upon rule match"),
        required=False,
        update_allowed=True,
    )
    all_headers_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log all HTTP headers upon rule match"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'redirect_action',
        'hdr_action',
        'rewrite_url_action',
        'switching_action',
        'log',
        'all_headers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'redirect_action': redirect_action_schema,
        'hdr_action': hdr_action_schema,
        'rewrite_url_action': rewrite_url_action_schema,
        'switching_action': switching_action_schema,
        'log': log_schema,
        'all_headers': all_headers_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rewrite_url_action': getattr(HTTPRewriteURLAction, 'field_references', {}),
        'redirect_action': getattr(HTTPRedirectAction, 'field_references', {}),
        'hdr_action': getattr(HTTPHdrAction, 'field_references', {}),
        'match': getattr(MatchTarget, 'field_references', {}),
        'switching_action': getattr(HTTPSwitchingAction, 'field_references', {}),
    }

    unique_keys = {
        'rewrite_url_action': getattr(HTTPRewriteURLAction, 'unique_keys', {}),
        'my_key': 'index',
        'switching_action': getattr(HTTPSwitchingAction, 'unique_keys', {}),
        'redirect_action': getattr(HTTPRedirectAction, 'unique_keys', {}),
        'hdr_action': getattr(HTTPHdrAction, 'unique_keys', {}),
        'match': getattr(MatchTarget, 'unique_keys', {}),
    }



class HTTPResponseRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the rule"),
        required=True,
        update_allowed=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the rule"),
        required=True,
        update_allowed=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the rule (Default: True)"),
        required=True,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add match criteria to the rule"),
        schema=ResponseMatchTarget.properties_schema,
        required=False,
        update_allowed=True,
    )
    hdr_action_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP header rewrite action"),
        schema=HTTPHdrAction.properties_schema,
        required=True,
        update_allowed=False,
    )
    hdr_action_schema = properties.Schema(
        properties.Schema.LIST,
        _("HTTP header rewrite action"),
        schema=hdr_action_item_schema,
        required=False,
        update_allowed=True,
    )
    loc_hdr_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Location header rewrite action"),
        schema=HTTPRewriteLocHdrAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log HTTP request upon rule match"),
        required=False,
        update_allowed=True,
    )
    all_headers_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log all HTTP headers upon rule match"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'hdr_action',
        'loc_hdr_action',
        'log',
        'all_headers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'hdr_action': hdr_action_schema,
        'loc_hdr_action': loc_hdr_action_schema,
        'log': log_schema,
        'all_headers': all_headers_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'loc_hdr_action': getattr(HTTPRewriteLocHdrAction, 'field_references', {}),
        'hdr_action': getattr(HTTPHdrAction, 'field_references', {}),
        'match': getattr(ResponseMatchTarget, 'field_references', {}),
    }

    unique_keys = {
        'loc_hdr_action': getattr(HTTPRewriteLocHdrAction, 'unique_keys', {}),
        'my_key': 'index',
        'hdr_action': getattr(HTTPHdrAction, 'unique_keys', {}),
        'match': getattr(ResponseMatchTarget, 'unique_keys', {}),
    }



class HTTPSecurityRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the rule"),
        required=True,
        update_allowed=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the rule"),
        required=True,
        update_allowed=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the rule (Default: True)"),
        required=True,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add match criteria to the rule"),
        schema=MatchTarget.properties_schema,
        required=False,
        update_allowed=True,
    )
    action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Action to be performed upon successful matching"),
        schema=HTTPSecurityAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log HTTP request upon rule match"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'action',
        'log',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'action': action_schema,
        'log': log_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'action': getattr(HTTPSecurityAction, 'field_references', {}),
        'match': getattr(MatchTarget, 'field_references', {}),
    }

    unique_keys = {
        'action': getattr(HTTPSecurityAction, 'unique_keys', {}),
        'my_key': 'index',
        'match': getattr(MatchTarget, 'unique_keys', {}),
    }



class HTTPRequestPolicy(object):
    # all schemas
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add rules to the HTTP request policy"),
        schema=HTTPRequestRule.properties_schema,
        required=True,
        update_allowed=False,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("Add rules to the HTTP request policy"),
        schema=rules_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rules': rules_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rules': getattr(HTTPRequestRule, 'field_references', {}),
    }

    unique_keys = {
        'rules': getattr(HTTPRequestRule, 'unique_keys', {}),
    }



class HTTPSecurityPolicy(object):
    # all schemas
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add rules to the HTTP security policy"),
        schema=HTTPSecurityRule.properties_schema,
        required=True,
        update_allowed=False,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("Add rules to the HTTP security policy"),
        schema=rules_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rules': rules_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rules': getattr(HTTPSecurityRule, 'field_references', {}),
    }

    unique_keys = {
        'rules': getattr(HTTPSecurityRule, 'unique_keys', {}),
    }



class HTTPResponsePolicy(object):
    # all schemas
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add rules to the HTTP response policy"),
        schema=HTTPResponseRule.properties_schema,
        required=True,
        update_allowed=False,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("Add rules to the HTTP response policy"),
        schema=rules_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rules': rules_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rules': getattr(HTTPResponseRule, 'field_references', {}),
    }

    unique_keys = {
        'rules': getattr(HTTPResponseRule, 'unique_keys', {}),
    }



class HTTPPolicySet(AviResource):
    resource_name = "httppolicyset"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the HTTP Policy Set"),
        required=True,
        update_allowed=True,
    )
    http_security_policy_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP security policy for the virtual service."),
        schema=HTTPSecurityPolicy.properties_schema,
        required=False,
        update_allowed=True,
    )
    http_request_policy_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP request policy for the virtual service."),
        schema=HTTPRequestPolicy.properties_schema,
        required=False,
        update_allowed=True,
    )
    http_response_policy_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP response policy for the virtual service."),
        schema=HTTPResponsePolicy.properties_schema,
        required=False,
        update_allowed=True,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("Creator name"),
        required=False,
        update_allowed=True,
    )
    cloud_config_cksum_schema = properties.Schema(
        properties.Schema.STRING,
        _("Checksum of cloud configuration for Pool. Internally set by cloud connector"),
        required=False,
        update_allowed=True,
    )
    is_internal_policy_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(" (Default: False)"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'http_security_policy',
        'http_request_policy',
        'http_response_policy',
        'created_by',
        'cloud_config_cksum',
        'is_internal_policy',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'http_security_policy': http_security_policy_schema,
        'http_request_policy': http_request_policy_schema,
        'http_response_policy': http_response_policy_schema,
        'created_by': created_by_schema,
        'cloud_config_cksum': cloud_config_cksum_schema,
        'is_internal_policy': is_internal_policy_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'http_request_policy': getattr(HTTPRequestPolicy, 'field_references', {}),
        'http_response_policy': getattr(HTTPResponsePolicy, 'field_references', {}),
        'http_security_policy': getattr(HTTPSecurityPolicy, 'field_references', {}),
    }

    unique_keys = {
        'http_request_policy': getattr(HTTPRequestPolicy, 'unique_keys', {}),
        'http_response_policy': getattr(HTTPResponsePolicy, 'unique_keys', {}),
        'http_security_policy': getattr(HTTPSecurityPolicy, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::HTTPPolicySet': HTTPPolicySet,
    }

