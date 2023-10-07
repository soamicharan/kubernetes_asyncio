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


class V1alpha1ValidatingAdmissionPolicySpec(object):
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
        'audit_annotations': 'list[V1alpha1AuditAnnotation]',
        'failure_policy': 'str',
        'match_conditions': 'list[V1alpha1MatchCondition]',
        'match_constraints': 'V1alpha1MatchResources',
        'param_kind': 'V1alpha1ParamKind',
        'validations': 'list[V1alpha1Validation]',
        'variables': 'list[V1alpha1Variable]'
    }

    attribute_map = {
        'audit_annotations': 'auditAnnotations',
        'failure_policy': 'failurePolicy',
        'match_conditions': 'matchConditions',
        'match_constraints': 'matchConstraints',
        'param_kind': 'paramKind',
        'validations': 'validations',
        'variables': 'variables'
    }

    def __init__(self, audit_annotations=None, failure_policy=None, match_conditions=None, match_constraints=None, param_kind=None, validations=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ValidatingAdmissionPolicySpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._audit_annotations = None
        self._failure_policy = None
        self._match_conditions = None
        self._match_constraints = None
        self._param_kind = None
        self._validations = None
        self._variables = None
        self.discriminator = None

        if audit_annotations is not None:
            self.audit_annotations = audit_annotations
        if failure_policy is not None:
            self.failure_policy = failure_policy
        if match_conditions is not None:
            self.match_conditions = match_conditions
        if match_constraints is not None:
            self.match_constraints = match_constraints
        if param_kind is not None:
            self.param_kind = param_kind
        if validations is not None:
            self.validations = validations
        if variables is not None:
            self.variables = variables

    @property
    def audit_annotations(self):
        """Gets the audit_annotations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501

        auditAnnotations contains CEL expressions which are used to produce audit annotations for the audit event of the API request. validations and auditAnnotations may not both be empty; a least one of validations or auditAnnotations is required.  # noqa: E501

        :return: The audit_annotations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: list[V1alpha1AuditAnnotation]
        """
        return self._audit_annotations

    @audit_annotations.setter
    def audit_annotations(self, audit_annotations):
        """Sets the audit_annotations of this V1alpha1ValidatingAdmissionPolicySpec.

        auditAnnotations contains CEL expressions which are used to produce audit annotations for the audit event of the API request. validations and auditAnnotations may not both be empty; a least one of validations or auditAnnotations is required.  # noqa: E501

        :param audit_annotations: The audit_annotations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type audit_annotations: list[V1alpha1AuditAnnotation]
        """

        self._audit_annotations = audit_annotations

    @property
    def failure_policy(self):
        """Gets the failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501

        failurePolicy defines how to handle failures for the admission policy. Failures can occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-configured policy definitions or bindings.  A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource.  failurePolicy does not define how validations that evaluate to false are handled.  When failurePolicy is set to Fail, ValidatingAdmissionPolicyBinding validationActions define how failures are enforced.  Allowed values are Ignore or Fail. Defaults to Fail.  # noqa: E501

        :return: The failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """Sets the failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.

        failurePolicy defines how to handle failures for the admission policy. Failures can occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-configured policy definitions or bindings.  A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource.  failurePolicy does not define how validations that evaluate to false are handled.  When failurePolicy is set to Fail, ValidatingAdmissionPolicyBinding validationActions define how failures are enforced.  Allowed values are Ignore or Fail. Defaults to Fail.  # noqa: E501

        :param failure_policy: The failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type failure_policy: str
        """

        self._failure_policy = failure_policy

    @property
    def match_conditions(self):
        """Gets the match_conditions of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501

        MatchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  If a parameter object is provided, it can be accessed via the `params` handle in the same manner as validation expressions.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the policy is skipped.   2. If ALL matchConditions evaluate to TRUE, the policy is evaluated.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore, the policy is skipped  # noqa: E501

        :return: The match_conditions of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: list[V1alpha1MatchCondition]
        """
        return self._match_conditions

    @match_conditions.setter
    def match_conditions(self, match_conditions):
        """Sets the match_conditions of this V1alpha1ValidatingAdmissionPolicySpec.

        MatchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  If a parameter object is provided, it can be accessed via the `params` handle in the same manner as validation expressions.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the policy is skipped.   2. If ALL matchConditions evaluate to TRUE, the policy is evaluated.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore, the policy is skipped  # noqa: E501

        :param match_conditions: The match_conditions of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type match_conditions: list[V1alpha1MatchCondition]
        """

        self._match_conditions = match_conditions

    @property
    def match_constraints(self):
        """Gets the match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501


        :return: The match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: V1alpha1MatchResources
        """
        return self._match_constraints

    @match_constraints.setter
    def match_constraints(self, match_constraints):
        """Sets the match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.


        :param match_constraints: The match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type match_constraints: V1alpha1MatchResources
        """

        self._match_constraints = match_constraints

    @property
    def param_kind(self):
        """Gets the param_kind of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501


        :return: The param_kind of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: V1alpha1ParamKind
        """
        return self._param_kind

    @param_kind.setter
    def param_kind(self, param_kind):
        """Sets the param_kind of this V1alpha1ValidatingAdmissionPolicySpec.


        :param param_kind: The param_kind of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type param_kind: V1alpha1ParamKind
        """

        self._param_kind = param_kind

    @property
    def validations(self):
        """Gets the validations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501

        Validations contain CEL expressions which is used to apply the validation. Validations and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is required.  # noqa: E501

        :return: The validations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: list[V1alpha1Validation]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this V1alpha1ValidatingAdmissionPolicySpec.

        Validations contain CEL expressions which is used to apply the validation. Validations and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is required.  # noqa: E501

        :param validations: The validations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type validations: list[V1alpha1Validation]
        """

        self._validations = validations

    @property
    def variables(self):
        """Gets the variables of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501

        Variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under `variables` in other expressions of the policy except MatchConditions because MatchConditions are evaluated before the rest of the policy.  The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, Variables must be sorted by the order of first appearance and acyclic.  # noqa: E501

        :return: The variables of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: list[V1alpha1Variable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this V1alpha1ValidatingAdmissionPolicySpec.

        Variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under `variables` in other expressions of the policy except MatchConditions because MatchConditions are evaluated before the rest of the policy.  The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, Variables must be sorted by the order of first appearance and acyclic.  # noqa: E501

        :param variables: The variables of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type variables: list[V1alpha1Variable]
        """

        self._variables = variables

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
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicySpec):
            return True

        return self.to_dict() != other.to_dict()
