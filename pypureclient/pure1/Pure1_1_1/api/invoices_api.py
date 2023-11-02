# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class InvoicesApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api11_invoices_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        offset=None,  # type: int
        sort=None,  # type: List[str]
        partner_purchase_orders=None,  # type: List[str]
        subscription_ids=None,  # type: List[str]
        subscription_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.InvoiceGetResponse
        """Get invoices

        Retrieves information about Pure1 subscription invoices.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api11_invoices_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each `id` element, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :param list[str] partner_purchase_orders: A comma-separated list of partner purchase order numbers. If there is not at least one resource that matches each `partner_purchase_order` element, an error is returned. Single quotes are required around all strings.
        :param list[str] subscription_ids: A comma-separated list of subscription IDs. If there is not at least one resource that matches each `subscription.id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] subscription_names: A comma-separated list of subscription names. If there is not at least one resource that matches each `subscription.name` element, an error is returned. Single quotes are required around all strings.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: InvoiceGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        continuation_token = models.quoteString(continuation_token)
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        ids = models.quoteStrings(ids)
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        if partner_purchase_orders is not None:
            if not isinstance(partner_purchase_orders, list):
                partner_purchase_orders = [partner_purchase_orders]
        partner_purchase_orders = models.quoteStrings(partner_purchase_orders)
        if subscription_ids is not None:
            if not isinstance(subscription_ids, list):
                subscription_ids = [subscription_ids]
        subscription_ids = models.quoteStrings(subscription_ids)
        if subscription_names is not None:
            if not isinstance(subscription_names, list):
                subscription_names = [subscription_names]
        subscription_names = models.quoteStrings(subscription_names)
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api11_invoices_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'partner_purchase_orders' in params:
            query_params.append(('partner_purchase_orders', params['partner_purchase_orders']))
            collection_formats['partner_purchase_orders'] = 'csv'
        if 'subscription_ids' in params:
            query_params.append(('subscription_ids', params['subscription_ids']))
            collection_formats['subscription_ids'] = 'csv'
        if 'subscription_names' in params:
            query_params.append(('subscription_names', params['subscription_names']))
            collection_formats['subscription_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.1/invoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
