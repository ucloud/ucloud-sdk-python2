# -*- coding: utf-8 -*-

from ucloud.core.client import Client
from ucloud.services.udb.schemas import apis


class UDBClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(UDBClient, self).__init__(config, transport, middleware, logger)

    def backup_udb_instance(self, req=None, **kwargs):
        """ BackupUDBInstance - 备份UDB实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupName** (str) - (Required) 备份名称
        - **DBId** (str) - (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        - **BackupMethod** (str) - 使用的备份方式。（快照备份即物理备份。注意只有SSD版本的mysql实例支持设置为snapshot）
        - **Blacklist** (str) - 备份黑名单列表，以 ; 分隔。注意：只有逻辑备份下备份黑名单才生效，快照备份备份黑名单下无效
        - **ForceBackup** (bool) - true表示逻辑备份时是使用 --force 参数，false表示不使用 --force 参数。物理备份此参数无效。
        - **UseBlacklist** (bool) - 是否使用黑名单备份，默认false
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("BackupUDBInstance", d, **kwargs)
        return apis.BackupUDBInstanceResponseSchema().loads(resp)

    def backup_udb_instance_binlog(self, req=None, **kwargs):
        """ BackupUDBInstanceBinlog - 备份UDB指定时间段的binlog列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupFile** (str) - (Required) 需要备份文件,可通过DescribeUDBInstanceBinlog获得 如果要传入多个文件名，以空格键分割,用单引号包含.
        - **DBId** (str) - (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        - **BackupName** (str) - DB备份文件名称
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceBinlogRequestSchema().dumps(d)
        resp = self.invoke("BackupUDBInstanceBinlog", d, **kwargs)
        return apis.BackupUDBInstanceBinlogResponseSchema().loads(resp)

    def backup_udb_instance_error_log(self, req=None, **kwargs):
        """ BackupUDBInstanceErrorLog - 备份UDB指定时间段的errorlog

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupName** (str) - (Required) 备份名称
        - **DBId** (str) - (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceErrorLogRequestSchema().dumps(d)
        resp = self.invoke("BackupUDBInstanceErrorLog", d, **kwargs)
        return apis.BackupUDBInstanceErrorLogResponseSchema().loads(resp)

    def backup_udb_instance_slow_log(self, req=None, **kwargs):
        """ BackupUDBInstanceSlowLog - 备份UDB指定时间段的slowlog分析结果

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupName** (str) - (Required) 备份文件名称
        - **BeginTime** (int) - (Required) 过滤条件:起始时间(时间戳)
        - **DBId** (str) - (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        - **EndTime** (int) - (Required) 过滤条件:结束时间(时间戳)
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BackupUDBInstanceSlowLogRequestSchema().dumps(d)
        resp = self.invoke("BackupUDBInstanceSlowLog", d, **kwargs)
        return apis.BackupUDBInstanceSlowLogResponseSchema().loads(resp)

    def check_recover_udb_instance(self, req=None, **kwargs):
        """ CheckRecoverUDBInstance - 核查db是否可以使用回档功能

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SrcDBId** (str) - (Required) 源实例的Id(只支持普通版DB不支持高可用)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **LastestTime** (int) - 核查成功返回值为可以回档到的最近时刻,核查失败不返回
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CheckRecoverUDBInstanceRequestSchema().dumps(d)
        resp = self.invoke("CheckRecoverUDBInstance", d, **kwargs)
        return apis.CheckRecoverUDBInstanceResponseSchema().loads(resp)

    def check_udb_instance_to_ha_allowance(self, req=None, **kwargs):
        """ CheckUDBInstanceToHAAllowance - 核查db是否可以升级为高可用

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        
        **Response**

        - **Allowance** (str) - Yes ，No ，Yes即可以升级，No为不可以升级
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CheckUDBInstanceToHAAllowanceRequestSchema().dumps(d)
        resp = self.invoke("CheckUDBInstanceToHAAllowance", d, **kwargs)
        return apis.CheckUDBInstanceToHAAllowanceResponseSchema().loads(resp)

    def clear_udb_log(self, req=None, **kwargs):
        """ ClearUDBLog - 清除UDB实例的log

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) DB实例的id,该值可以通过DescribeUDBInstance获取
        - **LogType** (int) - (Required) 日志类型，10-error（暂不支持）、20-slow（暂不支持 ）、30-binlog
        - **BeforeTime** (int) - 删除时间点(至少前一天)之前log，采用时间戳(秒)，默认当 前时间点前一天
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ClearUDBLogRequestSchema().dumps(d)
        resp = self.invoke("ClearUDBLog", d, **kwargs)
        return apis.ClearUDBLogResponseSchema().loads(resp)

    def create_udb_instance(self, req=None, **kwargs):
        """ CreateUDBInstance - 创建UDB实例（包括创建mysql master节点、mongodb primary/configsvr节点和从备份恢复实例）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **AdminPassword** (str) - (Required) 管理员密码
        - **DBTypeId** (str) - (Required) DB类型id，mysql/mongodb/postgesql按版本细分 1：mysql-5.1，2：mysql-5.5，3：percona-5.5，4：mysql-5.6，5：percona-5.6，6：mysql-5.7，7：percona-5.7，8：mariadb-10.0，9：mongodb-2.4，10：mongodb-2.6，11：mongodb-3.0，12：mongodb-3.2,13：postgresql-9.4，14：postgresql-9.6，14：postgresql-10.4
        - **DiskSpace** (int) - (Required) 磁盘空间(GB), 暂时支持20G - 3000G
        - **MemoryLimit** (int) - (Required) 内存限制(MB)，目前支持以下几档 1000M/2000M/4000M/ 6000M/8000M/12000M/16000M/ 24000M/32000M/48000M/ 64000M/96000M
        - **Name** (str) - (Required) 实例名称，至少6位
        - **ParamGroupId** (int) - (Required) DB实例使用的配置参数组id
        - **Port** (int) - (Required) 端口号，mysql默认3306，mongodb默认27017，postgresql默认5432
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **AdminUser** (str) - 管理员帐户名，默认root
        - **BackupCount** (int) - 备份策略，每周备份数量，默认7次
        - **BackupDuration** (int) - 备份策略，备份时间间隔，单位小时计，默认24小时
        - **BackupId** (int) - 备份id，如果指定，则表明从备份恢复实例
        - **BackupTime** (int) - 备份策略，备份开始时间，单位小时计，默认1点
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区，参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **CPU** (int) - cpu核数
        - **ChargeType** (str) - Year， Month， Dynamic，Trial，默认: Month
        - **ClusterRole** (str) - 当DB类型(DBTypeId)为mongodb时，需要指定mongo的角色，可选值为configsrv (配置节点)，shardsrv (数据节点)
        - **CouponId** (str) - 使用的代金券id
        - **DisableSemisync** (bool) - 是否开启异步高可用，默认不填，可置为true
        - **HAArch** (str) - 高可用架构:1） haproxy（默认）: 当前仅支持mysql。2） sentinel: 基于vip和哨兵节点的架构，当前支持mysql和pg。
        - **InstanceMode** (str) - UDB实例模式类型, 可选值如下: "Normal": 普通版UDB实例 "HA": 高可用版UDB实例 默认是"Normal"
        - **InstanceType** (str) - UDB数据库机型
        - **Quantity** (int) - 购买时长，默认值1
        - **SSDType** (str) - SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        - **SubnetId** (str) - 子网ID
        - **Tag** (str) - 
        - **UDBCId** (str) - 专区ID信息（如果这个参数存在这说明是在专区中创建DB）
        - **UseSSD** (bool) - 是否使用SSD，默认为false。目前主要可用区、海外机房、新机房只提供SSD资源，非SSD资源不再提供。
        - **VPCId** (str) - VPC的ID
        
        **Response**

        - **DBId** (str) - BD实例id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBInstanceRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDBInstance", d, **kwargs)
        return apis.CreateUDBInstanceResponseSchema().loads(resp)

    def create_udb_instance_by_recovery(self, req=None, **kwargs):
        """ CreateUDBInstanceByRecovery - 创建db，将新创建的db恢复到指定db某个指定时间点

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 实例名称，至少6位
        - **RecoveryTime** (int) - (Required) 恢复到某个时间点的时间戳(UTC时间格式，默认单位秒)
        - **SrcDBId** (str) - (Required) 源实例的Id
        - **ChargeType** (str) - Year， Month， Dynamic，Trial，默认: Dynamic
        - **CouponId** (str) - 使用的代金券id
        - **Quantity** (int) - 购买时长，默认值1
        - **SubnetId** (str) - 子网ID
        - **UDBCId** (str) - 专区的Id
        - **UseSSD** (bool) - 指定是否是否使用SSD，默认使用主库的配置
        - **VPCId** (str) - VPC的ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DBId** (str) - db实例id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBInstanceByRecoveryRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDBInstanceByRecovery", d, **kwargs)
        return apis.CreateUDBInstanceByRecoveryResponseSchema().loads(resp)

    def create_udb_param_group(self, req=None, **kwargs):
        """ CreateUDBParamGroup - 从已有配置文件创建新配置文件

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBTypeId** (str) - (Required) DB类型id，mysql/mongodb/postgesql按版本细分 1：mysql-5.1，2：mysql-5.5，3：percona-5.5，4：mysql-5.6，5：percona-5.6，6：mysql-5.7，7：percona-5.7，8：mariadb-10.0，9：mongodb-2.4，10：mongodb-2.6，11：mongodb-3.0，12：mongodb-3.2,13：postgresql-9.4，14：postgresql-9.6
        - **Description** (str) - (Required) 参数组描述
        - **GroupName** (str) - (Required) 新配置参数组名称
        - **SrcGroupId** (int) - (Required) 源参数组id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **RegionFlag** (bool) - 是否是地域级别的配置文件，默认是false
        
        **Response**

        - **GroupId** (int) - 新配置参数组id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBParamGroupRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDBParamGroup", d, **kwargs)
        return apis.CreateUDBParamGroupResponseSchema().loads(resp)

    def create_udb_replication_instance(self, req=None, **kwargs):
        """ CreateUDBReplicationInstance - 创建MongoDB的副本节点（包括仲裁）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 实例名称，至少6位
        - **SrcId** (str) - (Required) primary节点的DBId,该值可以通过DescribeUDBInstance获取
        - **CouponId** (str) - 使用的代金券id
        - **IsArbiter** (bool) - 是否是仲裁节点，默认false，仲裁节点按最小机型创建
        - **Port** (int) - 端口号，默认27017，取值范围3306至65535。
        - **UseSSD** (bool) - 是否使用SSD，默认不使用
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DBId** (str) - 创建从节点的DBId
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBReplicationInstanceRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDBReplicationInstance", d, **kwargs)
        return apis.CreateUDBReplicationInstanceResponseSchema().loads(resp)

    def create_udb_route_instance(self, req=None, **kwargs):
        """ CreateUDBRouteInstance - 创建mongos实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ConfigsvrId** (list) - (Required) 配置服务器的dbid，允许一个或者三个。
        - **DBTypeId** (str) - (Required) DB类型id，mongodb按版本细分有1：mongodb-2.4，2：mongodb-2.6,3：mongodb-3.0，4：mongodb-3.2
        - **DiskSpace** (int) - (Required) 磁盘空间(GB), 暂时支持20G - 500G
        - **MemoryLimit** (int) - (Required) 内存限制(MB)，目前支持以下几档 600M/1500M/3000M /6000M/15000M/30000M
        - **Name** (str) - (Required) 实例名称，至少6位
        - **ParamGroupId** (int) - (Required) DB实例使用的配置参数组id
        - **Port** (int) - (Required) 端口号，mongodb默认27017
        - **ChargeType** (str) - Year， Month， Dynamic，Trial，默认: Month
        - **CouponId** (str) - 使用的代金券id
        - **Quantity** (int) - 购买时长，默认值1
        - **UseSSD** (bool) - 是否使用SSD，默认为false
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DBId** (str) - db实例id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBRouteInstanceRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDBRouteInstance", d, **kwargs)
        return apis.CreateUDBRouteInstanceResponseSchema().loads(resp)

    def create_udb_slave(self, req=None, **kwargs):
        """ CreateUDBSlave - 创建UDB实例的slave

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 实例名称，至少6位
        - **SrcId** (str) - (Required) master实例的DBId,该值可以通过DescribeUDBInstance获取
        - **CouponId** (str) - 使用的代金券id
        - **DiskSpace** (int) - 磁盘空间(GB), 暂时支持20G - 3000G（API支持，前端暂时只开放内存定制）
        - **InstanceMode** (str) - UDB实例部署模式，可选值如下：Normal: 普通单点实例HA: 高可用部署实例
        - **InstanceType** (str) - UDB实例类型：Normal和SATA_SSD
        - **IsLock** (bool) - 是否锁主库，默认为true
        - **MemoryLimit** (int) - 内存限制(MB)，目前支持以下几档 1000M/2000M/4000M/ 6000M/8000M/12000M/16000M/ 24000M/32000M/48000M/ 64000M/96000M
        - **Port** (int) - 端口号，mysql默认3306
        - **SSDType** (str) - SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        - **UseSSD** (bool) - 是否使用SSD，默认为false
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DBId** (str) - 创建slave的DBId
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDBSlaveRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDBSlave", d, **kwargs)
        return apis.CreateUDBSlaveResponseSchema().loads(resp)

    def delete_udb_backup(self, req=None, **kwargs):
        """ DeleteUDBBackup - 删除UDB实例备份

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (int) - (Required) 备份id，可通过DescribeUDBBackup获得
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区，参见［可用区列表］
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBBackupRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDBBackup", d, **kwargs)
        return apis.DeleteUDBBackupResponseSchema().loads(resp)

    def delete_udb_instance(self, req=None, **kwargs):
        """ DeleteUDBInstance - 删除UDB实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) DB实例的id,该值可以通过DescribeUDBInstance获取
        - **UDBCId** (str) - 专区ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBInstanceRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDBInstance", d, **kwargs)
        return apis.DeleteUDBInstanceResponseSchema().loads(resp)

    def delete_udb_log_package(self, req=None, **kwargs):
        """ DeleteUDBLogPackage - 删除UDB日志包

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (int) - (Required) 日志包id，可通过DescribeUDBLogPackage获得
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBLogPackageRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDBLogPackage", d, **kwargs)
        return apis.DeleteUDBLogPackageResponseSchema().loads(resp)

    def delete_udb_param_group(self, req=None, **kwargs):
        """ DeleteUDBParamGroup - 删除配置参数组

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (int) - (Required) 参数组id,可通过DescribeUDBParamGroup获取
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **RegionFlag** (bool) - 是否属于地域级别
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDBParamGroupRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDBParamGroup", d, **kwargs)
        return apis.DeleteUDBParamGroupResponseSchema().loads(resp)

    def describe_udb_backup(self, req=None, **kwargs):
        """ DescribeUDBBackup - 列表UDB实例备份信息.Zone不填表示多可用区，填代表单可用区

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - (Required) 分页显示的条目数，列表操作则指定
        - **Offset** (int) - (Required) 分页显示的起始偏移，列表操作则指定
        - **BackupId** (int) - 如果填了BackupId, 那么只拉取这个备份的记录
        - **BackupType** (int) - 备份类型,取值为0或1，0表示自动，1表示手动
        - **BeginTime** (int) - 过滤条件:起始时间(Unix时间戳)
        - **ClassType** (str) - 如果未指定GroupId，则可选是否选取特定DB类型的配置(sql, nosql, postgresql, sqlserver)
        - **DBId** (str) - DB实例Id，如果指定，则只获取该db的备份信息 该值可以通过DescribeUDBInstance获取
        - **EndTime** (int) - 过滤条件:结束时间(Unix时间戳)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DataSet** (list) - 见 **UDBBackupSet** 模型定义
        - **TotalCount** (int) - 满足条件备份总数，如果指定dbid，则是该db备份总数
        
        **Response Model**
        
        **UDBBackupSet** 
        
        - **DBId** (str) - dbid
        - **BackupEndTime** (int) - 备份完成时间(Unix时间戳)
        - **BackupTime** (int) - 备份时间(Unix时间戳)
        - **BackupSize** (int) - 备份文件大小(字节)
        - **BackupType** (int) - 备份类型,取值为0或1,0表示自动，1表示手动
        - **State** (str) - 备份状态 Backuping // 备份中 Success // 备份成功 Failed // 备份失败 Expired // 备份过期
        - **ErrorInfo** (str) - 备份错误信息
        - **DBName** (str) - 对应的db名称
        - **BackupZone** (str) - 跨机房高可用备库所在可用区
        - **Zone** (str) - 备份所在可用区
        - **BackupId** (int) - 备份id
        - **BackupName** (str) - 备份名称

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBBackupRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBBackup", d, **kwargs)
        return apis.DescribeUDBBackupResponseSchema().loads(resp)

    def describe_udb_backup_blacklist(self, req=None, **kwargs):
        """ DescribeUDBBackupBlacklist - 获取UDB实例的备份黑名单

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **Blacklist** (str) - DB的黑名单列表, db.%为指定库 dbname.tablename为指定表
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBBackupBlacklistRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBBackupBlacklist", d, **kwargs)
        return apis.DescribeUDBBackupBlacklistResponseSchema().loads(resp)

    def describe_udb_binlog_backup_url(self, req=None, **kwargs):
        """ DescribeUDBBinlogBackupURL - 获取UDB的Binlog备份地址

        **Request**

        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (int) - (Required) DB实例备份ID
        - **DBId** (str) - (Required) DB实例Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **BackupPath** (str) - DB实例备份文件的公网地址
        - **InnerBackupPath** (str) - DB实例备份文件的内网地址
        
        """
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBBinlogBackupURLRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBBinlogBackupURL", d, **kwargs)
        return apis.DescribeUDBBinlogBackupURLResponseSchema().loads(resp)

    def describe_udb_instance(self, req=None, **kwargs):
        """ DescribeUDBInstance - 获取UDB实例信息，支持两类操作：（1）指定DBId用于获取该db的信息；（2）指定ClassType、Offset、Limit用于列表操作，查询某一个类型db。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ClassType** (str) - (Required) DB种类，如果是列表操作，则需要指定,不区分大小写，其取值如下：mysql: SQL；mongo: NOSQL；postgresql: postgresql
        - **Limit** (int) - (Required) 分页显示数量，列表操作则指定
        - **Offset** (int) - (Required) 分页显示起始偏移位置，列表操作则指定
        - **DBId** (str) - DB实例id，如果指定则获取描述，否则为列表操作， 指定Offset/Limit/ClassType DBId可通过DescribeUDBInstance获取
        - **IncludeSlaves** (bool) - 当只获取这个特定DBId的信息时，如果有该选项，那么把这个DBId实例的所有从库信息一起拉取并返回
        - **IsInUDBC** (bool) - 是否查看专区里面DB
        - **UDBCId** (str) - IsInUDBC为True,UDBCId为空，说明查看整个可用区的专区的db，如果UDBId不为空则只查看此专区下面的db
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DataSet** (list) - 见 **UDBInstanceSet** 模型定义
        - **TotalCount** (int) - 用户db组的数量，对于 mysql: 主从结对数量，没有slave，则只有master mongodb: 副本集数量
        
        **Response Model**
        
        **UDBSlaveInstanceSet** 
        
        - **VirtualIPMac** (str) - DB实例虚ip的mac地址
        - **CreateTime** (int) - DB实例创建时间，采用UTC计时时间戳
        - **SubnetId** (str) - 子网ID
        - **BackupBlacklist** (str) - 备份策略，备份黑名单，mongodb则不适用
        - **ModifyTime** (int) - DB实例修改时间，采用UTC计时时间戳
        - **UseSSD** (bool) - 是否使用SSD
        - **InstanceTypeId** (int) - UDB数据库机型ID
        - **Tag** (str) - 获取资源其他信息
        - **Zone** (str) - 可用区
        - **DBId** (str) - DB实例id
        - **BackupCount** (int) - 备份策略，不可修改，备份文件保留的数量，默认7次
        - **SystemFileSize** (float) - DB实例系统文件大小，单位GB
        - **VPCId** (str) - VPC的ID
        - **State** (str) - DB状态标记 Init：初始化中，Fail：安装失败，Starting：启动中，Running：运行，Shutdown：关闭中，Shutoff：已关闭，Delete：已删除，Upgrading：升级中，Promoting：提升为独库进行中，Recovering：恢复中，Recover fail：恢复失败
        - **SSDType** (str) - SSD类型，SATA/PCI-E
        - **Role** (str) - DB实例角色，mysql区分master/slave，mongodb多种角色
        - **ClusterRole** (str) - 当DB类型为mongodb时，返回该实例所在集群中的角色，包括：mongos、configsrv_sccc、configsrv_csrs、shardsrv_datanode、shardsrv_arbiter，其中congfigsrv分为sccc和csrs两种模式，shardsrv分为datanode和arbiter两种模式
        - **ParamGroupId** (int) - DB实例使用的配置参数组id
        - **DataFileSize** (float) - DB实例数据文件大小，单位GB
        - **BackupDate** (str) - 备份日期标记位。共7位,每一位为一周中一天的备份情况 0表示关闭当天备份,1表示打开当天备份。最右边的一位 为星期天的备份开关，其余从右到左依次为星期一到星期 六的备份配置开关，每周必须至少设置两天备份。 例如：1100000 表示打开星期六和星期五的自动备份功能
        - **DiskUsedSize** (float) - DB实例磁盘已使用空间，单位GB
        - **LogFileSize** (float) - DB实例日志文件大小，单位GB
        - **InstanceMode** (str) - UDB实例模式类型, 可选值如下: "Normal": 普通版UDB实例;"HA": 高可用版UDB实例
        - **DiskSpace** (int) - 磁盘空间(GB), 默认根据配置机型
        - **InstanceType** (str) - UDB数据库机型
        - **Name** (str) - 实例名称，至少6位
        - **BackupDuration** (int) - 备份策略，一天内备份时间间隔，单位小时，默认24小时
        - **ExpiredTime** (int) - DB实例过期时间，采用UTC计时时间戳
        - **VirtualIP** (str) - DB实例虚ip
        - **Port** (int) - 端口号，mysql默认3306，mongodb默认27017
        - **ChargeType** (str) - Year， Month， Dynamic，Trial，默认: Dynamic
        - **BackupBeginTime** (int) - 备份策略，不可修改，开始时间，单位小时计，默认3点
        - **MemoryLimit** (int) - 内存限制(MB)，默认根据配置机型
        - **DBTypeId** (str) - DB类型id，mysql/mongodb按版本细分各有一个id 目前id的取值范围为[1,7],数值对应的版本如下： 1：mysql-5.5，2：mysql-5.1，3：percona-5.5 4：mongodb-2.4，5：mongodb-2.6，6：mysql-5.6， 7：percona-5.6
        - **AdminUser** (str) - 管理员帐户名，默认root
        - **SrcDBId** (str) - 对mysql的slave而言是master的DBId，对master则为空， 对mongodb则是副本集id

        **UDBInstanceSet** 
        
        - **Role** (str) - DB实例角色，mysql区分master/slave，mongodb多种角色
        - **SubnetId** (str) - 子网ID
        - **InstanceTypeId** (int) - UDB数据库机型ID
        - **DiskSpace** (int) - 磁盘空间(GB), 默认根据配置机型
        - **State** (str) - DB状态标记 Init：初始化中，Fail：安装失败，Starting：启动中，Running：运行，Shutdown：关闭中，Shutoff：已关闭，Delete：已删除，Upgrading：升级中，Promoting：提升为独库进行中，Recovering：恢复中，Recover fail：恢复失败
        - **ModifyTime** (int) - DB实例修改时间，采用UTC计时时间戳
        - **ChargeType** (str) - Year， Month， Dynamic，Trial，默认: Dynamic
        - **Port** (int) - 端口号，mysql默认3306，mongodb默认27017
        - **SrcDBId** (str) - 对mysql的slave而言是master的DBId，对master则为空， 对mongodb则是副本集id
        - **BackupCount** (int) - 备份策略，不可修改，备份文件保留的数量，默认7次
        - **SystemFileSize** (float) - DB实例系统文件大小，单位GB
        - **LogFileSize** (float) - DB实例日志文件大小，单位GB
        - **Name** (str) - 实例名称，至少6位
        - **ParamGroupId** (int) - DB实例使用的配置参数组id
        - **VPCId** (str) - VPC的ID
        - **DataSet** (list) - 见 **UDBSlaveInstanceSet** 模型定义
        - **InstanceType** (str) - UDB数据库机型
        - **ExpiredTime** (int) - DB实例过期时间，采用UTC计时时间戳
        - **InstanceMode** (str) - UDB实例模式类型, 可选值如下: “Normal”： 普通版UDB实例 “HA”: 高可用版UDB实例
        - **BackupDuration** (int) - 备份策略，一天内备份时间间隔，单位小时，默认24小时
        - **BackupDate** (str) - 备份日期标记位。共7位,每一位为一周中一天的备份情况 0表示关闭当天备份,1表示打开当天备份。最右边的一位 为星期天的备份开关，其余从右到左依次为星期一到星期 六的备份配置开关，每周必须至少设置两天备份。 例如：1100000 表示打开星期六和星期五的自动备份功能
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区
        - **Tag** (str) - 获取资源其他信息
        - **BackupBeginTime** (int) - 备份策略，不可修改，开始时间，单位小时计，默认3点
        - **BackupBlacklist** (str) - 备份策略，备份黑名单，mongodb则不适用
        - **CreateTime** (int) - DB实例创建时间，采用UTC计时时间戳
        - **UseSSD** (bool) - 是否使用SSD
        - **DBTypeId** (str) - DB类型id，mysql/mongodb按版本细分各有一个id 目前id的取值范围为[1,7],数值对应的版本如下： 1：mysql-5.5，2：mysql-5.1，3：percona-5.5 4：mongodb-2.4，5：mongodb-2.6，6：mysql-5.6， 7：percona-5.6
        - **VirtualIP** (str) - DB实例虚ip
        - **VirtualIPMac** (str) - DB实例虚ip的mac地址
        - **SSDType** (str) - SSD类型，SATA/PCI-E
        - **DiskUsedSize** (float) - DB实例磁盘已使用空间，单位GB
        - **AdminUser** (str) - 管理员帐户名，默认root
        - **MemoryLimit** (int) - 内存限制(MB)，默认根据配置机型
        - **DataFileSize** (float) - DB实例数据文件大小，单位GB
        - **Zone** (str) - DB实例所在可用区
        - **CluserRole** (str) - 当DB类型为mongodb时，返回该实例所在集群中的角色，包括：mongos、configsrv_sccc、configsrv_csrs、shardsrv_datanode、shardsrv_arbiter，其中congfigsrv分为sccc和csrs两种模式，shardsrv分为datanode和arbiter两种模式
        - **DBId** (str) - DB实例id

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstance", d, **kwargs)
        return apis.DescribeUDBInstanceResponseSchema().loads(resp)

    def describe_udb_instance_backup_state(self, req=None, **kwargs):
        """ DescribeUDBInstanceBackupState - 获取UDB实例备份状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (int) - (Required) 备份记录ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区，参见［可用区列表］
        
        **Response**

        - **State** (str) - 备份状态 0 Backuping // 备份中 1 Success // 备份成功 2 Failed // 备份失败 3 Expired // 备份过期
        - **BackupSize** (int) - 
        - **BackupEndTime** (int) - 
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBackupStateRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstanceBackupState", d, **kwargs)
        return apis.DescribeUDBInstanceBackupStateResponseSchema().loads(resp)

    def describe_udb_instance_backup_url(self, req=None, **kwargs):
        """ DescribeUDBInstanceBackupURL - 获取UDB备份下载地址

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (int) - (Required) DB实例备份ID,该值可以通过DescribeUDBBackup获取
        - **DBId** (str) - (Required) DB实例Id,该值可通过DescribeUDBInstance获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **BackupPath** (str) - DB实例备份文件公网的地址
        - **InnerBackupPath** (str) - DB实例备份文件内网的地址
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBackupURLRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstanceBackupURL", d, **kwargs)
        return apis.DescribeUDBInstanceBackupURLResponseSchema().loads(resp)

    def describe_udb_instance_binlog(self, req=None, **kwargs):
        """ DescribeUDBInstanceBinlog - 获取UDB指定时间段的binlog列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BeginTime** (int) - (Required) 过滤条件:起始时间(时间戳)
        - **DBId** (str) - (Required) DB实例Id
        - **EndTime** (int) - (Required) 过滤条件:结束时间(时间戳)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DataSet** (list) - 见 **UDBInstanceBinlogSet** 模型定义
        
        **Response Model**
        
        **UDBInstanceBinlogSet** 
        
        - **Size** (int) - Binlog文件大小
        - **BeginTime** (int) - Binlog文件生成时间(时间戳)
        - **EndTime** (int) - Binlog文件结束时间(时间戳)
        - **Name** (str) - Binlog文件名

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBinlogRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstanceBinlog", d, **kwargs)
        return apis.DescribeUDBInstanceBinlogResponseSchema().loads(resp)

    def describe_udb_instance_binlog_backup_state(self, req=None, **kwargs):
        """ DescribeUDBInstanceBinlogBackupState - 获取udb实例备份状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (int) - (Required) 备份记录ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区
        
        **Response**

        - **State** (str) - 备份状态 0 Backuping // 备份中 1 Success // 备份成功 2 Failed // 备份失败 3 Expired // 备份过期
        - **BackupSize** (int) - 备份文件大小(字节)
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceBinlogBackupStateRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstanceBinlogBackupState", d, **kwargs)
        return apis.DescribeUDBInstanceBinlogBackupStateResponseSchema().loads(resp)

    def describe_udb_instance_price(self, req=None, **kwargs):
        """ DescribeUDBInstancePrice - 获取UDB实例价格信息

        **Request**

        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBTypeId** (str) - (Required) UDB实例的DB版本字符串
        - **DiskSpace** (int) - (Required) 磁盘空间(GB),暂时支持20(GB) - 3000(GB), 输入不带单位
        - **MemoryLimit** (int) - (Required) 内存限制(MB)，单位为MB.目前支持：1000-96000
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - Year，按年付费； Month，按月付费 Dynamic，按需付费（需开启权限) Trial，试用（需开启权限）默认为月付
        - **Count** (int) - 购买DB实例数量,最大数量为10台, 默认为1台
        - **InstanceMode** (str) - 实例的部署类型。可选值为：Normal: 普通单点实例，Slave: 从库实例,HA: 高可用部署实例，默认是Normal
        - **Quantity** (int) - DB购买多少个"计费时间单位"，默认值为1。比如：买2个月，Quantity就是2。如果计费单位是“按月”，并且Quantity为0，表示“购买到月底”
        - **SSDType** (str) - SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必填
        - **UseSSD** (bool) - 是否使用SSD，默认为false
        
        **Response**

        - **DataSet** (list) - 见 **UDBInstancePriceSet** 模型定义
        
        **Response Model**
        
        **UDBInstancePriceSet** 
        
        - **ChargeType** (str) - Year， Month， Dynamic，Trial
        - **Price** (float) - 价格，单位为分，保留小数点后两位

        """
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstancePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstancePrice", d, **kwargs)
        return apis.DescribeUDBInstancePriceResponseSchema().loads(resp)

    def describe_udb_instance_state(self, req=None, **kwargs):
        """ DescribeUDBInstanceState - 获取UDB实例状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **State** (str) - DB状态标记 Init：初始化中；Fail：安装失败； Starting：启动中； Running ： 运行 ；Shutdown：关闭中； Shutoff ：已关闭； Delete：已删除； Upgrading：升级中； Promoting： 提升为独库进行中； Recovering： 恢复中； Recover fail：恢复失败。
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceStateRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstanceState", d, **kwargs)
        return apis.DescribeUDBInstanceStateResponseSchema().loads(resp)

    def describe_udb_instance_upgrade_price(self, req=None, **kwargs):
        """ DescribeUDBInstanceUpgradePrice - 获取UDB实例升降级价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id
        - **DiskSpace** (int) - (Required) 磁盘空间(GB), 暂时支持20G - 500G
        - **MemoryLimit** (int) - (Required) 内存限制(MB)
        - **SSDType** (str) - SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        - **UseSSD** (bool) - 是否使用SSD，默认为false
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **Price** (float) - 价格，单位分
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBInstanceUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBInstanceUpgradePrice", d, **kwargs)
        return apis.DescribeUDBInstanceUpgradePriceResponseSchema().loads(resp)

    def describe_udb_log_backup_url(self, req=None, **kwargs):
        """ DescribeUDBLogBackupURL - 获取UDB的slowlog备份地址

        **Request**

        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (int) - (Required) DB实例备份ID
        - **DBId** (str) - (Required) DB实例Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **BackupPath** (str) - 备份外网URL
        - **UsernetPath** (str) - 备份用户网URL
        
        """
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBLogBackupURLRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBLogBackupURL", d, **kwargs)
        return apis.DescribeUDBLogBackupURLResponseSchema().loads(resp)

    def describe_udb_log_package(self, req=None, **kwargs):
        """ DescribeUDBLogPackage - 列表UDB实例binlog或slowlog或errorlog备份信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - (Required) 分页显示的条目数，列表操作则指定
        - **Offset** (int) - (Required) 分页显示的起始偏移，列表操作则指定
        - **BeginTime** (int) - 过滤条件:起始时间(时间戳)
        - **DBId** (str) - DB实例Id，如果指定，则只获取该db的备份信息
        - **EndTime** (int) - 过滤条件:结束时间(时间戳)
        - **Type** (int) - 需要列出的备份文件类型，每种文件的值如下 2 : BINLOG\\_BACKUP 3 : SLOW\\_QUERY\\_BACKUP 4 : ERRORLOG\\_BACKUP
        - **Types** (list) - Types作为Type的补充，支持多值传入，可以获取多个类型的日志记录，如：Types.0=2&Types.1=3
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DataSet** (list) - 见 **LogPackageDataSet** 模型定义
        - **TotalCount** (int) - 备份总数，如果指定dbid，则是该db备份总数
        
        **Response Model**
        
        **LogPackageDataSet** 
        
        - **BackupTime** (int) - 备份时间
        - **State** (str) - 备份状态 Backuping // 备份中 Success // 备份成功 Failed // 备份失败 Expired // 备份过期
        - **Zone** (str) - 所在可用区
        - **BackupType** (int) - 备份类型，包括2-binlog备份，3-slowlog备份
        - **DBId** (str) - dbid
        - **DBName** (str) - 对应的db名称
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区
        - **BackupId** (int) - 备份id
        - **BackupName** (str) - 备份名称
        - **BackupSize** (int) - 备份文件大小

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBLogPackageRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBLogPackage", d, **kwargs)
        return apis.DescribeUDBLogPackageResponseSchema().loads(resp)

    def describe_udb_param_group(self, req=None, **kwargs):
        """ DescribeUDBParamGroup - 获取参数组详细参数信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - (Required) 分页显示的条目数，列表操作则指定
        - **Offset** (int) - (Required) 分页显示的起始偏移，列表操作则指定
        - **ClassType** (str) - 如果未指定GroupId，则可选是否选取特定DB类型的配置(sql, nosql, postgresql, sqlserver)
        - **GroupId** (int) - 参数组id，如果指定则获取描述，否则是列表操作，需要 指定Offset/Limit
        - **IsInUDBC** (bool) - 是否选取专区中配置
        - **RegionFlag** (bool) - 当请求没有填写Zone时，如果指定为true，表示只拉取跨可用区的相关配置文件，否则，拉取所有机房的配置文件（包括每个单可用区和跨可用区）
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DataSet** (list) - 见 **UDBParamGroupSet** 模型定义
        - **TotalCount** (int) - 参数组总数，列表操作时才会有该参数
        
        **Response Model**
        
        **UDBParamMemberSet** 
        
        - **Key** (str) - 参数名称
        - **Value** (str) - 参数值
        - **ValueType** (int) - 参数值应用类型，取值范围为{0,10,20,30},各值 代表意义为 0-unknown、10-int、20-string、 30-bool
        - **AllowedVal** (str) - 允许的值(根据参数类型，用分隔符表示)
        - **ApplyType** (int) - 参数值应用类型,取值范围为{0,10,20}，各值代表 意义为0-unknown、10-static、20-dynamic
        - **Modifiable** (bool) - 是否可更改，默认为false
        - **FormatType** (int) - 允许值的格式类型，取值范围为{0,10,20}，意义分 别为PVFT_UNKOWN=0,PVFT_RANGE=10, PVFT_ENUM=20

        **UDBParamGroupSet** 
        
        - **ParamMember** (list) - 见 **UDBParamMemberSet** 模型定义
        - **Zone** (str) - 
        - **RegionFlag** (bool) - 
        - **GroupId** (int) - 参数组id
        - **GroupName** (str) - 参数组名称
        - **DBTypeId** (str) - DB类型id，mysql/mongodb按版本细分各有一个id 目前id的取值范围为[1,7],数值对应的版本如下 1：mysql-5.5，2：mysql-5.1，3：percona-5.5 4：mongodb-2.4，5：mongodb-2.6，6：mysql-5.6 7：percona-5.6
        - **Description** (str) - 参数组描述
        - **Modifiable** (bool) - 参数组是否可修改

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBParamGroupRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBParamGroup", d, **kwargs)
        return apis.DescribeUDBParamGroupResponseSchema().loads(resp)

    def describe_udb_type(self, req=None, **kwargs):
        """ DescribeUDBType - 获取UDB支持的类型信息

        **Request**

        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBClusterType** (str) - DB实例类型，如mysql，sqlserver，mongo，postgresql
        - **DiskType** (str) - 返回支持某种磁盘类型的DB类型。如果没传，则表示任何磁盘类型均可。
        - **InstanceMode** (str) - 返回支持某种实例类型的DB类型。如果没传，则表示任何实例类型均可。normal:单点,ha:高可用,sharded_cluster:分片集群
        
        **Response**

        - **DataSet** (list) - 见 **UDBTypeSet** 模型定义
        
        **Response Model**
        
        **UDBTypeSet** 
        
        - **DBTypeId** (str) - DB类型id，mysql/mongodb按版本细分各有一个id, 目前id的取值范围为[1,7],数值对应的版本如下： 1：mysql-5.5，2：mysql-5.1，3：percona-5.5 4：mongodb-2.4，5：mongodb-2.6，6：mysql-5.6， 7：percona-5.6

        """
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDBTypeRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDBType", d, **kwargs)
        return apis.DescribeUDBTypeResponseSchema().loads(resp)

    def edit_udb_backup_blacklist(self, req=None, **kwargs):
        """ EditUDBBackupBlacklist - 编辑UDB实例的备份黑名单

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Blacklist** (str) - (Required) 黑名单，规范示例,指定库mysql.%;test.%; 指定表city.address;
        - **DBId** (str) - (Required) DB实例Id,该值可以通过DescribeUDBInstance获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.EditUDBBackupBlacklistRequestSchema().dumps(d)
        resp = self.invoke("EditUDBBackupBlacklist", d, **kwargs)
        return apis.EditUDBBackupBlacklistResponseSchema().loads(resp)

    def fetch_udb_instance_earliest_recover_time(self, req=None, **kwargs):
        """ FetchUDBInstanceEarliestRecoverTime - 获取UDB最早可回档的时间点

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) DB实例Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **EarliestTime** (int) - 获取最早可回档时间点
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.FetchUDBInstanceEarliestRecoverTimeRequestSchema().dumps(d)
        resp = self.invoke("FetchUDBInstanceEarliestRecoverTime", d, **kwargs)
        return apis.FetchUDBInstanceEarliestRecoverTimeResponseSchema().loads(resp)

    def modify_udb_instance_name(self, req=None, **kwargs):
        """ ModifyUDBInstanceName - 重命名UDB实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        - **Name** (str) - (Required) 实例的新名字, 长度要求为6~63位
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUDBInstanceNameRequestSchema().dumps(d)
        resp = self.invoke("ModifyUDBInstanceName", d, **kwargs)
        return apis.ModifyUDBInstanceNameResponseSchema().loads(resp)

    def modify_udb_instance_password(self, req=None, **kwargs):
        """ ModifyUDBInstancePassword - 修改DB实例的管理员密码

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的ID,该值可以通过DescribeUDBInstance获取
        - **Password** (str) - (Required) 实例的新密码
        - **AccountName** (str) - sqlserver帐号，仅在sqlserver的情况下填该参数
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUDBInstancePasswordRequestSchema().dumps(d)
        resp = self.invoke("ModifyUDBInstancePassword", d, **kwargs)
        return apis.ModifyUDBInstancePasswordResponseSchema().loads(resp)

    def promote_udb_instance_to_ha(self, req=None, **kwargs):
        """ PromoteUDBInstanceToHA - 普通db升级为高可用(只针对mysql5.5及以上版本)

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PromoteUDBInstanceToHARequestSchema().dumps(d)
        resp = self.invoke("PromoteUDBInstanceToHA", d, **kwargs)
        return apis.PromoteUDBInstanceToHAResponseSchema().loads(resp)

    def promote_udb_slave(self, req=None, **kwargs):
        """ PromoteUDBSlave - 从库提升为独立库

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        - **IsForce** (bool) - 是否强制(如果从库落后可能会禁止提升)，默认false 如果落后情况下，强制提升丢失数据
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PromoteUDBSlaveRequestSchema().dumps(d)
        resp = self.invoke("PromoteUDBSlave", d, **kwargs)
        return apis.PromoteUDBSlaveResponseSchema().loads(resp)

    def resize_udb_instance(self, req=None, **kwargs):
        """ ResizeUDBInstance - 修改（升级和降级）UDB实例的配置，包括内存和磁盘的配置，对于内存升级无需关闭实例，其他场景需要事先关闭实例。两套参数可以配置升降机：1.配置UseSSD和SSDType  2.配置InstanceType，不需要配置InstanceMode。这两套第二套参数的优先级更高

        **Request**

        - **ProjectId** (int) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id
        - **DiskSpace** (int) - (Required) 磁盘空间(GB), 暂时支持20G-3000G
        - **MemoryLimit** (int) - (Required) 内存限制(MB)，目前支持以下几档 1000M/2000M/4000M/ 6000M/8000M/ 12000M/16000M/ 24000M/32000M/ 48000M/64000M/96000M。
        - **CouponId** (str) - 使用的代金券id
        - **InstanceMode** (str) - UDB实例模式类型, 可选值如下: "Normal": 普通版UDB实例 "HA": 高可用版UDB实例 默认是"Normal"
        - **InstanceType** (str) - UDB数据库机型: "Normal": "标准机型" ,  "SATA_SSD": "SSD机型" , "PCIE_SSD": "SSD高性能机型" ,  "Normal_Volume": "标准大容量机型",  "SATA_SSD_Volume": "SSD大容量机型" ,  "PCIE_SSD_Volume": "SSD高性能大容量机型"
        - **SSDType** (str) - SSD类型，可选值为"SATA"、"PCI-E"，如果UseSSD为true ，则必选
        - **StartAfterUpgrade** (bool) - DB关闭状态下升降级，升降级后是否启动DB，默认为false
        - **UDBCId** (str) - 专区的ID，如果有值表示专区中的DB配置升降级
        - **UseSSD** (bool) - 是否使用SSD，默认为false
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUDBInstanceRequestSchema().dumps(d)
        resp = self.invoke("ResizeUDBInstance", d, **kwargs)
        return apis.ResizeUDBInstanceResponseSchema().loads(resp)

    def restart_udb_instance(self, req=None, **kwargs):
        """ RestartUDBInstance - 重启UDB实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RestartUDBInstanceRequestSchema().dumps(d)
        resp = self.invoke("RestartUDBInstance", d, **kwargs)
        return apis.RestartUDBInstanceResponseSchema().loads(resp)

    def start_udb_instance(self, req=None, **kwargs):
        """ StartUDBInstance - 启动UDB实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StartUDBInstanceRequestSchema().dumps(d)
        resp = self.invoke("StartUDBInstance", d, **kwargs)
        return apis.StartUDBInstanceResponseSchema().loads(resp)

    def stop_udb_instance(self, req=None, **kwargs):
        """ StopUDBInstance - 关闭UDB实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        - **ForceToKill** (bool) - 是否使用强制手段关闭DB，默认是false
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StopUDBInstanceRequestSchema().dumps(d)
        resp = self.invoke("StopUDBInstance", d, **kwargs)
        return apis.StopUDBInstanceResponseSchema().loads(resp)

    def switch_udb_instance_to_ha(self, req=None, **kwargs):
        """ SwitchUDBInstanceToHA - 普通UDB切换为高可用，原db状态为WaitForSwitch时，调用该api

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 实例的Id,该值可以通过DescribeUDBInstance获取
        - **ChargeType** (str) - Year， Month， Dynamic，Trial，不填则按现在单点计费执行
        - **Quantity** (str) - 购买时长，需要和 ChargeType 搭配使用，否则使用单点计费策略的值
        - **Tag** (str) - 业务组
        
        **Response**

        - **DBId** (str) - 切换后高可用db实例的Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.SwitchUDBInstanceToHARequestSchema().dumps(d)
        resp = self.invoke("SwitchUDBInstanceToHA", d, **kwargs)
        return apis.SwitchUDBInstanceToHAResponseSchema().loads(resp)

    def update_udb_instance_backup_strategy(self, req=None, **kwargs):
        """ UpdateUDBInstanceBackupStrategy - 修改UDB自动备份策略

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DBId** (str) - (Required) 主节点的Id
        - **BackupDate** (str) - 备份时期标记位。共7位，每一位为一周中一天的备份情况，0表示关闭当天备份，1表示打开当天备份。最右边的一位为星期天的备份开关，其余从右到左依次为星期一到星期六的备份配置开关，每周必须至少设置两天备份。例如：1100000表示打开星期六和星期五的备份功能
        - **BackupMethod** (str) - 选择默认的备份方式，可选 snapshot 表示使用快照/物理备份，填 logic 表示使用逻辑备份。需要同时设置BackupDate字段。（注意现在只有SSD 版本的 MySQL实例支持物理备份）
        - **BackupTime** (int) - 备份的整点时间，范围[0,23]
        - **ForceDump** (bool) - 当导出某些数据遇到问题后，是否强制导出其他剩余数据默认是false需要同时设置BackupDate字段
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateUDBInstanceBackupStrategyRequestSchema().dumps(d)
        resp = self.invoke("UpdateUDBInstanceBackupStrategy", d, **kwargs)
        return apis.UpdateUDBInstanceBackupStrategyResponseSchema().loads(resp)

    def update_udb_instance_slave_backup_switch(self, req=None, **kwargs):
        """ UpdateUDBInstanceSlaveBackupSwitch - 开启或者关闭UDB从库备份

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupSwitch** (int) - (Required) 从库的备份开关，范围[0,1],0表示从库备份功能关闭,1 表示从库备份开关打开。
        - **MasterDBId** (str) - (Required) 主库的Id
        - **SlaveDBId** (str) - 从库的Id,如果从库备份开关设定为打开，则必须赋值。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateUDBInstanceSlaveBackupSwitchRequestSchema().dumps(d)
        resp = self.invoke("UpdateUDBInstanceSlaveBackupSwitch", d, **kwargs)
        return apis.UpdateUDBInstanceSlaveBackupSwitchResponseSchema().loads(resp)

    def update_udb_param_group(self, req=None, **kwargs):
        """ UpdateUDBParamGroup - 更新UDB配置参数项

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (int) - (Required) 配置参数组id，使用DescribeUDBParamGroup获得
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Description** (str) - 参数组的描述
        - **Key** (str) - 参数名称（与Value配合使用）
        - **Name** (str) - 参数组的名字
        - **RegionFlag** (bool) - 该配置文件是否是地域级别配置文件，默认是false
        - **Value** (str) - 参数值（与Key配合使用）
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateUDBParamGroupRequestSchema().dumps(d)
        resp = self.invoke("UpdateUDBParamGroup", d, **kwargs)
        return apis.UpdateUDBParamGroupResponseSchema().loads(resp)

    def upload_udb_param_group(self, req=None, **kwargs):
        """ UploadUDBParamGroup - 导入UDB配置

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Content** (str) - (Required) 配置内容，导入的配置内容采用base64编码
        - **DBTypeId** (str) - (Required) DB类型id，DB类型id，mysql/mongodb/postgesql按版本细分 1：mysql-5.1，2：mysql-5.5，3：percona-5.5，4：mysql-5.6，5：percona-5.6，6：mysql-5.7，7：percona-5.7，8：mariadb-10.0，9：mongodb-2.4，10：mongodb-2.6，11：mongodb-3.0，12：mongodb-3.2,13：postgresql-9.4，14：postgresql-9.6
        - **Description** (str) - (Required) 参数组描述
        - **GroupName** (str) - (Required) 配置参数组名称
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ParamGroupTypeId** (int) - 配置文件子类型 0-未知, 1-Shardsvr-MMAPv1, 2-Shardsvr-WiredTiger, 3-Configsvr-MMAPv1, 4-Configsvr-WiredTiger, 5-Mongos
        - **RegionFlag** (bool) - 该配置文件是否是地域级别配置文件，默认是false
        
        **Response**

        - **GroupId** (int) - 配置参数组id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UploadUDBParamGroupRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("UploadUDBParamGroup", d, **kwargs)
        return apis.UploadUDBParamGroupResponseSchema().loads(resp)
