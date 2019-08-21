# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
from ucloud.core.typesystem import schema, fields
from ucloud.services.udpn.schemas import models

""" UDPN API Schema
"""
"""
API: AllocateUDPN

分配一条 UDPN 专线
"""


class AllocateUDPNRequestSchema(schema.RequestSchema):
    """ AllocateUDPN - 分配一条 UDPN 专线
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Peer1": fields.Str(required=True, dump_to="Peer1"),
        "Peer2": fields.Str(required=True, dump_to="Peer2"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=False, dump_to="Region"),
    }


class AllocateUDPNResponseSchema(schema.ResponseSchema):
    """ AllocateUDPN - 分配一条 UDPN 专线
    """

    fields = {"UDPNId": fields.Str(required=True, load_from="UDPNId")}


"""
API: DescribeUDPN

描述 UDPN
"""


class DescribeUDPNRequestSchema(schema.RequestSchema):
    """ DescribeUDPN - 描述 UDPN
    """

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "UDPNId": fields.Str(required=False, dump_to="UDPNId"),
    }


class DescribeUDPNResponseSchema(schema.ResponseSchema):
    """ DescribeUDPN - 描述 UDPN
    """

    fields = {
        "DataSet": fields.List(
            models.UDPNDataSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: GetUDPNLineList

获取当前支持的专线线路列表
"""


class GetUDPNLineListRequestSchema(schema.RequestSchema):
    """ GetUDPNLineList - 获取当前支持的专线线路列表
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
    }


class GetUDPNLineListResponseSchema(schema.ResponseSchema):
    """ GetUDPNLineList - 获取当前支持的专线线路列表
    """

    fields = {
        "DataSet": fields.List(
            models.UDPNLineSetSchema(), required=True, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: GetUDPNPrice

获取 UDPN 价格
"""


class GetUDPNPriceRequestSchema(schema.RequestSchema):
    """ GetUDPNPrice - 获取 UDPN 价格
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Peer1": fields.Str(required=True, dump_to="Peer1"),
        "Peer2": fields.Str(required=True, dump_to="Peer2"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=False, dump_to="Region"),
    }


class GetUDPNPriceResponseSchema(schema.ResponseSchema):
    """ GetUDPNPrice - 获取 UDPN 价格
    """

    fields = {
        "Price": fields.Float(required=True, load_from="Price"),
        "PurchaseValue": fields.Int(required=True, load_from="PurchaseValue"),
    }


"""
API: GetUDPNUpgradePrice

获取专线升级价格
"""


class GetUDPNUpgradePriceRequestSchema(schema.RequestSchema):
    """ GetUDPNUpgradePrice - 获取专线升级价格
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "UDPNId": fields.Str(required=True, dump_to="UDPNId"),
    }


class GetUDPNUpgradePriceResponseSchema(schema.ResponseSchema):
    """ GetUDPNUpgradePrice - 获取专线升级价格
    """

    fields = {"Price": fields.Float(required=True, load_from="Price")}


"""
API: ModifyUDPNBandwidth

修改带宽值
"""


class ModifyUDPNBandwidthRequestSchema(schema.RequestSchema):
    """ ModifyUDPNBandwidth - 修改带宽值
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "UDPNId": fields.Str(required=True, dump_to="UDPNId"),
    }


class ModifyUDPNBandwidthResponseSchema(schema.ResponseSchema):
    """ ModifyUDPNBandwidth - 修改带宽值
    """

    fields = {}


"""
API: ReleaseUDPN

释放 UDPN
"""


class ReleaseUDPNRequestSchema(schema.RequestSchema):
    """ ReleaseUDPN - 释放 UDPN
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "UDPNId": fields.Str(required=True, dump_to="UDPNId"),
    }


class ReleaseUDPNResponseSchema(schema.ResponseSchema):
    """ ReleaseUDPN - 释放 UDPN
    """

    fields = {}
