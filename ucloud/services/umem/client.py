# -*- coding: utf-8 -*-

from ucloud.core.client import Client
from ucloud.services.umem.schemas import apis


class UMemClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(UMemClient, self).__init__(config, transport, middleware, logger)

    def create_umem_space(self, req=None, **kwargs):
        """ CreateUMemSpace - 创建UMem内存空间

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 空间名称,长度(6<=size<=63)
        - **Size** (int) - (Required) 内存大小, 单位:GB, 范围[1~1024]
        - **ChargeType** (str) - Year , Month, Dynamic, Trial 默认: Month
        - **CouponId** (str) - 使用的代金券id
        - **Password** (str) - URedis密码。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定密码。密码需使用base64进行编码，举例如下：# echo -n Password1 | base64UGFzc3dvcmQx。
        - **Protocol** (str) - 协议:memcache, redis (默认redis).注意:redis无single类型
        - **Quantity** (int) - 购买时长 默认: 1
        - **SubnetId** (str) - 
        - **Tag** (str) - 
        - **Type** (str) - 空间类型:single(无热备),double(热备)(默认: double)
        - **VPCId** (str) - 
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **SpaceId** (str) - 创建内存空间ID列表
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUMemSpaceRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUMemSpace", d, **kwargs)
        return apis.CreateUMemSpaceResponseSchema().loads(resp)

    def create_umem_cache_group(self, req=None, **kwargs):
        """ CreateUMemcacheGroup - 创建单机Memcache

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 请求创建组的名称 范围[6-60]
        - **ChargeType** (str) - 计费模式，Year , Month, Dynamic 默认: Month
        - **ConfigId** (str) - 配置ID,目前仅支持默认配置id 默认配置id:"9a891891-c245-4b66-bce8-67e59430d67c"
        - **CouponId** (str) - 代金券ID
        - **Protocol** (str) - 
        - **Quantity** (int) - 购买时长，默认为1
        - **Size** (int) - 每个节点的内存大小,单位GB,默认1GB 目前仅支持1/2/4/8/16/32这几档
        - **SubnetId** (str) - 
        - **Tag** (str) - 业务组 默认：Default
        - **VPCId** (str) - 
        - **Version** (str) - Memcache版本信息,默认为1.4.31
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **GroupId** (str) - 创建的组ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUMemcacheGroupRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUMemcacheGroup", d, **kwargs)
        return apis.CreateUMemcacheGroupResponseSchema().loads(resp)

    def create_uredis_group(self, req=None, **kwargs):
        """ CreateURedisGroup - 创建主备redis

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **HighAvailability** (str) - (Required) 是否开启高可用,enable或disable
        - **Name** (str) - (Required) 请求创建组的名称 (范围[6-63],只能包含英文、数字以及符号-和_)
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **AutoBackup** (str) - 是否自动备份,enable或disable，默认disable
        - **BackupId** (str) - 有此项代表从备份中创建，无代表正常创建
        - **BackupTime** (int) - 自动备份开始时间,范围[0-23],默认3点
        - **ChargeType** (str) - 计费模式，Year , Month, Dynamic 默认: Month
        - **ConfigId** (str) - 配置ID,目前仅支持默认配置id 默认创建3.0版本 配置id:"03f58ca9-b64d-4bdd-abc7-c6b9a46fd801"，3.0版本配置ID：03f58ca9-b64d-4bdd-abc7-c6b9a46fd8013.2版本配置ID：3e45ac48-f8a2-a9q2-261d-l342dab130gf4.0版本配置ID：6c9298a3-9d7f-428c-b1d0-e87ab3b8a1ea,从备份创建为必传项
        - **CouponId** (str) - 代金券ID
        - **MasterGroupId** (str) - Master Redis Group的ID，创建只读Slave时，必须填写
        - **Password** (str) - 初始化密码,需要 base64 编码
        - **Quantity** (int) - 购买时长，默认为1
        - **Size** (int) - 每个节点的内存大小,单位GB,默认1GB,目前仅支持1/2/4/8/16/32,六种
        - **SlaveZone** (str) - 跨机房URedis，slave所在可用区（必须和Zone在同一Region，且不可相同）
        - **SubnetId** (str) - 
        - **Tag** (str) - 业务组名称
        - **VPCId** (str) - 
        - **Version** (str) - Redis版本信息(详见DescribeURedisVersion返回结果),默认版本3.0
        
        **Response**

        - **GroupId** (str) - 创建的组ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateURedisGroupRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateURedisGroup", d, **kwargs)
        return apis.CreateURedisGroupResponseSchema().loads(resp)

    def delete_umem_space(self, req=None, **kwargs):
        """ DeleteUMemSpace - 删除UMem内存空间

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SpaceId** (str) - (Required) UMem内存空间ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUMemSpaceRequestSchema().dumps(d)
        resp = self.invoke("DeleteUMemSpace", d, **kwargs)
        return apis.DeleteUMemSpaceResponseSchema().loads(resp)

    def delete_umem_cache_group(self, req=None, **kwargs):
        """ DeleteUMemcacheGroup - 删除单机Memcache

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - (Required) 组ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUMemcacheGroupRequestSchema().dumps(d)
        resp = self.invoke("DeleteUMemcacheGroup", d, **kwargs)
        return apis.DeleteUMemcacheGroupResponseSchema().loads(resp)

    def delete_uredis_group(self, req=None, **kwargs):
        """ DeleteURedisGroup - 删除主备redis

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - (Required) 组ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteURedisGroupRequestSchema().dumps(d)
        resp = self.invoke("DeleteURedisGroup", d, **kwargs)
        return apis.DeleteURedisGroupResponseSchema().loads(resp)

    def describe_umem_price(self, req=None, **kwargs):
        """ DescribeUMemPrice - 获取UMem实例价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 购买umem大小,单位:GB,范围[1~1024]
        - **Type** (str) - (Required) 空间类型:single(无热备),double(热备)(默认: double)
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - Year， Month， Dynamic，Trial 如果不指定，则一次性获取三种计费
        - **Quantity** (int) - 购买UMem的时长，默认值为1
        - **RegionFlag** (bool) - 
        
        **Response**

        - **DataSet** (list) - 见 **UMemPriceSet** 模型定义
        
        **Response Model**
        
        **UMemPriceSet** 
        
        - **ChargeType** (str) - Year， Month， Dynamic，Trial
        - **Price** (float) - 价格，单位: 元，保留小数点后两位有效数字

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemPriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemPrice", d, **kwargs)
        return apis.DescribeUMemPriceResponseSchema().loads(resp)

    def describe_umem_space(self, req=None, **kwargs):
        """ DescribeUMemSpace - 获取UMem内存空间列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - 返回数据长度, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0
        - **SpaceId** (str) - 内存空间ID (无ID，则获取所有)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DataSet** (list) - 见 **UMemSpaceSet** 模型定义
        - **TotalCount** (int) - 根据过滤条件得到的总数
        
        **Response Model**
        
        **UMemSpaceAddressSet** 
        
        - **IP** (str) - UMem实例访问IP
        - **Port** (int) - UMem实例访问Port

        **UMemSpaceSet** 
        
        - **ExpireTime** (int) - 到期时间
        - **Protocol** (str) - 协议类型: memcache, redis
        - **Size** (int) - 容量单位GB
        - **Zone** (str) - 可用区，参见 `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **RewriteTime** (int) - 运维时间0   //0点1   //1点依次类推
        - **SpaceId** (str) - 内存空间ID
        - **VPCId** (str) - 
        - **ChargeType** (str) - Year, Month, Dynamic, Trial
        - **Type** (str) - 空间类型:single(无热备),double(热备)
        - **UsedSize** (int) - 使用量单位MB
        - **Tag** (str) - 
        - **SubnetId** (str) - 
        - **CreateTime** (int) - 创建时间
        - **Name** (str) - 内存空间名称
        - **State** (str) - Starting:创建中 Running:运行中 Fail:失败
        - **Address** (list) - 见 **UMemSpaceAddressSet** 模型定义

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemSpaceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemSpace", d, **kwargs)
        return apis.DescribeUMemSpaceResponseSchema().loads(resp)

    def describe_umem_upgrade_price(self, req=None, **kwargs):
        """ DescribeUMemUpgradePrice - 获取UMem升级价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 购买UMem大小,单位:GB
        - **SpaceId** (str) - (Required) 需要升级的空间的SpaceId
        - **Type** (str) - (Required) 空间类型:single(无热备),double(热备)(默认: double)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **Price** (float) - 价格
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemUpgradePrice", d, **kwargs)
        return apis.DescribeUMemUpgradePriceResponseSchema().loads(resp)

    def describe_umem_cache_group(self, req=None, **kwargs):
        """ DescribeUMemcacheGroup - 显示Memcache

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - 组的ID,如果指定则获取描述，否则为列表操 作,需指定Offset/Limit
        - **Limit** (int) - 分页显示的条目数, 默认值为20
        - **Offset** (int) - 分页显示的起始偏移, 默认值为0
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - 组的总的节点个数
        - **DataSet** (list) - 见 **UMemcacheGroupSet** 模型定义
        
        **Response Model**
        
        **UMemcacheGroupSet** 
        
        - **GroupId** (str) - 组ID
        - **CreateTime** (int) - 创建时间 (UNIX时间戳)
        - **ExpireTime** (int) - 过期时间 (UNIX时间戳)
        - **Tag** (str) - 业务组名称
        - **SubnetId** (str) - 
        - **Port** (int) - 节点分配的服务端口
        - **Size** (int) - 容量单位GB
        - **Version** (str) - Memcache版本信息,默认为1.4.31
        - **ChargeType** (str) - 计费类型:Year,Month,Dynamic 默认Dynamic
        - **ConfigId** (str) - 节点的配置ID
        - **UsedSize** (int) - 使用量单位MB
        - **State** (str) - 状态标记 Creating // 初始化中 CreateFail // 创建失败 Deleting // 删除中 DeleteFail // 删除失败 Running // 运行 Resizing // 容量调整中 ResizeFail // 容量调整失败 Configing // 配置中 ConfigFail // 配置失败Restarting // 重启中
        - **VPCId** (str) - 
        - **Name** (str) - 组名称
        - **VirtualIP** (str) - 节点的虚拟IP地址
        - **ModifyTime** (int) - 修改时间 (UNIX时间戳)

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemcacheGroupRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemcacheGroup", d, **kwargs)
        return apis.DescribeUMemcacheGroupResponseSchema().loads(resp)

    def describe_umem_cache_price(self, req=None, **kwargs):
        """ DescribeUMemcachePrice - 获取umemcache组价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 容量大小,单位:GB 取值范围[1-32]
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - 计费模式，Year， Month， Dynamic，默认: Dynamic 默认: 获取所有计费模式的价格
        - **Quantity** (int) - 购买umemcache的时长，默认值为1
        - **Type** (str) - 空间类型:single(无热备),double(热备)(默认: double)
        
        **Response**

        - **DataSet** (list) - 见 **UMemcachePriceSet** 模型定义
        
        **Response Model**
        
        **UMemcachePriceSet** 
        
        - **ChargeType** (str) - 计费模式，Year, Month, Dynamic
        - **Price** (float) - 价格，单位: 元，保留小数点后两位有效数字

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemcachePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemcachePrice", d, **kwargs)
        return apis.DescribeUMemcachePriceResponseSchema().loads(resp)

    def describe_umem_cache_upgrade_price(self, req=None, **kwargs):
        """ DescribeUMemcacheUpgradePrice - 获取umemcache升级价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - (Required) 需要升级的空间的GroupId,请参考DescribeUMemcacheGroup接口
        - **Size** (int) - (Required) 购买umemcache大小,单位:GB
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **Price** (float) - 价格，单位：元
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUMemcacheUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUMemcacheUpgradePrice", d, **kwargs)
        return apis.DescribeUMemcacheUpgradePriceResponseSchema().loads(resp)

    def describe_uredis_backup(self, req=None, **kwargs):
        """ DescribeURedisBackup - 查询主备redis备份

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - 组的ID
        - **Limit** (int) - 分页显示的条目数, 默认值为10
        - **Offset** (int) - 分页显示的起始偏移, 默认值为0
        
        **Response**

        - **TotalCount** (int) - 用户名下总的备份个数
        - **DataSet** (list) - 见 **URedisBackupSet** 模型定义
        
        **Response Model**
        
        **URedisBackupSet** 
        
        - **State** (str) - 备份的状态: Backuping 备份中 Success 备份成功 Error 备份失败 Expired 备份过期
        - **Zone** (str) - 可用区，参见 `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - 对应的实例ID
        - **GroupName** (str) - 组名称
        - **BackupName** (str) - 备份的名称
        - **BackupId** (str) - 备份ID
        - **BackupTime** (int) - 备份时间 (UNIX时间戳)
        - **BackupSize** (int) - 备份文件大小, 以字节为单位
        - **BackupType** (str) - 备份类型: Manual 手动 Auto 自动

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisBackupRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisBackup", d, **kwargs)
        return apis.DescribeURedisBackupResponseSchema().loads(resp)

    def describe_uredis_backup_url(self, req=None, **kwargs):
        """ DescribeURedisBackupURL - 获取主备Redis备份下载链接

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackupId** (str) - (Required) 备份ID
        - **GroupId** (str) - (Required) 
        - **RegionFlag** (bool) - 是否是跨机房URedis(默认false)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **BackupPath** (str) - 备份文件公网的地址
        - **BackupURL** (str) - 备份文件公网的地址
        - **InnerBackupPath** (str) - 
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisBackupURLRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisBackupURL", d, **kwargs)
        return apis.DescribeURedisBackupURLResponseSchema().loads(resp)

    def describe_uredis_group(self, req=None, **kwargs):
        """ DescribeURedisGroup - 查询主备Redis

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - 组的ID,如果指定则获取描述，否则为列表操 作,需指定Offset/Limit
        - **Limit** (int) - 分页显示的条目数, 默认值为20
        - **Offset** (int) - 分页显示的起始偏移, 默认值为0
        - **Zone** (str) - 
        
        **Response**

        - **TotalCount** (int) - 组的总的节点个数
        - **DataSet** (list) - 见 **URedisGroupSet** 模型定义
        
        **Response Model**
        
        **URedisGroupSet** 
        
        - **Zone** (str) - 实例所在可用区，或者master redis所在可用区，参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - 组名称
        - **SubnetId** (str) - 
        - **Tag** (str) - 业务组名称
        - **VPCId** (str) - 
        - **GroupName** (str) - 组名称
        - **AutoBackup** (str) - 是否需要自动备份,enable,disable
        - **Version** (str) - Redis版本信息
        - **ChargeType** (str) - 计费类型:Year,Month,Dynamic 默认Dynamic
        - **UsedSize** (int) - 使用量单位MB
        - **BackupTime** (int) - 组自动备份开始时间,单位小时计,范围[0-23]
        - **HighAvailability** (str) - 是否开启高可用,enable,disable
        - **Type** (str) - 
        - **Protocol** (str) - 协议
        - **MemorySize** (int) - 容量单位GB
        - **ConfigId** (str) - 节点的配置ID
        - **Port** (int) - 节点分配的服务端口
        - **ExpireTime** (int) - 过期时间 (UNIX时间戳)
        - **CreateTime** (int) - 创建时间 (UNIX时间戳)
        - **ModifyTime** (int) - 修改时间 (UNIX时间戳)
        - **GroupId** (str) - 组ID
        - **VirtualIP** (str) - 节点的虚拟IP地址
        - **Size** (int) - 容量单位GB
        - **State** (str) - 状态标记 Creating // 初始化中 CreateFail // 创建失败 Deleting // 删除中 DeleteFail // 删除失败 Running // 运行 Resizing // 容量调整中 ResizeFail // 容量调整失败 Configing // 配置中 ConfigFail // 配置失败
        - **SlaveZone** (str) - 跨机房URedis，slave redis所在可用区，参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisGroupRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisGroup", d, **kwargs)
        return apis.DescribeURedisGroupResponseSchema().loads(resp)

    def describe_uredis_price(self, req=None, **kwargs):
        """ DescribeURedisPrice - 取uredis价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 量大小,单位:GB  取值范围[1-32]
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - 计费模式，Year， Month， Dynamic；如果不指定，则一次性获取三种计费
        - **ProductType** (str) - 产品类型：MS_Redis（标准主备版），S_Redis（从库），默认为MS_Redis
        - **Quantity** (int) - 计费模式为Dynamic时，购买的时长, 默认为1
        - **RegionFlag** (bool) - 是否是跨机房URedis(默认false)
        - **Type** (str) - 
        
        **Response**

        - **DataSet** (list) - 见 **URedisPriceSet** 模型定义
        
        **Response Model**
        
        **URedisPriceSet** 
        
        - **ChargeType** (str) - Year， Month， Dynamic，Trial
        - **Price** (float) - 价格，单位: 元，保留小数点后两位有效数字

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisPriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisPrice", d, **kwargs)
        return apis.DescribeURedisPriceResponseSchema().loads(resp)

    def describe_uredis_upgrade_price(self, req=None, **kwargs):
        """ DescribeURedisUpgradePrice - 获取uredis升级价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - (Required) 要升级的空间的GroupId,请参考DescribeURedisGroup接口
        - **Size** (int) - (Required) 购买uredis大小,单位:GB,范围是[1-32]
        - **Type** (str) - 
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **Price** (float) - 扩容差价，单位: 元，保留小数点后两位有效数字
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeURedisUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeURedisUpgradePrice", d, **kwargs)
        return apis.DescribeURedisUpgradePriceResponseSchema().loads(resp)

    def get_umem_space_state(self, req=None, **kwargs):
        """ GetUMemSpaceState - 获取UMem内存空间列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SpaceId** (str) - (Required) 内存空间ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **State** (str) - Starting:创建中 Running:运行中 Fail:失败
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUMemSpaceStateRequestSchema().dumps(d)
        resp = self.invoke("GetUMemSpaceState", d, **kwargs)
        return apis.GetUMemSpaceStateResponseSchema().loads(resp)

    def modify_umem_space_name(self, req=None, **kwargs):
        """ ModifyUMemSpaceName - 修改UMem内存空间名称

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 新的名称,长度(6<=size<=63)
        - **SpaceId** (str) - (Required) UMem内存空间ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUMemSpaceNameRequestSchema().dumps(d)
        resp = self.invoke("ModifyUMemSpaceName", d, **kwargs)
        return apis.ModifyUMemSpaceNameResponseSchema().loads(resp)

    def modify_uredis_group_name(self, req=None, **kwargs):
        """ ModifyURedisGroupName - 修改主备redis名称

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - (Required) 组的ID
        - **Name** (str) - (Required) Redis组名称 (范围[6-63],只能包含英文、数字以及符号-和_)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyURedisGroupNameRequestSchema().dumps(d)
        resp = self.invoke("ModifyURedisGroupName", d, **kwargs)
        return apis.ModifyURedisGroupNameResponseSchema().loads(resp)

    def resize_udredis_space(self, req=None, **kwargs):
        """ ResizeUDredisSpace - 调整内存空间容量

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 内存大小, 单位:GB (需要大于原size,<= 1024)
        - **SpaceId** (str) - (Required) 高性能UMem 内存空间Id
        - **CouponId** (str) - 使用的代金券Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUDredisSpaceRequestSchema().dumps(d)
        resp = self.invoke("ResizeUDredisSpace", d, **kwargs)
        return apis.ResizeUDredisSpaceResponseSchema().loads(resp)

    def resize_umem_space(self, req=None, **kwargs):
        """ ResizeUMemSpace - 调整内存空间容量

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 内存大小, 单位:GB (需要大于原size,<= 1024)
        - **SpaceId** (str) - (Required) UMem 内存空间Id
        - **ChargeType** (str) - 
        - **CouponId** (str) - 使用的代金券Id
        - **Type** (str) - 空间类型:single(无热备),double(热备)(默认: double)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUMemSpaceRequestSchema().dumps(d)
        resp = self.invoke("ResizeUMemSpace", d, **kwargs)
        return apis.ResizeUMemSpaceResponseSchema().loads(resp)

    def resize_uredis_group(self, req=None, **kwargs):
        """ ResizeURedisGroup - 调整主备redis容量

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - (Required) 组ID
        - **Size** (int) - (Required) 内存大小, 单位:GB (需要大于原size,且小于等于32) 目前仅支持1/2/4/8/16/32 G 六种容量规格
        - **ChargeType** (str) - 
        - **CouponId** (int) - 代金券ID 请参考DescribeCoupon接口
        - **Type** (str) - 空间类型:single(无热备),double(热备)(默认: double)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeURedisGroupRequestSchema().dumps(d)
        resp = self.invoke("ResizeURedisGroup", d, **kwargs)
        return apis.ResizeURedisGroupResponseSchema().loads(resp)

    def restart_umem_cache_group(self, req=None, **kwargs):
        """ RestartUMemcacheGroup - 重启单机Memcache

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **GroupId** (str) - (Required) 组的ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RestartUMemcacheGroupRequestSchema().dumps(d)
        resp = self.invoke("RestartUMemcacheGroup", d, **kwargs)
        return apis.RestartUMemcacheGroupResponseSchema().loads(resp)
