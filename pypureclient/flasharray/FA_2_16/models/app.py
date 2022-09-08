# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_16 import models

class App(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'enabled': 'bool',
        'status': 'str',
        'version': 'str',
        'details': 'str',
        'vnc_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled',
        'status': 'status',
        'version': 'version',
        'details': 'details',
        'vnc_enabled': 'vnc_enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        description=None,  # type: str
        enabled=None,  # type: bool
        status=None,  # type: str
        version=None,  # type: str
        details=None,  # type: str
        vnc_enabled=None,  # type: bool
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified.
            description (str): A description of the app.
            enabled (bool): If set to `true`, the app is enabled. By default, apps are disabled.
            status (str): The status of the app. Values include `healthy` and `unhealthy`. For cluster apps, this represents the aggregate status of the app. The aggregate status is only `healthy` if all nodes are `healthy`&#59; otherwise, it is `unhealthy`.
            version (str): The app version. For cluster apps, this represents the node version if all nodes are of the same version. If the node versions differ, a value of `null` is returned.
            details (str): Details of the status of the app.
            vnc_enabled (bool): If set to `true`, VNC access is enabled. By default, VNC access is disabled.
        """
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if details is not None:
            self.details = details
        if vnc_enabled is not None:
            self.vnc_enabled = vnc_enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `App`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
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
        if issubclass(App, dict):
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
        if not isinstance(other, App):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
