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


class VsDebugFilter(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    se_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'se_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'se_uuid': se_uuid_schema,
    }




class AutoScaleMgrDebugFilter(object):
    # all schemas
    pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("uuid of the Pool"),
        required=False,
        update_allowed=True,
    )
    intelligent_autoscale_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("period of running intelligent autoscale check"),
        required=False,
        update_allowed=True,
    )
    enable_aws_autoscale_integration_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Enable aws autoscale integration. This is an alpha feature. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'pool_uuid',
        'intelligent_autoscale_period',
        'enable_aws_autoscale_integration',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': pool_uuid_schema,
        'intelligent_autoscale_period': intelligent_autoscale_period_schema,
        'enable_aws_autoscale_integration': enable_aws_autoscale_integration_schema,
    }




class CloudConnectorDebugFilter(object):
    # all schemas
    se_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("filter debugs for a SE"),
        required=False,
        update_allowed=True,
    )
    app_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("filter debugs for an app"),
        required=False,
        update_allowed=True,
    )
    disable_se_reboot_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Disable SE reboot via cloud connector on HB miss"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'se_id',
        'app_id',
        'disable_se_reboot',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'se_id': se_id_schema,
        'app_id': app_id_schema,
        'disable_se_reboot': disable_se_reboot_schema,
    }




class HSMgrDebugFilter(object):
    # all schemas
    metric_entity_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['APPLICATION_METRICS_ENTITY', 'SE_METRICS_ENTITY', 'VM_METRICS_ENTITY', 'CONTROLLER_METRICS_ENTITY', 'TENANT_METRICS_ENTITY', 'VSERVER_METRICS_ENTITY']),
        ],
    )
    entity_schema = properties.Schema(
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
    server_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    skip_hs_db_writes_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'metric_entity',
        'entity',
        'pool',
        'server',
        'period',
        'skip_hs_db_writes',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'metric_entity': metric_entity_schema,
        'entity': entity_schema,
        'pool': pool_schema,
        'server': server_schema,
        'period': period_schema,
        'skip_hs_db_writes': skip_hs_db_writes_schema,
    }




class SeMgrDebugFilter(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
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




class AlertMgrDebugFilter(object):
    # all schemas
    alert_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("filter debugs for an alert id"),
        required=False,
        update_allowed=True,
    )
    alert_objid_schema = properties.Schema(
        properties.Schema.STRING,
        _("filter debugs for entity uuid"),
        required=False,
        update_allowed=True,
    )
    cfg_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("filter debugs for an alert config"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'alert_uuid',
        'alert_objid',
        'cfg_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'alert_uuid': alert_uuid_schema,
        'alert_objid': alert_objid_schema,
        'cfg_uuid': cfg_uuid_schema,
    }




class MesosMetricsDebugFilter(object):
    # all schemas
    metric_entity_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['APPLICATION_METRICS_ENTITY', 'SE_METRICS_ENTITY', 'VM_METRICS_ENTITY', 'CONTROLLER_METRICS_ENTITY', 'TENANT_METRICS_ENTITY', 'VSERVER_METRICS_ENTITY']),
        ],
    )
    mesos_master_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    mesos_slave_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    metrics_collection_frq_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Default: 60)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'metric_entity',
        'mesos_master',
        'mesos_slave',
        'metrics_collection_frq',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'metric_entity': metric_entity_schema,
        'mesos_master': mesos_master_schema,
        'mesos_slave': mesos_slave_schema,
        'metrics_collection_frq': metrics_collection_frq_schema,
    }




class MetricsMgrDebugFilter(object):
    # all schemas
    obj_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    entity_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    skip_metrics_db_writes_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    logging_freq_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    log_first_n_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    metric_instance_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    skip_cluster_map_check_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    disable_hw_training_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    license_grace_period_schema = properties.Schema(
        properties.Schema.STRING,
        _("setting to reduce the grace period for license expiry in hours"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'obj',
        'entity',
        'skip_metrics_db_writes',
        'logging_freq',
        'log_first_n',
        'metric_instance_id',
        'skip_cluster_map_check',
        'disable_hw_training',
        'license_grace_period',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'obj': obj_schema,
        'entity': entity_schema,
        'skip_metrics_db_writes': skip_metrics_db_writes_schema,
        'logging_freq': logging_freq_schema,
        'log_first_n': log_first_n_schema,
        'metric_instance_id': metric_instance_id_schema,
        'skip_cluster_map_check': skip_cluster_map_check_schema,
        'disable_hw_training': disable_hw_training_schema,
        'license_grace_period': license_grace_period_schema,
    }




class StateCacheMgrDebugFilter(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("VirtualService UUID"),
        required=False,
        update_allowed=True,
    )
    pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Pool UUID"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'pool_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'pool_uuid': pool_uuid_schema,
    }




class DebugFilterUnion(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['RPC_INFRA_DEBUG', 'TRANSACTION_DEBUG', 'NSX_AGENT_DEBUG', 'ALERT_MGR_DEBUG', 'VIRTUALSERVICE_DEBUG', 'HS_MGR_DEBUG', 'MESOS_METRICS_DEBUG', 'RES_MGR_DEBUG', 'REDIS_INFRA_DEBUG', 'EVENT_API_DEBUG', 'AUTOSCALE_MGR_DEBUG', 'CLOUD_CONNECTOR_DEBUG', 'TASK_QUEUE_DEBUG', 'VI_MGR_DEBUG', 'SE_MGR_DEBUG', 'SE_AGENT_DEBUG', 'SE_AGENT_METRICS_DEBUG', 'METRICS_MANAGER_DEBUG', 'APIC_AGENT_DEBUG', 'METRICS_MGR_DEBUG', 'STATECACHE_MGR_DEBUG', 'JOB_MGR_DEBUG']),
        ],
    )
    se_mgr_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SeMgrDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    vs_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    metrics_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=MetricsMgrDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    hs_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HSMgrDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    alert_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AlertMgrDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    autoscale_mgr_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AutoScaleMgrDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    cloud_connector_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CloudConnectorDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    mesos_metrics_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=MesosMetricsDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    state_cache_mgr_debug_filter_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=StateCacheMgrDebugFilter.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'type',
        'se_mgr_debug_filter',
        'vs_debug_filter',
        'metrics_debug_filter',
        'hs_debug_filter',
        'alert_debug_filter',
        'autoscale_mgr_debug_filter',
        'cloud_connector_debug_filter',
        'mesos_metrics_debug_filter',
        'state_cache_mgr_debug_filter',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'se_mgr_debug_filter': se_mgr_debug_filter_schema,
        'vs_debug_filter': vs_debug_filter_schema,
        'metrics_debug_filter': metrics_debug_filter_schema,
        'hs_debug_filter': hs_debug_filter_schema,
        'alert_debug_filter': alert_debug_filter_schema,
        'autoscale_mgr_debug_filter': autoscale_mgr_debug_filter_schema,
        'cloud_connector_debug_filter': cloud_connector_debug_filter_schema,
        'mesos_metrics_debug_filter': mesos_metrics_debug_filter_schema,
        'state_cache_mgr_debug_filter': state_cache_mgr_debug_filter_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'mesos_metrics_debug_filter': getattr(MesosMetricsDebugFilter, 'field_references', {}),
        'cloud_connector_debug_filter': getattr(CloudConnectorDebugFilter, 'field_references', {}),
        'metrics_debug_filter': getattr(MetricsMgrDebugFilter, 'field_references', {}),
        'alert_debug_filter': getattr(AlertMgrDebugFilter, 'field_references', {}),
        'se_mgr_debug_filter': getattr(SeMgrDebugFilter, 'field_references', {}),
        'state_cache_mgr_debug_filter': getattr(StateCacheMgrDebugFilter, 'field_references', {}),
        'autoscale_mgr_debug_filter': getattr(AutoScaleMgrDebugFilter, 'field_references', {}),
        'vs_debug_filter': getattr(VsDebugFilter, 'field_references', {}),
        'hs_debug_filter': getattr(HSMgrDebugFilter, 'field_references', {}),
    }



class DebugController(AviResource):
    resource_name = "debugcontroller"
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
    sub_module_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['RPC_INFRA_DEBUG', 'TRANSACTION_DEBUG', 'NSX_AGENT_DEBUG', 'ALERT_MGR_DEBUG', 'VIRTUALSERVICE_DEBUG', 'HS_MGR_DEBUG', 'MESOS_METRICS_DEBUG', 'RES_MGR_DEBUG', 'REDIS_INFRA_DEBUG', 'EVENT_API_DEBUG', 'AUTOSCALE_MGR_DEBUG', 'CLOUD_CONNECTOR_DEBUG', 'TASK_QUEUE_DEBUG', 'VI_MGR_DEBUG', 'SE_MGR_DEBUG', 'SE_AGENT_DEBUG', 'SE_AGENT_METRICS_DEBUG', 'METRICS_MANAGER_DEBUG', 'APIC_AGENT_DEBUG', 'METRICS_MGR_DEBUG', 'STATECACHE_MGR_DEBUG', 'JOB_MGR_DEBUG']),
        ],
    )
    trace_level_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['TRACE_LEVEL_DEBUG', 'TRACE_LEVEL_ERROR', 'TRACE_LEVEL_DISABLED', 'TRACE_LEVEL_DEBUG_DETAIL']),
        ],
    )
    log_level_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LOG_LEVEL_ERROR', 'LOG_LEVEL_DISABLED', 'LOG_LEVEL_INFO', 'LOG_LEVEL_WARNING']),
        ],
    )
    filters_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugFilterUnion.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'version',
        'name',
        'sub_module',
        'trace_level',
        'log_level',
        'filters',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'version': version_schema,
        'name': name_schema,
        'sub_module': sub_module_schema,
        'trace_level': trace_level_schema,
        'log_level': log_level_schema,
        'filters': filters_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'filters': getattr(DebugFilterUnion, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::DebugController': DebugController,
    }

