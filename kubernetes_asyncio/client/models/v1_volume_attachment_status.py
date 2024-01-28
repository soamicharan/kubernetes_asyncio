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


class V1VolumeAttachmentStatus(object):
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
        'attach_error': 'V1VolumeError',
        'attached': 'bool',
        'attachment_metadata': 'dict(str, str)',
        'detach_error': 'V1VolumeError'
    }

    attribute_map = {
        'attach_error': 'attachError',
        'attached': 'attached',
        'attachment_metadata': 'attachmentMetadata',
        'detach_error': 'detachError'
    }

    def __init__(self, attach_error=None, attached=None, attachment_metadata=None, detach_error=None, local_vars_configuration=None):  # noqa: E501
        """V1VolumeAttachmentStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._attach_error = None
        self._attached = None
        self._attachment_metadata = None
        self._detach_error = None
        self.discriminator = None

        if attach_error is not None:
            self.attach_error = attach_error
        self.attached = attached
        if attachment_metadata is not None:
            self.attachment_metadata = attachment_metadata
        if detach_error is not None:
            self.detach_error = detach_error

    @property
    def attach_error(self):
        """Gets the attach_error of this V1VolumeAttachmentStatus.  # noqa: E501


        :return: The attach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: V1VolumeError
        """
        return self._attach_error

    @attach_error.setter
    def attach_error(self, attach_error):
        """Sets the attach_error of this V1VolumeAttachmentStatus.


        :param attach_error: The attach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :type attach_error: V1VolumeError
        """

        self._attach_error = attach_error

    @property
    def attached(self):
        """Gets the attached of this V1VolumeAttachmentStatus.  # noqa: E501

        attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :return: The attached of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: bool
        """
        return self._attached

    @attached.setter
    def attached(self, attached):
        """Sets the attached of this V1VolumeAttachmentStatus.

        attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :param attached: The attached of this V1VolumeAttachmentStatus.  # noqa: E501
        :type attached: bool
        """
        if self.local_vars_configuration.client_side_validation and attached is None:  # noqa: E501
            raise ValueError("Invalid value for `attached`, must not be `None`")  # noqa: E501

        self._attached = attached

    @property
    def attachment_metadata(self):
        """Gets the attachment_metadata of this V1VolumeAttachmentStatus.  # noqa: E501

        attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :return: The attachment_metadata of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attachment_metadata

    @attachment_metadata.setter
    def attachment_metadata(self, attachment_metadata):
        """Sets the attachment_metadata of this V1VolumeAttachmentStatus.

        attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :param attachment_metadata: The attachment_metadata of this V1VolumeAttachmentStatus.  # noqa: E501
        :type attachment_metadata: dict(str, str)
        """

        self._attachment_metadata = attachment_metadata

    @property
    def detach_error(self):
        """Gets the detach_error of this V1VolumeAttachmentStatus.  # noqa: E501


        :return: The detach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :rtype: V1VolumeError
        """
        return self._detach_error

    @detach_error.setter
    def detach_error(self, detach_error):
        """Sets the detach_error of this V1VolumeAttachmentStatus.


        :param detach_error: The detach_error of this V1VolumeAttachmentStatus.  # noqa: E501
        :type detach_error: V1VolumeError
        """

        self._detach_error = detach_error

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
        if not isinstance(other, V1VolumeAttachmentStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VolumeAttachmentStatus):
            return True

        return self.to_dict() != other.to_dict()
