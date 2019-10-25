# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
from ucloud.core.typesystem import schema, fields


class CacheConfSchema(schema.ResponseSchema):
    """ CacheConf - 缓存配置
    """

    fields = {
        "CacheBehavior": fields.Int(required=False, load_from="CacheBehavior"),
        "CacheTTL": fields.Int(required=False, load_from="CacheTTL"),
        "CacheUnit": fields.Str(required=False, load_from="CacheUnit"),
        "Description": fields.Str(required=False, load_from="Description"),
        "FollowOriginRule": fields.Int(
            required=False, load_from="FollowOriginRule"
        ),
        "HttpCodePattern": fields.Str(
            required=False, load_from="HttpCodePattern"
        ),
        "IgnoreQueryString": fields.Int(
            required=False, load_from="IgnoreQueryString"
        ),
        "PathPattern": fields.Str(required=False, load_from="PathPattern"),
    }


class AccessConfSchema(schema.ResponseSchema):
    """ AccessConf - 访问控制
    """

    fields = {
        "IpBlacklist": fields.Str(required=False, load_from="IpBlacklist")
    }


class DomainInfoSchema(schema.ResponseSchema):
    """ DomainInfo - 域名配置
    """

    fields = {
        "AccessConf": AccessConfSchema(),
        "AreaCode": fields.Str(required=False, load_from="AreaCode"),
        "CacheConf": fields.List(CacheConfSchema()),
        "CacheHost": fields.Str(required=False, load_from="CacheHost"),
        "CdnProtocol": fields.Str(required=False, load_from="CdnProtocol"),
        "CdnType": fields.Str(required=True, load_from="CdnType"),
        "CertName": fields.Str(required=False, load_from="CertName"),
        "Cname": fields.Str(required=False, load_from="Cname"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Domain": fields.Str(required=False, load_from="Domain"),
        "DomainId": fields.Str(required=False, load_from="DomainId"),
        "HttpsStatusAbroad": fields.Str(
            required=False, load_from="HttpsStatusAbroad"
        ),
        "HttpsStatusCn": fields.Str(required=False, load_from="HttpsStatusCn"),
        "NullRefer": fields.Bool(required=False, load_from="NullRefer"),
        "OriginHost": fields.Str(required=False, load_from="OriginHost"),
        "OriginIp": fields.List(fields.Str()),
        "OriginPort": fields.Int(required=False, load_from="OriginPort"),
        "OriginProtocol": fields.Str(
            required=False, load_from="OriginProtocol"
        ),
        "ReferList": fields.List(fields.Str()),
        "ReferStatus": fields.Bool(required=False, load_from="ReferStatus"),
        "ReferType": fields.Int(required=False, load_from="ReferType"),
        "Status": fields.Str(required=False, load_from="Status"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TestUrl": fields.Str(required=True, load_from="TestUrl"),
        "ValidTime": fields.Int(required=False, load_from="ValidTime"),
    }


class UrlProgressInfoSchema(schema.ResponseSchema):
    """ UrlProgressInfo - UrlProgressInfo
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "FinishTime": fields.Int(required=False, load_from="FinishTime"),
        "Progress": fields.Int(required=False, load_from="Progress"),
        "Status": fields.Str(required=False, load_from="Status"),
        "Url": fields.Str(required=False, load_from="Url"),
    }


class TaskInfoSchema(schema.ResponseSchema):
    """ TaskInfo - 预取刷新的任务信息
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Status": fields.Str(required=False, load_from="Status"),
        "TaskId": fields.Str(required=False, load_from="TaskId"),
        "Type": fields.Str(required=False, load_from="Type"),
        "UrlLists": fields.List(UrlProgressInfoSchema()),
    }


class BandwidthInfoSchema(schema.ResponseSchema):
    """ BandwidthInfo - BandwidthInfo
    """

    fields = {
        "CdnBandwidth": fields.Str(required=False, load_from="CdnBandwidth"),
        "Time": fields.Int(required=False, load_from="Time"),
    }


class HitRateInfoSchema(schema.ResponseSchema):
    """ HitRateInfo - HitRateInfo
    """

    fields = {
        "FlowHitRate": fields.Float(required=False, load_from="FlowHitRate"),
        "RequestHitRate": fields.Float(
            required=False, load_from="RequestHitRate"
        ),
        "Time": fields.Int(required=False, load_from="Time"),
    }


class HttpCodeInfoSchema(schema.ResponseSchema):
    """ HttpCodeInfo - HttpCodeInfo
    """

    fields = {
        "HttpFiveXX": fields.Int(required=False, load_from="HttpFiveXX"),
        "HttpFourXX": fields.Int(required=False, load_from="HttpFourXX"),
        "HttpOneXX": fields.Int(required=False, load_from="HttpOneXX"),
        "HttpThreeXX": fields.Int(required=False, load_from="HttpThreeXX"),
        "HttpTwoXX": fields.Int(required=False, load_from="HttpTwoXX"),
        "Time": fields.Int(required=False, load_from="Time"),
    }


class HttpCodeV2DetailSchema(schema.ResponseSchema):
    """ HttpCodeV2Detail - HTTP状态码详细信息
    """

    fields = {
        "Http100": fields.Int(required=False, load_from="Http100"),
        "Http101": fields.Int(required=False, load_from="Http101"),
        "Http102": fields.Int(required=False, load_from="Http102"),
        "Http200": fields.Int(required=False, load_from="Http200"),
        "Http201": fields.Int(required=False, load_from="Http201"),
        "Http202": fields.Int(required=False, load_from="Http202"),
        "Http203": fields.Int(required=False, load_from="Http203"),
        "Http204": fields.Int(required=False, load_from="Http204"),
        "Http205": fields.Int(required=False, load_from="Http205"),
        "Http206": fields.Int(required=False, load_from="Http206"),
        "Http207": fields.Int(required=False, load_from="Http207"),
        "Http300": fields.Int(required=False, load_from="Http300"),
        "Http301": fields.Int(required=False, load_from="Http301"),
        "Http302": fields.Int(required=False, load_from="Http302"),
        "Http303": fields.Int(required=False, load_from="Http303"),
        "Http304": fields.Int(required=False, load_from="Http304"),
        "Http305": fields.Int(required=False, load_from="Http305"),
        "Http306": fields.Int(required=False, load_from="Http306"),
        "Http307": fields.Int(required=False, load_from="Http307"),
        "Http400": fields.Int(required=False, load_from="Http400"),
        "Http401": fields.Int(required=False, load_from="Http401"),
        "Http402": fields.Int(required=False, load_from="Http402"),
        "Http403": fields.Int(required=False, load_from="Http403"),
        "Http404": fields.Int(required=False, load_from="Http404"),
        "Http405": fields.Int(required=False, load_from="Http405"),
        "Http406": fields.Int(required=False, load_from="Http406"),
        "Http407": fields.Int(required=False, load_from="Http407"),
        "Http408": fields.Int(required=False, load_from="Http408"),
        "Http409": fields.Int(required=False, load_from="Http409"),
        "Http410": fields.Int(required=False, load_from="Http410"),
        "Http411": fields.Int(required=False, load_from="Http411"),
        "Http412": fields.Int(required=False, load_from="Http412"),
        "Http413": fields.Int(required=False, load_from="Http413"),
        "Http414": fields.Int(required=False, load_from="Http414"),
        "Http415": fields.Int(required=False, load_from="Http415"),
        "Http416": fields.Int(required=False, load_from="Http416"),
        "Http417": fields.Int(required=False, load_from="Http417"),
        "Http418": fields.Int(required=False, load_from="Http418"),
        "Http421": fields.Int(required=False, load_from="Http421"),
        "Http422": fields.Int(required=False, load_from="Http422"),
        "Http423": fields.Int(required=False, load_from="Http423"),
        "Http424": fields.Int(required=False, load_from="Http424"),
        "Http425": fields.Int(required=False, load_from="Http425"),
        "Http426": fields.Int(required=False, load_from="Http426"),
        "Http449": fields.Int(required=False, load_from="Http449"),
        "Http451": fields.Int(required=False, load_from="Http451"),
        "Http500": fields.Int(required=False, load_from="Http500"),
        "Http501": fields.Int(required=False, load_from="Http501"),
        "Http502": fields.Int(required=False, load_from="Http502"),
        "Http503": fields.Int(required=False, load_from="Http503"),
        "Http504": fields.Int(required=False, load_from="Http504"),
        "Http505": fields.Int(required=False, load_from="Http505"),
        "Http506": fields.Int(required=False, load_from="Http506"),
        "Http507": fields.Int(required=False, load_from="Http507"),
        "Http509": fields.Int(required=False, load_from="Http509"),
        "Http510": fields.Int(required=False, load_from="Http510"),
        "Time": fields.Int(required=True, load_from="Time"),
    }


class RequestInfoSchema(schema.ResponseSchema):
    """ RequestInfo - RequestInfo
    """

    fields = {
        "CdnRequest": fields.Float(required=False, load_from="CdnRequest"),
        "OriginRequest": fields.Float(
            required=False, load_from="OriginRequest"
        ),
        "Time": fields.Int(required=False, load_from="Time"),
    }


class LogSetInfoSchema(schema.ResponseSchema):
    """ LogSetInfo - 日志信息
    """

    fields = {
        "AbroadLog": fields.List(fields.Str()),
        "CnLog": fields.List(fields.Str()),
        "Time": fields.Int(required=False, load_from="Time"),
    }


class LogSetListSchema(schema.ResponseSchema):
    """ LogSetList - 日志信息列表
    """

    fields = {
        "Domain": fields.Str(required=False, load_from="Domain"),
        "Logs": fields.List(LogSetInfoSchema()),
    }


class UcdnDomainTrafficSetSchema(schema.ResponseSchema):
    """ UcdnDomainTrafficSet - GetUcdnDomainTraffic
    """

    fields = {
        "Time": fields.Int(required=False, load_from="Time"),
        "Value": fields.Float(required=False, load_from="Value"),
    }


class BandwidthInfoDetailSchema(schema.ResponseSchema):
    """ BandwidthInfoDetail - 带宽值信息模型(时间-带宽)
    """

    fields = {
        "Bandwidth": fields.Float(required=True, load_from="Bandwidth"),
        "Time": fields.Int(required=True, load_from="Time"),
    }


class TrafficSetSchema(schema.ResponseSchema):
    """ TrafficSet - GetUcdnTraffic
    """

    fields = {
        "Areacode": fields.Str(required=False, load_from="Areacode"),
        "TrafficLeft": fields.Str(required=False, load_from="TrafficLeft"),
        "TrafficTotal": fields.Str(required=False, load_from="TrafficTotal"),
        "TrafficUsed": fields.Str(required=False, load_from="TrafficUsed"),
    }
