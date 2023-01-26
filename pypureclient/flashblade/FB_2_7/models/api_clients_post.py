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

class ApiClientsPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token_ttl_in_ms': 'int',
        'issuer': 'str',
        'max_role': 'Reference',
        'public_key': 'str'
    }

    attribute_map = {
        'access_token_ttl_in_ms': 'access_token_ttl_in_ms',
        'issuer': 'issuer',
        'max_role': 'max_role',
        'public_key': 'public_key'
    }

    required_args = {
        'max_role',
        'public_key',
    }

    def __init__(
        self,
        max_role,  # type: models.Reference
        public_key,  # type: str
        access_token_ttl_in_ms=None,  # type: int
        issuer=None,  # type: str
    ):
        """
        Keyword args:
            access_token_ttl_in_ms (int): The TTL (Time To Live) duration for which the exchanged access token is valid. Measured in milliseconds. If not specified, defaults to `86400000`.
            issuer (str): The name of the identity provider that will be issuing ID Tokens for this API client. The `iss` claim in the JWT issued must match this string. If not specified, defaults to the API client name.
            max_role (Reference, required): The maximum role allowed for ID Tokens issued by this API client. The bearer of an access token will be authorized to perform actions within the intersection of this `max_role` and the role of the array user specified as the JWT `sub` (subject) claim. The `max_role` field is a reference to a `role`. Valid `role`s are `readonly`, `ops_admin`, `array_admin`, and `storage_admin`. Users with the `readonly` (Read Only) role can perform operations that convey the state of the array. Read Only users cannot alter the state of the array. Users with the `ops_admin` (Ops Admin) role can perform the same operations as Read Only users plus enable and disable remote assistance sessions. Ops Admin users cannot alter the state of the array. Users with the `storage_admin` (Storage Admin) role can perform the same operations as Read Only users plus storage related operations, such as administering volumes, hosts, and host groups. Storage Admin users cannot perform operations that deal with global and system configurations. Users with the `array_admin` (Array Admin) role can perform the same operations as Storage Admin users plus array-wide changes dealing with global and system configurations. In other words, Array Admin users can perform all operations.
            public_key (str, required): The API client's PEM formatted (Base64 encoded) RSA public key. It must include the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` lines.
        """
        if access_token_ttl_in_ms is not None:
            self.access_token_ttl_in_ms = access_token_ttl_in_ms
        if issuer is not None:
            self.issuer = issuer
        self.max_role = max_role
        self.public_key = public_key

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ApiClientsPost`".format(key))
        if key == "max_role" and value is None:
            raise ValueError("Invalid value for `max_role`, must not be `None`")
        if key == "public_key" and value is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")
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
        if issubclass(ApiClientsPost, dict):
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
        if not isinstance(other, ApiClientsPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
