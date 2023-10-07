# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.28.2
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


class V1EndpointSubset(object):
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
        'addresses': 'list[V1EndpointAddress]',
        'not_ready_addresses': 'list[V1EndpointAddress]',
        'ports': 'list[CoreV1EndpointPort]'
    }

    attribute_map = {
        'addresses': 'addresses',
        'not_ready_addresses': 'notReadyAddresses',
        'ports': 'ports'
    }

    def __init__(self, addresses=None, not_ready_addresses=None, ports=None, local_vars_configuration=None):  # noqa: E501
        """V1EndpointSubset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._not_ready_addresses = None
        self._ports = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if not_ready_addresses is not None:
            self.not_ready_addresses = not_ready_addresses
        if ports is not None:
            self.ports = ports

    @property
    def addresses(self):
        """Gets the addresses of this V1EndpointSubset.  # noqa: E501

        IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.  # noqa: E501

        :return: The addresses of this V1EndpointSubset.  # noqa: E501
        :rtype: list[V1EndpointAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this V1EndpointSubset.

        IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.  # noqa: E501

        :param addresses: The addresses of this V1EndpointSubset.  # noqa: E501
        :type addresses: list[V1EndpointAddress]
        """

        self._addresses = addresses

    @property
    def not_ready_addresses(self):
        """Gets the not_ready_addresses of this V1EndpointSubset.  # noqa: E501

        IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.  # noqa: E501

        :return: The not_ready_addresses of this V1EndpointSubset.  # noqa: E501
        :rtype: list[V1EndpointAddress]
        """
        return self._not_ready_addresses

    @not_ready_addresses.setter
    def not_ready_addresses(self, not_ready_addresses):
        """Sets the not_ready_addresses of this V1EndpointSubset.

        IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.  # noqa: E501

        :param not_ready_addresses: The not_ready_addresses of this V1EndpointSubset.  # noqa: E501
        :type not_ready_addresses: list[V1EndpointAddress]
        """

        self._not_ready_addresses = not_ready_addresses

    @property
    def ports(self):
        """Gets the ports of this V1EndpointSubset.  # noqa: E501

        Port numbers available on the related IP addresses.  # noqa: E501

        :return: The ports of this V1EndpointSubset.  # noqa: E501
        :rtype: list[CoreV1EndpointPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this V1EndpointSubset.

        Port numbers available on the related IP addresses.  # noqa: E501

        :param ports: The ports of this V1EndpointSubset.  # noqa: E501
        :type ports: list[CoreV1EndpointPort]
        """

        self._ports = ports

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
        if not isinstance(other, V1EndpointSubset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1EndpointSubset):
            return True

        return self.to_dict() != other.to_dict()
