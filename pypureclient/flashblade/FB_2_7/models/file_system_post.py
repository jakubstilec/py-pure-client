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

class FileSystemPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_group_quota': 'int',
        'default_user_quota': 'int',
        'fast_remove_directory_enabled': 'bool',
        'hard_limit_enabled': 'bool',
        'http': 'Http',
        'multi_protocol': 'MultiProtocolPost',
        'nfs': 'Nfs',
        'provisioned': 'int',
        'requested_promotion_state': 'str',
        'smb': 'Smb',
        'snapshot_directory_enabled': 'bool',
        'source': 'Reference',
        'writable': 'bool'
    }

    attribute_map = {
        'default_group_quota': 'default_group_quota',
        'default_user_quota': 'default_user_quota',
        'fast_remove_directory_enabled': 'fast_remove_directory_enabled',
        'hard_limit_enabled': 'hard_limit_enabled',
        'http': 'http',
        'multi_protocol': 'multi_protocol',
        'nfs': 'nfs',
        'provisioned': 'provisioned',
        'requested_promotion_state': 'requested_promotion_state',
        'smb': 'smb',
        'snapshot_directory_enabled': 'snapshot_directory_enabled',
        'source': 'source',
        'writable': 'writable'
    }

    required_args = {
    }

    def __init__(
        self,
        default_group_quota=None,  # type: int
        default_user_quota=None,  # type: int
        fast_remove_directory_enabled=None,  # type: bool
        hard_limit_enabled=None,  # type: bool
        http=None,  # type: models.Http
        multi_protocol=None,  # type: models.MultiProtocolPost
        nfs=None,  # type: models.Nfs
        provisioned=None,  # type: int
        requested_promotion_state=None,  # type: str
        smb=None,  # type: models.Smb
        snapshot_directory_enabled=None,  # type: bool
        source=None,  # type: models.Reference
        writable=None,  # type: bool
    ):
        """
        Keyword args:
            default_group_quota (int): The default space quota for a group writing to this file system.
            default_user_quota (int): The default space quota for a user writing to this file system.
            fast_remove_directory_enabled (bool): If set to `true`, the file system, when mounted, will contain a directory that can be used for fast removal of other directories. Directories can be moved into the fast remove directory in order to have them deleted, and their space freed, more quickly than a normal removal operation. If not specified, defaults to `false`.
            hard_limit_enabled (bool): If set to `true`, the file system's size, as defined by `provisioned`, is used as a hard limit quota. If not specified, defaults to `false`.
            http (Http): HTTP configuration.
            multi_protocol (MultiProtocolPost): Multi-protocol configuration.
            nfs (Nfs)
            provisioned (int): The provisioned size of the file system, displayed in bytes. If set to an empty string (`\"\"`), the file system is unlimited in size. If not specified, defaults to unlimited.
            requested_promotion_state (str): Possible values are `promoted` and `demoted`. The `demoted` state is used for replication targets and is only allowed to be set if the file system is in a replica-link relationship. The additional query param `discard-non-snapshotted-data` must be set to `true` when demoting a file system. The default for new file systems is `promoted`.
            smb (Smb): SMB configuration.
            snapshot_directory_enabled (bool): If set to `true`, a hidden .snapshot directory will be present in each directory of the file system when it is mounted. The .snapshot directory allows clients read access to the contents of the snapshots that have been taken of a directory. If set to `false`, the .snapshot directory will not be present in any directories within a mounted file system. If not specified, defaults to `true`.
            source (Reference): The source snapshot whose data is copied to the file system specified.
            writable (bool): Whether the file system is writable or not. If `false`, this overrides any protocol or file permission settings and prevents changes. If `true`, then the protocol and file permission settings are evaluated. If not specified, defaults to `true`. Modifiable.
        """
        if default_group_quota is not None:
            self.default_group_quota = default_group_quota
        if default_user_quota is not None:
            self.default_user_quota = default_user_quota
        if fast_remove_directory_enabled is not None:
            self.fast_remove_directory_enabled = fast_remove_directory_enabled
        if hard_limit_enabled is not None:
            self.hard_limit_enabled = hard_limit_enabled
        if http is not None:
            self.http = http
        if multi_protocol is not None:
            self.multi_protocol = multi_protocol
        if nfs is not None:
            self.nfs = nfs
        if provisioned is not None:
            self.provisioned = provisioned
        if requested_promotion_state is not None:
            self.requested_promotion_state = requested_promotion_state
        if smb is not None:
            self.smb = smb
        if snapshot_directory_enabled is not None:
            self.snapshot_directory_enabled = snapshot_directory_enabled
        if source is not None:
            self.source = source
        if writable is not None:
            self.writable = writable

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileSystemPost`".format(key))
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
        if issubclass(FileSystemPost, dict):
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
        if not isinstance(other, FileSystemPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
