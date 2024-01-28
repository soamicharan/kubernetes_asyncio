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


class V1LifecycleHandler(object):
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
        '_exec': 'V1ExecAction',
        'http_get': 'V1HTTPGetAction',
        'sleep': 'V1SleepAction',
        'tcp_socket': 'V1TCPSocketAction'
    }

    attribute_map = {
        '_exec': 'exec',
        'http_get': 'httpGet',
        'sleep': 'sleep',
        'tcp_socket': 'tcpSocket'
    }

    def __init__(self, _exec=None, http_get=None, sleep=None, tcp_socket=None, local_vars_configuration=None):  # noqa: E501
        """V1LifecycleHandler - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self.__exec = None
        self._http_get = None
        self._sleep = None
        self._tcp_socket = None
        self.discriminator = None

        if _exec is not None:
            self._exec = _exec
        if http_get is not None:
            self.http_get = http_get
        if sleep is not None:
            self.sleep = sleep
        if tcp_socket is not None:
            self.tcp_socket = tcp_socket

    @property
    def _exec(self):
        """Gets the _exec of this V1LifecycleHandler.  # noqa: E501


        :return: The _exec of this V1LifecycleHandler.  # noqa: E501
        :rtype: V1ExecAction
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this V1LifecycleHandler.


        :param _exec: The _exec of this V1LifecycleHandler.  # noqa: E501
        :type _exec: V1ExecAction
        """

        self.__exec = _exec

    @property
    def http_get(self):
        """Gets the http_get of this V1LifecycleHandler.  # noqa: E501


        :return: The http_get of this V1LifecycleHandler.  # noqa: E501
        :rtype: V1HTTPGetAction
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """Sets the http_get of this V1LifecycleHandler.


        :param http_get: The http_get of this V1LifecycleHandler.  # noqa: E501
        :type http_get: V1HTTPGetAction
        """

        self._http_get = http_get

    @property
    def sleep(self):
        """Gets the sleep of this V1LifecycleHandler.  # noqa: E501


        :return: The sleep of this V1LifecycleHandler.  # noqa: E501
        :rtype: V1SleepAction
        """
        return self._sleep

    @sleep.setter
    def sleep(self, sleep):
        """Sets the sleep of this V1LifecycleHandler.


        :param sleep: The sleep of this V1LifecycleHandler.  # noqa: E501
        :type sleep: V1SleepAction
        """

        self._sleep = sleep

    @property
    def tcp_socket(self):
        """Gets the tcp_socket of this V1LifecycleHandler.  # noqa: E501


        :return: The tcp_socket of this V1LifecycleHandler.  # noqa: E501
        :rtype: V1TCPSocketAction
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        """Sets the tcp_socket of this V1LifecycleHandler.


        :param tcp_socket: The tcp_socket of this V1LifecycleHandler.  # noqa: E501
        :type tcp_socket: V1TCPSocketAction
        """

        self._tcp_socket = tcp_socket

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
        if not isinstance(other, V1LifecycleHandler):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1LifecycleHandler):
            return True

        return self.to_dict() != other.to_dict()
