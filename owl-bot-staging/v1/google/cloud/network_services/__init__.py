# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.cloud.network_services_v1.services.network_services.client import NetworkServicesClient
from google.cloud.network_services_v1.services.network_services.async_client import NetworkServicesAsyncClient

from google.cloud.network_services_v1.types.common import EndpointMatcher
from google.cloud.network_services_v1.types.common import OperationMetadata
from google.cloud.network_services_v1.types.common import TrafficPortSelector
from google.cloud.network_services_v1.types.endpoint_policy import CreateEndpointPolicyRequest
from google.cloud.network_services_v1.types.endpoint_policy import DeleteEndpointPolicyRequest
from google.cloud.network_services_v1.types.endpoint_policy import EndpointPolicy
from google.cloud.network_services_v1.types.endpoint_policy import GetEndpointPolicyRequest
from google.cloud.network_services_v1.types.endpoint_policy import ListEndpointPoliciesRequest
from google.cloud.network_services_v1.types.endpoint_policy import ListEndpointPoliciesResponse
from google.cloud.network_services_v1.types.endpoint_policy import UpdateEndpointPolicyRequest

__all__ = ('NetworkServicesClient',
    'NetworkServicesAsyncClient',
    'EndpointMatcher',
    'OperationMetadata',
    'TrafficPortSelector',
    'CreateEndpointPolicyRequest',
    'DeleteEndpointPolicyRequest',
    'EndpointPolicy',
    'GetEndpointPolicyRequest',
    'ListEndpointPoliciesRequest',
    'ListEndpointPoliciesResponse',
    'UpdateEndpointPolicyRequest',
)
