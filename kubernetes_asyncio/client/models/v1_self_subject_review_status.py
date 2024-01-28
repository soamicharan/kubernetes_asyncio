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


class V1SelfSubjectReviewStatus(object):
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
        'user_info': 'V1UserInfo'
    }

    attribute_map = {
        'user_info': 'userInfo'
    }

    def __init__(self, user_info=None, local_vars_configuration=None):  # noqa: E501
        """V1SelfSubjectReviewStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._user_info = None
        self.discriminator = None

        if user_info is not None:
            self.user_info = user_info

    @property
    def user_info(self):
        """Gets the user_info of this V1SelfSubjectReviewStatus.  # noqa: E501


        :return: The user_info of this V1SelfSubjectReviewStatus.  # noqa: E501
        :rtype: V1UserInfo
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this V1SelfSubjectReviewStatus.


        :param user_info: The user_info of this V1SelfSubjectReviewStatus.  # noqa: E501
        :type user_info: V1UserInfo
        """

        self._user_info = user_info

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
        if not isinstance(other, V1SelfSubjectReviewStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SelfSubjectReviewStatus):
            return True

        return self.to_dict() != other.to_dict()
