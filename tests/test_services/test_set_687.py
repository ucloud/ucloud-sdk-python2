# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
import pytest
import logging
from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)
scenario = utest.Scenario(687)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_687(client, variables):
    scenario.initial(variables)
    scenario.variables["VPC_name_1"] = "VPC_api_test_1"
    scenario.variables["remark"] = "remark_api_test"
    scenario.variables["tag"] = "tag_api_test"
    scenario.variables["Subnet_name_1_1"] = "subnet_1_1"
    scenario.variables["subnet_netmask"] = 24
    scenario.variables["project_id"] = "org-achi1o"
    scenario.run(client)


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetProjectListResponse"),
    ],
    action="GetProjectList",
)
def get_project_list_00(client, variables):
    d = {}
    try:
        resp = client.uaccount().get_project_list(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["project_list"] = utest.value_at_path(resp, "ProjectSet")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateVPC",
)
def create_vpc_01(client, variables):
    d = {
        "Tag": variables.get("tag"),
        "Remark": variables.get("remark"),
        "Region": variables.get("Region"),
        "Network": ["172.16.16.0/20"],
        "Name": variables.get("VPC_name_1"),
    }
    try:
        resp = client.vpc().create_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["VPCId_1"] = utest.value_at_path(resp, "VPCId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSubnet",
)
def create_subnet_02(client, variables):
    d = {
        "VPCId": variables.get("VPCId_1"),
        "Tag": variables.get("tag"),
        "SubnetName": variables.get("Subnet_name_1_1"),
        "Subnet": "172.16.17.0",
        "Remark": variables.get("remark"),
        "Region": variables.get("Region"),
        "Netmask": variables.get("subnet_netmask"),
    }
    try:
        resp = client.vpc().create_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["SubnetId_1_1"] = utest.value_at_path(resp, "SubnetId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "UpdateSubnetAttributeResponse"),
    ],
    action="UpdateSubnetAttribute",
)
def update_subnet_attribute_03(client, variables):
    d = {
        "Tag": "qa",
        "SubnetId": variables.get("SubnetId_1_1"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().update_subnet_attribute(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeSubnet",
)
def describe_subnet_04(client, variables):
    d = {
        "SubnetId": variables.get("SubnetId_1_1"),
        "Region": variables.get("Region"),
        "Offset": 1,
        "Limit": 1,
    }
    try:
        resp = client.vpc().describe_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    action="CreateVPC",
)
def create_vpc_05(client, variables):
    d = {
        "Region": variables.get("Region"),
        "Network": ["192.168.16.0/20"],
        "Name": "vpc_2",
    }
    try:
        resp = client.vpc().create_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["VPCId_2"] = utest.value_at_path(resp, "VPCId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSubnet",
)
def create_subnet_06(client, variables):
    d = {
        "VPCId": variables.get("VPCId_2"),
        "SubnetName": "Subnet_2_1",
        "Subnet": "192.168.17.0",
        "Region": variables.get("Region"),
        "Netmask": variables.get("subnet_netmask"),
    }
    try:
        resp = client.vpc().create_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["SubnetId_2_1"] = utest.value_at_path(resp, "SubnetId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CreateSubnetResponse"),
    ],
    action="CreateSubnet",
)
def create_subnet_07(client, variables):
    d = {
        "VPCId": variables.get("VPCId_2"),
        "Tag": "Subnet_2_2",
        "SubnetName": "Subnet_2_2",
        "Subnet": "192.168.18.0",
        "Region": variables.get("Region"),
        "Netmask": variables.get("subnet_netmask"),
    }
    try:
        resp = client.vpc().create_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["SubnetId_2_2"] = utest.value_at_path(resp, "SubnetId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.VPCId", variables.get("VPCId_1")),
        ("str_eq", "DataSet.0.VPCName", variables.get("VPC_name_1")),
        ("str_eq", "DataSet.0.SubnetId", variables.get("SubnetId_1_1")),
        ("str_eq", "DataSet.0.SubnetName", variables.get("Subnet_name_1_1")),
        ("str_eq", "DataSet.0.Tag", "qa"),
        ("str_eq", "DataSet.0.Remark", variables.get("remark")),
        ("str_eq", "DataSet.0.SubnetType", 2),
        ("str_eq", "DataSet.0.Netmask", 24),
    ],
    action="DescribeSubnet",
)
def describe_subnet_08(client, variables):
    d = {
        "VPCId": variables.get("VPCId_1"),
        "SubnetId": variables.get("SubnetId_1_1"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().describe_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="AllocateVIP",
)
def allocate_vip_09(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "VPCId": variables.get("VPCId_1"),
        "SubnetId": variables.get("SubnetId_1_1"),
        "Remark": "vip_tag1",
        "Region": variables.get("Region"),
        "Name": "vip_api_auto",
    }
    try:
        resp = client.unet().allocate_vip(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["VIPId_1"] = utest.value_at_path(resp, "VIPSet.0.VIPId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "VIPSet.0.VPCId", variables.get("VPCId_1")),
        ("str_eq", "VIPSet.0.VIPId", variables.get("VIPId_1")),
        ("str_eq", "VIPSet.0.SubnetId", variables.get("SubnetId_1_1")),
    ],
    action="DescribeVIP",
)
def describe_vip_10(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "VPCId": variables.get("VPCId_1"),
        "SubnetId": variables.get("SubnetId_1_1"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.unet().describe_vip(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["VIP_ip_1"] = utest.value_at_path(resp, "DataSet.0")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "TotalCount", 1),
        ("str_eq", "DataSet.0.ResourceId", variables.get("VIPId_1")),
        ("str_eq", "DataSet.0.IP", variables.get("VIP_ip_1")),
    ],
    action="DescribeSubnetResource",
)
def describe_subnet_resource_11(client, variables):
    d = {
        "SubnetId": variables.get("SubnetId_1_1"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 20,
    }
    try:
        resp = client.vpc().describe_subnet_resource(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ReleaseVIP",
)
def release_vip_12(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "VIPId": variables.get("VIPId_1"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.unet().release_vip(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSubnet",
)
def delete_subnet_13(client, variables):
    d = {
        "SubnetId": variables.get("SubnetId_1_1"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().delete_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSubnet",
)
def delete_subnet_14(client, variables):
    d = {
        "SubnetId": variables.get("SubnetId_2_1"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().delete_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSubnet",
)
def delete_subnet_15(client, variables):
    d = {
        "SubnetId": variables.get("SubnetId_2_2"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().delete_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "AddVPCNetworkResponse"),
    ],
    action="AddVPCNetwork",
)
def add_vpc_network_16(client, variables):
    d = {
        "VPCId": variables.get("VPCId_1"),
        "Region": variables.get("Region"),
        "Network": ["10.100.96.0/20"],
    }
    try:
        resp = client.vpc().add_vpc_network(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeVPCResponse"),
    ],
    action="DescribeVPC",
)
def describe_vpc_17(client, variables):
    d = {
        "VPCIds": [variables.get("VPCId_1")],
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().describe_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateVPCIntercom",
)
def create_vpc_intercom_18(client, variables):
    d = {
        "VPCId": variables.get("VPCId_1"),
        "Region": variables.get("Region"),
        "DstVPCId": variables.get("VPCId_2"),
        "DstRegion": variables.get("Region"),
        "DstProjectId": funcs.search_value(
            variables.get("project_list"), "IsDefault", True, "ProjectId"
        ),
    }
    try:
        resp = client.vpc().create_vpc_intercom(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.VPCId", variables.get("VPCId_2")),
    ],
    action="DescribeVPCIntercom",
)
def describe_vpc_intercom_19(client, variables):
    d = {"VPCId": variables.get("VPCId_1"), "Region": variables.get("Region")}
    try:
        resp = client.vpc().describe_vpc_intercom(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteVPCIntercom",
)
def delete_vpc_intercom_20(client, variables):
    d = {
        "VPCId": variables.get("VPCId_1"),
        "Region": variables.get("Region"),
        "DstVPCId": variables.get("VPCId_2"),
        "DstRegion": variables.get("Region"),
        "DstProjectId": funcs.search_value(
            variables.get("project_list"), "IsDefault", True, "ProjectId"
        ),
    }
    try:
        resp = client.vpc().delete_vpc_intercom(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteVPC",
)
def delete_vpc_21(client, variables):
    d = {"VPCId": variables.get("VPCId_1"), "Region": variables.get("Region")}
    try:
        resp = client.vpc().delete_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=2,
    fast_fail=False,
    action="DeleteVPC",
)
def delete_vpc_22(client, variables):
    d = {"VPCId": variables.get("VPCId_2"), "Region": variables.get("Region")}
    try:
        resp = client.vpc().delete_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp