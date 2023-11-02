# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_24 import models

class EulaGetResponse(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'more_items_remaining': 'bool',
        'total_item_count': 'int',
        'continuation_token': 'str',
        'items': 'list[Eula]'
    }

    attribute_map = {
        'more_items_remaining': 'more_items_remaining',
        'total_item_count': 'total_item_count',
        'continuation_token': 'continuation_token',
        'items': 'items'
    }

    required_args = {
    }

    def __init__(
        self,
        more_items_remaining=None,  # type: bool
        total_item_count=None,  # type: int
        continuation_token=None,  # type: str
        items=None,  # type: List[models.Eula]
    ):
        """
        Keyword args:
            more_items_remaining (bool): Returns a value of `true` if subsequent items can be retrieved.
            total_item_count (int): The total number of records after applying all filter query parameters. The `total_item_count` will be calculated if and only if the corresponding query parameter `total_item_count` is set to `true`. If this query parameter is not set or set to `false`, a value of `null` will be returned.
            continuation_token (str): Continuation token that can be provided in the `continuation_token` query param to get the next page of data. If you use the continuation token to page through data you are guaranteed to get all items exactly once regardless of how items are modified. If an item is added or deleted during the pagination then it may or may not be returned. The continuation token is generated if the limit is less than the remaining number of items, and the default sort is used (no sort is specified).
            items (list[Eula])
        """
        if more_items_remaining is not None:
            self.more_items_remaining = more_items_remaining
        if total_item_count is not None:
            self.total_item_count = total_item_count
        if continuation_token is not None:
            self.continuation_token = continuation_token
        if items is not None:
            self.items = items

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `EulaGetResponse`".format(key))
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
            raise KeyError("Invalid key `{}` for `EulaGetResponse`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `EulaGetResponse`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `EulaGetResponse`".format(key))
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
        if issubclass(EulaGetResponse, dict):
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
        if not isinstance(other, EulaGetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
