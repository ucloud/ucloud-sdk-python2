# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
from ucloud.core.typesystem import schema, fields


class DiskInfoSchema(schema.ResponseSchema):
    """ DiskInfo - 磁盘信息
    """

    fields = {
        "AttachResourceID": fields.Str(
            required=False, load_from="AttachResourceID"
        ),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskID": fields.Str(required=False, load_from="DiskID"),
        "DiskStatus": fields.Str(required=False, load_from="DiskStatus"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Region": fields.Str(required=False, load_from="Region"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SetType": fields.Str(required=False, load_from="SetType"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class EIPInfoSchema(schema.ResponseSchema):
    """ EIPInfo - 外网IP信息
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BindResourceID": fields.Str(
            required=False, load_from="BindResourceID"
        ),
        "BindResourceType": fields.Str(
            required=False, load_from="BindResourceType"
        ),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EIPID": fields.Str(required=False, load_from="EIPID"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "IP": fields.Str(required=False, load_from="IP"),
        "Name": fields.Str(required=False, load_from="Name"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "Region": fields.Str(required=False, load_from="Region"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Status": fields.Str(required=False, load_from="Status"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class ImageInfoSchema(schema.ResponseSchema):
    """ ImageInfo - 镜像信息
    """

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ImageID": fields.Str(required=True, load_from="ImageID"),
        "ImageStatus": fields.Str(required=True, load_from="ImageStatus"),
        "ImageType": fields.Str(required=True, load_from="ImageType"),
        "Name": fields.Str(required=True, load_from="Name"),
        "OSDistribution": fields.Str(required=True, load_from="OSDistribution"),
        "OSName": fields.Str(required=True, load_from="OSName"),
        "OSType": fields.Str(required=True, load_from="OSType"),
        "Region": fields.Str(required=True, load_from="Region"),
        "SetArch": fields.Str(required=True, load_from="SetArch"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class LBInfoSchema(schema.ResponseSchema):
    """ LBInfo - 负载均衡信息
    """

    fields = {
        "AlarmTemplateID": fields.Str(
            required=True, load_from="AlarmTemplateID"
        ),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "LBID": fields.Str(required=True, load_from="LBID"),
        "LBStatus": fields.Str(required=True, load_from="LBStatus"),
        "LBType": fields.Str(required=True, load_from="LBType"),
        "Name": fields.Str(required=True, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "PublicIP": fields.Str(required=False, load_from="PublicIP"),
        "Region": fields.Str(required=True, load_from="Region"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SGID": fields.Str(required=False, load_from="SGID"),
        "SubnetID": fields.Str(required=True, load_from="SubnetID"),
        "VPCID": fields.Str(required=True, load_from="VPCID"),
        "VSCount": fields.Int(required=True, load_from="VSCount"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class MetricSetSchema(schema.ResponseSchema):
    """ MetricSet - 监控值
    """

    fields = {
        "Timestamp": fields.Int(required=False, load_from="Timestamp"),
        "Value": fields.Float(required=False, load_from="Value"),
    }


class MetricInfoSchema(schema.ResponseSchema):
    """ MetricInfo - 监控信息
    """

    fields = {
        "Infos": fields.List(MetricSetSchema()),
        "MetricName": fields.Str(required=False, load_from="MetricName"),
    }


class NATGWInfoSchema(schema.ResponseSchema):
    """ NATGWInfo - NAT网关信息
    """

    fields = {
        "AlarmTemplateID": fields.Str(
            required=True, load_from="AlarmTemplateID"
        ),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "EIP": fields.Str(required=True, load_from="EIP"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "NATGWID": fields.Str(required=True, load_from="NATGWID"),
        "NATGWStatus": fields.Str(required=True, load_from="NATGWStatus"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Region": fields.Str(required=True, load_from="Region"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "SGID": fields.Str(required=True, load_from="SGID"),
        "SubnetID": fields.Str(required=True, load_from="SubnetID"),
        "VPCID": fields.Str(required=True, load_from="VPCID"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class NATGWRuleInfoSchema(schema.ResponseSchema):
    """ NATGWRuleInfo - NAT网关关联的白名单资源信息
    """

    fields = {
        "BindResourceID": fields.Str(required=True, load_from="BindResourceID"),
        "BindResourceType": fields.Str(
            required=True, load_from="BindResourceType"
        ),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IP": fields.Str(required=True, load_from="IP"),
        "NATGWID": fields.Str(required=True, load_from="NATGWID"),
        "NATGWType": fields.Str(required=True, load_from="NATGWType"),
        "Name": fields.Str(required=True, load_from="Name"),
        "RuleID": fields.Str(required=True, load_from="RuleID"),
        "RuleStatus": fields.Str(required=True, load_from="RuleStatus"),
    }


class PhysicalIPInfoSchema(schema.ResponseSchema):
    """ PhysicalIPInfo - 物理IP信息
    """

    fields = {
        "BindResourceID": fields.Str(required=True, load_from="BindResourceID"),
        "BindResourceType": fields.Str(
            required=True, load_from="BindResourceType"
        ),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IP": fields.Str(required=True, load_from="IP"),
        "Name": fields.Str(required=True, load_from="Name"),
        "OperatorName": fields.Str(required=True, load_from="OperatorName"),
        "PhysicalIPID": fields.Str(required=True, load_from="PhysicalIPID"),
        "Region": fields.Str(required=True, load_from="Region"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "Status": fields.Str(required=True, load_from="Status"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class RSInfoSchema(schema.ResponseSchema):
    """ RSInfo - 转发规则关联的服务节点信息
    """

    fields = {
        "BindResourceID": fields.Str(required=True, load_from="BindResourceID"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IP": fields.Str(required=True, load_from="IP"),
        "LBID": fields.Str(required=True, load_from="LBID"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Port": fields.Int(required=True, load_from="Port"),
        "RSID": fields.Str(required=True, load_from="RSID"),
        "RSMode": fields.Str(required=True, load_from="RSMode"),
        "RSStatus": fields.Str(required=True, load_from="RSStatus"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "VSID": fields.Str(required=True, load_from="VSID"),
        "Weight": fields.Int(required=True, load_from="Weight"),
    }


class RecycledResourceInfoSchema(schema.ResponseSchema):
    """ RecycledResourceInfo - 回收站资源信息
    """

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "DeleteTime": fields.Int(required=True, load_from="DeleteTime"),
        "Description": fields.Str(required=True, load_from="Description"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "IsAutoTerminated": fields.Bool(
            required=True, load_from="IsAutoTerminated"
        ),
        "Name": fields.Str(required=True, load_from="Name"),
        "Region": fields.Str(required=True, load_from="Region"),
        "ResourceID": fields.Str(required=True, load_from="ResourceID"),
        "ResourceType": fields.Str(required=True, load_from="ResourceType"),
        "Status": fields.Str(required=False, load_from="Status"),
        "WillTerminateTime": fields.Int(
            required=True, load_from="WillTerminateTime"
        ),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class SGRuleInfoSchema(schema.ResponseSchema):
    """ SGRuleInfo - 安全组规则信息
    """

    fields = {
        "DstPort": fields.Str(required=False, load_from="DstPort"),
        "IsIn": fields.Str(required=False, load_from="IsIn"),
        "Priority": fields.Str(required=False, load_from="Priority"),
        "ProtocolType": fields.Str(required=False, load_from="ProtocolType"),
        "RuleAction": fields.Str(required=False, load_from="RuleAction"),
        "RuleID": fields.Str(required=False, load_from="RuleID"),
        "SrcIP": fields.Str(required=False, load_from="SrcIP"),
    }


class SGInfoSchema(schema.ResponseSchema):
    """ SGInfo - 安全组信息
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Region": fields.Str(required=False, load_from="Region"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceCount": fields.Int(required=False, load_from="ResourceCount"),
        "Rule": fields.List(SGRuleInfoSchema()),
        "RuleCount": fields.Int(required=False, load_from="RuleCount"),
        "SGID": fields.Str(required=False, load_from="SGID"),
        "Status": fields.Str(required=False, load_from="Status"),
        "UpdateTime": fields.Int(required=False, load_from="UpdateTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class StorageTypeInfoSchema(schema.ResponseSchema):
    """ StorageTypeInfo - 存储类型信息
    """

    fields = {
        "Region": fields.Str(required=True, load_from="Region"),
        "SetArch": fields.Str(required=True, load_from="SetArch"),
        "StorageType": fields.Str(required=True, load_from="StorageType"),
        "StorageTypeAlias": fields.Str(
            required=True, load_from="StorageTypeAlias"
        ),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class SubnetInfoSchema(schema.ResponseSchema):
    """ SubnetInfo - 子网信息
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Network": fields.Str(required=False, load_from="Network"),
        "Region": fields.Str(required=False, load_from="Region"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetID": fields.Str(required=False, load_from="SubnetID"),
        "UpdateTime": fields.Int(required=False, load_from="UpdateTime"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UserInfoSchema(schema.ResponseSchema):
    """ UserInfo - 租户信息
    """

    fields = {
        "Amount": fields.Float(required=False, load_from="Amount"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Email": fields.Str(required=False, load_from="Email"),
        "PrivateKey": fields.Str(required=False, load_from="PrivateKey"),
        "PublicKey": fields.Str(required=False, load_from="PublicKey"),
        "Status": fields.Str(required=False, load_from="Status"),
        "UpdateTime": fields.Int(required=False, load_from="UpdateTime"),
        "UserID": fields.Int(required=False, load_from="UserID"),
    }


class VMIPInfoSchema(schema.ResponseSchema):
    """ VMIPInfo - UCloudStack虚拟机IP信息
    """

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "InterfaceID": fields.Str(required=False, load_from="InterfaceID"),
        "IsElastic": fields.Str(required=False, load_from="IsElastic"),
        "MAC": fields.Str(required=False, load_from="MAC"),
        "SGID": fields.Str(required=False, load_from="SGID"),
        "SGName": fields.Str(required=False, load_from="SGName"),
        "SubnetID": fields.Str(required=False, load_from="SubnetID"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "Type": fields.Str(required=False, load_from="Type"),
        "VPCID": fields.Str(required=False, load_from="VPCID"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
    }


class VMDiskInfoSchema(schema.ResponseSchema):
    """ VMDiskInfo - UCloudStack虚拟机磁盘信息
    """

    fields = {
        "DiskID": fields.Str(required=False, load_from="DiskID"),
        "Drive": fields.Str(required=False, load_from="Drive"),
        "IsElastic": fields.Str(required=False, load_from="IsElastic"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class VMInstanceInfoSchema(schema.ResponseSchema):
    """ VMInstanceInfo - UCloudStack虚拟机信息
    """

    fields = {
        "CPU": fields.Int(required=False, load_from="CPU"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DiskInfos": fields.List(VMDiskInfoSchema()),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "IPInfos": fields.List(VMIPInfoSchema()),
        "ImageID": fields.Str(required=False, load_from="ImageID"),
        "Memory": fields.Int(required=False, load_from="Memory"),
        "Name": fields.Str(required=False, load_from="Name"),
        "OSName": fields.Str(required=False, load_from="OSName"),
        "OSType": fields.Str(required=False, load_from="OSType"),
        "Region": fields.Str(required=False, load_from="Region"),
        "RegionAlias": fields.Str(required=False, load_from="RegionAlias"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetID": fields.Str(required=False, load_from="SubnetID"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "VMID": fields.Str(required=False, load_from="VMID"),
        "VMType": fields.Str(required=False, load_from="VMType"),
        "VMTypeAlias": fields.Str(required=False, load_from="VMTypeAlias"),
        "VPCID": fields.Str(required=False, load_from="VPCID"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Zone": fields.Str(required=False, load_from="Zone"),
        "ZoneAlias": fields.Str(required=False, load_from="ZoneAlias"),
    }


class VMTypeInfoSchema(schema.ResponseSchema):
    """ VMTypeInfo - 主机机型信息
    """

    fields = {
        "Region": fields.Str(required=True, load_from="Region"),
        "SetArch": fields.Str(required=True, load_from="SetArch"),
        "VMType": fields.Str(required=True, load_from="VMType"),
        "VMTypeAlias": fields.Str(required=True, load_from="VMTypeAlias"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class VPCInfoSchema(schema.ResponseSchema):
    """ VPCInfo - VPC信息
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Network": fields.Str(required=False, load_from="Network"),
        "Region": fields.Str(required=False, load_from="Region"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetCount": fields.Int(required=False, load_from="SubnetCount"),
        "SubnetInfos": fields.List(SubnetInfoSchema()),
        "UpdateTime": fields.Int(required=False, load_from="UpdateTime"),
        "VPCID": fields.Str(required=False, load_from="VPCID"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class VSPolicyInfoSchema(schema.ResponseSchema):
    """ VSPolicyInfo - 内容转发规则信息
    """

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Domain": fields.Str(required=True, load_from="Domain"),
        "LBID": fields.Str(required=True, load_from="LBID"),
        "Path": fields.Str(required=True, load_from="Path"),
        "PolicyID": fields.Str(required=True, load_from="PolicyID"),
        "PolicyStatus": fields.Str(required=True, load_from="PolicyStatus"),
        "RSInfos": fields.List(RSInfoSchema()),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "VSID": fields.Str(required=True, load_from="VSID"),
    }


class VSInfoSchema(schema.ResponseSchema):
    """ VSInfo - RServer信息
    """

    fields = {
        "AlarmTemplateID": fields.Str(
            required=True, load_from="AlarmTemplateID"
        ),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "Domain": fields.Str(required=False, load_from="Domain"),
        "HealthcheckType": fields.Str(
            required=True, load_from="HealthcheckType"
        ),
        "KeepaliveTimeout": fields.Int(
            required=True, load_from="KeepaliveTimeout"
        ),
        "LBID": fields.Str(required=True, load_from="LBID"),
        "Path": fields.Str(required=False, load_from="Path"),
        "PersistenceKey": fields.Str(
            required=False, load_from="PersistenceKey"
        ),
        "PersistenceType": fields.Str(
            required=True, load_from="PersistenceType"
        ),
        "Port": fields.Int(required=True, load_from="Port"),
        "Protocol": fields.Str(required=True, load_from="Protocol"),
        "RSHealthStatus": fields.Str(required=True, load_from="RSHealthStatus"),
        "RSInfos": fields.List(RSInfoSchema()),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "VSID": fields.Str(required=True, load_from="VSID"),
        "VSPolicyInfos": fields.List(VSPolicyInfoSchema()),
        "VSStatus": fields.Str(required=True, load_from="VSStatus"),
    }


class PriceInfoSchema(schema.ResponseSchema):
    """ PriceInfo - 价格信息
    """

    fields = {
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "Price": fields.Float(required=True, load_from="Price"),
    }
