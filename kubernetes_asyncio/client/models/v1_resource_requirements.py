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


class V1ResourceRequirements(object):
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
        'claims': 'list[V1ResourceClaim]',
        'limits': 'dict(str, str)',
        'requests': 'dict(str, str)'
    }

    attribute_map = {
        'claims': 'claims',
        'limits': 'limits',
        'requests': 'requests'
    }

    def __init__(self, claims=None, limits=None, requests=None, local_vars_configuration=None):  # noqa: E501
        """V1ResourceRequirements - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._claims = None
        self._limits = None
        self._requests = None
        self.discriminator = None

        if claims is not None:
            self.claims = claims
        if limits is not None:
            self.limits = limits
        if requests is not None:
            self.requests = requests

    @property
    def claims(self):
        """Gets the claims of this V1ResourceRequirements.  # noqa: E501

        Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.  # noqa: E501

        :return: The claims of this V1ResourceRequirements.  # noqa: E501
        :rtype: list[V1ResourceClaim]
        """
        return self._claims

    @claims.setter
    def claims(self, claims):
        """Sets the claims of this V1ResourceRequirements.

        Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.  # noqa: E501

        :param claims: The claims of this V1ResourceRequirements.  # noqa: E501
        :type claims: list[V1ResourceClaim]
        """

        self._claims = claims

    @property
    def limits(self):
        """Gets the limits of this V1ResourceRequirements.  # noqa: E501

        Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/  # noqa: E501

        :return: The limits of this V1ResourceRequirements.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this V1ResourceRequirements.

        Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/  # noqa: E501

        :param limits: The limits of this V1ResourceRequirements.  # noqa: E501
        :type limits: dict(str, str)
        """

        self._limits = limits

    @property
    def requests(self):
        """Gets the requests of this V1ResourceRequirements.  # noqa: E501

        Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/  # noqa: E501

        :return: The requests of this V1ResourceRequirements.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this V1ResourceRequirements.

        Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/  # noqa: E501

        :param requests: The requests of this V1ResourceRequirements.  # noqa: E501
        :type requests: dict(str, str)
        """

        self._requests = requests

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
        if not isinstance(other, V1ResourceRequirements):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ResourceRequirements):
            return True

        return self.to_dict() != other.to_dict()
