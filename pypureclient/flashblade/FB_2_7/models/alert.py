# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.7, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_7 import models

class Alert(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'action': 'str',
        'code': 'int',
        'component_name': 'str',
        'component_type': 'str',
        'created': 'int',
        'description': 'str',
        'flagged': 'bool',
        'index': 'int',
        'knowledge_base_url': 'str',
        'notified': 'int',
        'severity': 'str',
        'state': 'str',
        'summary': 'str',
        'updated': 'int',
        'variables': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'action': 'action',
        'code': 'code',
        'component_name': 'component_name',
        'component_type': 'component_type',
        'created': 'created',
        'description': 'description',
        'flagged': 'flagged',
        'index': 'index',
        'knowledge_base_url': 'knowledge_base_url',
        'notified': 'notified',
        'severity': 'severity',
        'state': 'state',
        'summary': 'summary',
        'updated': 'updated',
        'variables': 'variables'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        action=None,  # type: str
        code=None,  # type: int
        component_name=None,  # type: str
        component_type=None,  # type: str
        created=None,  # type: int
        description=None,  # type: str
        flagged=None,  # type: bool
        index=None,  # type: int
        knowledge_base_url=None,  # type: str
        notified=None,  # type: int
        severity=None,  # type: str
        state=None,  # type: str
        summary=None,  # type: str
        updated=None,  # type: int
        variables=None,  # type: dict(str, str)
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            action (str): The action of the alert.
            code (int): Alert code.
            component_name (str): The component name of the alert.
            component_type (str): The component type of the alert.
            created (int): The creation timestamp of the alert.
            description (str): The description of the alert.
            flagged (bool): Flagged state of the alert.
            index (int): The unique index of the alert.
            knowledge_base_url (str): URL of the relevant Knowledge Base page.
            notified (int): The last notification timestamp of the alert.
            severity (str): Severity of the alert. Valid values are `info`, `warning`, and `critical`.
            state (str): The current state of the alert. Valid values are `open`, `closing`, `closed`, and `waiting to downgrade`.
            summary (str): The summary of the alert.
            updated (int): The last updated timestamp of the alert.
            variables (dict(str, str)): Key-value pairs of additional information of the alert.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if action is not None:
            self.action = action
        if code is not None:
            self.code = code
        if component_name is not None:
            self.component_name = component_name
        if component_type is not None:
            self.component_type = component_type
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if flagged is not None:
            self.flagged = flagged
        if index is not None:
            self.index = index
        if knowledge_base_url is not None:
            self.knowledge_base_url = knowledge_base_url
        if notified is not None:
            self.notified = notified
        if severity is not None:
            self.severity = severity
        if state is not None:
            self.state = state
        if summary is not None:
            self.summary = summary
        if updated is not None:
            self.updated = updated
        if variables is not None:
            self.variables = variables

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(Alert, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
