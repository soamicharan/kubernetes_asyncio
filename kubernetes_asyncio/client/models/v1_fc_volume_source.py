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


class V1FCVolumeSource(object):
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
        'fs_type': 'str',
        'lun': 'int',
        'read_only': 'bool',
        'target_wwns': 'list[str]',
        'wwids': 'list[str]'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'lun': 'lun',
        'read_only': 'readOnly',
        'target_wwns': 'targetWWNs',
        'wwids': 'wwids'
    }

    def __init__(self, fs_type=None, lun=None, read_only=None, target_wwns=None, wwids=None, local_vars_configuration=None):  # noqa: E501
        """V1FCVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._fs_type = None
        self._lun = None
        self._read_only = None
        self._target_wwns = None
        self._wwids = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        if lun is not None:
            self.lun = lun
        if read_only is not None:
            self.read_only = read_only
        if target_wwns is not None:
            self.target_wwns = target_wwns
        if wwids is not None:
            self.wwids = wwids

    @property
    def fs_type(self):
        """Gets the fs_type of this V1FCVolumeSource.  # noqa: E501

        fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :return: The fs_type of this V1FCVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1FCVolumeSource.

        fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :param fs_type: The fs_type of this V1FCVolumeSource.  # noqa: E501
        :type fs_type: str
        """

        self._fs_type = fs_type

    @property
    def lun(self):
        """Gets the lun of this V1FCVolumeSource.  # noqa: E501

        lun is Optional: FC target lun number  # noqa: E501

        :return: The lun of this V1FCVolumeSource.  # noqa: E501
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """Sets the lun of this V1FCVolumeSource.

        lun is Optional: FC target lun number  # noqa: E501

        :param lun: The lun of this V1FCVolumeSource.  # noqa: E501
        :type lun: int
        """

        self._lun = lun

    @property
    def read_only(self):
        """Gets the read_only of this V1FCVolumeSource.  # noqa: E501

        readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :return: The read_only of this V1FCVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1FCVolumeSource.

        readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :param read_only: The read_only of this V1FCVolumeSource.  # noqa: E501
        :type read_only: bool
        """

        self._read_only = read_only

    @property
    def target_wwns(self):
        """Gets the target_wwns of this V1FCVolumeSource.  # noqa: E501

        targetWWNs is Optional: FC target worldwide names (WWNs)  # noqa: E501

        :return: The target_wwns of this V1FCVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_wwns

    @target_wwns.setter
    def target_wwns(self, target_wwns):
        """Sets the target_wwns of this V1FCVolumeSource.

        targetWWNs is Optional: FC target worldwide names (WWNs)  # noqa: E501

        :param target_wwns: The target_wwns of this V1FCVolumeSource.  # noqa: E501
        :type target_wwns: list[str]
        """

        self._target_wwns = target_wwns

    @property
    def wwids(self):
        """Gets the wwids of this V1FCVolumeSource.  # noqa: E501

        wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.  # noqa: E501

        :return: The wwids of this V1FCVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._wwids

    @wwids.setter
    def wwids(self, wwids):
        """Sets the wwids of this V1FCVolumeSource.

        wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.  # noqa: E501

        :param wwids: The wwids of this V1FCVolumeSource.  # noqa: E501
        :type wwids: list[str]
        """

        self._wwids = wwids

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
        if not isinstance(other, V1FCVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1FCVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
