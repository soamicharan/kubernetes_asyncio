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


class V1ContainerImage(object):
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
        'names': 'list[str]',
        'size_bytes': 'int'
    }

    attribute_map = {
        'names': 'names',
        'size_bytes': 'sizeBytes'
    }

    def __init__(self, names=None, size_bytes=None, local_vars_configuration=None):  # noqa: E501
        """V1ContainerImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._names = None
        self._size_bytes = None
        self.discriminator = None

        if names is not None:
            self.names = names
        if size_bytes is not None:
            self.size_bytes = size_bytes

    @property
    def names(self):
        """Gets the names of this V1ContainerImage.  # noqa: E501

        Names by which this image is known. e.g. [\"kubernetes.example/hyperkube:v1.0.7\", \"cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7\"]  # noqa: E501

        :return: The names of this V1ContainerImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this V1ContainerImage.

        Names by which this image is known. e.g. [\"kubernetes.example/hyperkube:v1.0.7\", \"cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7\"]  # noqa: E501

        :param names: The names of this V1ContainerImage.  # noqa: E501
        :type names: list[str]
        """

        self._names = names

    @property
    def size_bytes(self):
        """Gets the size_bytes of this V1ContainerImage.  # noqa: E501

        The size of the image in bytes.  # noqa: E501

        :return: The size_bytes of this V1ContainerImage.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this V1ContainerImage.

        The size of the image in bytes.  # noqa: E501

        :param size_bytes: The size_bytes of this V1ContainerImage.  # noqa: E501
        :type size_bytes: int
        """

        self._size_bytes = size_bytes

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
        if not isinstance(other, V1ContainerImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ContainerImage):
            return True

        return self.to_dict() != other.to_dict()
