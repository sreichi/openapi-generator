# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from petstore_api.api_client import ApiClient
from petstore_api.exceptions import (
    ApiTypeError,
    ApiValueError
)
from petstore_api.model_utils import (
    check_allowed_values,
    check_validations
)


class StoreApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_order(self, order_id, **kwargs):  # noqa: E501
            """Delete purchase order by ID  # noqa: E501

            For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.delete_order(order_id, async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param str order_id: ID of the order that needs to be deleted (required)
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: None
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['order_id'] = order_id
            return self.call_with_http_info(**kwargs)

        self.delete_order = Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/store/order/{order_id}',
                'operation_id': 'delete_order',
                'http_method': 'DELETE',
                'servers': [],
            },
            params_map={
                'all': [
                    'order_id',
                ],
                'required': [
                    'order_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'order_id': 'str',
                },
                'attribute_map': {
                    'order_id': 'order_id',
                },
                'location_map': {
                    'order_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_order
        )

        def __get_inventory(self, **kwargs):  # noqa: E501
            """Returns pet inventories by status  # noqa: E501

            Returns a map of status codes to quantities  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.get_inventory(async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: dict(str, int)
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            return self.call_with_http_info(**kwargs)

        self.get_inventory = Endpoint(
            settings={
                'response_type': 'dict(str, int)',
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/store/inventory',
                'operation_id': 'get_inventory',
                'http_method': 'GET',
                'servers': [],
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_inventory
        )

        def __get_order_by_id(self, order_id, **kwargs):  # noqa: E501
            """Find purchase order by ID  # noqa: E501

            For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.get_order_by_id(order_id, async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param int order_id: ID of pet that needs to be fetched (required)
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: Order
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['order_id'] = order_id
            return self.call_with_http_info(**kwargs)

        self.get_order_by_id = Endpoint(
            settings={
                'response_type': 'Order',
                'auth': [],
                'endpoint_path': '/store/order/{order_id}',
                'operation_id': 'get_order_by_id',
                'http_method': 'GET',
                'servers': [],
            },
            params_map={
                'all': [
                    'order_id',
                ],
                'required': [
                    'order_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'order_id',
                ]
            },
            root_map={
                'validations': {
                    ('order_id',): {

                        'inclusive_maximum': 5,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'order_id': 'int',
                },
                'attribute_map': {
                    'order_id': 'order_id',
                },
                'location_map': {
                    'order_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/xml',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_order_by_id
        )

        def __place_order(self, body, **kwargs):  # noqa: E501
            """Place an order for a pet  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.place_order(body, async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param Order body: order placed for purchasing the pet (required)
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: Order
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['body'] = body
            return self.call_with_http_info(**kwargs)

        self.place_order = Endpoint(
            settings={
                'response_type': 'Order',
                'auth': [],
                'endpoint_path': '/store/order',
                'operation_id': 'place_order',
                'http_method': 'POST',
                'servers': [],
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body': 'Order',
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/xml',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__place_order
        )


class Endpoint(object):
    def __init__(self, settings=None, params_map=None, root_map=None,
                 headers_map=None, api_client=None, callable=None):
        """Creates an endpoint

        Args:
            settings (dict): see below key value pairs
                'response_type' (str): response type
                'auth' (list): a list of auth type keys
                'endpoint_path' (str): the endpoint path
                'operation_id' (str): endpoint string identifier
                'http_method' (str): POST/PUT/PATCH/GET etc
                'servers' (list): list of str servers that this endpoint is at
            params_map (dict): see below key value pairs
                'all' (list): list of str endpoint parameter names
                'required' (list): list of required parameter names
                'nullable' (list): list of nullable parameter names
                'enum' (list): list of parameters with enum values
                'validation' (list): list of parameters with validations
            root_map
                'validations' (dict): the dict mapping endpoint parameter tuple
                    paths to their validation dictionaries
                'allowed_values' (dict): the dict mapping endpoint parameter
                    tuple paths to their allowed_values (enum) dictionaries
                'openapi_types' (dict): param_name to openapi type
                'attribute_map' (dict): param_name to camelCase name
                'location_map' (dict): param_name to  'body', 'file', 'form',
                    'header', 'path', 'query'
                collection_format_map (dict): param_name to `csv` etc.
            headers_map (dict): see below key value pairs
                'accept' (list): list of Accept header strings
                'content_type' (list): list of Content-Type header strings
            api_client (ApiClient) api client instance
            callable (function): the function which is invoked when the
                Endpoint is called
        """
        self.settings = settings
        self.params_map = params_map
        self.params_map['all'].extend([
            'async_req',
            '_host_index',
            '_preload_content',
            '_request_timeout',
            '_return_http_data_only'
        ])
        self.validations = root_map['validations']
        self.allowed_values = root_map['allowed_values']
        self.openapi_types = root_map['openapi_types']
        self.attribute_map = root_map['attribute_map']
        self.location_map = root_map['location_map']
        self.collection_format_map = root_map['collection_format_map']
        self.headers_map = headers_map
        self.api_client = api_client
        self.callable = callable

    def __validate_inputs(self, kwargs):
        for param in self.params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    self.allowed_values,
                    (param,),
                    kwargs[param],
                    self.validations
                )

        for param in self.params_map['validation']:
            if param in kwargs:
                check_validations(
                    self.validations,
                    (param,),
                    kwargs[param]
                )

    def __gather_params(self, kwargs):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {},
            'path': {},
            'query': []
        }

        for param_name, param_value in six.iteritems(kwargs):
            param_location = self.location_map.get(param_name)
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = self.attribute_map[param_name]
                if (param_location == 'form' and
                        self.openapi_types[param_name] == 'file'):
                    param_location = 'file'
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = self.collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        return params

    def __call__(self, *args, **kwargs):
        """ This method is invoked when endpoints are called
        Example:
        pet_api = PetApi()
        pet_api.add_pet  # this is an instance of the class Endpoint
        pet_api.add_pet()  # this invokes pet_api.add_pet.__call__()
        which then invokes the callable functions stored in that endpoint at
        pet_api.add_pet.callable or self.callable in this class
        """
        return self.callable(self, *args, **kwargs)

    def call_with_http_info(self, **kwargs):

        if kwargs.get('_host_index') and self.settings['servers']:
            _host_index = kwargs.get('_host_index')
            try:
                _host = self.settings['servers'][_host_index]
            except IndexError:
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s" %
                    len(self.settings['servers'])
                )
        else:
            try:
                _host = self.settings['servers'][0]
            except IndexError:
                _host = None

        for key, value in six.iteritems(kwargs):
            if key not in self.params_map['all']:
                raise ApiTypeError(
                    "Got an unexpected parameter '%s'"
                    " to method `%s`" %
                    (key, self.settings['operation_id'])
                )
            if key not in self.params_map['nullable'] and value is None:
                raise ApiValueError(
                    "Value may not be None for non-nullable parameter `%s`"
                    " when calling `%s`" %
                    (key, self.settings['operation_id'])
                )

        for key in self.params_map['required']:
            if key not in kwargs.keys():
                raise ApiValueError(
                    "Missing the required parameter `%s` when calling "
                    "`%s`" % (key, self.settings['operation_id'])
                )

        self.__validate_inputs(kwargs)

        params = self.__gather_params(kwargs)

        accept_headers_list = self.headers_map['accept']
        if accept_headers_list:
            params['header']['Accept'] = self.api_client.select_header_accept(
                accept_headers_list)

        content_type_headers_list = self.headers_map['content_type']
        if content_type_headers_list:
            header_list = self.api_client.select_header_content_type(
                content_type_headers_list)
            params['header']['Content-Type'] = header_list

        return self.api_client.call_api(
            self.settings['endpoint_path'], self.settings['http_method'],
            params['path'],
            params['query'],
            params['header'],
            body=params['body'],
            post_params=params['form'],
            files=params['file'],
            response_type=self.settings['response_type'],
            auth_settings=self.settings['auth'],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            _host=_host,
            collection_formats=params['collection_format'])