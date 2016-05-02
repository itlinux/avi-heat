# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from common import *
from vs import *
from options import *
from debug_se import *
from analytics_policy import *
from pool import *


class VsSeAssigned(AviResource):
    resource_name = "vsseassigned"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    primary_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    standby_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    connected_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=True,
        update_allowed=True,
    )
    scalein_in_progress_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    oper_status_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=OperationalStatus.properties_schema,
        required=False,
        update_allowed=True,
    )
    snat_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'primary',
        'standby',
        'connected',
        'scalein_in_progress',
        'oper_status',
        'snat_ip',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'primary': primary_schema,
        'standby': standby_schema,
        'connected': connected_schema,
        'scalein_in_progress': scalein_in_progress_schema,
        'oper_status': oper_status_schema,
        'snat_ip': snat_ip_schema,
    }


class VsPlacementResolutionInfo(object):
    # all schemas
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    networks_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DiscoveredNetwork.properties_schema,
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
        'ip',
        'pool_uuid',
        'networks',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip': ip_schema,
        'pool_uuid': pool_uuid_schema,
        'networks': networks_schema,
    }


class ScaleStatus(object):
    # all schemas
    state_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    reason_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    reason_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=reason_item_schema,
        required=False,
        update_allowed=True,
    )
    reason_code_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    start_time_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TimeStamp.properties_schema,
        required=False,
        update_allowed=True,
    )
    end_time_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TimeStamp.properties_schema,
        required=False,
        update_allowed=True,
    )
    scale_se_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_se_requested_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_se_assigned_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    reason_code_string_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    vs_placement_resolution_info_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsPlacementResolutionInfo.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'state',
        'reason',
        'reason_code',
        'start_time',
        'end_time',
        'scale_se',
        'num_se_requested',
        'num_se_assigned',
        'reason_code_string',
        'vs_placement_resolution_info',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'state': state_schema,
        'reason': reason_schema,
        'reason_code': reason_code_schema,
        'start_time': start_time_schema,
        'end_time': end_time_schema,
        'scale_se': scale_se_schema,
        'num_se_requested': num_se_requested_schema,
        'num_se_assigned': num_se_assigned_schema,
        'reason_code_string': reason_code_string_schema,
        'vs_placement_resolution_info': vs_placement_resolution_info_schema,
    }


class VirtualServiceRuntime(AviResource):
    resource_name = "virtualserviceruntime"
    # all schemas
    fsm_state_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    fsm_state_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    last_req_type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    last_req_rc_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    datapath_debug_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugVirtualService.properties_schema,
        required=False,
        update_allowed=True,
    )
    scaleout_in_progress_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    scalein_in_progress_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    servers_configured_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    rules_configured_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    one_plus_one_ha_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    apic_extension_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsApicExtension.properties_schema,
        required=False,
        update_allowed=True,
    )
    last_changed_time_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TimeStamp.properties_schema,
        required=False,
        update_allowed=True,
    )
    controller_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    prev_controller_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    migrate_in_progress_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    marked_for_delete_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    migrate_request_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsMigrateParams.properties_schema,
        required=False,
        update_allowed=True,
    )
    user_scaleout_pending_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    scale_status_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ScaleStatus.properties_schema,
        required=False,
        update_allowed=True,
    )
    progress_percent_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    scale_history_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ScaleStatus.properties_schema,
        required=True,
        update_allowed=False,
    )
    scale_history_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=scale_history_item_schema,
        required=False,
        update_allowed=True,
    )
    metrics_mgr_port_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    prev_metrics_mgr_port_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    manual_placement_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    se_create_in_progress_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    initial_placement_in_progress_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    scalein_request_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsScaleinParams.properties_schema,
        required=False,
        update_allowed=True,
    )
    upgrade_in_progress_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    first_time_placement_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    migrate_scaleout_pending_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    migrate_scalein_pending_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    initial_placement_request_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsInitialPlacementParams.properties_schema,
        required=False,
        update_allowed=True,
    )
    initial_placement_se_params_index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    assigned_static_se_uuid_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    assigned_static_se_uuid_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=assigned_static_se_uuid_item_schema,
        required=False,
        update_allowed=True,
    )
    requested_static_se_uuid_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    requested_static_se_uuid_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=requested_static_se_uuid_item_schema,
        required=False,
        update_allowed=True,
    )
    vh_child_vs_uuid_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    vh_child_vs_uuid_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=vh_child_vs_uuid_item_schema,
        required=False,
        update_allowed=True,
    )
    se_list_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SeList.properties_schema,
        required=True,
        update_allowed=False,
    )
    se_list_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_list_item_schema,
        required=False,
        update_allowed=True,
    )
    requested_resource_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceResource.properties_schema,
        required=False,
        update_allowed=True,
    )
    redis_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    redis_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    redis_db_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    tls_ticket_key_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TLSTicket.properties_schema,
        required=True,
        update_allowed=False,
    )
    tls_ticket_key_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=tls_ticket_key_item_schema,
        required=False,
        update_allowed=True,
    )
    lif_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    lif_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=lif_item_schema,
        required=False,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    supp_runtime_status_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=OperationalStatus.properties_schema,
        required=False,
        update_allowed=True,
    )
    first_se_assigned_time_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TimeStamp.properties_schema,
        required=False,
        update_allowed=True,
    )
    east_west_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_additional_se_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'fsm_state_name',
        'fsm_state_id',
        'last_req_type',
        'last_req_rc',
        'datapath_debug',
        'scaleout_in_progress',
        'scalein_in_progress',
        'servers_configured',
        'rules_configured',
        'one_plus_one_ha',
        'apic_extension',
        'last_changed_time',
        'controller_ip',
        'prev_controller_ip',
        'migrate_in_progress',
        'marked_for_delete',
        'migrate_request',
        'user_scaleout_pending',
        'scale_status',
        'progress_percent',
        'scale_history',
        'metrics_mgr_port',
        'prev_metrics_mgr_port',
        'manual_placement',
        'se_create_in_progress',
        'initial_placement_in_progress',
        'scalein_request',
        'upgrade_in_progress',
        'first_time_placement',
        'migrate_scaleout_pending',
        'migrate_scalein_pending',
        'initial_placement_request',
        'initial_placement_se_params_index',
        'assigned_static_se_uuid',
        'requested_static_se_uuid',
        'vh_child_vs_uuid',
        'se_list',
        'requested_resource',
        'redis_ip',
        'redis_port',
        'redis_db',
        'tls_ticket_key',
        'lif',
        'type',
        'supp_runtime_status',
        'first_se_assigned_time',
        'east_west',
        'num_additional_se',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'fsm_state_name': fsm_state_name_schema,
        'fsm_state_id': fsm_state_id_schema,
        'last_req_type': last_req_type_schema,
        'last_req_rc': last_req_rc_schema,
        'datapath_debug': datapath_debug_schema,
        'scaleout_in_progress': scaleout_in_progress_schema,
        'scalein_in_progress': scalein_in_progress_schema,
        'servers_configured': servers_configured_schema,
        'rules_configured': rules_configured_schema,
        'one_plus_one_ha': one_plus_one_ha_schema,
        'apic_extension': apic_extension_schema,
        'last_changed_time': last_changed_time_schema,
        'controller_ip': controller_ip_schema,
        'prev_controller_ip': prev_controller_ip_schema,
        'migrate_in_progress': migrate_in_progress_schema,
        'marked_for_delete': marked_for_delete_schema,
        'migrate_request': migrate_request_schema,
        'user_scaleout_pending': user_scaleout_pending_schema,
        'scale_status': scale_status_schema,
        'progress_percent': progress_percent_schema,
        'scale_history': scale_history_schema,
        'metrics_mgr_port': metrics_mgr_port_schema,
        'prev_metrics_mgr_port': prev_metrics_mgr_port_schema,
        'manual_placement': manual_placement_schema,
        'se_create_in_progress': se_create_in_progress_schema,
        'initial_placement_in_progress': initial_placement_in_progress_schema,
        'scalein_request': scalein_request_schema,
        'upgrade_in_progress': upgrade_in_progress_schema,
        'first_time_placement': first_time_placement_schema,
        'migrate_scaleout_pending': migrate_scaleout_pending_schema,
        'migrate_scalein_pending': migrate_scalein_pending_schema,
        'initial_placement_request': initial_placement_request_schema,
        'initial_placement_se_params_index': initial_placement_se_params_index_schema,
        'assigned_static_se_uuid': assigned_static_se_uuid_schema,
        'requested_static_se_uuid': requested_static_se_uuid_schema,
        'vh_child_vs_uuid': vh_child_vs_uuid_schema,
        'se_list': se_list_schema,
        'requested_resource': requested_resource_schema,
        'redis_ip': redis_ip_schema,
        'redis_port': redis_port_schema,
        'redis_db': redis_db_schema,
        'tls_ticket_key': tls_ticket_key_schema,
        'lif': lif_schema,
        'type': type_schema,
        'supp_runtime_status': supp_runtime_status_schema,
        'first_se_assigned_time': first_se_assigned_time_schema,
        'east_west': east_west_schema,
        'num_additional_se': num_additional_se_schema,
    }


def resource_mapping():
    return {
        'Avi::VirtualServiceRuntime': VirtualServiceRuntime,
        'Avi::VsSeAssigned': VsSeAssigned,
    }

