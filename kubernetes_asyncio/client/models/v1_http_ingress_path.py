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


class V1HTTPIngressPath(object):
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
        'backend': 'V1IngressBackend',
        'path': 'str',
        'path_type': 'str'
    }

    attribute_map = {
        'backend': 'backend',
        'path': 'path',
        'path_type': 'pathType'
    }

    def __init__(self, backend=None, path=None, path_type=None, local_vars_configuration=None):  # noqa: E501
        """V1HTTPIngressPath - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._backend = None
        self._path = None
        self._path_type = None
        self.discriminator = None

        self.backend = backend
        if path is not None:
            self.path = path
        self.path_type = path_type

    @property
    def backend(self):
        """Gets the backend of this V1HTTPIngressPath.  # noqa: E501


        :return: The backend of this V1HTTPIngressPath.  # noqa: E501
        :rtype: V1IngressBackend
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this V1HTTPIngressPath.


        :param backend: The backend of this V1HTTPIngressPath.  # noqa: E501
        :type backend: V1IngressBackend
        """
        if self.local_vars_configuration.client_side_validation and backend is None:  # noqa: E501
            raise ValueError("Invalid value for `backend`, must not be `None`")  # noqa: E501

        self._backend = backend

    @property
    def path(self):
        """Gets the path of this V1HTTPIngressPath.  # noqa: E501

        path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value \"Exact\" or \"Prefix\".  # noqa: E501

        :return: The path of this V1HTTPIngressPath.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1HTTPIngressPath.

        path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value \"Exact\" or \"Prefix\".  # noqa: E501

        :param path: The path of this V1HTTPIngressPath.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def path_type(self):
        """Gets the path_type of this V1HTTPIngressPath.  # noqa: E501

        pathType determines the interpretation of the path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is   done on a path element by element basis. A path element refers is the   list of labels in the path split by the '/' separator. A request is a   match for path p if every p is an element-wise prefix of p of the   request path. Note that if the last element of the path is a substring   of the last element in request path, it is not a match (e.g. /foo/bar   matches /foo/bar/baz, but does not match /foo/barbaz). * ImplementationSpecific: Interpretation of the Path matching is up to   the IngressClass. Implementations can treat this as a separate PathType   or treat it identically to Prefix or Exact path types. Implementations are required to support all path types.  # noqa: E501

        :return: The path_type of this V1HTTPIngressPath.  # noqa: E501
        :rtype: str
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        """Sets the path_type of this V1HTTPIngressPath.

        pathType determines the interpretation of the path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is   done on a path element by element basis. A path element refers is the   list of labels in the path split by the '/' separator. A request is a   match for path p if every p is an element-wise prefix of p of the   request path. Note that if the last element of the path is a substring   of the last element in request path, it is not a match (e.g. /foo/bar   matches /foo/bar/baz, but does not match /foo/barbaz). * ImplementationSpecific: Interpretation of the Path matching is up to   the IngressClass. Implementations can treat this as a separate PathType   or treat it identically to Prefix or Exact path types. Implementations are required to support all path types.  # noqa: E501

        :param path_type: The path_type of this V1HTTPIngressPath.  # noqa: E501
        :type path_type: str
        """
        if self.local_vars_configuration.client_side_validation and path_type is None:  # noqa: E501
            raise ValueError("Invalid value for `path_type`, must not be `None`")  # noqa: E501

        self._path_type = path_type

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
        if not isinstance(other, V1HTTPIngressPath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1HTTPIngressPath):
            return True

        return self.to_dict() != other.to_dict()
