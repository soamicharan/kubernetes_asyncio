# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.28.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.scheduling_api import SchedulingApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestSchedulingApi(unittest.TestCase):
    """SchedulingApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.scheduling_api.SchedulingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
