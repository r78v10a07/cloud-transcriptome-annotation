"""Generated client library for composer version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.composer.v1beta1 import composer_v1beta1_messages as messages


class ComposerV1beta1(base_api.BaseApiClient):
  """Generated client library for service composer version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://composer.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'composer'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ComposerV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new composer handle."""
    url = url or self.BASE_URL
    super(ComposerV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_environments = self.ProjectsLocationsEnvironmentsService(self)
    self.projects_locations_imageVersions = self.ProjectsLocationsImageVersionsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsEnvironmentsService(base_api.BaseApiService):
    """Service class for the projects_locations_environments resource."""

    _NAME = u'projects_locations_environments'

    def __init__(self, client):
      super(ComposerV1beta1.ProjectsLocationsEnvironmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/environments',
        http_method=u'POST',
        method_id=u'composer.projects.locations.environments.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta1/{+parent}/environments',
        request_field=u'environment',
        request_type_name=u'ComposerProjectsLocationsEnvironmentsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method=u'DELETE',
        method_id=u'composer.projects.locations.environments.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ComposerProjectsLocationsEnvironmentsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an existing environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Environment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method=u'GET',
        method_id=u'composer.projects.locations.environments.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ComposerProjectsLocationsEnvironmentsGetRequest',
        response_type_name=u'Environment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List environments.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListEnvironmentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/environments',
        http_method=u'GET',
        method_id=u'composer.projects.locations.environments.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/environments',
        request_field='',
        request_type_name=u'ComposerProjectsLocationsEnvironmentsListRequest',
        response_type_name=u'ListEnvironmentsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method=u'PATCH',
        method_id=u'composer.projects.locations.environments.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1beta1/{+name}',
        request_field=u'environment',
        request_type_name=u'ComposerProjectsLocationsEnvironmentsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ProjectsLocationsImageVersionsService(base_api.BaseApiService):
    """Service class for the projects_locations_imageVersions resource."""

    _NAME = u'projects_locations_imageVersions'

    def __init__(self, client):
      super(ComposerV1beta1.ProjectsLocationsImageVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""List ImageVersions for provided location.

      Args:
        request: (ComposerProjectsLocationsImageVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListImageVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/imageVersions',
        http_method=u'GET',
        method_id=u'composer.projects.locations.imageVersions.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/imageVersions',
        request_field='',
        request_type_name=u'ComposerProjectsLocationsImageVersionsListRequest',
        response_type_name=u'ListImageVersionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = u'projects_locations_operations'

    def __init__(self, client):
      super(ComposerV1beta1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (ComposerProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'composer.projects.locations.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ComposerProjectsLocationsOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (ComposerProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'composer.projects.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ComposerProjectsLocationsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (ComposerProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method=u'GET',
        method_id=u'composer.projects.locations.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+name}/operations',
        request_field='',
        request_type_name=u'ComposerProjectsLocationsOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(ComposerV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(ComposerV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }