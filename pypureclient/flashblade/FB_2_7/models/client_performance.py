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

class ClientPerformance(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'bytes_per_op': 'int',
        'bytes_per_read': 'int',
        'bytes_per_write': 'int',
        'others_per_sec': 'int',
        'read_bytes_per_sec': 'int',
        'reads_per_sec': 'int',
        'time': 'int',
        'usec_per_other_op': 'int',
        'usec_per_read_op': 'int',
        'usec_per_write_op': 'int',
        'write_bytes_per_sec': 'int',
        'writes_per_sec': 'int'
    }

    attribute_map = {
        'name': 'name',
        'bytes_per_op': 'bytes_per_op',
        'bytes_per_read': 'bytes_per_read',
        'bytes_per_write': 'bytes_per_write',
        'others_per_sec': 'others_per_sec',
        'read_bytes_per_sec': 'read_bytes_per_sec',
        'reads_per_sec': 'reads_per_sec',
        'time': 'time',
        'usec_per_other_op': 'usec_per_other_op',
        'usec_per_read_op': 'usec_per_read_op',
        'usec_per_write_op': 'usec_per_write_op',
        'write_bytes_per_sec': 'write_bytes_per_sec',
        'writes_per_sec': 'writes_per_sec'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        bytes_per_op=None,  # type: int
        bytes_per_read=None,  # type: int
        bytes_per_write=None,  # type: int
        others_per_sec=None,  # type: int
        read_bytes_per_sec=None,  # type: int
        reads_per_sec=None,  # type: int
        time=None,  # type: int
        usec_per_other_op=None,  # type: int
        usec_per_read_op=None,  # type: int
        usec_per_write_op=None,  # type: int
        write_bytes_per_sec=None,  # type: int
        writes_per_sec=None,  # type: int
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            bytes_per_op (int): Average operation size (read bytes+write bytes/read ops+write ops).
            bytes_per_read (int): Average read size in bytes per read operation.
            bytes_per_write (int): Average write size in bytes per write operation.
            others_per_sec (int): Other operations processed per second.
            read_bytes_per_sec (int): Bytes read per second.
            reads_per_sec (int): Read requests processed per second.
            time (int): Sample time in milliseconds since UNIX epoch.
            usec_per_other_op (int): Average time, measured in microseconds, it takes the client to process other operations.
            usec_per_read_op (int): Average time, measured in microseconds, it takes the client to process a read request.
            usec_per_write_op (int): Average time, measured in microseconds, it takes the client to process a write request.
            write_bytes_per_sec (int): Bytes written per second.
            writes_per_sec (int): Write requests processed per second.
        """
        if name is not None:
            self.name = name
        if bytes_per_op is not None:
            self.bytes_per_op = bytes_per_op
        if bytes_per_read is not None:
            self.bytes_per_read = bytes_per_read
        if bytes_per_write is not None:
            self.bytes_per_write = bytes_per_write
        if others_per_sec is not None:
            self.others_per_sec = others_per_sec
        if read_bytes_per_sec is not None:
            self.read_bytes_per_sec = read_bytes_per_sec
        if reads_per_sec is not None:
            self.reads_per_sec = reads_per_sec
        if time is not None:
            self.time = time
        if usec_per_other_op is not None:
            self.usec_per_other_op = usec_per_other_op
        if usec_per_read_op is not None:
            self.usec_per_read_op = usec_per_read_op
        if usec_per_write_op is not None:
            self.usec_per_write_op = usec_per_write_op
        if write_bytes_per_sec is not None:
            self.write_bytes_per_sec = write_bytes_per_sec
        if writes_per_sec is not None:
            self.writes_per_sec = writes_per_sec

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ClientPerformance`".format(key))
        if key == "bytes_per_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_op`, must be a value greater than or equal to `0`")
        if key == "bytes_per_read" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_read`, must be a value greater than or equal to `0`")
        if key == "bytes_per_write" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_write`, must be a value greater than or equal to `0`")
        if key == "others_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `others_per_sec`, must be a value greater than or equal to `0`")
        if key == "read_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `read_bytes_per_sec`, must be a value greater than or equal to `0`")
        if key == "reads_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `reads_per_sec`, must be a value greater than or equal to `0`")
        if key == "usec_per_other_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_other_op`, must be a value greater than or equal to `0`")
        if key == "usec_per_read_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_read_op`, must be a value greater than or equal to `0`")
        if key == "usec_per_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_write_op`, must be a value greater than or equal to `0`")
        if key == "write_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `write_bytes_per_sec`, must be a value greater than or equal to `0`")
        if key == "writes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `writes_per_sec`, must be a value greater than or equal to `0`")
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
        if issubclass(ClientPerformance, dict):
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
        if not isinstance(other, ClientPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
