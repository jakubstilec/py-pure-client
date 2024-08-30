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

class Arrays(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'as_of': 'int',
        'banner': 'str',
        'capacity': 'int',
        'console_lock_enabled': 'bool',
        'encryption': 'ArrayEncryption',
        'eradication_config': 'EradicationConfig',
        'idle_timeout': 'int',
        'ntp_servers': 'list[str]',
        'ntp_symmetric_key': 'str',
        'os': 'str',
        'parity': 'float',
        'scsi_timeout': 'int',
        'space': 'Space',
        'time_zone': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'as_of': '_as_of',
        'banner': 'banner',
        'capacity': 'capacity',
        'console_lock_enabled': 'console_lock_enabled',
        'encryption': 'encryption',
        'eradication_config': 'eradication_config',
        'idle_timeout': 'idle_timeout',
        'ntp_servers': 'ntp_servers',
        'ntp_symmetric_key': 'ntp_symmetric_key',
        'os': 'os',
        'parity': 'parity',
        'scsi_timeout': 'scsi_timeout',
        'space': 'space',
        'time_zone': 'time_zone',
        'version': 'version'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        as_of=None,  # type: int
        banner=None,  # type: str
        capacity=None,  # type: int
        console_lock_enabled=None,  # type: bool
        encryption=None,  # type: models.ArrayEncryption
        eradication_config=None,  # type: models.EradicationConfig
        idle_timeout=None,  # type: int
        ntp_servers=None,  # type: List[str]
        ntp_symmetric_key=None,  # type: str
        os=None,  # type: str
        parity=None,  # type: float
        scsi_timeout=None,  # type: int
        space=None,  # type: models.Space
        time_zone=None,  # type: str
        version=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            as_of (int): The time in milliseconds since UNIX epoch.
            banner (str)
            capacity (int): The usable capacity in bytes. If the user does not have sufficient access, this field will return `null`.
            console_lock_enabled (bool): If `true`, console lock is enabled for the array. If the user does not have sufficient access, this field will return `null`.
            encryption (ArrayEncryption)
            eradication_config (EradicationConfig)
            idle_timeout (int): The idle timeout in milliseconds. Valid values include `0` and any multiple of `60000` in the range of `300000` and `10800000`. Any other values are rounded down to the nearest multiple of `60000`.
            ntp_servers (list[str]): NTP Servers. If the user does not have sufficient access, this field will return `null`.
            ntp_symmetric_key (str): The text of ntp symmetric authentication key. Supported formats include a hex-encoded string no longer than 64 characters, or an ASCII string no longer than 20 characters, excluding \"#\". Any configured key will be masked as \"****\" on return. If the user does not have sufficient access, this field will return `null`.
            os (str): Specifies the operating system. Valid values are `Purity`, `Purity//FA`, and `Purity//FB`.
            parity (float): A representation of data redundancy on the array. Data redundancy is rebuilt automatically by the system whenever parity is less than `1.0`. If the user does not have sufficient access, this field will return `null`.
            scsi_timeout (int): The SCSI timeout. If not specified, defaults to `60s`. If the user does not have sufficient access, this field will return `null`.
            space (Space)
            time_zone (str): The time zone of the array.
            version (str)
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if as_of is not None:
            self.as_of = as_of
        if banner is not None:
            self.banner = banner
        if capacity is not None:
            self.capacity = capacity
        if console_lock_enabled is not None:
            self.console_lock_enabled = console_lock_enabled
        if encryption is not None:
            self.encryption = encryption
        if eradication_config is not None:
            self.eradication_config = eradication_config
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if ntp_symmetric_key is not None:
            self.ntp_symmetric_key = ntp_symmetric_key
        if os is not None:
            self.os = os
        if parity is not None:
            self.parity = parity
        if scsi_timeout is not None:
            self.scsi_timeout = scsi_timeout
        if space is not None:
            self.space = space
        if time_zone is not None:
            self.time_zone = time_zone
        if version is not None:
            self.version = version

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Arrays`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Arrays`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Arrays`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Arrays`".format(key))
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
        if issubclass(Arrays, dict):
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
        if not isinstance(other, Arrays):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
