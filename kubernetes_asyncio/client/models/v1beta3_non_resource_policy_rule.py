# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.29.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1beta3NonResourcePolicyRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'non_resource_urls': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'non_resource_urls': 'nonResourceURLs',
        'verbs': 'verbs'
    }

    def __init__(self, non_resource_urls=None, verbs=None, local_vars_configuration=None):  # noqa: E501
        """V1beta3NonResourcePolicyRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._non_resource_urls = None
        self._verbs = None
        self.discriminator = None

        self.non_resource_urls = non_resource_urls
        self.verbs = verbs

    @property
    def non_resource_urls(self):
        """Gets the non_resource_urls of this V1beta3NonResourcePolicyRule.  # noqa: E501

        `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:   - \"/healthz\" is legal   - \"/hea*\" is illegal   - \"/hea\" is legal but matches nothing   - \"/hea/*\" also matches nothing   - \"/healthz/*\" matches all per-component health checks. \"*\" matches all non-resource urls. if it is present, it must be the only entry. Required.  # noqa: E501

        :return: The non_resource_urls of this V1beta3NonResourcePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._non_resource_urls

    @non_resource_urls.setter
    def non_resource_urls(self, non_resource_urls):
        """Sets the non_resource_urls of this V1beta3NonResourcePolicyRule.

        `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:   - \"/healthz\" is legal   - \"/hea*\" is illegal   - \"/hea\" is legal but matches nothing   - \"/hea/*\" also matches nothing   - \"/healthz/*\" matches all per-component health checks. \"*\" matches all non-resource urls. if it is present, it must be the only entry. Required.  # noqa: E501

        :param non_resource_urls: The non_resource_urls of this V1beta3NonResourcePolicyRule.  # noqa: E501
        :type non_resource_urls: list[str]
        """
        if self.local_vars_configuration.client_side_validation and non_resource_urls is None:  # noqa: E501
            raise ValueError("Invalid value for `non_resource_urls`, must not be `None`")  # noqa: E501

        self._non_resource_urls = non_resource_urls

    @property
    def verbs(self):
        """Gets the verbs of this V1beta3NonResourcePolicyRule.  # noqa: E501

        `verbs` is a list of matching verbs and may not be empty. \"*\" matches all verbs. If it is present, it must be the only entry. Required.  # noqa: E501

        :return: The verbs of this V1beta3NonResourcePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """Sets the verbs of this V1beta3NonResourcePolicyRule.

        `verbs` is a list of matching verbs and may not be empty. \"*\" matches all verbs. If it is present, it must be the only entry. Required.  # noqa: E501

        :param verbs: The verbs of this V1beta3NonResourcePolicyRule.  # noqa: E501
        :type verbs: list[str]
        """
        if self.local_vars_configuration.client_side_validation and verbs is None:  # noqa: E501
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta3NonResourcePolicyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta3NonResourcePolicyRule):
            return True

        return self.to_dict() != other.to_dict()
