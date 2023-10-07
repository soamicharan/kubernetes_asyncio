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


class V1HorizontalPodAutoscalerStatus(object):
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
        'current_cpu_utilization_percentage': 'int',
        'current_replicas': 'int',
        'desired_replicas': 'int',
        'last_scale_time': 'datetime',
        'observed_generation': 'int'
    }

    attribute_map = {
        'current_cpu_utilization_percentage': 'currentCPUUtilizationPercentage',
        'current_replicas': 'currentReplicas',
        'desired_replicas': 'desiredReplicas',
        'last_scale_time': 'lastScaleTime',
        'observed_generation': 'observedGeneration'
    }

    def __init__(self, current_cpu_utilization_percentage=None, current_replicas=None, desired_replicas=None, last_scale_time=None, observed_generation=None, local_vars_configuration=None):  # noqa: E501
        """V1HorizontalPodAutoscalerStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._current_cpu_utilization_percentage = None
        self._current_replicas = None
        self._desired_replicas = None
        self._last_scale_time = None
        self._observed_generation = None
        self.discriminator = None

        if current_cpu_utilization_percentage is not None:
            self.current_cpu_utilization_percentage = current_cpu_utilization_percentage
        self.current_replicas = current_replicas
        self.desired_replicas = desired_replicas
        if last_scale_time is not None:
            self.last_scale_time = last_scale_time
        if observed_generation is not None:
            self.observed_generation = observed_generation

    @property
    def current_cpu_utilization_percentage(self):
        """Gets the current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.  # noqa: E501

        :return: The current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_cpu_utilization_percentage

    @current_cpu_utilization_percentage.setter
    def current_cpu_utilization_percentage(self, current_cpu_utilization_percentage):
        """Sets the current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.

        currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.  # noqa: E501

        :param current_cpu_utilization_percentage: The current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type current_cpu_utilization_percentage: int
        """

        self._current_cpu_utilization_percentage = current_cpu_utilization_percentage

    @property
    def current_replicas(self):
        """Gets the current_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        currentReplicas is the current number of replicas of pods managed by this autoscaler.  # noqa: E501

        :return: The current_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """Sets the current_replicas of this V1HorizontalPodAutoscalerStatus.

        currentReplicas is the current number of replicas of pods managed by this autoscaler.  # noqa: E501

        :param current_replicas: The current_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type current_replicas: int
        """
        if self.local_vars_configuration.client_side_validation and current_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `current_replicas`, must not be `None`")  # noqa: E501

        self._current_replicas = current_replicas

    @property
    def desired_replicas(self):
        """Gets the desired_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        desiredReplicas is the  desired number of replicas of pods managed by this autoscaler.  # noqa: E501

        :return: The desired_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._desired_replicas

    @desired_replicas.setter
    def desired_replicas(self, desired_replicas):
        """Sets the desired_replicas of this V1HorizontalPodAutoscalerStatus.

        desiredReplicas is the  desired number of replicas of pods managed by this autoscaler.  # noqa: E501

        :param desired_replicas: The desired_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type desired_replicas: int
        """
        if self.local_vars_configuration.client_side_validation and desired_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `desired_replicas`, must not be `None`")  # noqa: E501

        self._desired_replicas = desired_replicas

    @property
    def last_scale_time(self):
        """Gets the last_scale_time of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.  # noqa: E501

        :return: The last_scale_time of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scale_time

    @last_scale_time.setter
    def last_scale_time(self, last_scale_time):
        """Sets the last_scale_time of this V1HorizontalPodAutoscalerStatus.

        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.  # noqa: E501

        :param last_scale_time: The last_scale_time of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type last_scale_time: datetime
        """

        self._last_scale_time = last_scale_time

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        observedGeneration is the most recent generation observed by this autoscaler.  # noqa: E501

        :return: The observed_generation of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1HorizontalPodAutoscalerStatus.

        observedGeneration is the most recent generation observed by this autoscaler.  # noqa: E501

        :param observed_generation: The observed_generation of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type observed_generation: int
        """

        self._observed_generation = observed_generation

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
        if not isinstance(other, V1HorizontalPodAutoscalerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1HorizontalPodAutoscalerStatus):
            return True

        return self.to_dict() != other.to_dict()
