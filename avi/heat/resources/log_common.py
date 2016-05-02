# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *


class ConnErrorInfo(object):
    # all schemas
    out_of_orders_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    retransmits_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    timeouts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    rx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    tx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    zero_window_size_events_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_out_of_orders_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_retransmits_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_timeouts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_rx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_tx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_zero_window_size_events_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_window_shrink_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_num_window_shrink_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_syn_retransmit_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'out_of_orders',
        'retransmits',
        'timeouts',
        'rx_pkts',
        'tx_pkts',
        'zero_window_size_events',
        'server_out_of_orders',
        'server_retransmits',
        'server_timeouts',
        'server_rx_pkts',
        'server_tx_pkts',
        'server_zero_window_size_events',
        'num_window_shrink',
        'server_num_window_shrink',
        'num_syn_retransmit',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'out_of_orders': out_of_orders_schema,
        'retransmits': retransmits_schema,
        'timeouts': timeouts_schema,
        'rx_pkts': rx_pkts_schema,
        'tx_pkts': tx_pkts_schema,
        'zero_window_size_events': zero_window_size_events_schema,
        'server_out_of_orders': server_out_of_orders_schema,
        'server_retransmits': server_retransmits_schema,
        'server_timeouts': server_timeouts_schema,
        'server_rx_pkts': server_rx_pkts_schema,
        'server_tx_pkts': server_tx_pkts_schema,
        'server_zero_window_size_events': server_zero_window_size_events_schema,
        'num_window_shrink': num_window_shrink_schema,
        'server_num_window_shrink': server_num_window_shrink_schema,
        'num_syn_retransmit': num_syn_retransmit_schema,
    }


class ConnectionLog(object):
    # all schemas
    adf_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=True,
        update_allowed=True,
    )
    significant_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    significance_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    udf_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=True,
        update_allowed=True,
    )
    virtualservice_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_location_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    client_src_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_dest_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    start_timestamp_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    report_timestamp_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    total_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    connection_ended_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_rtt_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    mss_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    rx_bytes_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    tx_bytes_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    total_bytes_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    rx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    tx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    total_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    out_of_orders_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    retransmits_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    timeouts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    zero_window_size_events_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    service_engine_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    vcpu_id_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    log_id_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    network_security_policy_rule_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    pool_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    pool_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_ip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_conn_src_ip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_dest_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_src_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_rtt_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_total_bytes_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_rx_bytes_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_tx_bytes_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_total_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_rx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_tx_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_out_of_orders_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_retransmits_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_timeouts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_zero_window_size_events_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    significant_log_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    significant_log_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of enums which indicate why a log is significant"),
        schema=significant_log_item_schema,
        required=False,
        update_allowed=True,
    )
    num_transaction_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    average_turntime_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_window_shrink_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_num_window_shrink_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_syn_retransmit_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    microservice_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    microservice_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'adf',
        'significant',
        'significance',
        'udf',
        'virtualservice',
        'client_ip',
        'client_location',
        'client_src_port',
        'client_dest_port',
        'start_timestamp',
        'report_timestamp',
        'total_time',
        'connection_ended',
        'client_rtt',
        'mss',
        'rx_bytes',
        'tx_bytes',
        'total_bytes',
        'rx_pkts',
        'tx_pkts',
        'total_pkts',
        'out_of_orders',
        'retransmits',
        'timeouts',
        'zero_window_size_events',
        'service_engine',
        'vcpu_id',
        'log_id',
        'network_security_policy_rule_name',
        'pool',
        'pool_name',
        'server_ip',
        'server_name',
        'server_conn_src_ip',
        'server_dest_port',
        'server_src_port',
        'server_rtt',
        'server_total_bytes',
        'server_rx_bytes',
        'server_tx_bytes',
        'server_total_pkts',
        'server_rx_pkts',
        'server_tx_pkts',
        'server_out_of_orders',
        'server_retransmits',
        'server_timeouts',
        'server_zero_window_size_events',
        'significant_log',
        'num_transaction',
        'average_turntime',
        'num_window_shrink',
        'server_num_window_shrink',
        'num_syn_retransmit',
        'microservice',
        'microservice_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'adf': adf_schema,
        'significant': significant_schema,
        'significance': significance_schema,
        'udf': udf_schema,
        'virtualservice': virtualservice_schema,
        'client_ip': client_ip_schema,
        'client_location': client_location_schema,
        'client_src_port': client_src_port_schema,
        'client_dest_port': client_dest_port_schema,
        'start_timestamp': start_timestamp_schema,
        'report_timestamp': report_timestamp_schema,
        'total_time': total_time_schema,
        'connection_ended': connection_ended_schema,
        'client_rtt': client_rtt_schema,
        'mss': mss_schema,
        'rx_bytes': rx_bytes_schema,
        'tx_bytes': tx_bytes_schema,
        'total_bytes': total_bytes_schema,
        'rx_pkts': rx_pkts_schema,
        'tx_pkts': tx_pkts_schema,
        'total_pkts': total_pkts_schema,
        'out_of_orders': out_of_orders_schema,
        'retransmits': retransmits_schema,
        'timeouts': timeouts_schema,
        'zero_window_size_events': zero_window_size_events_schema,
        'service_engine': service_engine_schema,
        'vcpu_id': vcpu_id_schema,
        'log_id': log_id_schema,
        'network_security_policy_rule_name': network_security_policy_rule_name_schema,
        'pool': pool_schema,
        'pool_name': pool_name_schema,
        'server_ip': server_ip_schema,
        'server_name': server_name_schema,
        'server_conn_src_ip': server_conn_src_ip_schema,
        'server_dest_port': server_dest_port_schema,
        'server_src_port': server_src_port_schema,
        'server_rtt': server_rtt_schema,
        'server_total_bytes': server_total_bytes_schema,
        'server_rx_bytes': server_rx_bytes_schema,
        'server_tx_bytes': server_tx_bytes_schema,
        'server_total_pkts': server_total_pkts_schema,
        'server_rx_pkts': server_rx_pkts_schema,
        'server_tx_pkts': server_tx_pkts_schema,
        'server_out_of_orders': server_out_of_orders_schema,
        'server_retransmits': server_retransmits_schema,
        'server_timeouts': server_timeouts_schema,
        'server_zero_window_size_events': server_zero_window_size_events_schema,
        'significant_log': significant_log_schema,
        'num_transaction': num_transaction_schema,
        'average_turntime': average_turntime_schema,
        'num_window_shrink': num_window_shrink_schema,
        'server_num_window_shrink': server_num_window_shrink_schema,
        'num_syn_retransmit': num_syn_retransmit_schema,
        'microservice': microservice_schema,
        'microservice_name': microservice_name_schema,
    }


class DataScriptErrorTrace(object):
    # all schemas
    error_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    stack_trace_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    event_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'error',
        'stack_trace',
        'event',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'error': error_schema,
        'stack_trace': stack_trace_schema,
        'event': event_schema,
    }


class ApplicationLog(object):
    # all schemas
    adf_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=True,
        update_allowed=True,
    )
    significant_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    significance_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    udf_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=True,
        update_allowed=True,
    )
    virtualservice_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    report_timestamp_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    service_engine_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    vcpu_id_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    log_id_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_location_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    client_src_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_dest_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_rtt_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    ssl_session_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    ssl_version_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    ssl_cipher_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    http_version_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    method_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    uri_path_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    rewritten_uri_path_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    uri_query_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    rewritten_uri_query_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    redirected_uri_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_side_redirect_uri_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    referer_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    user_agent_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    client_device_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    client_browser_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    client_os_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    xff_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    persistence_used_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    host_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    etag_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    persistent_session_id_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    request_content_type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    response_content_type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    request_length_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    cache_hit_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    cacheable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    network_security_policy_rule_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    http_security_policy_rule_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    http_request_policy_rule_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    http_response_policy_rule_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    pool_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    pool_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_ip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_conn_src_ip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_dest_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_src_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_rtt_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_response_length_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_response_code_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_response_time_first_byte_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    server_response_time_last_byte_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    app_response_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    data_transfer_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    total_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    response_length_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    response_code_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    response_time_first_byte_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    response_time_last_byte_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    compression_percentage_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    compression_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    client_insights_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    connection_error_info_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ConnErrorInfo.properties_schema,
        required=False,
        update_allowed=True,
    )
    spdy_version_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    request_headers_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    response_headers_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    request_state_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    datascript_error_trace_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DataScriptErrorTrace.properties_schema,
        required=False,
        update_allowed=True,
    )
    all_request_headers_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    all_response_headers_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    user_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    significant_log_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    significant_log_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of enums which indicate why a log is significant"),
        schema=significant_log_item_schema,
        required=False,
        update_allowed=True,
    )
    datascript_log_schema = properties.Schema(
        properties.Schema.STRING,
        _("Log created by the invocations of the DataScript api avi.vs.log()"),
        required=False,
        update_allowed=True,
    )
    microservice_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    microservice_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    headers_sent_to_server_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request headers sent to backend server"),
        required=False,
        update_allowed=True,
    )
    headers_received_from_server_schema = properties.Schema(
        properties.Schema.STRING,
        _("Response headers received from backend server"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'adf',
        'significant',
        'significance',
        'udf',
        'virtualservice',
        'report_timestamp',
        'service_engine',
        'vcpu_id',
        'log_id',
        'client_ip',
        'client_location',
        'client_src_port',
        'client_dest_port',
        'client_rtt',
        'ssl_session_id',
        'ssl_version',
        'ssl_cipher',
        'http_version',
        'method',
        'uri_path',
        'rewritten_uri_path',
        'uri_query',
        'rewritten_uri_query',
        'redirected_uri',
        'server_side_redirect_uri',
        'referer',
        'user_agent',
        'client_device',
        'client_browser',
        'client_os',
        'xff',
        'persistence_used',
        'host',
        'etag',
        'persistent_session_id',
        'request_content_type',
        'response_content_type',
        'request_length',
        'cache_hit',
        'cacheable',
        'network_security_policy_rule_name',
        'http_security_policy_rule_name',
        'http_request_policy_rule_name',
        'http_response_policy_rule_name',
        'pool',
        'pool_name',
        'server_ip',
        'server_name',
        'server_conn_src_ip',
        'server_dest_port',
        'server_src_port',
        'server_rtt',
        'server_response_length',
        'server_response_code',
        'server_response_time_first_byte',
        'server_response_time_last_byte',
        'app_response_time',
        'data_transfer_time',
        'total_time',
        'response_length',
        'response_code',
        'response_time_first_byte',
        'response_time_last_byte',
        'compression_percentage',
        'compression',
        'client_insights',
        'connection_error_info',
        'spdy_version',
        'request_headers',
        'response_headers',
        'request_state',
        'datascript_error_trace',
        'all_request_headers',
        'all_response_headers',
        'user_id',
        'significant_log',
        'datascript_log',
        'microservice',
        'microservice_name',
        'headers_sent_to_server',
        'headers_received_from_server',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'adf': adf_schema,
        'significant': significant_schema,
        'significance': significance_schema,
        'udf': udf_schema,
        'virtualservice': virtualservice_schema,
        'report_timestamp': report_timestamp_schema,
        'service_engine': service_engine_schema,
        'vcpu_id': vcpu_id_schema,
        'log_id': log_id_schema,
        'client_ip': client_ip_schema,
        'client_location': client_location_schema,
        'client_src_port': client_src_port_schema,
        'client_dest_port': client_dest_port_schema,
        'client_rtt': client_rtt_schema,
        'ssl_session_id': ssl_session_id_schema,
        'ssl_version': ssl_version_schema,
        'ssl_cipher': ssl_cipher_schema,
        'http_version': http_version_schema,
        'method': method_schema,
        'uri_path': uri_path_schema,
        'rewritten_uri_path': rewritten_uri_path_schema,
        'uri_query': uri_query_schema,
        'rewritten_uri_query': rewritten_uri_query_schema,
        'redirected_uri': redirected_uri_schema,
        'server_side_redirect_uri': server_side_redirect_uri_schema,
        'referer': referer_schema,
        'user_agent': user_agent_schema,
        'client_device': client_device_schema,
        'client_browser': client_browser_schema,
        'client_os': client_os_schema,
        'xff': xff_schema,
        'persistence_used': persistence_used_schema,
        'host': host_schema,
        'etag': etag_schema,
        'persistent_session_id': persistent_session_id_schema,
        'request_content_type': request_content_type_schema,
        'response_content_type': response_content_type_schema,
        'request_length': request_length_schema,
        'cache_hit': cache_hit_schema,
        'cacheable': cacheable_schema,
        'network_security_policy_rule_name': network_security_policy_rule_name_schema,
        'http_security_policy_rule_name': http_security_policy_rule_name_schema,
        'http_request_policy_rule_name': http_request_policy_rule_name_schema,
        'http_response_policy_rule_name': http_response_policy_rule_name_schema,
        'pool': pool_schema,
        'pool_name': pool_name_schema,
        'server_ip': server_ip_schema,
        'server_name': server_name_schema,
        'server_conn_src_ip': server_conn_src_ip_schema,
        'server_dest_port': server_dest_port_schema,
        'server_src_port': server_src_port_schema,
        'server_rtt': server_rtt_schema,
        'server_response_length': server_response_length_schema,
        'server_response_code': server_response_code_schema,
        'server_response_time_first_byte': server_response_time_first_byte_schema,
        'server_response_time_last_byte': server_response_time_last_byte_schema,
        'app_response_time': app_response_time_schema,
        'data_transfer_time': data_transfer_time_schema,
        'total_time': total_time_schema,
        'response_length': response_length_schema,
        'response_code': response_code_schema,
        'response_time_first_byte': response_time_first_byte_schema,
        'response_time_last_byte': response_time_last_byte_schema,
        'compression_percentage': compression_percentage_schema,
        'compression': compression_schema,
        'client_insights': client_insights_schema,
        'connection_error_info': connection_error_info_schema,
        'spdy_version': spdy_version_schema,
        'request_headers': request_headers_schema,
        'response_headers': response_headers_schema,
        'request_state': request_state_schema,
        'datascript_error_trace': datascript_error_trace_schema,
        'all_request_headers': all_request_headers_schema,
        'all_response_headers': all_response_headers_schema,
        'user_id': user_id_schema,
        'significant_log': significant_log_schema,
        'datascript_log': datascript_log_schema,
        'microservice': microservice_schema,
        'microservice_name': microservice_name_schema,
        'headers_sent_to_server': headers_sent_to_server_schema,
        'headers_received_from_server': headers_received_from_server_schema,
    }
