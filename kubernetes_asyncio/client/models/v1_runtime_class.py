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


class V1RuntimeClass(object):
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
        'api_version': 'str',
        'handler': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'overhead': 'V1Overhead',
        'scheduling': 'V1Scheduling'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'handler': 'handler',
        'kind': 'kind',
        'metadata': 'metadata',
        'overhead': 'overhead',
        'scheduling': 'scheduling'
    }

    def __init__(self, api_version=None, handler=None, kind=None, metadata=None, overhead=None, scheduling=None, local_vars_configuration=None):  # noqa: E501
        """V1RuntimeClass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._handler = None
        self._kind = None
        self._metadata = None
        self._overhead = None
        self._scheduling = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        self.handler = handler
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if overhead is not None:
            self.overhead = overhead
        if scheduling is not None:
            self.scheduling = scheduling

    @property
    def api_version(self):
        """Gets the api_version of this V1RuntimeClass.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1RuntimeClass.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1RuntimeClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1RuntimeClass.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def handler(self):
        """Gets the handler of this V1RuntimeClass.  # noqa: E501

        handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.  # noqa: E501

        :return: The handler of this V1RuntimeClass.  # noqa: E501
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this V1RuntimeClass.

        handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.  # noqa: E501

        :param handler: The handler of this V1RuntimeClass.  # noqa: E501
        :type handler: str
        """
        if self.local_vars_configuration.client_side_validation and handler is None:  # noqa: E501
            raise ValueError("Invalid value for `handler`, must not be `None`")  # noqa: E501

        self._handler = handler

    @property
    def kind(self):
        """Gets the kind of this V1RuntimeClass.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1RuntimeClass.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1RuntimeClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1RuntimeClass.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1RuntimeClass.  # noqa: E501


        :return: The metadata of this V1RuntimeClass.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1RuntimeClass.


        :param metadata: The metadata of this V1RuntimeClass.  # noqa: E501
        :type metadata: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def overhead(self):
        """Gets the overhead of this V1RuntimeClass.  # noqa: E501


        :return: The overhead of this V1RuntimeClass.  # noqa: E501
        :rtype: V1Overhead
        """
        return self._overhead

    @overhead.setter
    def overhead(self, overhead):
        """Sets the overhead of this V1RuntimeClass.


        :param overhead: The overhead of this V1RuntimeClass.  # noqa: E501
        :type overhead: V1Overhead
        """

        self._overhead = overhead

    @property
    def scheduling(self):
        """Gets the scheduling of this V1RuntimeClass.  # noqa: E501


        :return: The scheduling of this V1RuntimeClass.  # noqa: E501
        :rtype: V1Scheduling
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling):
        """Sets the scheduling of this V1RuntimeClass.


        :param scheduling: The scheduling of this V1RuntimeClass.  # noqa: E501
        :type scheduling: V1Scheduling
        """

        self._scheduling = scheduling

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
        if not isinstance(other, V1RuntimeClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1RuntimeClass):
            return True

        return self.to_dict() != other.to_dict()
