# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
from ucloud.core.client import Client
from ucloud.services.ufs.schemas import apis


class UFSClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(UFSClient, self).__init__(config, transport, middleware, logger)

    def create_ufs_volume(self, req=None, **kwargs):
        """ CreateUFSVolume - 创建文件系统

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ProtocolType** (str) - (Required) 文件系统协议，枚举值，NFSv3表示NFS V3协议，NFSv4表示NFS V4协议
        - **Size** (int) - (Required) 文件系统大小，单位为GB，最大不超过20T，香港容量型必须为100的整数倍，Size最小为500GB，北京，上海，广州的容量型必须为1024的整数倍，Size最小为1024GB。性能型文件系统Size最小为100GB
        - **StorageType** (str) - (Required) 文件系统存储类型，枚举值，Basic表示容量型，Advanced表示性能型
        - **ChargeType** (str) - 计费模式，枚举值为： Year，按年付费； Month，按月付费； Dynamic，按需付费（需开启权限）； Trial，试用（需开启权限） 默认为Dynamic
        - **CouponId** (str) - 使用的代金券id
        - **Quantity** (int) - 购买时长 默认: 1
        - **Remark** (str) - 备注
        - **Tag** (str) - 文件系统所属业务组
        - **VolumeName** (str) - 文件系统名称
        
        **Response**

        - **VolumeId** (str) - 文件系统ID
        - **VolumeName** (str) - 文件系统名称
        - **VolumeStatus** (str) - 文件系统挂载点状态
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUFSVolumeRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUFSVolume", d, **kwargs)
        return apis.CreateUFSVolumeResponseSchema().loads(resp)

    def describe_ufs_volume_2(self, req=None, **kwargs):
        """ DescribeUFSVolume2 - 获取文件系统列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - 文件列表长度
        - **Offset** (int) - 文件列表起始
        - **VolumeId** (str) - 文件系统ID
        
        **Response**

        - **DataSet** (list) - 见 **UFSVolumeInfo2** 模型定义
        - **TotalCount** (int) - 文件系统总数
        
        **Response Model**
        
        **UFSVolumeInfo2** 
        
        - **CreateTime** (int) - 文件系统创建时间（unix时间戳）
        - **ExpiredTime** (int) - 文件系统过期时间（unix时间戳）
        - **IsExpired** (str) - 是否过期
        - **MaxMountPointNum** (int) - 文件系统允许创建的最大挂载点数目
        - **ProtocolType** (str) - 文件系统协议，枚举值，NFSv3表示NFS V3协议，NFSv4表示NFS V4协议
        - **Remark** (str) - 文件系统备注信息
        - **Size** (int) - 文件系统大小，单位GB
        - **StorageType** (str) - 文件系统存储类型，枚举值，Basic表示容量型，Advanced表示性能型
        - **Tag** (str) - 文件系统所属业务组
        - **TotalMountPointNum** (int) - 当前文件系统已创建的挂载点数目
        - **UsedSize** (int) - 文件系统当前使用容量，单位GB
        - **VolumeId** (str) - 文件系统ID
        - **VolumeName** (str) - 文件系统名称

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUFSVolume2RequestSchema().dumps(d)
        resp = self.invoke("DescribeUFSVolume2", d, **kwargs)
        return apis.DescribeUFSVolume2ResponseSchema().loads(resp)

    def extend_ufs_volume(self, req=None, **kwargs):
        """ ExtendUFSVolume - 文件系统扩容

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 文件系统大小，单位为GB，最大不超过20T，香港容量型必须为100的整数倍，Size最小为500GB，北京，上海，广州的容量型必须为1024的整数倍，Size最小为1024GB。性能型文件系统Size最小为100GB
        - **VolumeId** (str) - (Required) 文件系统ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ExtendUFSVolumeRequestSchema().dumps(d)
        resp = self.invoke("ExtendUFSVolume", d, **kwargs)
        return apis.ExtendUFSVolumeResponseSchema().loads(resp)

    def remove_ufs_volume(self, req=None, **kwargs):
        """ RemoveUFSVolume - 删除UFS文件系统

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **VolumeId** (str) - (Required) 文件系统ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RemoveUFSVolumeRequestSchema().dumps(d)
        resp = self.invoke("RemoveUFSVolume", d, **kwargs)
        return apis.RemoveUFSVolumeResponseSchema().loads(resp)
