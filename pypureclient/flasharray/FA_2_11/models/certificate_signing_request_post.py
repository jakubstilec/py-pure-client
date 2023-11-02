# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_11 import models

class CertificateSigningRequestPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'certificate': 'ReferenceNoId',
        'common_name': 'str',
        'country': 'str',
        'email': 'str',
        'locality': 'str',
        'organization': 'str',
        'organizational_unit': 'str',
        'state': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'common_name': 'common_name',
        'country': 'country',
        'email': 'email',
        'locality': 'locality',
        'organization': 'organization',
        'organizational_unit': 'organizational_unit',
        'state': 'state'
    }

    required_args = {
    }

    def __init__(
        self,
        certificate=None,  # type: models.ReferenceNoId
        common_name=None,  # type: str
        country=None,  # type: str
        email=None,  # type: str
        locality=None,  # type: str
        organization=None,  # type: str
        organizational_unit=None,  # type: str
        state=None,  # type: str
    ):
        """
        Keyword args:
            certificate (ReferenceNoId)
            common_name (str): The common name field listed in the certificate.
            country (str): Two-letter country (ISO) code listed in the certificate.
            email (str): The email field listed in the certificate.
            locality (str): The locality field listed in the certificate.
            organization (str): The organization field listed in the certificate.
            organizational_unit (str): The organizational unit field listed in the certificate.
            state (str): The state/province field listed in the certificate.
        """
        if certificate is not None:
            self.certificate = certificate
        if common_name is not None:
            self.common_name = common_name
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if locality is not None:
            self.locality = locality
        if organization is not None:
            self.organization = organization
        if organizational_unit is not None:
            self.organizational_unit = organizational_unit
        if state is not None:
            self.state = state

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CertificateSigningRequestPost`".format(key))
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
            raise KeyError("Invalid key `{}` for `CertificateSigningRequestPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CertificateSigningRequestPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CertificateSigningRequestPost`".format(key))
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
        if issubclass(CertificateSigningRequestPost, dict):
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
        if not isinstance(other, CertificateSigningRequestPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
