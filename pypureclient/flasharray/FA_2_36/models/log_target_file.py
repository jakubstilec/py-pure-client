# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.36
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_36 import models

class LogTargetFile(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'target_type': 'str',
        'directory': 'ReferenceWithType',
        'keep_for': 'int',
        'keep_size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'target_type': 'target_type',
        'directory': 'directory',
        'keep_for': 'keep_for',
        'keep_size': 'keep_size'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        target_type=None,  # type: str
        directory=None,  # type: models.ReferenceWithType
        keep_for=None,  # type: int
        keep_size=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A user-specified name. The name must be locally unique and cannot be changed.
            target_type (str): The type of log target. Valid values include `file`, and `syslog`.
            directory (ReferenceWithType): Directory name to be used as log target.
            keep_for (int): Specifies the period that audit logs are retained before they are deleted, in milliseconds. If not specified, defaults to `null` which means size based retention does not apply. Use 0 to reset the value to `null`. At least one of the `keep_for` or `keep_size` parameters are required, and they can be set together.
            keep_size (int): Specifies the maximum size of audit logs to be retained. Measured in bytes. When exceeded, older logs will be deleted. If not specified, defaults to `null` which means size based retention does not apply. Use 0 to reset the value to `null`.
        """
        if name is not None:
            self.name = name
        if target_type is not None:
            self.target_type = target_type
        if directory is not None:
            self.directory = directory
        if keep_for is not None:
            self.keep_for = keep_for
        if keep_size is not None:
            self.keep_size = keep_size

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LogTargetFile`".format(key))
        if key == "keep_for" and value is not None:
            if value < 86400000:
                raise ValueError("Invalid value for `keep_for`, must be a value greater than or equal to `86400000`")
        if key == "keep_size" and value is not None:
            if value < 1000000:
                raise ValueError("Invalid value for `keep_size`, must be a value greater than or equal to `1000000`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LogTargetFile`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LogTargetFile`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LogTargetFile`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

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
        if issubclass(LogTargetFile, dict):
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
        if not isinstance(other, LogTargetFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
