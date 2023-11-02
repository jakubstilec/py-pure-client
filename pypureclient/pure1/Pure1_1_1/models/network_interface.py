# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_1 import models

class NetworkInterface(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'id': 'str',
        'name': 'str',
        'arrays': 'list[FixedReferenceFqdn]',
        'address': 'str',
        'enabled': 'bool',
        'gateway': 'str',
        'hwaddr': 'str',
        'mtu': 'int',
        'netmask': 'str',
        'services': 'list[str]',
        'speed': 'int',
        'subinterfaces': 'list[str]'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'address': 'address',
        'enabled': 'enabled',
        'gateway': 'gateway',
        'hwaddr': 'hwaddr',
        'mtu': 'mtu',
        'netmask': 'netmask',
        'services': 'services',
        'speed': 'speed',
        'subinterfaces': 'subinterfaces'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        arrays=None,  # type: List[models.FixedReferenceFqdn]
        address=None,  # type: str
        enabled=None,  # type: bool
        gateway=None,  # type: str
        hwaddr=None,  # type: str
        mtu=None,  # type: int
        netmask=None,  # type: str
        services=None,  # type: List[str]
        speed=None,  # type: int
        subinterfaces=None,  # type: List[str]
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A non-modifiable, locally unique name chosen by the system.
            arrays (list[FixedReferenceFqdn]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.
            address (str): IP address of this network interface.
            enabled (bool)
            gateway (str)
            hwaddr (str): Hardware address.
            mtu (int): Maximum transmission unit.
            netmask (str)
            services (list[str]): Services and protocols that are enabled on the interface.
            speed (int): Speed in bytes per second.
            subinterfaces (list[str])
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if arrays is not None:
            self.arrays = arrays
        if address is not None:
            self.address = address
        if enabled is not None:
            self.enabled = enabled
        if gateway is not None:
            self.gateway = gateway
        if hwaddr is not None:
            self.hwaddr = hwaddr
        if mtu is not None:
            self.mtu = mtu
        if netmask is not None:
            self.netmask = netmask
        if services is not None:
            self.services = services
        if speed is not None:
            self.speed = speed
        if subinterfaces is not None:
            self.subinterfaces = subinterfaces

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            if item in self.attribute_map:
                return None
            else:
                raise AttributeError(f"{self} object has no attribute '{name}'")
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
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
        if issubclass(NetworkInterface, dict):
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
        if not isinstance(other, NetworkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
