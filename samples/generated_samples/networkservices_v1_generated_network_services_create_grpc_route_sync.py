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
# Generated code. DO NOT EDIT!
#
# Snippet for CreateGrpcRoute
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-network-services


# [START networkservices_v1_generated_NetworkServices_CreateGrpcRoute_sync]
from google.cloud import network_services_v1


def sample_create_grpc_route():
    # Create a client
    client = network_services_v1.NetworkServicesClient()

    # Initialize request argument(s)
    grpc_route = network_services_v1.GrpcRoute()
    grpc_route.name = "name_value"
    grpc_route.hostnames = ['hostnames_value_1', 'hostnames_value_2']

    request = network_services_v1.CreateGrpcRouteRequest(
        parent="parent_value",
        grpc_route_id="grpc_route_id_value",
        grpc_route=grpc_route,
    )

    # Make the request
    operation = client.create_grpc_route(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END networkservices_v1_generated_NetworkServices_CreateGrpcRoute_sync]