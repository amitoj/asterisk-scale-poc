# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PlaybacksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def playbacks_playback_id_control_post(self, playback_id, operation, **kwargs):  # noqa: E501
        """Control a playback.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.playbacks_playback_id_control_post(playback_id, operation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: Playback's id (required)
        :param str operation: Operation to perform on the playback. (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.playbacks_playback_id_control_post_with_http_info(playback_id, operation, **kwargs)  # noqa: E501
        else:
            (data) = self.playbacks_playback_id_control_post_with_http_info(playback_id, operation, **kwargs)  # noqa: E501
            return data

    def playbacks_playback_id_control_post_with_http_info(self, playback_id, operation, **kwargs):  # noqa: E501
        """Control a playback.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.playbacks_playback_id_control_post_with_http_info(playback_id, operation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: Playback's id (required)
        :param str operation: Operation to perform on the playback. (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['playback_id', 'operation', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method playbacks_playback_id_control_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'playback_id' is set
        if ('playback_id' not in params or
                params['playback_id'] is None):
            raise ValueError("Missing the required parameter `playback_id` when calling `playbacks_playback_id_control_post`")  # noqa: E501
        # verify the required parameter 'operation' is set
        if ('operation' not in params or
                params['operation'] is None):
            raise ValueError("Missing the required parameter `operation` when calling `playbacks_playback_id_control_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'playback_id' in params:
            path_params['playbackId'] = params['playback_id']  # noqa: E501

        query_params = []
        if 'operation' in params:
            query_params.append(('operation', params['operation']))  # noqa: E501

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/playbacks/{playbackId}/control', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def playbacks_playback_id_delete(self, playback_id, **kwargs):  # noqa: E501
        """Stop a playback.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.playbacks_playback_id_delete(playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: Playback's id (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.playbacks_playback_id_delete_with_http_info(playback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.playbacks_playback_id_delete_with_http_info(playback_id, **kwargs)  # noqa: E501
            return data

    def playbacks_playback_id_delete_with_http_info(self, playback_id, **kwargs):  # noqa: E501
        """Stop a playback.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.playbacks_playback_id_delete_with_http_info(playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: Playback's id (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['playback_id', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method playbacks_playback_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'playback_id' is set
        if ('playback_id' not in params or
                params['playback_id'] is None):
            raise ValueError("Missing the required parameter `playback_id` when calling `playbacks_playback_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'playback_id' in params:
            path_params['playbackId'] = params['playback_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/playbacks/{playbackId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def playbacks_playback_id_get(self, playback_id, **kwargs):  # noqa: E501
        """Get a playback's details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.playbacks_playback_id_get(playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: Playback's id (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Playback
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.playbacks_playback_id_get_with_http_info(playback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.playbacks_playback_id_get_with_http_info(playback_id, **kwargs)  # noqa: E501
            return data

    def playbacks_playback_id_get_with_http_info(self, playback_id, **kwargs):  # noqa: E501
        """Get a playback's details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.playbacks_playback_id_get_with_http_info(playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: Playback's id (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Playback
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['playback_id', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method playbacks_playback_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'playback_id' is set
        if ('playback_id' not in params or
                params['playback_id'] is None):
            raise ValueError("Missing the required parameter `playback_id` when calling `playbacks_playback_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'playback_id' in params:
            path_params['playbackId'] = params['playback_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/playbacks/{playbackId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Playback',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
