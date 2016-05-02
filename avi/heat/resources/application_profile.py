# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *
from compression_profile import *
from httpcache import *
from common import *
from ssl import *
from rate import *
from dos import *


class DosRateLimitProfile(object):
    # all schemas
    rl_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Profile for Connections/Requests rate limiting."),
        schema=RateLimiterProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    dos_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Profile for DoS attack detection."),
        schema=DosThresholdProfile.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rl_profile',
        'dos_profile',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rl_profile': rl_profile_schema,
        'dos_profile': dos_profile_schema,
    }


class SSLClientRequestHeader(object):
    # all schemas
    request_header_schema = properties.Schema(
        properties.Schema.STRING,
        _("If this header exists, reset the connection. If the ssl variable is specified, add a header with this value"),
        required=False,
        update_allowed=True,
    )
    request_header_value_schema = properties.Schema(
        properties.Schema.STRING,
        _("Set the request header with the value as indicated by this SSL variable. Eg. send the whole certificate in PEM format"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'request_header',
        'request_header_value',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'request_header': request_header_schema,
        'request_header_value': request_header_value_schema,
    }


class SSLClientCertificateAction(object):
    # all schemas
    headers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLClientRequestHeader.properties_schema,
        required=True,
        update_allowed=False,
    )
    headers_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=headers_item_schema,
        required=False,
        update_allowed=True,
    )
    close_connection_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'headers',
        'close_connection',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'headers': headers_schema,
        'close_connection': close_connection_schema,
    }


class HTTPApplicationProfile(object):
    # all schemas
    connection_multiplexing_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Allows HTTP requests, not just TCP connections, to be load balanced across servers.  Proxied TCP connections to servers may be reused by multiple clients to improve performance."),
        required=False,
        update_allowed=True,
    )
    xff_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("The client's original IP address is inserted into an HTTP request header sent to the server.  Servers may use this address for logging or other purposes, rather than Avi's source NAT address used in the Avi to server IP connection."),
        required=False,
        update_allowed=True,
    )
    xff_alternate_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Provide a custom name for the X-Forwarded-For header sent to the servers."),
        required=False,
        update_allowed=True,
    )
    ssl_everywhere_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable common settings to increase the level of security for  virtual services running HTTP and HTTPS.  For sites that are  HTTP only, these settings will have no effect."),
        required=False,
        update_allowed=True,
    )
    hsts_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Inserts HTTP Strict-Transport-Security header in the HTTPS response.  HSTS can help mitigate man-in-the-middle attacks by telling browsers that support HSTS that they should only access this site via HTTPS."),
        required=False,
        update_allowed=True,
    )
    hsts_max_age_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of days for which the client should regard this virtual service as a known HSTS host."),
        required=False,
        update_allowed=True,
    )
    secure_cookie_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Mark server cookies with the 'Secure' attribute.  Client browsers will not send a cookie marked as secure over an unencrypted connection.  If Avi is terminating SSL from clients and passing it as HTTP to the server, the server may return cookies without the secure flag set."),
        required=False,
        update_allowed=True,
    )
    httponly_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Mark HTTP cookies as HTTPonly.  This helps mitigate cross site scripting attacks as browsers will not allow these cookies to be read by third parties, such as javascript."),
        required=False,
        update_allowed=True,
    )
    http_to_https_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Client requests received via HTTP will be redirected to HTTPS."),
        required=False,
        update_allowed=True,
    )
    server_side_redirect_to_https_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When terminating client SSL sessions at Avi, servers may incorrectly send redirect to clients as HTTP.  This option will rewrite the server's redirect responses for this virtual service from HTTP to HTTPS."),
        required=False,
        update_allowed=True,
    )
    x_forwarded_proto_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Insert an X-Forwarded-Proto header in the request sent to the server.  When the client connects via SSL, Avi terminates the SSL, and then forwards the requests to the servers via HTTP, so the servers can determine the original protocol via this header.  In this example, the value will be 'https'."),
        required=False,
        update_allowed=True,
    )
    compression_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP Compression settings to use with this HTTP Profile."),
        schema=CompressionProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    spdy_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable SPDY proxy for traffic from clients to the virtual service.  SPDY requires SSL from the clients to Avi.  Avi ADC will proxy the SPDY protocol, and forward requests to servers as HTTP 1.1. "),
        required=False,
        update_allowed=True,
    )
    spdy_fwd_proxy_mode_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable fwd proxy mode with SPDY. This makes the Proxy combine the :host and :uri spdy headers to create a fwd-proxy style request URI"),
        required=False,
        update_allowed=True,
    )
    post_accept_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The max allowed length of time between a client establishing a TCP connection until Avi receives the first byte of the client's HTTP request."),
        required=False,
        update_allowed=True,
    )
    client_header_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The max length of time allowed for a client to transmit the entire request headers.  This helps to mitigate various forms of SlowLoris attacks."),
        required=False,
        update_allowed=True,
    )
    client_body_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The max allowed length of time to receive a request body from a client. Default of 0 specifies no timeout.  This setting generally impacts the length of time allowed for a client to send a POST."),
        required=False,
        update_allowed=True,
    )
    keepalive_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The max idle time allowed between HTTP requests over a Keep-alive connection."),
        required=False,
        update_allowed=True,
    )
    client_max_header_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum size in Kbytes of a single HTTP header in the client request."),
        required=False,
        update_allowed=True,
    )
    client_max_request_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum size in Kbytes of all the client HTTP request headers."),
        required=False,
        update_allowed=True,
    )
    client_max_body_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum size for the client request body.  This limits the size of the client data that can be uploaded/posted as part of a single HTTP Request.  Default 0 => Unlimited."),
        required=False,
        update_allowed=True,
    )
    cache_config_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP Caching config to use with this HTTP Profile."),
        schema=HttpCacheConfig.properties_schema,
        required=False,
        update_allowed=True,
    )
    max_rps_unknown_uri_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum unknown URIs per second."),
        required=False,
        update_allowed=True,
    )
    max_rps_cip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum requests per second per client IP."),
        required=False,
        update_allowed=True,
    )
    max_rps_uri_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum requests per second per URI."),
        required=False,
        update_allowed=True,
    )
    max_rps_cip_uri_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum requests per second per client IP and URI."),
        required=False,
        update_allowed=True,
    )
    ssl_client_certificate_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Set of match/action rules that govern what happens when the client certificate request is enabled"),
        schema=SSLClientCertificateAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    ssl_client_certificate_mode_schema = properties.Schema(
        properties.Schema.STRING,
        _("Specifies whether the client side verification is set to none, request or require."),
        required=False,
        update_allowed=True,
    )
    pki_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Select the PKI profile to be associated with the Virtual Service. This profile defines the Certificate Authority and Revocation List."),
        required=False,
        update_allowed=True,
    )
    websockets_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable Websockets proxy for traffic from clients to the virtual service. Connections to this VS start in HTTP mode. If the client requests an Upgrade to Websockets, and the server responds back with success, then the connection is upgraded to WebSockets mode. "),
        required=False,
        update_allowed=True,
    )
    max_rps_unknown_cip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum unknown client IPs per second."),
        required=False,
        update_allowed=True,
    )
    max_bad_rps_cip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum bad requests per second per client IP."),
        required=False,
        update_allowed=True,
    )
    max_bad_rps_uri_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum bad requests per second per URI."),
        required=False,
        update_allowed=True,
    )
    max_bad_rps_cip_uri_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum bad requests per second per client IP and URI."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'connection_multiplexing_enabled',
        'xff_enabled',
        'xff_alternate_name',
        'ssl_everywhere_enabled',
        'hsts_enabled',
        'hsts_max_age',
        'secure_cookie_enabled',
        'httponly_enabled',
        'http_to_https',
        'server_side_redirect_to_https',
        'x_forwarded_proto_enabled',
        'compression_profile',
        'spdy_enabled',
        'spdy_fwd_proxy_mode',
        'post_accept_timeout',
        'client_header_timeout',
        'client_body_timeout',
        'keepalive_timeout',
        'client_max_header_size',
        'client_max_request_size',
        'client_max_body_size',
        'cache_config',
        'max_rps_unknown_uri',
        'max_rps_cip',
        'max_rps_uri',
        'max_rps_cip_uri',
        'ssl_client_certificate_action',
        'ssl_client_certificate_mode',
        'pki_profile_uuid',
        'websockets_enabled',
        'max_rps_unknown_cip',
        'max_bad_rps_cip',
        'max_bad_rps_uri',
        'max_bad_rps_cip_uri',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'connection_multiplexing_enabled': connection_multiplexing_enabled_schema,
        'xff_enabled': xff_enabled_schema,
        'xff_alternate_name': xff_alternate_name_schema,
        'ssl_everywhere_enabled': ssl_everywhere_enabled_schema,
        'hsts_enabled': hsts_enabled_schema,
        'hsts_max_age': hsts_max_age_schema,
        'secure_cookie_enabled': secure_cookie_enabled_schema,
        'httponly_enabled': httponly_enabled_schema,
        'http_to_https': http_to_https_schema,
        'server_side_redirect_to_https': server_side_redirect_to_https_schema,
        'x_forwarded_proto_enabled': x_forwarded_proto_enabled_schema,
        'compression_profile': compression_profile_schema,
        'spdy_enabled': spdy_enabled_schema,
        'spdy_fwd_proxy_mode': spdy_fwd_proxy_mode_schema,
        'post_accept_timeout': post_accept_timeout_schema,
        'client_header_timeout': client_header_timeout_schema,
        'client_body_timeout': client_body_timeout_schema,
        'keepalive_timeout': keepalive_timeout_schema,
        'client_max_header_size': client_max_header_size_schema,
        'client_max_request_size': client_max_request_size_schema,
        'client_max_body_size': client_max_body_size_schema,
        'cache_config': cache_config_schema,
        'max_rps_unknown_uri': max_rps_unknown_uri_schema,
        'max_rps_cip': max_rps_cip_schema,
        'max_rps_uri': max_rps_uri_schema,
        'max_rps_cip_uri': max_rps_cip_uri_schema,
        'ssl_client_certificate_action': ssl_client_certificate_action_schema,
        'ssl_client_certificate_mode': ssl_client_certificate_mode_schema,
        'pki_profile_uuid': pki_profile_uuid_schema,
        'websockets_enabled': websockets_enabled_schema,
        'max_rps_unknown_cip': max_rps_unknown_cip_schema,
        'max_bad_rps_cip': max_bad_rps_cip_schema,
        'max_bad_rps_uri': max_bad_rps_uri_schema,
        'max_bad_rps_cip_uri': max_bad_rps_cip_uri_schema,
    }


class ApplicationProfile(AviResource):
    resource_name = "applicationprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("The name of the application profile."),
        required=True,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Specifies which application layer proxy is enabled for the virtual service."),
        required=True,
        update_allowed=True,
    )
    http_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the HTTP application proxy profile parameters."),
        schema=HTTPApplicationProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    dos_rl_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies various security related controls for virtual service."),
        schema=DosRateLimitProfile.properties_schema,
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
        'name',
        'type',
        'http_profile',
        'dos_rl_profile',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'type': type_schema,
        'http_profile': http_profile_schema,
        'dos_rl_profile': dos_rl_profile_schema,
        'description': description_schema,
    }


def resource_mapping():
    return {
        'Avi::ApplicationProfile': ApplicationProfile,
    }

