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

class Session(object):
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
        'end_time': 'int',
        'event': 'str',
        'event_count': 'int',
        'location': 'str',
        'method': 'str',
        'start_time': 'int',
        'user': 'str',
        'user_interface': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'end_time': 'end_time',
        'event': 'event',
        'event_count': 'event_count',
        'location': 'location',
        'method': 'method',
        'start_time': 'start_time',
        'user': 'user',
        'user_interface': 'user_interface'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        end_time=None,  # type: int
        event=None,  # type: str
        event_count=None,  # type: int
        location=None,  # type: str
        method=None,  # type: str
        start_time=None,  # type: int
        user=None,  # type: str
        user_interface=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            end_time (int): Date and time the user logged out of the Purity//FB interface in milliseconds since UNIX epoch. Set to 0 if the session is still active.
            event (str): Description of session events. Valid values include `failed authentication`, `user session`, `login`, `logout`, `API token obtained`, and `request without session`.
            event_count (int): Number of session events.
            location (str): IP address of the user client connecting to the array or console if connected through local console.
            method (str): Method by which the user attempted to log in. Valid values include `API token`, `password`, and `public key`.
            start_time (int): Date and time the user logged in to the Purity//FB interface in milliseconds since UNIX epoch.
            user (str): Username of the Purity//FB user who triggered the user session event.
            user_interface (str): The user interface through which the user session event was performed. Valid values include `CLI`, `GUI`, and `REST`.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if end_time is not None:
            self.end_time = end_time
        if event is not None:
            self.event = event
        if event_count is not None:
            self.event_count = event_count
        if location is not None:
            self.location = location
        if method is not None:
            self.method = method
        if start_time is not None:
            self.start_time = start_time
        if user is not None:
            self.user = user
        if user_interface is not None:
            self.user_interface = user_interface

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Session`".format(key))
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
        if issubclass(Session, dict):
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
        if not isinstance(other, Session):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
