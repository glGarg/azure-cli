# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['account'] = """
type: group
short-summary: Manage Azure subscription information.
"""

helps['account clear'] = """
type: command
short-summary: Clear all subscriptions from the CLI's local cache.
long-summary: To clear the current subscription, use 'az logout'.
"""

helps['account get-access-token'] = """
type: command
short-summary: Get a token for utilities to access Azure.
long-summary: >
    The token will be valid for at least 5 minutes with the maximum at 60 minutes.
    If the subscription argument isn't specified, the current account is used.
"""

helps['account list'] = """
type: command
short-summary: Get a list of subscriptions for the logged in account.
"""

helps['account list-locations'] = """
type: command
short-summary: List supported regions for the current subscription.
"""

helps['account lock'] = """
type: group
short-summary: Manage Azure subscription level locks.
"""

helps['account lock create'] = """
type: command
short-summary: Create a subscription lock.
examples:
  - name: Create a read-only subscription level lock.
    text: >
        az account lock create --lock-type ReadOnly -n lockName
"""

helps['account lock delete'] = """
type: command
short-summary: Delete a subscription lock.
examples:
  - name: Delete a subscription lock
    text: >
        az account lock delete --name lockName
"""

helps['account lock list'] = """
type: command
short-summary: List lock information in the subscription.
examples:
  - name: List out all locks on the subscription level
    text: >
        az account lock list
"""

helps['account lock show'] = """
type: command
short-summary: Show the details of a subscription lock
examples:
  - name: Show a subscription level lock
    text: >
        az account lock show -n lockname
"""

helps['account lock update'] = """
type: command
short-summary: Update a subscription lock.
examples:
  - name: Update a subscription lock with new notes and type
    text: >
        az account lock update --name lockName --notes newNotesHere --lock-type CanNotDelete
"""

helps['account management-group'] = """
type: group
short-summary: Manage Azure Management Groups.
"""

helps['account management-group create'] = """
type: command
short-summary: Create a new management group.
long-summary: Create a new management group.
parameters:
  - name: --name -n
    type: string
    short-summary: Name of the management group.
  - name: --display-name -d
    type: string
    short-summary: Sets the display name of the management group. If null, the group name is set as the display name.
  - name: --parent -p
    type: string
    short-summary: Sets the parent of the management group. Can be the fully qualified id or the name of the management group. If null, the root tenant group is set as the parent.
examples:
  - name: Create a new management group.
    text: >
        az account management-group create --name GroupName
  - name: Create a new management group with a specific display name.
    text: >
        az account management-group create --name GroupName --display-name DisplayName
  - name: Create a new management group with a specific parent.
    text: >
        az account management-group create --name GroupName --parent ParentId/ParentName
  - name: Create a new management group with a specific display name and parent.
    text: >
        az account management-group create --name GroupName --display-name DisplayName --parent ParentId/ParentName
"""

helps['account management-group delete'] = """
type: command
short-summary: Delete an existing management group.
long-summary: Delete an existing management group.
parameters:
  - name: --name -n
    type: string
    short-summary: Name of the management group.
examples:
  - name: Delete an existing management group
    text: >
        az account management-group delete --name GroupName
"""

helps['account management-group list'] = """
type: command
short-summary: List all management groups.
long-summary: List of all management groups in the current tenant.
examples:
  - name: List all management groups
    text: >
        az account management-group list
"""

helps['account management-group show'] = """
type: command
short-summary: Get a specific management group.
long-summary: Get the details of the management group.
parameters:
  - name: --name -n
    type: string
    short-summary: Name of the management group.
  - name: --expand -e
    type: bool
    short-summary: If given, lists the children in the first level of hierarchy.
  - name: --recurse -r
    type: bool
    short-summary: If given, lists the children in all levels of hierarchy.
examples:
  - name: Get a management group.
    text: >
        az account management-group show --name GroupName
  - name: Get a management group with children in the first level of hierarchy.
    text: >
        az account management-group show --name GroupName -e
  - name: Get a management group with children in all levels of hierarchy.
    text: >
        az account management-group show --name GroupName -e -r
"""

helps['account management-group subscription'] = """
type: group
short-summary: Subscription operations for Management Groups.
"""

helps['account management-group subscription add'] = """
type: command
short-summary: Add a subscription to a management group.
long-summary: Add a subscription to a management group.
parameters:
  - name: --name -n
    type: string
    short-summary: Name of the management group.
  - name: --subscription -s
    type: string
    short-summary: Subscription Id or Name
examples:
  - name: Add a subscription to a management group.
    text: >
        az account management-group subscription add --name GroupName --subscription Subscription
"""

helps['account management-group subscription remove'] = """
type: command
short-summary: Remove an existing subscription from a management group.
long-summary: Remove an existing subscription from a management group.
parameters:
  - name: --name -n
    type: string
    short-summary: Name of the management group.
  - name: --subscription -s
    type: string
    short-summary: Subscription Id or Name
examples:
  - name: Remove an existing subscription from a management group.
    text: >
        az account management-group subscription remove --name GroupName --subscription Subscription
"""

helps['account management-group update'] = """
type: command
short-summary: Update an existing management group.
long-summary: Update an existing management group.
parameters:
  - name: --name -n
    type: string
    short-summary: Name of the management group.
  - name: --display-name -d
    type: string
    short-summary: Updates the display name of the management group. If null, no change is made.
  - name: --parent -p
    type: string
    short-summary: Update the parent of the management group. Can be the fully qualified id or the name of the management group. If null, no change is made.
examples:
  - name: Update an existing management group with a specific display name.
    text: >
        az account management-group update --name GroupName --display-name DisplayName
  - name: Update an existing management group with a specific parent.
    text: >
        az account management-group update --name GroupName --parent ParentId/ParentName
  - name: Update an existing management group with a specific display name and parent.
    text: >
        az account management-group update --name GroupName --display-name DisplayName --parent ParentId/ParentName
"""

helps['account set'] = """
type: command
short-summary: Set a subscription to be the current active subscription.
"""

helps['account show'] = """
type: command
short-summary: Get the details of a subscription.
long-summary: If the subscription isn't specified, shows the details of the default subscription.
"""

helps['ad'] = """
type: group
short-summary: Manage Azure Active Directory Graph entities needed for Role Based Access Control
"""

helps['ad app'] = """
type: group
short-summary: Manage applications with AAD Graph.
"""

helps['ad app create'] = """
type: command
short-summary: Create a web application, web API or native application
examples:
  - name: Create a native application with delegated permission of "access the AAD directory as the signed-in user"
    text: |
        az ad app create --display-name my-native --native-app --required-resource-accesses @manifest.json
        ("manifest.json" contains the following content)
        [{
            "resourceAppId": "00000002-0000-0000-c000-000000000000",
            "resourceAccess": [
                {
                    "id": "a42657d6-7f20-40e3-b6f0-cee03008a62a",
                    "type": "Scope"
                }
           ]
        }]
  - name: Create an application with a role
    text: |
        az ad app create --id e042ec79-34cd-498f-9d9f-123456781234 --display-name mytestapp --identifier-uris https://mytestapp.websites.net --app-roles @manifest.json
        ("manifest.json" contains the following content)
        [{
            "allowedMemberTypes": [
              "User"
            ],
            "description": "Approvers can mark documents as approved",
            "displayName": "Approver",
            "isEnabled": "true",
            "value": "approver"
        }]
"""

helps['ad app credential'] = """
type: group
short-summary: manage an application's password or certificate credentials
"""

helps['ad app credential delete'] = """
type: command
short-summary: delete an application's password or certificate credentials
"""

helps['ad app credential list'] = """
type: command
short-summary: list an application's password or certificate credentials
examples:
  - name: list an application's password or certificate credentials (autogenerated)
    text: az ad app credential list --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad app credential reset'] = """
type: command
short-summary: append or overwrite an application's password or certificate credentials
examples:
  - name: append or overwrite an application's password or certificate credentials (autogenerated)
    text: az ad app credential reset --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad app delete'] = """
type: command
short-summary: Delete an application.
examples:
  - name: Delete an application. (autogenerated)
    text: az ad app delete --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad app list'] = """
type: command
short-summary: List applications.
long-summary: for low latency, by default, only the first 100 will be returned unless you provide filter arguments or use "--all"
"""

helps['ad app owner'] = """
type: group
short-summary: Manage application owners.
"""

helps['ad app owner add'] = """
type: command
short-summary: add an application owner.
examples:
  - name: add an application owner. (autogenerated)
    text: az ad app owner add --id 00000000-0000-0000-0000-000000000000 --owner-object-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    crafted: true
"""

helps['ad app owner list'] = """
type: command
short-summary: List application owners.
examples:
  - name: List application owners. (autogenerated)
    text: az ad app owner list --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad app owner remove'] = """
type: command
short-summary: remove an application owner.
"""

helps['ad app permission'] = """
type: group
short-summary: manage an application's OAuth2 permissions.
"""

helps['ad app permission add'] = """
type: command
short-summary: add an API permission
long-summary: invoking "az ad app permission grant" is needed to activate it
examples:
  - name: add a Graph API permission of "Sign in and read user profile"
    text: az ad app permission add --id eeba0b46-78e5-4a1a-a1aa-cafe6c123456 --api 00000002-0000-0000-c000-000000000000 --api-permissions 311a71cc-e848-46a1-bdf8-97ff7156d8e6=Scope
"""

helps['ad app permission admin-consent'] = """
type: command
short-summary: grant Application & Delegated permissions through admin-consent.
long-summary: you must login as a directory administrator
"""

helps['ad app permission delete'] = """
type: command
short-summary: remove an API permission
examples:
  - name: remove an AAD graph permission
    text: az ad app permission delete --id eeba0b46-78e5-4a1a-a1aa-cafe6c123456 --api 00000002-0000-0000-c000-000000000000
"""

helps['ad app permission grant'] = """
type: command
short-summary: Grant the app an API Delegated permissions
long-summary: for Application permissions, please use "ad app permission admin-consent"
examples:
  - name: Grant a native application with permissions to access an existing API with TTL of 2 years
    text: az ad app permission grant --id e042ec79-34cd-498f-9d9f-1234234 --api a0322f79-57df-498f-9d9f-12678 --expires 2
"""

helps['ad app permission list'] = """
type: command
short-summary: List API permissions the application has requested
examples:
  - name: List the OAuth2 permissions for an existing AAD app
    text: az ad app permission list --id e042ec79-34cd-498f-9d9f-1234234
"""

helps['ad app permission list-grants'] = """
type: command
short-summary: List Oauth2 permission grants
examples:
  - name: list oauth2 permissions granted to the service principal
    text: az ad app permission list-grants --id e042ec79-34cd-498f-9d9f-1234234123456
"""

helps['ad app show'] = """
type: command
short-summary: Get the details of an application.
examples:
  - name: Get the details of an application. (autogenerated)
    text: az ad app show --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad app update'] = """
type: command
short-summary: Update an application.
examples:
  - name: update a native application with delegated permission of "access the AAD directory as the signed-in user"
    text: |
        az ad app update --id e042ec79-34cd-498f-9d9f-123456781234 --required-resource-accesses @manifest.json
        ("manifest.json" contains the following content)
        [{
            "resourceAppId": "00000002-0000-0000-c000-000000000000",
            "resourceAccess": [
                {
                    "id": "a42657d6-7f20-40e3-b6f0-cee03008a62a",
                    "type": "Scope"
                }
           ]
        }]
  - name: declare an application role
    text: |
        az ad app update --id e042ec79-34cd-498f-9d9f-123456781234 --app-roles @manifest.json
        ("manifest.json" contains the following content)
        [{
            "allowedMemberTypes": [
              "User"
            ],
            "description": "Approvers can mark documents as approved",
            "displayName": "Approver",
            "isEnabled": "true",
            "value": "approver"
        }]
  - name: update an application's group membership claims to "All"
    text: >
        az ad app update --id e042ec79-34cd-498f-9d9f-123456781234 --set groupMembershipClaims=All

"""

helps['ad group'] = """
type: group
short-summary: Manage Azure Active Directory groups.
"""

helps['ad group create'] = """
type: command
short-summary: Create a group in the directory.
examples:
  - name: Create a group in the directory. (autogenerated)
    text: az ad group create --display-name MyDisplay --mail-nickname MyDisplay
    crafted: true
"""

helps['ad group member'] = """
type: group
short-summary: Manage Azure Active Directory group members.
"""

helps['ad group member check'] = """
type: command
short-summary: Check if a member is in a group.
examples:
  - name: Check if a member is in a group. (autogenerated)
    text: az ad group member check --group MyGroupDisplayName --member-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    crafted: true
"""

helps['ad group owner'] = """
type: group
short-summary: Manage Azure Active Directory group owners.
"""

helps['ad group owner add'] = """
type: command
short-summary: add a group owner.
examples:
  - name: add a group owner. (autogenerated)
    text: az ad group owner add --group MyGroupDisplayName --owner-object-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    crafted: true
"""

helps['ad group owner list'] = """
type: command
short-summary: List group owners.
examples:
  - name: List group owners. (autogenerated)
    text: az ad group owner list --group MyGroupDisplayName
    crafted: true
"""

helps['ad group owner remove'] = """
type: command
short-summary: remove a group owner.
"""

helps['ad signed-in-user'] = """
type: group
short-summary: Show graph information about current signed-in user in CLI
"""

helps['ad signed-in-user list-owned-objects'] = """
type: command
short-summary: Get the list of directory objects that are owned by the user
"""

helps['ad sp'] = """
type: group
short-summary: Manage Azure Active Directory service principals for automation authentication.
"""

helps['ad sp create'] = """
type: command
short-summary: Create a service principal.
examples:
  - name: Create a service principal. (autogenerated)
    text: az ad sp create --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad sp create-for-rbac'] = """
type: command
short-summary: Create a service principal and configure its access to Azure resources.
parameters:
  - name: --name -n
    short-summary: a URI to use as the logic name. It doesn't need to exist. If not present, CLI will generate one.
  - name: --cert
    short-summary: Certificate to use for credentials.
    long-summary: When used with `--keyvault,` indicates the name of the cert to use or create. Otherwise, supply a PEM or DER formatted public certificate string. Use `@{path}` to load from a file. Do not include private key info.
  - name: --create-cert
    short-summary: Create a self-signed certificate to use for the credential.
    long-summary: Use with `--keyvault` to create the certificate in Key Vault. Otherwise, a certificate will be created locally.
  - name: --keyvault
    short-summary: Name or ID of a KeyVault to use for creating or retrieving certificates.
  - name: --years
    short-summary: 'Number of years for which the credentials will be valid. Default: 1 year'
  - name: --scopes
    short-summary: >
        Space-separated list of scopes the service principal's role assignment applies to.
        Defaults to the root of the current subscription.
  - name: --role
    short-summary: Role of the service principal.
examples:
  - name: Create with a default role assignment.
    text: >
        az ad sp create-for-rbac
  - name: Create using a custom name, and with a default assignment.
    text: >
        az ad sp create-for-rbac -n "MyApp"
  - name: Create without a default assignment.
    text: >
        az ad sp create-for-rbac --skip-assignment
  - name: Create with customized contributor assignments.
    text: |
        az ad sp create-for-rbac -n "MyApp" --role contributor \\
            --scopes /subscriptions/{SubID}/resourceGroups/{ResourceGroup1} \\
            /subscriptions/{SubID}/resourceGroups/{ResourceGroup2}
  - name: Create using a self-signed certificte.
    text: az ad sp create-for-rbac --create-cert
  - name: Create using a self-signed certificate, and store it within KeyVault.
    text: az ad sp create-for-rbac --keyvault MyVault --cert CertName --create-cert
  - name: Create using existing certificate in KeyVault.
    text: az ad sp create-for-rbac --keyvault MyVault --cert CertName
"""

helps['ad sp credential'] = """
type: group
short-summary: manage a service principal's credentials.
long-summary: the credential update will be applied on the Application object the service principal is associated with. In other words, you can accomplish the same thing using "az ad app credential"
"""

helps['ad sp credential delete'] = """
type: command
short-summary: delete a service principal's credential.
examples:
  - name: delete a service principal's credential. (autogenerated)
    text: az ad sp credential delete --id 00000000-0000-0000-0000-000000000000 --key-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    crafted: true
"""

helps['ad sp credential list'] = """
type: command
short-summary: list a service principal's credentials.
examples:
  - name: list a service principal's credentials. (autogenerated)
    text: az ad sp credential list --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad sp credential reset'] = """
type: command
short-summary: Reset a service principal credential.
long-summary: Use upon expiration of the service principal's credentials, or in the event that login credentials are lost.
parameters:
  - name: --name -n
    short-summary: Name or app ID of the service principal.
  - name: --password -p
    short-summary: The password used to log in.
    long-summary: If not present and `--cert` is not specified, a random password will be generated.
  - name: --cert
    short-summary: Certificate to use for credentials.
    long-summary: When using `--keyvault,` indicates the name of the cert to use or create. Otherwise, supply a PEM or DER formatted public certificate string. Use `@{path}` to load from a file. Do not include private key info.
  - name: --create-cert
    short-summary: Create a self-signed certificate to use for the credential.
    long-summary: Use with `--keyvault` to create the certificate in Key Vault. Otherwise, a certificate will be created locally.
  - name: --keyvault
    short-summary: Name or ID of a KeyVault to use for creating or retrieving certificates.
  - name: --years
    short-summary: 'Number of years for which the credentials will be valid. Default: 1 year'
examples:
  - name: Reset a service principal credential. (autogenerated)
    text: az ad sp credential reset --name MyAppURIForCredential
    crafted: true
"""

helps['ad sp delete'] = """
type: command
short-summary: Delete a service principal and its role assignments.
examples:
  - name: Delete a service principal and its role assignments. (autogenerated)
    text: az ad sp delete --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad sp list'] = """
type: command
short-summary: List service principals.
long-summary: For low latency, by default, only the first 100 will be returned unless you provide filter arguments or use "--all"
"""

helps['ad sp owner'] = """
type: group
short-summary: Manage service principal owners.
"""

helps['ad sp owner list'] = """
type: command
short-summary: List service principal owners.
examples:
  - name: List service principal owners. (autogenerated)
    text: az ad sp owner list --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad sp show'] = """
type: command
short-summary: Get the details of a service principal.
examples:
  - name: Get the details of a service principal. (autogenerated)
    text: az ad sp show --id 00000000-0000-0000-0000-000000000000
    crafted: true
"""

helps['ad sp update'] = """
type: command
short-summary: update a service principal
"""

helps['ad user'] = """
type: group
short-summary: Manage Azure Active Directory users and user authentication.
"""

helps['ad user create'] = """
type: command
short-summary: Create an Azure Active Directory user.
parameters:
  - name: --force-change-password-next-login
    short-summary: |
        Marks this user as needing to update their password the next time they
        authenticate.
  - name: --password
    short-summary: The password that should be assigned to the user for authentication.
"""

helps['ad user get-member-groups'] = """
type: command
short-summary: Get groups of which the user is a member
examples:
  - name: Get groups of which the user is a member (autogenerated)
    text: az ad user get-member-groups --upn-or-object-id myuser@consoso.com
    crafted: true
"""

helps['ad user list'] = """
type: command
short-summary: List Azure Active Directory users.
"""

helps['ad user update'] = """
type: command
short-summary: Update Azure Active Directory users.
"""

helps['ams'] = """
type: group
short-summary: Manage Azure Media Services resources.
"""

helps['ams account'] = """
type: group
short-summary: Manage Azure Media Services accounts.
"""

helps['ams account check-name'] = """
type: command
short-summary: Checks whether the Media Service resource name is available.
"""

helps['ams account create'] = """
type: command
short-summary: Create an Azure Media Services account.
"""

helps['ams account delete'] = """
type: command
short-summary: Delete an Azure Media Services account.
"""

helps['ams account list'] = """
type: command
short-summary: List Azure Media Services accounts for the entire subscription.
"""

helps['ams account mru'] = """
type: group
short-summary: Manage media reserved units for an Azure Media Services account.
"""

helps['ams account mru set'] = """
type: command
short-summary: Set the type and number of media reserved units for an Azure Media Services account.
"""

helps['ams account mru show'] = """
type: command
short-summary: Show the details of media reserved units for an Azure Media Services account.
"""

helps['ams account show'] = """
type: command
short-summary: Show the details of an Azure Media Services account.
"""

helps['ams account sp'] = """
type: group
short-summary: Manage service principal and role based access for an Azure Media Services account.
"""

helps['ams account sp create'] = """
type: command
short-summary: Create a service principal and configure its access to an Azure Media Services account.
long-summary: Service principal propagation throughout Azure Active Directory may take some extra seconds to complete.
examples:
  - name: Create a service principal with password and configure its access to an Azure Media Services account. Output will be in xml format.
    text: >
        az ams account sp create -a myAmsAccount -g myRG -n mySpName --password mySecret --role Owner --xml
"""

helps['ams account sp reset-credentials'] = """
type: command
short-summary: Generate a new client secret for a service principal configured for an Azure Media Services account.
"""

helps['ams account storage'] = """
type: group
short-summary: Manage storage for an Azure Media Services account.
"""

helps['ams account storage add'] = """
type: command
short-summary: Attach a secondary storage to an Azure Media Services account.
"""

helps['ams account storage remove'] = """
type: command
short-summary: Detach a secondary storage from an Azure Media Services account.
"""

helps['ams account storage sync-storage-keys'] = """
type: command
short-summary: Synchronize storage account keys for a storage account associated with an Azure Media Services account.
"""

helps['ams account update'] = """
type: command
short-summary: Update the details of an Azure Media Services account.
"""

helps['ams account-filter'] = """
type: group
short-summary: Manage account filters for an Azure Media Services account.
"""

helps['ams account-filter create'] = """
type: command
short-summary: Create an account filter.
examples:
  - name: Create an asset filter with filter track selections.
    text: >
        az ams account-filter create -a amsAccount -g resourceGroup -n filterName --force-end-timestamp=False --end-timestamp 200000 --start-timestamp 100000 --live-backoff-duration 60 --presentation-window-duration 600000 --timescale 1000 --first-quality 720 --tracks @C:\\tracks.json
"""

helps['ams account-filter delete'] = """
type: command
short-summary: Delete an account filter.
"""

helps['ams account-filter list'] = """
type: command
short-summary: List all the account filters of an Azure Media Services account.
"""

helps['ams account-filter show'] = """
type: command
short-summary: Show the details of an account filter.
"""

helps['ams account-filter update'] = """
type: command
short-summary: Update the details of an account filter.
"""

helps['ams asset'] = """
type: group
short-summary: Manage assets for an Azure Media Services account.
"""

helps['ams asset create'] = """
type: command
short-summary: Create an asset.
"""

helps['ams asset delete'] = """
type: command
short-summary: Delete an asset.
"""

helps['ams asset get-encryption-key'] = """
type: command
short-summary: Get the asset storage encryption keys used to decrypt content created by version 2 of the Media Services API.
"""

helps['ams asset get-sas-urls'] = """
type: command
short-summary: Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.
"""

helps['ams asset list'] = """
type: command
short-summary: List all the assets of an Azure Media Services account.
examples:
  - name: List all the assets whose names start with the string 'Something'.
    text: >
        az ams asset list -a amsAccount -g resourceGroup --query [?starts_with(name,'Something')]
"""

helps['ams asset list-streaming-locators'] = """
type: command
short-summary: List streaming locators which are associated with this asset.
"""

helps['ams asset show'] = """
type: command
short-summary: Show the details of an asset.
"""

helps['ams asset update'] = """
type: command
short-summary: Update the details of an asset.
"""

helps['ams asset-filter'] = """
type: group
short-summary: Manage asset filters for an Azure Media Services account.
"""

helps['ams asset-filter create'] = """
type: command
short-summary: Create an asset filter.
examples:
  - name: Create an asset filter with filter track selections.
    text: >
        az ams asset-filter create -a amsAccount -g resourceGroup -n filterName --force-end-timestamp=False --end-timestamp 200000 --start-timestamp 100000 --live-backoff-duration 60 --presentation-window-duration 600000 --timescale 1000 --first-quality 720 --asset-name assetName --tracks @C:\\tracks.json
"""

helps['ams asset-filter delete'] = """
type: command
short-summary: Delete an asset filter.
"""

helps['ams asset-filter list'] = """
type: command
short-summary: List all the asset filters of an Azure Media Services account.
"""

helps['ams asset-filter show'] = """
type: command
short-summary: Show the details of an asset filter.
"""

helps['ams asset-filter update'] = """
type: command
short-summary: Update the details of an asset filter.
"""

helps['ams content-key-policy'] = """
type: group
short-summary: Manage content key policies for an Azure Media Services account.
"""

helps['ams content-key-policy create'] = """
type: command
short-summary: Create a new content key policy.
"""

helps['ams content-key-policy delete'] = """
type: command
short-summary: Delete a content key policy.
"""

helps['ams content-key-policy list'] = """
type: command
short-summary: List all the content key policies within an Azure Media Services account.
"""

helps['ams content-key-policy option'] = """
type: group
short-summary: Manage options for an existing content key policy.
"""

helps['ams content-key-policy option add'] = """
type: command
short-summary: Add a new option to an existing content key policy.
"""

helps['ams content-key-policy option remove'] = """
type: command
short-summary: Remove an option from an existing content key policy.
"""

helps['ams content-key-policy option update'] = """
type: command
short-summary: Update an option from an existing content key policy.
examples:
  - name: Update an existing content-key-policy by adding an alternate token key to an existing option.
    text: >
        az ams content-key-policy option update -n contentKeyPolicyName -g resourceGroup -a amsAccount --policy-option-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --add-alt-token-key tokenKey --add-alt-token-key-type Symmetric
"""

helps['ams content-key-policy show'] = """
type: command
short-summary: Show an existing content key policy.
"""

helps['ams content-key-policy update'] = """
type: command
short-summary: Update an existing content key policy.
examples:
  - name: Update an existing content-key-policy, set a new description and edit its first option setting a new issuer and audience.
    text: >
        az ams content-key-policy update -n contentKeyPolicyName -a amsAccount --description newDescription --set options[0].restriction.issuer=newIssuer --set options[0].restriction.audience=newAudience
"""

helps['ams job'] = """
type: group
short-summary: Manage jobs for a transform.
"""

helps['ams job cancel'] = """
type: command
short-summary: Cancel a job.
"""

helps['ams job delete'] = """
type: command
short-summary: Delete a job.
"""

helps['ams job list'] = """
type: command
short-summary: List all the jobs of a transform within an Azure Media Services account.
examples:
  - name: List all the jobs of a transform with 'Normal' priority by name.
    text: >
        az ams job list -a amsAccount -g resourceGroup -t transformName --query [?priority=='Normal'].{jobName:name}
  - name: List all the jobs of a transform by name and input.
    text: >
        az ams job list -a amsAccount -g resourceGroup -t transformName --query [].{jobName:name,jobInput:input}
"""

helps['ams job show'] = """
type: command
short-summary: Show the details of a job.
"""

helps['ams job start'] = """
type: command
short-summary: Start a job.
"""

helps['ams job update'] = """
type: command
short-summary: Update an existing job.
"""

helps['ams live-event'] = """
type: group
short-summary: Manage live events for an Azure Media Service account.
"""

helps['ams live-event create'] = """
type: command
short-summary: Create a live event.
"""

helps['ams live-event delete'] = """
type: command
short-summary: Delete a live event.
"""

helps['ams live-event list'] = """
type: command
short-summary: List all the live events of an Azure Media Services account.
examples:
  - name: List all the live events by name and resourceState quickly.
    text: >
        az ams live-event list -a amsAccount -g resourceGroup --query [].{liveEventName:name,state:resourceState}
"""

helps['ams live-event reset'] = """
type: command
short-summary: Reset a live event.
"""

helps['ams live-event show'] = """
type: command
short-summary: Show the details of a live event.
"""

helps['ams live-event start'] = """
type: command
short-summary: Start a live event.
"""

helps['ams live-event stop'] = """
type: command
short-summary: Stop a live event.
"""

helps['ams live-event update'] = """
type: command
short-summary: Update the details of a live event.
examples:
  - name: Set a new allowed IP address and remove an existing IP address at index '0'.
    text: >
        az ams live-event update -a amsAccount -g resourceGroup -n liveEventName --remove input.accessControl.ip.allow 0 --add input.accessControl.ip.allow 1.2.3.4/22
  - name: Clear existing IP addresses and set new ones.
    text: >
        az ams live-event update -a amsAccount -g resourceGroup -n liveEventName --ips 1.2.3.4/22 5.6.7.8/30

"""

helps['ams live-event wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the live event is met.
examples:
  - name: Place the CLI in a waiting state until the live event is created.
    text: az ams live-event wait -g MyResourceGroup -a MyAmsAccount -n MyLiveEvent --created
"""

helps['ams live-output'] = """
type: group
short-summary: Manage live outputs for an Azure Media Service account.
"""

helps['ams live-output create'] = """
type: command
short-summary: Create a live output.
"""

helps['ams live-output delete'] = """
type: command
short-summary: Delete a live output.
"""

helps['ams live-output list'] = """
type: command
short-summary: List all the live outputs in a live event.
"""

helps['ams live-output show'] = """
type: command
short-summary: Show the details of a live output.
"""

helps['ams streaming-endpoint'] = """
type: group
short-summary: Manage streaming endpoints for an Azure Media Service account.
"""

helps['ams streaming-endpoint akamai'] = """
type: group
short-summary: Manage AkamaiAccessControl objects to be used on streaming endpoints.
"""

helps['ams streaming-endpoint akamai add'] = """
type: command
short-summary: Add an AkamaiAccessControl to an existing streaming endpoint.
"""

helps['ams streaming-endpoint akamai remove'] = """
type: command
short-summary: Remove an AkamaiAccessControl from an existing streaming endpoint.
"""

helps['ams streaming-endpoint create'] = """
type: command
short-summary: Create a streaming endpoint.
"""

helps['ams streaming-endpoint delete'] = """
type: command
short-summary: Delete a streaming endpoint.
"""

helps['ams streaming-endpoint list'] = """
type: command
short-summary: List all the streaming endpoints within an Azure Media Services account.
"""

helps['ams streaming-endpoint scale'] = """
type: command
short-summary: Set the scale of a streaming endpoint.
"""

helps['ams streaming-endpoint show'] = """
type: command
short-summary: Show the details of a streaming endpoint.
"""

helps['ams streaming-endpoint start'] = """
type: command
short-summary: Start a streaming endpoint.
"""

helps['ams streaming-endpoint stop'] = """
type: command
short-summary: Stop a streaming endpoint.
"""

helps['ams streaming-endpoint update'] = """
type: command
short-summary: Update the details of a streaming endpoint.
"""

helps['ams streaming-endpoint wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the streaming endpoint is met.
examples:
  - name: Place the CLI in a waiting state until the streaming endpoint is created.
    text: az ams streaming-endpoint wait -g MyResourceGroup -a MyAmsAccount -n MyStreamingEndpoint --created
"""

helps['ams streaming-locator'] = """
type: group
short-summary: Manage streaming locators for an Azure Media Services account.
"""

helps['ams streaming-locator create'] = """
type: command
short-summary: Create a streaming locator.
"""

helps['ams streaming-locator get-paths'] = """
type: command
short-summary: List paths supported by a streaming locator.
"""

helps['ams streaming-locator list'] = """
type: command
short-summary: List all the streaming locators within an Azure Media Services account.
"""

helps['ams streaming-locator list-content-keys'] = """
type: command
short-summary: List content keys used by a streaming locator.
"""

helps['ams streaming-locator show'] = """
type: command
short-summary: Show the details of a streaming locator.
"""

helps['ams streaming-policy'] = """
type: group
short-summary: Manage streaming policies for an Azure Media Services account.
"""

helps['ams streaming-policy create'] = """
type: command
short-summary: Create a streaming policy.
"""

helps['ams streaming-policy list'] = """
type: command
short-summary: List all the streaming policies within an Azure Media Services account.
"""

helps['ams streaming-policy show'] = """
type: command
short-summary: Show the details of a streaming policy.
"""

helps['ams transform'] = """
type: group
short-summary: Manage transforms for an Azure Media Services account.
"""

helps['ams transform create'] = """
type: command
short-summary: Create a transform.
examples:
  - name: Create a transform with AdaptiveStreaming built-in preset and High relative priority.
    text: >
        az ams transform create -a myAmsAccount -n transformName -g myResourceGroup --preset AdaptiveStreaming --relative-priority High
  - name: Create a transform with a custom Standard Encoder preset from a JSON file and Low relative priority.
    text: >
        az ams transform create -a myAmsAccount -n transformName -g myResourceGroup --preset "C:\\MyPresets\\CustomPreset.json" --relative-priority Low
"""

helps['ams transform delete'] = """
type: command
short-summary: Delete a transform.
"""

helps['ams transform list'] = """
type: command
short-summary: List all the transforms of an Azure Media Services account.
"""

helps['ams transform output'] = """
type: group
short-summary: Manage transform outputs for an Azure Media Services account.
"""

helps['ams transform output add'] = """
type: command
short-summary: Add an output to an existing transform.
examples:
  - name: Add an output with a custom Standard Encoder preset from a JSON file.
    text: >
        az ams transform output add -a myAmsAccount -n transformName -g myResourceGroup --preset "C:\\MyPresets\\CustomPreset.json"
  - name: Add an output with a VideoAnalyzer preset with es-ES as audio language and only with audio insights.
    text: >
        az ams transform output add -a myAmsAccount -n transformName -g myResourceGroup --preset VideoAnalyzer --audio-language es-ES --insights-to-extract AudioInsightsOnly
"""

helps['ams transform output remove'] = """
type: command
short-summary: Remove an output from an existing transform.
examples:
  - name: Remove the output element at the index specified with --output-index argument.
    text: >
        az ams transform output remove -a myAmsAccount -n transformName -g myResourceGroup --output-index 1
"""

helps['ams transform show'] = """
type: command
short-summary: Show the details of a transform.
"""

helps['ams transform update'] = """
type: command
short-summary: Update the details of a transform.
examples:
  - name: Update the first transform output of a transform by setting its relative priority to High.
    text: >
        az ams transform update -a myAmsAccount -n transformName -g myResourceGroup --set outputs[0].relativePriority=High
"""

helps['apim'] = """
type: group
short-summary: Manage Azure API Management services.
"""

helps['apim backup'] = """
type: command
short-summary: Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.
"""

helps['apim create'] = """
type: command
short-summary: Create an API Management service instance.
parameters:
  - name: --name -n
    type: string
    short-summary: unique name of the service instance to be created
    long-summary: |
        The name must be globally unique since it will be included as the gateway
        hostname like' https://my-api-servicename.azure-api.net'.  See examples.
examples:
  - name: Create a Developer tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --publisher-email email@mydomain.com --publisher-name Microsoft
  - name: Create a Consumption tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --sku-name Consumption --enable-client-certificate \\
            --publisher-email email@mydomain.com --publisher-name Microsoft
"""

helps['apim delete'] = """
type: command
short-summary: Deletes an API Management service.
examples:
  - name: Delete an API Management service.
    text: >
        az apim delete -n MyApim -g MyResourceGroup
"""

helps['apim list'] = """
type: command
short-summary: List API Management service instances.
"""

helps['apim show'] = """
type: command
short-summary: Show details of an API Management service instance.
"""

helps['apim update'] = """
type: command
short-summary: Update an API Management service instance.
"""

helps['appconfig'] = """
type: group
short-summary: Manage App Configurations.
"""

helps['appconfig create'] = """
type: command
short-summary: Create an App Configuration.
examples:
  - name: Create an App Configuration with name, location and resource group.
    text: az appconfig create -g MyResourceGroup -n MyAppConfiguration -l westus
"""

helps['appconfig credential'] = """
type: group
short-summary: Manage credentials for App Configurations
"""

helps['appconfig credential list'] = """
type: command
short-summary: List access keys of an App Configuration.
examples:
  - name: List access keys of an App Configuration
    text: az appconfig credential list -g MyResourceGroup -n MyAppConfiguration
"""

helps['appconfig credential regenerate'] = """
type: command
short-summary: Regenerate an access key for an App Configuration.
examples:
  - name: Regenerate a read only access key for an App Configuration
    text: az appconfig credential regenerate -g MyResourceGroup -n MyAppConfiguration --id 0-l0-s0:8ldbreMVH+d7EjaSUg3H
"""

helps['appconfig delete'] = """
type: command
short-summary: Delete an App Configuration.
examples:
  - name: Delete an App Configuration under resource group
    text: az appconfig delete -g MyResourceGroup -n MyAppConfiguration
"""

helps['appconfig kv'] = """
type: group
short-summary: Manage key-values stored in an App Configuration.
"""

helps['appconfig kv delete'] = """
type: command
short-summary: Delete key-values.
examples:
  - name: Delete a key using App Configuration name without confirmation.
    text: az appconfig kv delete -n MyAppConfiguration --key color --label MyLabel --yes
  - name: Delete a key using connection string.
    text: az appconfig kv delete --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --key color --label MyLabel
"""

helps['appconfig kv export'] = """
type: command
short-summary: Export configurations to another place from your App Configuration.
examples:
  - name: Export all keys with label test to a json file.
    text: az appconfig kv export -n MyAppConfiguration --label test -d file --path D:/abc.json --format json
  - name: Export all keys with null label to another App Configuration.
    text: az appconfig kv export -n MyAppConfiguration -d appconfig --dest-name AnotherAppConfiguration
  - name: Export all keys with null label to an App Service appliaction.
    text: az appconfig kv export -n MyAppConfiguration -d appservice  --appservice-account MyAppService
"""

helps['appconfig kv import'] = """
type: command
short-summary: Import configurations into your App Configuration from another place.
examples:
  - name: Import all keys with label test from a file.
    text: az appconfig kv import -n MyAppConfiguration --label test -s file --path D:/abc.json --format json
  - name: Import all keys with null label from an App Configuration.
    text: az appconfig kv import -n MyAppConfiguration -s appconfig --src-name AnotherAppConfiguration
  - name: Import all keys with null label from an App Service appliaction.
    text: az appconfig kv import -n MyAppConfiguration -s appservice --appservice-account MyAppService
"""

helps['appconfig kv list'] = """
type: command
short-summary: List key-values.
examples:
  - name: List all key-values.
    text: az appconfig kv list -n MyAppConfiguration
  - name: List a specfic key for any label start with v1. using connection string.
    text: az appconfig kv list --key color --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --label v1.*
  - name: List all keys with any labels and query only key, value and tags.
    text: az appconfig kv list --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --fields key value tags --datetime "2019-05-01T11:24:12Z"
  - name: List 150 key-values with any labels.
    text: az appconfig kv list --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx  --top 150
"""

helps['appconfig kv lock'] = """
type: command
short-summary: Lock a key-value to prohibit write operations.
examples:
  - name: Lock a key-value using App Configuration name.
    text: az appconfig kv lock -n MyAppConfiguration --key color --label test
  - name: Force locking a key-value using connection string.
    text: az appconfig kv lock --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --key color --label test --yes
"""

helps['appconfig kv set'] = """
type: command
short-summary: Set a key-value.
examples:
  - name: Set a key-value with label MyLabel.
    text: az appconfig kv set -n MyAppConfiguration --key color --label MyLabel --value red
  - name: Set a key with null label using connection string.
    text: az appconfig kv set --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --key color --value red --tags key1=value1 key2=value2
"""

helps['appconfig kv show'] = """
type: command
short-summary: Show all attributes of a key-value.
examples:
  - name: Show a key-value using App Configuration name with a specific label and datetime
    text: az appconfig kv show -n MyAppConfiguration --key color --label MyLabel --datetime "2019-05-01T11:24:12Z"
  - name: Show a key-value using connection string with label
    text: az appconfig kv show --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --key color --label MyLabel
"""

helps['appconfig kv unlock'] = """
type: command
short-summary: Unlock a key-value to gain write operations.
examples:
  - name: Unlock a key-value using App Configuration name.
    text: az appconfig kv unlock -n MyAppConfiguration --key color --label test
  - name: Force unlocking a key-value using connection string.
    text: az appconfig kv unlock --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --key color --label test --yes
"""

helps['appconfig list'] = """
type: command
short-summary: Lists all App Configurations under the current subscription.
examples:
  - name: List all App Configurations under a resource group
    text: az appconfig list -g MyResourceGroup
"""

helps['appconfig revision'] = """
type: group
short-summary: Manage revisions for key-values stored in an App Configuration.
"""

helps['appconfig revision list'] = """
type: command
short-summary: Lists revision history of key-values.
examples:
  - name: List revision history of key "color" label "test" using App Configuration name.
    text: az appconfig revision list -n MyAppConfiguration --key color --label test
  - name: List revision history for key "color" with any labels using connection string
    text: az appconfig revision list --connection-string Endpoint=https://contoso.azconfig.io;Id=xxx;Secret=xxx --key color --datetime "2019-05-01T11:24:12Z"
"""

helps['appconfig show'] = """
type: command
short-summary: Show properties of an App Configuration.
examples:
  - name: Show properties of an App Configuration
    text: az appconfig show -g MyResourceGroup -n MyAppConfiguration
"""

helps['appconfig update'] = """
type: command
short-summary: Update an App Configuration.
examples:
  - name: Update tags of an App Configuration
    text: az appconfig update -g MyResourceGroup -n MyAppConfiguration --tags key1=value1 key2=value2
"""

helps['appservice'] = """
type: group
short-summary: Manage App Service plans.
"""

helps['appservice hybrid-connection'] = """
type: group
short-summary: a method that sets the key a hybrid-connection uses
"""

helps['appservice hybrid-connection set-key'] = """
type: command
short-summary: set the key that all apps in an appservice plan use to connect to the hybrid-connections in that appservice plan
examples:
  - name: set the key that all apps in an appservice plan use to connect to the hybrid-connections in that appservice plan
    text: az appservice hybrid-connection set-key -g MyResourceGroup --plan MyAppServicePlan --namespace [HybridConectionNamespace] --hybrid-connection [HybridConnectionName] --key-type ["primary"/"secondary"]
"""

helps['appservice list-locations'] = """
type: command
short-summary: List regions where a plan sku is available.
examples:
  - name: List regions where a plan sku is available. (autogenerated)
    text: az appservice list-locations --sku F1
    crafted: true
"""

helps['appservice plan'] = """
type: group
short-summary: Manage app service plans.
"""

helps['appservice plan create'] = """
type: command
short-summary: Create an app service plan.
examples:
  - name: Create a basic app service plan.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan
  - name: Create a standard app service plan with with four Linux workers.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan \\
            --is-linux --number-of-workers 4 --sku S1
"""

helps['appservice plan delete'] = """
type: command
short-summary: Delete an app service plan.
examples:
  - name: Delete an app service plan. (autogenerated)
    text: az appservice plan delete --name MyAppServicePlan --resource-group MyResourceGroup
    crafted: true
"""

helps['appservice plan list'] = """
type: command
short-summary: List app service plans.
examples:
  - name: List all free tier App Service plans.
    text: >
        az appservice plan list --query "[?sku.tier=='Free']"
"""

helps['appservice plan show'] = """
type: command
short-summary: Get the app service plans for a resource group or a set of resource groups.
examples:
  - name: Get the app service plans for a resource group or a set of resource groups. (autogenerated)
    text: az appservice plan show --name MyAppServicePlan   --resource-group MyResourceGroup
    crafted: true
"""

helps['appservice plan update'] = """
type: command
short-summary: Update an app service plan. See https://docs.microsoft.com/azure/app-service/app-service-plan-manage#move-an-app-to-another-app-service-plan to learn more
examples:
  - name: Update an app service plan. (autogenerated)
    text: az appservice plan update --name MyAppServicePlan --resource-group MyResourceGroup --sku F1
    crafted: true
"""

helps['appservice vnet-integration'] = """
type: group
short-summary: a method that lists the virtual network integrations used in an appservice plan
"""

helps['appservice vnet-integration list'] = """
type: command
short-summary: list the virtual network integrations used in an appservice plan
examples:
  - name: list the virtual network integrations used in an appservice plan
    text: az appservice vnet-integration list -g MyResourceGroup --plan MyAppServicePlan
"""

helps['backup'] = """
type: group
short-summary: Manage Azure Backups.
"""

helps['backup container'] = """
type: group
short-summary: Resource which houses items or applications to be protected.
"""

helps['backup container list'] = """
type: command
short-summary: List containers registered to a Recovery services vault.
examples:
  - name: List containers registered to a Recovery services vault. (autogenerated)
    text: az backup container list --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup container show'] = """
type: command
short-summary: Show details of a container registered to a Recovery services vault.
examples:
  - name: Show details of a container registered to a Recovery services vault. (autogenerated)
    text: az backup container show --name MyContainer --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup item'] = """
type: group
short-summary: An item which is already protected or backed up to an Azure Recovery services vault with an associated policy.
"""

helps['backup item list'] = """
type: command
short-summary: List all backed up items within a container.
examples:
  - name: List all backed up items within a container. (autogenerated)
    text: az backup item list --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup item set-policy'] = """
type: command
short-summary: Update the policy associated with this item.
"""

helps['backup item show'] = """
type: command
short-summary: Show details of a particular backed up item.
examples:
  - name: Show details of a particular backed up item. (autogenerated)
    text: az backup item show --container-name MyContainer --ids {ids} --name MyBackedUpItem
    crafted: true
"""

helps['backup job'] = """
type: group
short-summary: Entity which contains details of the job.
"""

helps['backup job list'] = """
type: command
short-summary: List all backup jobs of a Recovery Services vault.
examples:
  - name: List all backup jobs of a Recovery Services vault
    text: az backup job list --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup job show'] = """
type: command
short-summary: Show details of a particular job.
examples:
  - name: Show details of a particular job. (autogenerated)
    text: az backup job show --name MyJob --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup job stop'] = """
type: command
short-summary: Suspend or terminate a currently running job.
examples:
  - name: Suspend or terminate a currently running job. (autogenerated)
    text: az backup job stop --name MyJob --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup job wait'] = """
type: command
short-summary: Wait until either the job completes or the specified timeout value is reached.
examples:
  - name: Wait until either the job completes or the specified timeout value is reached
    text: az backup job wait --name MyJob --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy'] = """
type: group
short-summary: A backup policy defines when you want to take a backup and for how long you would retain each backup copy.
"""

helps['backup policy delete'] = """
type: command
short-summary: Before you can delete a Backup protection policy, the policy must not have any associated Backup items. To  associate another policy with a Backup item, use the backup item set-policy command.
examples:
  - name: Before you can delete a Backup protection policy, the policy must not have any associated Backup items. To  associate another policy with a Backup item, use the backup item set-policy command. (autogenerated)
    text: az backup policy delete --name MyBackupPolicy --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy get-default-for-vm'] = """
type: command
short-summary: Get the default policy with default values to backup a VM.
examples:
  - name: Get the default policy with default values to backup a VM. (autogenerated)
    text: az backup policy get-default-for-vm --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy list'] = """
type: command
short-summary: List all policies for a Recovery services vault.
examples:
  - name: List all policies for a Recovery services vault. (autogenerated)
    text: az backup policy list --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy list-associated-items'] = """
type: command
short-summary: List all items protected by a backup policy.
examples:
  - name: List all items protected by a backup policy
    text: az backup policy list-associated-items --name MyBackupPolicy --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy set'] = """
type: command
short-summary: Update the properties of the backup policy.
examples:
  - name: Update the properties of the backup policy. (autogenerated)
    text: az backup policy set --policy {policy} --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup policy show'] = """
type: command
short-summary: Show details of a particular policy.
examples:
  - name: Show details of a particular policy
    text: az backup policy show --name MyBackupPolicy --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup protection'] = """
type: group
short-summary: Manage protection of your items, enable protection or disable it, or take on-demand backups.
"""

helps['backup protection backup-now'] = """
type: command
short-summary: Perform an on-demand backup of a backed up item.
examples:
  - name: Perform an on-demand backup of a backed up item. (autogenerated)
    text: az backup protection backup-now --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --retain-until 01-02-2018 --vault-name MyVault
    crafted: true
"""

helps['backup protection check-vm'] = """
type: command
short-summary: Find out whether the virtual machine is protected or not. If protected, it returns the recovery services vault ID, otherwise it returns empty.
examples:
  - name: Find out whether the virtual machine is protected or not. If protected, it returns the recovery services vault ID, otherwise it returns empty. (autogenerated)
    text: az backup protection check-vm --vm-id {vm-id}
    crafted: true
"""

helps['backup protection disable'] = """
type: command
short-summary: Stop protecting a backed up Azure VM.
examples:
  - name: Stop protecting a backed up Azure VM. (autogenerated)
    text: az backup protection disable --container-name MyContainer --delete-backup-data false --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault --yes
    crafted: true
"""

helps['backup protection enable-for-vm'] = """
type: command
short-summary: Start protecting a previously unprotected Azure VM as per the specified policy to a Recovery services vault.
examples:
  - name: Start protecting a previously unprotected Azure VM as per the specified policy to a Recovery services vault. (autogenerated)
    text: az backup protection enable-for-vm --policy-name MyPolicy --resource-group MyResourceGroup --vault-name MyVault --vm myVM
    crafted: true
"""

helps['backup recoverypoint'] = """
type: group
short-summary: A snapshot of data at that point-of-time, stored in Recovery Services Vault, from which you can restore information.
"""

helps['backup recoverypoint list'] = """
type: command
short-summary: List all recovery points of a backed up item.
examples:
  - name: List all recovery points of a backed up item. (autogenerated)
    text: az backup recoverypoint list --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --vault-name MyVault
    crafted: true
"""

helps['backup recoverypoint show'] = """
type: command
short-summary: Shows details of a particular recovery point.
"""

helps['backup restore'] = """
type: group
short-summary: Restore backed up items from recovery points in a Recovery Services vault.
"""

helps['backup restore files'] = """
type: group
short-summary: Gives access to all files of a recovery point.
"""

helps['backup restore files mount-rp'] = """
type: command
short-summary: Download a script which mounts files of a recovery point.
examples:
  - name: Download a script which mounts files of a recovery point. (autogenerated)
    text: az backup restore files mount-rp --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --rp-name MyRp --vault-name MyVault
    crafted: true
"""

helps['backup restore files unmount-rp'] = """
type: command
short-summary: Close access to the recovery point.
"""

helps['backup restore restore-disks'] = """
type: command
short-summary: Restore disks of the backed VM from the specified recovery point.
examples:
  - name: Restore disks of the backed VM from the specified recovery point. (autogenerated)
    text: az backup restore restore-disks --container-name MyContainer --item-name MyItem --resource-group MyResourceGroup --rp-name MyRp --storage-account mystorageaccount --vault-name MyVault
    crafted: true
"""

helps['backup vault'] = """
type: group
short-summary: Online storage entity in Azure used to hold data such as backup copies, recovery points and backup policies.
"""

helps['backup vault backup-properties'] = """
type: group
short-summary: Properties of the Recovery Services vault.
"""

helps['backup vault backup-properties set'] = """
type: command
short-summary: Sets backup related properties of the Recovery Services vault.
examples:
  - name: Sets backup related properties of the Recovery Services vault. (autogenerated)
    text: az backup vault backup-properties set --backup-storage-redundancy GeoRedundant --name MyRecoveryServicesVault --resource-group MyResourceGroup
    crafted: true
"""

helps['backup vault backup-properties show'] = """
type: command
short-summary: Gets backup related properties of the Recovery Services vault.
examples:
  - name: Gets backup related properties of the Recovery Services vault. (autogenerated)
    text: az backup vault backup-properties show --name MyRecoveryServicesVault --resource-group MyResourceGroup
    crafted: true
"""

helps['backup vault create'] = """
type: command
short-summary: Create a new Recovery Services vault.
examples:
  - name: Create a new Recovery Services vault. (autogenerated)
    text: az backup vault create --location westus2 --name MyRecoveryServicesVault --resource-group MyResourceGroup
    crafted: true
"""

helps['backup vault delete'] = """
type: command
short-summary: Delete an existing Recovery services vault.
examples:
  - name: Delete an existing Recovery services vault. (autogenerated)
    text: az backup vault delete --name MyRecoveryServicesVault --resource-group MyResourceGroup --yes
    crafted: true
"""

helps['backup vault list'] = """
type: command
short-summary: List Recovery service vaults within a subscription.
"""

helps['backup vault show'] = """
type: command
short-summary: Show details of a particular Recovery service vault.
examples:
  - name: Show details of a particular Recovery service vault. (autogenerated)
    text: az backup vault show --name MyRecoveryServicesVault --resource-group MyResourceGroup
    crafted: true
"""

helps['batch'] = """
type: group
short-summary: Manage Azure Batch.
"""

helps['batch account'] = """
type: group
short-summary: Manage Azure Batch accounts.
"""

helps['batch account autostorage-keys'] = """
type: group
short-summary: Manage the access keys for the auto storage account configured for a Batch account.
"""

helps['batch account create'] = """
type: command
short-summary: Create a Batch account with the specified parameters.
"""

helps['batch account keys'] = """
type: group
short-summary: Manage Batch account keys.
"""

helps['batch account list'] = """
type: command
short-summary: List the Batch accounts associated with a subscription or resource group.
"""

helps['batch account login'] = """
type: command
short-summary: Log in to a Batch account through Azure Active Directory or Shared Key authentication.
"""

helps['batch account set'] = """
type: command
short-summary: Update properties for a Batch account.
"""

helps['batch account show'] = """
type: command
short-summary: Get a specified Batch account or the currently set account.
"""

helps['batch application'] = """
type: group
short-summary: Manage Batch applications.
"""

helps['batch application package'] = """
type: group
short-summary: Manage Batch application packages.
"""

helps['batch application package activate'] = """
type: command
short-summary: Activates a Batch application package.
long-summary: This step is unnecessary if the package has already been successfully activated by the `create` command.
"""

helps['batch application package create'] = """
type: command
short-summary: Create a Batch application package record and activate it.
"""

helps['batch application set'] = """
type: command
short-summary: Update properties for a Batch application.
"""

helps['batch application summary'] = """
type: group
short-summary: View a summary of Batch application packages.
"""

helps['batch application summary list'] = """
type: command
short-summary: Lists all of the applications available in the specified account.
long-summary: This operation returns only applications and versions that are available for use on compute nodes; that is, that can be used in an application package reference. For administrator information about applications and versions that are not yet available to compute nodes, use the Azure portal or the 'az batch application list' command.
"""

helps['batch application summary show'] = """
type: command
short-summary: Gets information about the specified application.
long-summary: This operation returns only applications and versions that are available for use on compute nodes; that is, that can be used in an application package reference. For administrator information about applications and versions that are not yet available to compute nodes, use the Azure portal or the 'az batch application list' command.
"""

helps['batch certificate'] = """
type: group
short-summary: Manage Batch certificates.
"""

helps['batch certificate create'] = """
type: command
short-summary: Add a certificate to a Batch account.
"""

helps['batch certificate delete'] = """
type: command
short-summary: Delete a certificate from a Batch account.
"""

helps['batch job'] = """
type: group
short-summary: Manage Batch jobs.
"""

helps['batch job all-statistics'] = """
type: group
short-summary: View statistics of all jobs under a Batch account.
"""

helps['batch job all-statistics show'] = """
type: command
short-summary: Get lifetime summary statistics for all of the jobs in a Batch account.
long-summary: Statistics are aggregated across all jobs that have ever existed in the account, from account creation to the last update time of the statistics.
"""

helps['batch job create'] = """
type: command
short-summary: Add a job to a Batch account.
"""

helps['batch job list'] = """
type: command
short-summary: List all of the jobs or job schedule in a Batch account.
"""

helps['batch job prep-release-status'] = """
type: group
short-summary: View the status of Batch job preparation and release tasks.
"""

helps['batch job reset'] = """
type: command
short-summary: Update the properties of a Batch job. Unspecified properties which can be updated are reset to their defaults.
"""

helps['batch job set'] = """
type: command
short-summary: Update the properties of a Batch job. Updating a property in a subgroup will reset the unspecified properties of that group.
"""

helps['batch job task-counts'] = """
type: group
short-summary: View the number of tasks in a Batch job and their states.
"""

helps['batch job-schedule'] = """
type: group
short-summary: Manage Batch job schedules.
"""

helps['batch job-schedule create'] = """
type: command
short-summary: Add a Batch job schedule to an account.
"""

helps['batch job-schedule reset'] = """
type: command
short-summary: Reset the properties of a job schedule.  An updated job specification only applies to new jobs.
"""

helps['batch job-schedule set'] = """
type: command
short-summary: Update the properties of a job schedule.
long-summary: You can independently update the schedule and the job specification, but any change to either of these entities will reset all properties in that entity.
"""

helps['batch location'] = """
type: group
short-summary: Manage Batch service options for a subscription at the region level.
"""

helps['batch location quotas'] = """
type: group
short-summary: Manage Batch service quotas at the region level.
"""

helps['batch node'] = """
type: group
short-summary: Manage Batch compute nodes.
"""

helps['batch node file'] = """
type: group
short-summary: Manage Batch compute node files.
"""

helps['batch node file download'] = """
type: command
short-summary: Download the content of the a node file.
"""

helps['batch node remote-desktop'] = """
type: group
short-summary: Retrieve the remote desktop protocol file for a Batch compute node.
"""

helps['batch node remote-login-settings'] = """
type: group
short-summary: Retrieve the remote login settings for a Batch compute node.
"""

helps['batch node scheduling'] = """
type: group
short-summary: Manage task scheduling for a Batch compute node.
"""

helps['batch node service-logs'] = """
type: group
short-summary: Manage the service log files of a Batch compute node.
"""

helps['batch node user'] = """
type: group
short-summary: Manage the user accounts of a Batch compute node.
"""

helps['batch node user create'] = """
type: command
short-summary: Add a user account to a Batch compute node.
"""

helps['batch node user reset'] = """
type: command
short-summary: Update the properties of a user account on a Batch compute node. Unspecified properties which can be updated are reset to their defaults.
"""

helps['batch pool'] = """
type: group
short-summary: Manage Batch pools.
"""

helps['batch pool all-statistics'] = """
type: group
short-summary: View statistics of all pools under a Batch account.
"""

helps['batch pool all-statistics show'] = """
type: command
short-summary: Get lifetime summary statistics for all of the pools in a Batch account.
long-summary: Statistics are aggregated across all pools that have ever existed in the account, from account creation to the last update time of the statistics.
"""

helps['batch pool autoscale'] = """
type: group
short-summary: Manage automatic scaling of Batch pools.
"""

helps['batch pool create'] = """
type: command
short-summary: Create a Batch pool in an account. When creating a pool, choose arguments from either Cloud Services Configuration or Virtual Machine Configuration.
"""

helps['batch pool node-counts'] = """
type: group
short-summary: Get node counts for Batch pools.
"""

helps['batch pool reset'] = """
type: command
short-summary: Update the properties of a Batch pool. Unspecified properties which can be updated are reset to their defaults.
"""

helps['batch pool resize'] = """
type: command
short-summary: Resize or stop resizing a Batch pool.
"""

helps['batch pool set'] = """
type: command
short-summary: Update the properties of a Batch pool. Updating a property in a subgroup will reset the unspecified properties of that group.
"""

helps['batch pool supported-images'] = """
type: group
short-summary: Query information on VM images supported by Azure Batch service.
"""

helps['batch pool supported-images list'] = """
type: command
short-summary: Lists all Virtual Machine Images supported by the Azure Batch service.
"""

helps['batch pool usage-metrics'] = """
type: group
short-summary: View usage metrics of Batch pools.
"""

helps['batch task'] = """
type: group
short-summary: Manage Batch tasks.
"""

helps['batch task create'] = """
type: command
short-summary: Create Batch tasks.
"""

helps['batch task file'] = """
type: group
short-summary: Manage Batch task files.
"""

helps['batch task file download'] = """
type: command
short-summary: Download the content of a Batch task file.
"""

helps['batch task reset'] = """
type: command
short-summary: Reset the properties of a Batch task.
"""

helps['batch task subtask'] = """
type: group
short-summary: Manage subtask information of a Batch task.
"""

helps['batchai'] = """
type: group
short-summary: Manage Batch AI resources.
"""

helps['batchai cluster'] = """
type: group
short-summary: Commands to manage clusters.
"""

helps['batchai cluster auto-scale'] = """
type: command
short-summary: Set auto-scale parameters for a cluster.
examples:
  - name: Make a cluster to auto scale between 0 and 10 nodes depending on number of queued and running jobs.
    text: az batchai cluster auto-scale -g MyResourceGroup -w MyWorkspace -n MyCluster --min 0 --max 10
"""

helps['batchai cluster create'] = """
type: command
short-summary: Create a cluster.
examples:
  - name: Create a single node GPU cluster with default image and auto-storage account.
    text: |
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster \\
            -s Standard_NC6 -t 1 --use-auto-storage --generate-ssh-keys
  - name: Create a cluster with a setup command which installs unzip on every node, the command output will be stored on auto storage account Azure File Share.
    text: |
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster \\
            --use-auto-storage \\
            -s Standard_NC6 -t 1 -k id_rsa.pub \\
            --setup-task 'apt update; apt install unzip -y' \\
            --setup-task-output '$AZ_BATCHAI_MOUNT_ROOT/autoafs'
  - name: Create a cluster providing all parameters manually.
    text: |
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster \\
            -i UbuntuLTS -s Standard_NC6 --vm-priority lowpriority \\
            --min 0 --target 1 --max 10 \\
            --storage-account-name MyStorageAccount \\
            --nfs MyNfsToMount --afs-name MyAzureFileShareToMount \\
            --bfs-name MyBlobContainerNameToMount \\
            -u AdminUserName -k id_rsa.pub -p ImpossibleToGuessPassword
  - name: Create a cluster using a configuration file.
    text: >
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster -f cluster.json

"""

helps['batchai cluster delete'] = """
type: command
short-summary: Delete a cluster.
examples:
  - name: Delete a cluster and wait for deletion to be completed.
    text: az batchai cluster delete -g MyResourceGroup -w MyWorkspace -n MyCluster
  - name: Send a delete command for a cluster and do not wait for deletion to be completed.
    text: az batchai cluster delete -g MyResourceGroup -w MyWorkspace -n MyCluster --no-wait
  - name: Delete cluster without asking for confirmation (for non-interactive scenarios).
    text: az batchai cluster delete -g MyResourceGroup -w MyWorkspace -n MyCluster -y
"""

helps['batchai cluster file'] = """
type: group
short-summary: Commands to work with files generated by node setup task.
"""

helps['batchai cluster file list'] = """
type: command
short-summary: List files generated by the cluster's node setup task.
long-summary: List files generated by the cluster's node setup task under $AZ_BATCHAI_STDOUTERR_DIR path. This functionality is available only if the node setup task output directory is located on mounted Azure File Share or Azure Blob Container.
examples:
  - name: List names and sizes of files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster -o table
  - name: List names, sizes and download URLs for files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster
  - name: List names, sizes and download URLs for files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR/folder/subfolder.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -p folder/subfolder
  - name: List names, sizes and download URLs for files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR making download URLs to remain valid for one hour.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            --expiry 60
"""

helps['batchai cluster list'] = """
type: command
short-summary: List clusters.
examples:
  - name: List all clusters in a workspace.
    text: az batchai cluster list -g MyResourceGroup -w MyWorkspace -o table
"""

helps['batchai cluster node'] = """
type: group
short-summary: Commands to work with cluster nodes.
"""

helps['batchai cluster node exec'] = """
type: command
short-summary: Executes a command line on a cluster's node with optional ports forwarding.
examples:
  - name: Report a snapshot of the current processes.
    text: |
        az batchai cluster node exec -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -n tvm-xxx --exec "ps axu"
  - name: Report a GPU information for a node.
    text: |
        az batchai cluster node exec -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -n tvm-xxx --exec "nvidia-smi"
  - name: Forward local 9000 to port 9001 on the node.
    text: |
        az batchai cluster node exec -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -n tvm-xxx -L 9000:localhost:9001
"""

helps['batchai cluster node list'] = """
type: command
short-summary: List remote login information for cluster's nodes.
long-summary: "List remote login information for cluster nodes. You can ssh to a particular node using the provided public IP address and the port number.\nE.g. ssh <admin user name>@<public ip> -p <node's SSH port number>"
examples:
  - name: List remote login information for a cluster.
    text: az batchai cluster node list -g MyResourceGroup -w MyWorkspace -c MyCluster -o table
"""

helps['batchai cluster resize'] = """
type: command
short-summary: Resize a cluster.
examples:
  - name: Resize a cluster to zero size to stop paying for it.
    text: az batchai cluster resize -g MyResourceGroup -w MyWorkspace -n MyCluster -t 0
  - name: Resize a cluster to have 10 nodes.
    text: az batchai cluster resize -g MyResourceGroup -w MyWorkspace -n MyCluster -t 10
"""

helps['batchai cluster show'] = """
type: command
short-summary: Show information about a cluster.
examples:
  - name: Show full information about a cluster.
    text: az batchai cluster show -g MyResourceGroup -w MyWorkspace -n MyCluster
  - name: Show cluster's summary.
    text: az batchai cluster show -g MyResourceGroup -w MyWorkspace -n MyCluster -o table
"""

helps['batchai experiment'] = """
type: group
short-summary: Commands to manage experiments.
"""

helps['batchai experiment create'] = """
type: command
short-summary: Create an experiment.
examples:
  - name: Create an experiment.
    text: az batchai experiment create -g MyResourceGroup -w MyWorkspace -n MyExperiment
"""

helps['batchai experiment delete'] = """
type: command
short-summary: Delete an experiment.
examples:
  - name: Delete an experiment. All running jobs will be terminated.
    text: az batchai experiment delete -g MyResourceGroup -w MyWorkspace -n MyExperiment
  - name: Delete an experiment without asking for confirmation (for non-interactive scenarios).
    text: az batchai experiment delete -g MyResourceGroup -w MyWorkspace -n MyExperiment -y
  - name: Request an experiment deletion without waiting for job to be deleted.
    text: az batchai experiment delete -g MyResourceGroup -w MyWorkspace -n MyExperiment --no-wait
"""

helps['batchai experiment list'] = """
type: command
short-summary: List experiments.
examples:
  - name: List experiments.
    text: az batchai experiment list -g MyResourceGroup -w MyWorkspace -o table
"""

helps['batchai experiment show'] = """
type: command
short-summary: Show information about an experiment.
examples:
  - name: Show information about an experiment.
    text: az batchai experiment show -g MyResourceGroup -w MyWorkspace -n MyExperiment -o table
"""

helps['batchai file-server'] = """
type: group
short-summary: Commands to manage file servers.
"""

helps['batchai file-server create'] = """
type: command
short-summary: Create a file server.
examples:
  - name: Create a NFS file server using a configuration file.
    text: az batchai file-server create -g MyResourceGroup -w MyWorkspace -n MyNFS -f nfs.json
  - name: Create a NFS manually providing parameters.
    text: |
        az batchai file-server create -g MyResourceGroup -w MyWorkspace -n MyNFS \\
            -s Standard_D14 --disk-count 4 --disk-size 512 \\
            --storage-sku Premium_LRS --caching-type readonly \\
            -u $USER -k ~/.ssh/id_rsa.pub
"""

helps['batchai file-server delete'] = """
type: command
short-summary: Delete a file server.
examples:
  - name: Delete file server and wait for deletion to be completed.
    text: az batchai file-server delete -g MyResourceGroup -w MyWorkspace -n MyNFS
  - name: Delete file server without asking for confirmation (for non-interactive scenarios).
    text: az batchai file-server delete -g MyResourceGroup -w MyWorkspace -n MyNFS -y
  - name: Request file server deletion without waiting for deletion to be completed.
    text: az batchai file-server delete -g MyResourceGroup -w MyWorkspace -n MyNFS --no-wait
"""

helps['batchai file-server list'] = """
type: command
short-summary: List file servers.
examples:
  - name: List all file servers in the given workspace.
    text: az batchai file-server list -g MyResourceGroup -w MyWorkspace -o table
"""

helps['batchai file-server show'] = """
type: command
short-summary: Show information about a file server.
examples:
  - name: Show full information about a file server.
    text: az batchai file-server show -g MyResourceGroup -w MyWorkspace -n MyNFS
  - name: Show file server summary.
    text: az batchai file-server show -g MyResourceGroup -w MyWorkspace -n MyNFS -o table

"""

helps['batchai job'] = """
type: group
short-summary: Commands to manage jobs.
"""

helps['batchai job create'] = """
type: command
short-summary: Create a job.
examples:
  - name: Create a job to run on a cluster in the same resource group.
    text: |
        az batchai job create -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob \\
            -c MyCluster -f job.json
  - name: Create a job to run on a cluster in a different workspace.
    text: |
        az batchai job create -g MyJobResourceGroup -w MyJobWorkspace -e MyExperiment -n MyJob \\
            -f job.json \\
            -c "/subscriptions/00000000-0000-0000-0000-000000000000/\\
            resourceGroups/MyClusterResourceGroup/\\
            providers/Microsoft.BatchAI/workspaces/MyClusterWorkspace/clusters/MyCluster"
"""

helps['batchai job delete'] = """
type: command
short-summary: Delete a job.
examples:
  - name: Delete a job. The job will be terminated if it's currently running.
    text: az batchai job delete -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob
  - name: Delete a job without asking for confirmation (for non-interactive scenarios).
    text: az batchai job delete -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob -y
  - name: Request job deletion without waiting for job to be deleted.
    text: az batchai job delete -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob --no-wait
"""

helps['batchai job file'] = """
type: group
short-summary: Commands to list and stream files in job's output directories.
"""

helps['batchai job file list'] = """
type: command
short-summary: List job's output files in a directory with given id.
long-summary: List job's output files in a directory with given id if the output directory is located on mounted Azure File Share or Blob Container.
examples:
  - name: List files in the standard output directory of the job.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob
  - name: List files in the standard output directory of the job. Generates output in a table format.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob -o table
  - name: List files in a folder 'MyFolder/MySubfolder' of an output directory with id 'MODELS'.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -d MODELS -p MyFolder/MySubfolder
  - name: List files in the standard output directory of the job making download URLs to remain valid for 15 minutes.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            --expiry 15
"""

helps['batchai job file stream'] = """
type: command
short-summary: Stream the content of a file (similar to 'tail -f').
long-summary: Waits for the job to create the given file and starts streaming it similar to 'tail -f' command. The command completes when the job finished execution.
examples:
  - name: Stream standard output file of the job.
    text: |
        az batchai job file stream -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -f stdout.txt
  - name: Stream a file 'log.txt' from a folder 'logs' of an output directory with id 'OUTPUTS'.
    text: |
        az batchai job file stream -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -d OUTPUTS -p logs -f log.txt
"""

helps['batchai job list'] = """
type: command
short-summary: List jobs.
examples:
  - name: List jobs.
    text: az batchai job list -g MyResourceGroup -w MyWorkspace -e MyExperiment -o table
"""

helps['batchai job node'] = """
type: group
short-summary: Commands to work with nodes which executed a job.
"""

helps['batchai job node exec'] = """
type: command
short-summary: Executes a command line on a cluster's node used to execute the job with optional ports forwarding.
examples:
  - name: Report a GPU state for a job's node.
    text: |
        az batchai job node exec -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            --exec "nvidia-smi"
  - name: Report a snapshot of the current processes.
    text: |
        az batchai job node exec -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            --exec "ps aux"
  - name: Forward local 9000 to port 9001 on the given node.
    text: |
        az batchai job node exec -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -n tvm-xxx -L 9000:localhost:9001
"""

helps['batchai job node list'] = """
type: command
short-summary: List remote login information for nodes which executed the job.
long-summary: "List remote login information for currently existing (not deallocated) nodes on which the job was executed. You can ssh to a particular node using the provided public IP address and the port number.\nE.g. ssh <admin user name>@<public ip> -p <node's SSH port number>"
examples:
  - name: List remote login information for a job nodes.
    text: az batchai job node list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob -o table
"""

helps['batchai job show'] = """
type: command
short-summary: Show information about a job.
examples:
  - name: Show full information about a job.
    text: az batchai job show -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob
  - name: Show job's summary.
    text: az batchai job show -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob -o table
"""

helps['batchai job terminate'] = """
type: command
short-summary: Terminate a job.
examples:
  - name: Terminate a job and wait for the job to be terminated.
    text: az batchai job terminate -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob
  - name: Terminate a job without asking for confirmation (for non-interactive scenarios).
    text: az batchai job terminate -g MyResourceGroup  -w MyWorkspace -e MyExperiment -n MyJob -y
  - name: Request job termination without waiting for the job to be terminated.
    text: |
        az batchai job terminate -g MyResourceGroup -e MyExperiment -w MyWorkspace -n MyJob \\
            --no-wait
"""

helps['batchai job wait'] = """
type: command
short-summary: Waits for specified job completion and setups the exit code to the job's exit code.
examples:
  - name: Wait for the job completion.
    text: |
        az batchai job wait -g MyResourceGroup -w MyWorkspace -n MyJob
"""

helps['batchai list-usages'] = """
type: command
short-summary: Gets the current usage information as well as limits for Batch AI resources for given location.
examples:
  - name: Get information for eastus location.
    text: az batchai list-usages -l eastus -o table
"""

helps['batchai workspace'] = """
type: group
short-summary: Commands to manage workspaces.
"""

helps['batchai workspace create'] = """
type: command
short-summary: Create a workspace.
examples:
  - name: Create a workspace in East US region.
    text: az batchai workspace create -g MyResourceGroup -n MyWorkspace -l eastus
"""

helps['batchai workspace delete'] = """
type: command
short-summary: Delete a workspace.
examples:
  - name: Delete a workspace.
    text: az batchai workspace delete -g MyResourceGroup -n MyWorkspace
"""

helps['batchai workspace list'] = """
type: command
short-summary: List workspaces.
examples:
  - name: List all workspaces under the current subscription.
    text: az batchai workspace list -o table
  - name: List workspaces in the given resource group.
    text: az batchai workspace list -g MyResourceGroup -o table
"""

helps['batchai workspace show'] = """
type: command
short-summary: Show information about a workspace.
examples:
  - name: Show information about a workspace.
    text: az batchai workspace show -g MyResourceGroup -n MyWorkspace -o table
"""

helps['billing'] = """
type: group
short-summary: Manage Azure Billing.
"""

helps['billing enrollment-account'] = """
type: group
short-summary: Get enrollment accounts.
"""

helps['billing invoice'] = """
type: group
short-summary: Get billing invoices for a subscription.
"""

helps['billing period'] = """
type: group
short-summary: Get billing periods for a subscription.
"""

helps['bot'] = """
type: group
short-summary: Manage Microsoft Azure Bot Service.
"""

helps['bot authsetting'] = """
type: group
short-summary: Manage OAuth connection settings on a bot.
"""

helps['bot authsetting create'] = """
type: command
short-summary: Create an OAuth connection setting on a bot.
examples:
  - name: Create a new OAuth connection setting on a bot.
    text: |-
        az bot authsetting create -g MyResourceGroup -n botName -c myConnectionName \\
        --client-id clientId --client-secret secret --provider-scope-string "scope1 scope2"\\
        --service google --parameters id=myid
"""

helps['bot authsetting delete'] = """
type: command
short-summary: Delete an OAuth connection setting on a bot.
"""

helps['bot authsetting list'] = """
type: command
short-summary: Show all OAuth connection settings on a bot.
"""

helps['bot authsetting list-providers'] = """
type: command
short-summary: List details for all service providers available for creating OAuth connection settings.
examples:
  - name: List all service providers.
    text: |-
        az bot authsetting list-providers
  - name: Filter by a particular type of service provider.
    text: |-
        az bot authsetting list-providers --provider-name google
"""

helps['bot authsetting show'] = """
type: command
short-summary: Show details of an OAuth connection setting on a bot.
"""

helps['bot create'] = """
type: command
short-summary: Create a new v4 SDK bot.
long-summary: Create a new v4 SDK bot.
"""

helps['bot delete'] = """
type: command
short-summary: Delete an existing bot.
"""

helps['bot directline'] = """
type: group
short-summary: Manage the Directline Channel on a bot.
"""

helps['bot directline create'] = """
type: command
short-summary: Create the DirectLine Channel on a bot with only v3 protocol enabled.
examples:
  - name: Create the DirectLine Channel for a bot.
    text: |-
        az bot directline create -n botName -g MyResourceGroup --disablev1
"""

helps['bot directline delete'] = """
type: command
short-summary: Delete the Directline Channel on a bot
"""

helps['bot directline show'] = """
type: command
short-summary: Get details of the Directline Channel on a bot
"""

helps['bot download'] = """
type: command
short-summary: Download an existing bot.
long-summary: The source code is downloaded from the web app associated with the bot. You can then make changes to it and publish it back to your app.
"""

helps['bot email'] = """
type: group
short-summary: Manage the email Channel on a bot.
"""

helps['bot email create'] = """
type: command
short-summary: Create the Email Channel on a bot.
examples:
  - name: Create the Email Channel for a bot
    text: |-
        az bot email create -n botName -g MyResourceGroup -a abc@outlook.com \\
        -p password
"""

helps['bot email delete'] = """
type: command
short-summary: Delete the email Channel on a bot
"""

helps['bot email show'] = """
type: command
short-summary: Get details of the email Channel on a bot
"""

helps['bot facebook'] = """
type: group
short-summary: Manage the Facebook Channel on a bot.
"""

helps['bot facebook create'] = """
type: command
short-summary: Create the Facebook Channel on a bot.
examples:
  - name: Create the Facebook Channel for a bot
    text: |
        az bot facebook create -n botName -g MyResourceGroup --appid myAppId \\
        --page-id myPageId --secret mySecret --token myToken
"""

helps['bot facebook delete'] = """
type: command
short-summary: Delete the Facebook Channel on a bot
"""

helps['bot facebook show'] = """
type: command
short-summary: Get details of the Facebook Channel on a bot
"""

helps['bot kik'] = """
type: group
short-summary: Manage the Kik Channel on a bot.
"""

helps['bot kik create'] = """
type: command
short-summary: Create the Kik Channel on a bot.
examples:
  - name: Create the Kik Channel for a bot.
    text: |-
        az bot kik create -n botName -g MyResourceGroup -u mykikname \\
        --key key --is-validated
"""

helps['bot kik delete'] = """
type: command
short-summary: Delete the Kik Channel on a bot
"""

helps['bot kik show'] = """
type: command
short-summary: Get details of the Kik Channel on a bot
"""

helps['bot msteams'] = """
type: group
short-summary: Manage the Microsoft Teams Channel on a bot.
"""

helps['bot msteams create'] = """
type: command
short-summary: Create the Microsoft Teams Channel on a bot.
examples:
  - name: Create the Microsoft Teams Channel for a bot with calling enabled
    text: |-
        az bot msteams create -n botName -g MyResourceGroup --enable-calling
        --calling-web-hook https://www.myapp.com/
"""

helps['bot msteams delete'] = """
type: command
short-summary: Delete the Microsoft Teams Channel on a bot
"""

helps['bot msteams show'] = """
type: command
short-summary: Get details of the Microsoft Teams Channel on a bot
"""

helps['bot prepare-deploy'] = """
type: command
short-summary: Add scripts/config files for publishing with `az webapp deployment`.
long-summary: Add scripts or configuration files to the root of your local source code directory to be able to publish using `az webapp deployment`. When your code is deployed to your App Service, the generated scripts or configuration files should be appear in D:\home\site\wwwroot on App Service's Kudu web page.
examples:
  - name: Prepare to use `az webapp` to deploy a Javascript bot by fetching a Node.js IIS web.config file.
    text: |-
        az bot prepare-deploy --lang Javascript --code-dir "MyBotCode"
  - name: Prepare to use `az webapp` to deploy a Csharp bot by creating a .deployment file.
    text: |-
        az bot prepare-deploy --lang Csharp --code-dir "." --proj-file-path "MyBot.csproj"
"""

helps['bot prepare-publish'] = """
type: command
short-summary: (Maintenance mode) Add scripts to your local source code directory to be able to publish back using `az bot publish` for v3 SDK bots.
"""

helps['bot publish'] = """
type: command
short-summary: Publish to a bot's associated app service.
long-summary: Publish your source code to your bot's associated app service. This is DEPRECATED for v4 bots and no longer recommended for publishing v4 bots to Azure. Instead use `az bot prepare-deploy` and `az webapp deployment` to deploy your v4 bot. For more information see https://aka.ms/deploy-your-bot.
examples:
  - name: Publish source code to your Azure App, from within the bot code folder
    text: |-
        az bot publish -n botName -g MyResourceGroup
"""

helps['bot show'] = """
type: command
short-summary: Get an existing bot.
long-summary: Get information about an existing bot. To get the information needed to connect to the bot, use the --msbot flag with the command.
examples:
  - name: Get the information needed to connect to an existing bot on Azure
    text: |-
        az bot show -n botName -g MyResourceGroup --msbot
"""

helps['bot skype'] = """
type: group
short-summary: Manage the Skype Channel on a bot.
"""

helps['bot skype create'] = """
type: command
short-summary: Create the Skype Channel on a bot.
examples:
  - name: Create the Skype Channel for a bot with messaging and screen sharing enabled
    text: |-
        az bot skype create -n botName -g MyResourceGroup --enable-messaging
        --enable-screen-sharing
"""

helps['bot skype delete'] = """
type: command
short-summary: Delete the Skype Channel on a bot
"""

helps['bot skype show'] = """
type: command
short-summary: Get details of the Skype Channel on a bot
"""

helps['bot slack'] = """
type: group
short-summary: Manage the Slack Channel on a bot.
"""

helps['bot slack create'] = """
type: command
short-summary: Create the Slack Channel on a bot.
examples:
  - name: Create the Slack Channel for a bot.
    text: |-
        az bot slack create -n botName -g MyResourceGroup --client-id clientid \\
        --client-secret secret --verification-token token
"""

helps['bot slack delete'] = """
type: command
short-summary: Delete the Slack Channel on a bot
"""

helps['bot slack show'] = """
type: command
short-summary: Get details of the Slack Channel on a bot
"""

helps['bot sms'] = """
type: group
short-summary: Manage the SMS Channel on a bot.
"""

helps['bot sms create'] = """
type: command
short-summary: Create the SMS Channel on a bot.
examples:
  - name: Create the SMS Channel for a bot.
    text: |-
        az bot sms create -n botName -g MyResourceGroup --account-sid sid \\
        --auth-token token --is-validated --phone 1234567890
"""

helps['bot sms delete'] = """
type: command
short-summary: Delete the SMS Channel on a bot
"""

helps['bot sms show'] = """
type: command
short-summary: Get details of the SMS Channel on a bot
"""

helps['bot telegram'] = """
type: group
short-summary: Manage the Telegram Channel on a bot.
"""

helps['bot telegram create'] = """
type: command
short-summary: Create the Telegram Channel on a bot.
examples:
  - name: Create the Telegram Channel for a bot.
    text: |-
        az bot telegram create -n botName -g MyResourceGroup --access-token token
        --is-validated
"""

helps['bot telegram delete'] = """
type: command
short-summary: Delete the Telegram Channel on a bot
"""

helps['bot telegram show'] = """
type: command
short-summary: Get details of the Telegram Channel on a bot
"""

helps['bot update'] = """
type: command
short-summary: Update an existing bot.
examples:
  - name: Update description on a bot
    text: |-
        az bot update -n botName -g MyResourceGroup --endpoint "https://bing.com/api/messages" --display-name "Hello World"
"""

helps['bot webchat'] = """
type: group
short-summary: Manage the Webchat Channel on a bot.
"""

helps['bot webchat show'] = """
type: command
short-summary: Get details of the Webchat Channel on a bot
"""

helps['cache'] = """
type: group
short-summary: Commands to manage CLI objects cached using the `--defer` argument.
"""

helps['cache delete'] = """
type: command
short-summary: Delete an object from the cache.
"""

helps['cache list'] = """
type: command
short-summary: List the contents of the object cache.
"""

helps['cache purge'] = """
type: command
short-summary: Clear the entire CLI object cache.
"""

helps['cache show'] = """
type: command
short-summary: Show the contents of a specific object in the cache.
"""

helps['cdn'] = """
type: group
short-summary: Manage Azure Content Delivery Networks (CDNs).
"""

helps['cdn custom-domain'] = """
type: group
short-summary: Manage Azure CDN Custom Domains to provide custom host names for endpoints.
"""

helps['cdn custom-domain create'] = """
type: command
short-summary: Create a new custom domain to provide a hostname for a CDN endpoint.
long-summary: >
    Creates a new custom domain which must point to the hostname of the endpoint.
    For example, the custom domain hostname cdn.contoso.com would need to have a
    CNAME record pointing to the hostname of the endpoint related to this custom
    domain.
parameters:
  - name: --profile-name
    type: string
    short-summary: Name of the CDN profile which is unique within the resource group.
  - name: --endpoint-name
    type: string
    short-summary: Name of the endpoint under the profile which is unique globally.
  - name: --hostname
    type: string
    short-summary: The host name of the custom domain. Must be a domain name.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az cdn custom-domain create -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name --hostname www.example.com
"""

helps['cdn custom-domain delete'] = """
type: command
short-summary: Delete the custom domain of a CDN.
examples:
  - name: Delete a custom domain.
    text: >
        az cdn custom-domain delete -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name
"""

helps['cdn custom-domain show'] = """
type: command
short-summary: Show details for the custom domain of a CDN.
examples:
  - name: Get the details of a custom domain.
    text: >
        az cdn custom-domain show -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name
"""

helps['cdn edge-node'] = """
type: group
short-summary: View all available CDN edge nodes.
"""

helps['cdn endpoint'] = """
type: group
short-summary: Manage CDN endpoints.
"""

helps['cdn endpoint create'] = """
type: command
short-summary: Create a named endpoint to connect to a CDN.
examples:
  - name: Create an endpoint to service content for hostname over HTTP or HTTPS.
    text: >
        az cdn endpoint create -g group -n endpoint --profile-name profile \\
            --origin www.example.com
  - name: Create an endpoint with a custom domain origin with HTTP and HTTPS ports.
    text: >
        az cdn endpoint create -g group -n endpoint --profile-name profile \\
            --origin www.example.com 88 4444
  - name: Create an endpoint with a custom domain with compression and only HTTPS.
    text: >
        az cdn endpoint create -g group -n endpoint --profile-name profile \\
            --origin www.example.com --no-http --enable-compression
"""

helps['cdn endpoint delete'] = """
type: command
short-summary: Delete a CDN endpoint.
examples:
  - name: Delete a CDN endpoint.
    text: >
        az cdn endpoint delete -g group -n endpoint --profile-name profile-name
"""

helps['cdn endpoint list'] = """
type: command
short-summary: List available endpoints for a CDN.
examples:
  - name: List all endpoints within a given CDN profile.
    text: >
        az cdn endpoint list -g group --profile-name profile-name
"""

helps['cdn endpoint load'] = """
type: command
short-summary: Pre-load content for a CDN endpoint.
examples:
  - name: Pre-load Javascript and CSS content for an endpoint.
    text: >
        az cdn endpoint load -g group -n endpoint --profile-name profile-name --content-paths \\
            '/scripts/app.js' '/styles/main.css'
"""

helps['cdn endpoint purge'] = """
type: command
short-summary: Purge pre-loaded content for a CDN endpoint.
examples:
  - name: Purge pre-loaded Javascript and CSS content.
    text: >
        az cdn endpoint purge -g group -n endpoint --profile-name profile-name --content-paths \\
            '/scripts/app.js' '/styles/*'
"""

helps['cdn endpoint start'] = """
type: command
short-summary: Start a CDN endpoint.
examples:
  - name: Start a CDN endpoint.
    text: >
        az cdn endpoint start -g group -n endpoint --profile-name profile-name
"""

helps['cdn endpoint stop'] = """
type: command
short-summary: Stop a CDN endpoint.
examples:
  - name: Stop a CDN endpoint.
    text: >
        az cdn endpoint stop -g group -n endpoint --profile-name profile-name
"""

helps['cdn endpoint update'] = """
type: command
short-summary: Update a CDN endpoint to manage how content is delivered.
examples:
  - name: Turn off HTTP traffic for an endpoint.
    text: >
        az cdn endpoint update -g group -n endpoint --profile-name profile --no-http
  - name: Enable content compression for an endpoint.
    text: >
        az cdn endpoint update -g group -n endpoint --profile-name profile \\
            --enable-compression
"""

helps['cdn origin'] = """
type: group
short-summary: List or show existing origins related to CDN endpoints.
"""

helps['cdn profile'] = """
type: group
short-summary: Manage CDN profiles to define an edge network.
"""

helps['cdn profile create'] = """
type: command
short-summary: Create a new CDN profile.
parameters:
  - name: --sku
    type: string
    short-summary: >
        The pricing tier (defines a CDN provider, feature list and rate) of the CDN profile.
        Defaults to Standard_Akamai.
examples:
  - name: Create a CDN profile using Verizon premium CDN.
    text: >
        az cdn profile create -g group -n profile --sku Premium_Verizon
  - name: Create a new CDN profile. (autogenerated)
    text: az cdn profile create --location westus2 --name profile --resource-group group --sku Standard_Verizon
    crafted: true
"""

helps['cdn profile delete'] = """
type: command
short-summary: Delete a CDN profile.
examples:
  - name: Delete a CDN profile.
    text: >
        az cdn profile delete -g group -n profile
"""

helps['cdn profile list'] = """
type: command
short-summary: List CDN profiles.
examples:
  - name: List CDN profiles in a resource group.
    text: >
        az cdn profile list -g group
"""

helps['cdn profile update'] = """
type: command
short-summary: Update a CDN profile.
"""

helps['cloud'] = """
type: group
short-summary: Manage registered Azure clouds.
"""

helps['cloud list'] = """
type: command
short-summary: List registered clouds.
"""

helps['cloud list-profiles'] = """
type: command
short-summary: List the supported profiles for a cloud.
"""

helps['cloud register'] = """
type: command
short-summary: Register a cloud.
long-summary: When registering a cloud, specify only the resource manager endpoint for the autodetection of other endpoints.
"""

helps['cloud set'] = """
type: command
short-summary: Set the active cloud.
"""

helps['cloud show'] = """
type: command
short-summary: Get the details of a registered cloud.
"""

helps['cloud unregister'] = """
type: command
short-summary: Unregister a cloud.
"""

helps['cloud update'] = """
type: command
short-summary: Update the configuration of a cloud.
"""

helps['cognitiveservices'] = """
type: group
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
"""

helps['cognitiveservices account'] = """
type: group
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
"""

helps['cognitiveservices account create'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
parameters:
  - name: --kind
    populator-commands:
      - az cognitiveservices account list-kinds
  - name: --sku
    populator-commands:
      - az cognitiveservices account list-skus
examples:
  - name: Create an S0 face API Cognitive Services account in West Europe without confirmation required.
    text: az cognitiveservices account create -n myresource -g myResourceGroup --kind Face --sku S0 -l WestEurope --yes
"""

helps['cognitiveservices account delete'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
examples:
  - name: Delete account.
    text: az cognitiveservices account delete --name myresource-luis -g cognitive-services-resource-group
"""

helps['cognitiveservices account keys'] = """
type: group
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
"""

helps['cognitiveservices account keys list'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
examples:
  - name: Get current resource keys.
    text: az cognitiveservices account keys list --name myresource -g cognitive-services-resource-group
"""

helps['cognitiveservices account keys regenerate'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
examples:
  - name: Get new keys for resource.
    text: az cognitiveservices account keys regenerate --name myresource -g cognitive-services-resource-group --key-name key1
"""

helps['cognitiveservices account list'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
examples:
  - name: List all the Cognitive Services accounts in a resource group.
    text: az cognitiveservices account list -g MyResourceGroup
"""

helps['cognitiveservices account list-skus'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
parameters:
  - name: --name -n
    long-summary: |
        --kind and --location will be ignored when --name is specified.
        --resource-group is required when when --name is specified.
  - name: --resource-group -g
    long-summary: |
        --resource-group is used when when --name is specified. In other cases it will be ignored.
  - name: --kind
    populator-commands:
      - az cognitiveservices account list-kinds
examples:
  - name: Show SKUs.
    text: az cognitiveservices account list-skus --kind Face --location westus
"""

helps['cognitiveservices account network-rule'] = """
type: group
short-summary: Manage network rules.
"""

helps['cognitiveservices account network-rule add'] = """
type: command
short-summary: Add a network rule.
long-summary: >
    Rules can be created for an IPv4 address, address range (CIDR format), or a virtual network subnet.
examples:
  - name: Create a rule to allow a specific address-range.
    text: az cognitiveservices account network-rule add -g myRg --name MyAccount --ip-address 23.45.1.0/24
  - name: Create a rule to allow access for a subnet.
    text: az cognitiveservices account network-rule add -g myRg --name MyAccount --vnet myvnet --subnet mysubnet
"""

helps['cognitiveservices account network-rule list'] = """
type: command
short-summary: List network rules.
examples:
  - name: List network rules.
    text: az cognitiveservices account network-rule list --name MyAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cognitiveservices account network-rule remove'] = """
type: command
short-summary: Remove a network rule.
examples:
  - name: Remove a network rule.
    text: az cognitiveservices account network-rule remove --name MyAccount --resource-group MyResourceGroup --subnet mysubnet
    crafted: true
  - name: Remove a network rule.
    text: az cognitiveservices account network-rule remove --name MyAccount --ip-address 23.45.1.0/24 --resource-group MyResourceGroup
    crafted: true
"""

helps['cognitiveservices account show'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
examples:
  - name: Show account information.
    text: az cognitiveservices account show --name myresource --resource-group cognitive-services-resource-group
"""

helps['cognitiveservices account update'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
parameters:
  - name: --sku
    populator-commands:
      - az cognitiveservices account list-skus
examples:
  - name: Update sku and tags.
    text: az cognitiveservices account update --name myresource -g cognitive-services-resource-group --sku S0 --tags external-app=chatbot-HR azure-web-app-bot=HR-external azure-app-service=HR-external-app-service
"""

helps['cognitiveservices list'] = """
type: command
short-summary: Manage Azure Cognitive Services accounts.
long-summary: This article lists the Azure CLI commands for Azure Cognitive Services account and subscription management only. Refer to the documentation at https://docs.microsoft.com/azure/cognitive-services/ for individual services to learn how to use the APIs and supported SDKs.
examples:
  - name: List all the Cognitive Services accounts in a resource group.
    text: az cognitiveservices list -g MyResourceGroup
"""

helps['configure'] = """
type: command
short-summary: Manage Azure CLI configuration. This command is interactive.
parameters:
  - name: --defaults -d
    short-summary: >
        Space-separated 'name=value' pairs for common argument defaults.
examples:
  - name: Set default resource group, webapp and VM names.
    text: az configure --defaults group=myRG web=myweb vm=myvm
  - name: Clear default webapp and VM names.
    text: az configure --defaults vm='' web=''
"""

helps['consumption'] = """
type: group
short-summary: Manage consumption of Azure resources.
"""

helps['consumption budget'] = """
type: group
short-summary: Manage budgets for an Azure subscription.
"""

helps['consumption budget create'] = """
type: command
short-summary: Create a budget for an Azure subscription.
"""

helps['consumption budget delete'] = """
type: command
short-summary: Delete a budget for an Azure subscription.
"""

helps['consumption budget list'] = """
type: command
short-summary: List budgets for an Azure subscription.
"""

helps['consumption budget show'] = """
type: command
short-summary: Show budget for an Azure subscription.
"""

helps['consumption marketplace'] = """
type: group
short-summary: Inspect the marketplace usage data of an Azure subscription within a billing period.
"""

helps['consumption marketplace list'] = """
type: command
short-summary: List the marketplace for an Azure subscription within a billing period.
"""

helps['consumption pricesheet'] = """
type: group
short-summary: Inspect the price sheet of an Azure subscription within a billing period.
"""

helps['consumption pricesheet show'] = """
type: command
short-summary: Show the price sheet for an Azure subscription within a billing period.
"""

helps['consumption reservation'] = """
type: group
short-summary: Manage reservations for Azure resources.
"""

helps['consumption reservation detail'] = """
type: group
short-summary: List reservation details.
"""

helps['consumption reservation detail list'] = """
type: command
short-summary: List the details of a reservation by order id or reservation id.
"""

helps['consumption reservation summary'] = """
type: group
short-summary: List reservation summaries.
"""

helps['consumption reservation summary list'] = """
type: command
short-summary: List reservation summaries for daily or monthly by order Id or reservation id.
"""

helps['consumption usage'] = """
type: group
short-summary: Inspect the usage of Azure resources.
"""

helps['consumption usage list'] = """
type: command
short-summary: List the details of Azure resource consumption, either as an invoice or within a billing period.
"""

helps['container'] = """
type: group
short-summary: Manage Azure Container Instances.
"""

helps['container attach'] = """
type: command
short-summary: Attach local standard output and error streams to a container in a container group.
"""

helps['container create'] = """
type: command
short-summary: Create a container group.
examples:
  - name: Create a container in a container group with 1 core and 1Gb of memory.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --cpu 1 --memory 1
  - name: Create a container in a container group that runs Windows, with 2 cores and 3.5Gb of memory.
    text: az container create -g MyResourceGroup --name mywinapp --image winappimage:latest --os-type Windows --cpu 2 --memory 3.5
  - name: Create a container in a container group with public IP address, ports and DNS name label.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --ports 80 443 --dns-name-label contoso
  - name: Create a container in a container group that invokes a script upon start.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --command-line "/bin/sh -c '/path to/myscript.sh'"
  - name: Create a container in a container group that runs a command and stop the container afterwards.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --command-line "echo hello" --restart-policy Never
  - name: Create a container in a container group with environment variables.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --environment-variables key1=value1 key2=value2
  - name: Create a container in a container group using container image from Azure Container Registry.
    text: az container create -g MyResourceGroup --name myapp --image myAcrRegistry.azurecr.io/myimage:latest --registry-password password
  - name: Create a container in a container group that mounts an Azure File share as volume.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --command-line "cat /mnt/azfile/myfile" --azure-file-volume-share-name myshare --azure-file-volume-account-name mystorageaccount --azure-file-volume-account-key mystoragekey --azure-file-volume-mount-path /mnt/azfile
  - name: Create a container in a container group that mounts a git repo as volume.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --command-line "cat /mnt/gitrepo" --gitrepo-url https://github.com/user/myrepo.git --gitrepo-dir ./dir1 --gitrepo-mount-path /mnt/gitrepo
  - name: Create a container in a container group using a yaml file.
    text: az container create -g MyResourceGroup -f containerGroup.yaml
  - name: Create a container group using Log Analytics from a workspace name.
    text: az container create -g MyResourceGroup --name myapp --log-analytics-workspace myworkspace
  - name: Create a container group with a system assigned identity.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --assign-identity
  - name: Create a container group with a system assigned identity. The group will have a 'Contributor' role with access to a storage account.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --assign-identity --scope /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/MyResourceGroup/myRG/providers/Microsoft.Storage/storageAccounts/storage1
  - name: Create a container group with a user assigned identity.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --assign-identity  /subscriptions/mySubscrpitionId/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
  - name: Create a container group with both system and user assigned identity.
    text: az container create -g MyResourceGroup --name myapp --image myimage:latest --assign-identity [system] /subscriptions/mySubscrpitionId/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
    supported-profiles: latest
"""

helps['container delete'] = """
type: command
short-summary: Delete a container group.
"""

helps['container exec'] = """
type: command
short-summary: Execute a command from within a running container of a container group.
long-summary: The most common use case is to open an interactive bash shell. See examples below. This command is currently not supported for Windows machines.
examples:
  - name: Stream a shell from within an nginx container.
    text: az container exec -g MyResourceGroup --name mynginx --container-name nginx --exec-command "/bin/bash"
"""

helps['container export'] = """
type: command
short-summary: Export a container group in yaml format.
examples:
  - name: Export a container group in yaml.
    text: az container export -g MyResourceGroup --name mynginx -f output.yaml
"""

helps['container list'] = """
type: command
short-summary: List container groups.
"""

helps['container logs'] = """
type: command
short-summary: Examine the logs for a container in a container group.
"""

helps['container show'] = """
type: command
short-summary: Get the details of a container group.
"""

helps['cosmosdb'] = """
type: group
short-summary: Manage Azure Cosmos DB database accounts.
"""

helps['cosmosdb cassandra'] = """
type: group
short-summary: Manage Cassandra resources of Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace'] = """
type: group
short-summary: Manage Azure Cosmos DB Cassandra keyspaces.
"""

helps['cosmosdb cassandra keyspace create'] = """
type: command
short-summary: Create an Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace delete'] = """
type: command
short-summary: Delete the Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace list'] = """
type: command
short-summary: List the Cassandra keyspaces under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace show'] = """
type: command
short-summary: Show the details of a Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace throughput'] = """
type: group
short-summary: Manage throughput of Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace throughput show'] = """
type: command
short-summary: Get the throughput of the Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace throughput update'] = """
type: command
short-summary: Update the throughput of the Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra table'] = """
type: group
short-summary: Manage Azure Cosmos DB Cassandra tables.
"""

helps['cosmosdb cassandra table create'] = """
type: command
short-summary: Create an Cassandra table under an Azure Cosmos DB Cassandra keyspace.
examples:
  - name: Create an Azure Cosmos DB Cassandra table.
    text: az cosmosdb cassandra table create -g MyResourceGroup -a MyAccount -k MyKeyspace -n MyTable --schema @indexes-file.json --throughput "500" --ttl 1000
    crafted: true
"""

helps['cosmosdb cassandra table delete'] = """
type: command
short-summary: Delete the Cassandra table under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb cassandra table list'] = """
type: command
short-summary: List the Cassandra tables under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb cassandra table show'] = """
type: command
short-summary: Show the details of a Cassandra table under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb cassandra table throughput'] = """
type: group
short-summary: Manage throughput of Cassandra table under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra table throughput show'] = """
type: command
short-summary: Get the throughput of the Cassandra table under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb cassandra table throughput update'] = """
type: command
short-summary: Update the throughput of the Cassandra table under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb cassandra table update'] = """
type: command
short-summary: Update an Cassandra table under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb check-name-exists'] = """
type: command
short-summary: Checks if an Azure Cosmos DB account name exists.
examples:
  - name: Checks if an Azure Cosmos DB account name exists. (autogenerated)
    text: az cosmosdb check-name-exists --name MyCosmosDBDatabaseAccount
    crafted: true
"""

helps['cosmosdb collection'] = """
type: group
short-summary: Manage Azure Cosmos DB collections.
"""

helps['cosmosdb create'] = """
type: command
short-summary: Creates a new Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations KEY=VALUE [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
examples:
  - name: Creates a new Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb create --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
  - name: Creates a new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb create -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
"""

helps['cosmosdb database'] = """
type: group
short-summary: Manage Azure Cosmos DB databases.
"""

helps['cosmosdb database create'] = """
type: command
short-summary: Creates an Azure Cosmos DB database
examples:
  - name: Creates an Azure Cosmos DB database.
    text: az cosmosdb database create --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --db-name MyDatabase
    crafted: true
"""

helps['cosmosdb database delete'] = """
type: command
short-summary: Deletes an Azure Cosmos DB database
examples:
  - name: Deletes an Azure Cosmos DB database.
    text: az cosmosdb database delete --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --db-name MyDatabase
    crafted: true
"""

helps['cosmosdb database exists'] = """
type: command
short-summary: Returns a boolean indicating whether the database exists
examples:
  - name: Returns a boolean indicating whether the database exists.
    text: az cosmosdb database exists --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --db-name MyDatabase
    crafted: true
"""

helps['cosmosdb database list'] = """
type: command
short-summary: Lists all Azure Cosmos DB databases
examples:
  - name: Lists all Azure Cosmos DB databases.
    text: az cosmosdb database list --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb database show'] = """
type: command
short-summary: Shows an Azure Cosmos DB database
examples:
  - name: Shows an Azure Cosmos DB database.
    text: az cosmosdb database show --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --db-name MyDatabase
    crafted: true
"""

helps['cosmosdb delete'] = """
type: command
short-summary: Deletes an Azure Cosmos DB database account.
examples:
  - name: Deletes an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb delete --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb failover-priority-change'] = """
type: command
short-summary: Changes the failover priority for the Azure Cosmos DB database account.
examples:
  - name: Changes the failover priority for the Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb failover-priority-change --failover-policies regionName=failoverPriority --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb gremlin'] = """
type: group
short-summary: Manage Gremlin resources of Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database'] = """
type: group
short-summary: Manage Azure Cosmos DB Gremlin databases.
"""

helps['cosmosdb gremlin database create'] = """
type: command
short-summary: Create an Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database delete'] = """
type: command
short-summary: Delete the Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database list'] = """
type: command
short-summary: List the Gremlin databases under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database show'] = """
type: command
short-summary: Show the details of a Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database throughput'] = """
type: group
short-summary: Manage throughput of Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database throughput show'] = """
type: command
short-summary: Get the throughput of the Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database throughput update'] = """
type: command
short-summary: Update the throughput of the Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin graph'] = """
type: group
short-summary: Manage Azure Cosmos DB Gremlin graphs.
"""

helps['cosmosdb gremlin graph create'] = """
type: command
short-summary: Create an Gremlin graph under an Azure Cosmos DB Gremlin database.
examples:
  - name: Create an Azure Cosmos DB Gremlin graph.
    text: az cosmosdb gremlin graph create -g MyResourceGroup -a MyAccount -d MyDatabase -n MyGraph --part "/my/path" --idx @policy-file.json --ttl 1000 --throughput "700"
    crafted: true
"""

helps['cosmosdb gremlin graph delete'] = """
type: command
short-summary: Delete the Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph list'] = """
type: command
short-summary: List the Gremlin graphs under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph show'] = """
type: command
short-summary: Show the details of a Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph throughput'] = """
type: group
short-summary: Manage throughput of Gremlin graph under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin graph throughput show'] = """
type: command
short-summary: Get the throughput of the Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph throughput update'] = """
type: command
short-summary: Update the throughput of the Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph update'] = """
type: command
short-summary: Update an Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb keys'] = """
type: group
short-summary: Manage Azure Comsos DB keys.
"""

helps['cosmosdb keys list'] = """
type: command
short-summary: List the access keys for a Azure Cosmos DB database account.
examples:
  - name: List the access keys for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb keys list --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['cosmosdb list'] = """
type: command
short-summary: List Azure Cosmos DB database accounts.
"""

helps['cosmosdb list-connection-strings'] = """
type: command
short-summary: List the connection strings for a Azure Cosmos DB database account.
examples:
  - name: List the connection strings for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-connection-strings --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb list-keys'] = """
type: command
short-summary: List the access keys for a Azure Cosmos DB database account.
examples:
  - name: List the access keys for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-keys --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['cosmosdb list-read-only-keys'] = """
type: command
short-summary: List the read-only access keys for a Azure Cosmos DB database account.
examples:
  - name: List the read-only access keys for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-read-only-keys --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb mongodb'] = """
type: group
short-summary: Manage MongoDB resources of Azure Cosmos DB account.
"""

helps['cosmosdb mongodb collection'] = """
type: group
short-summary: Manage Azure Cosmos DB MongoDB collections.
"""

helps['cosmosdb mongodb collection create'] = """
type: command
short-summary: Create an MongoDB collection under an Azure Cosmos DB MongoDB database.
examples:
  - name: Create an Azure Cosmos DB MongoDB collection.
    text: az cosmosdb mongodb collection create -g MyResourceGroup -a MyAccount -d MyDatabase -n MyCollection --shard "ShardingKey" --idx @indexes-file.json --throughput "500"
    crafted: true
"""

helps['cosmosdb mongodb collection delete'] = """
type: command
short-summary: Delete the MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection list'] = """
type: command
short-summary: List the MongoDB collections under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection show'] = """
type: command
short-summary: Show the details of a MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection throughput'] = """
type: group
short-summary: Manage throughput of MongoDB collection under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb collection throughput show'] = """
type: command
short-summary: Get the throughput of the MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection throughput update'] = """
type: command
short-summary: Update the throughput of the MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection update'] = """
type: command
short-summary: Update an MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb database'] = """
type: group
short-summary: Manage Azure Cosmos DB MongoDB databases.
"""

helps['cosmosdb mongodb database create'] = """
type: command
short-summary: Create an MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database delete'] = """
type: command
short-summary: Delete the MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database list'] = """
type: command
short-summary: List the MongoDB databases under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database show'] = """
type: command
short-summary: Show the details of a MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database throughput'] = """
type: group
short-summary: Manage throughput of MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database throughput show'] = """
type: command
short-summary: Get the throughput of the MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database throughput update'] = """
type: command
short-summary: Update the throughput of the MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb network-rule'] = """
type: group
short-summary: Manage Azure Comsos DB network rules.
"""

helps['cosmosdb regenerate-key'] = """
type: command
short-summary: Regenerate an access key for a Azure Cosmos DB database account.
examples:
  - name: Regenerate an access key for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb regenerate-key --key-kind primary --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb show'] = """
type: command
short-summary: Get the details of an Azure Cosmos DB database account.
examples:
  - name: Get the details of an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb show --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb sql'] = """
type: group
short-summary: Manage SQL resources of Azure Cosmos DB account.
"""

helps['cosmosdb sql container'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL containers.
"""

helps['cosmosdb sql container create'] = """
type: command
short-summary: Create an SQL container under an Azure Cosmos DB SQL database.
examples:
  - name: Create an Azure Cosmos DB SQL container.
    text: az cosmosdb sql container create -g MyResourceGroup -a MyAccount -d MyDatabase -n MyContainer --part "/my/path" --idx @policy-file.json --ttl 1000 --throughput "700"
    crafted: true
"""

helps['cosmosdb sql container delete'] = """
type: command
short-summary: Delete the SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container list'] = """
type: command
short-summary: List the SQL containers under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container show'] = """
type: command
short-summary: Show the details of a SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container throughput'] = """
type: group
short-summary: Manage throughput of SQL container under an Azure Cosmos DB account.
"""

helps['cosmosdb sql container throughput show'] = """
type: command
short-summary: Get the throughput of the SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container throughput update'] = """
type: command
short-summary: Update the throughput of the SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container update'] = """
type: command
short-summary: Update an SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql database'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL databases.
"""

helps['cosmosdb sql database create'] = """
type: command
short-summary: Create an SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database delete'] = """
type: command
short-summary: Delete the SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database list'] = """
type: command
short-summary: List the SQL databases under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database show'] = """
type: command
short-summary: Show the details of a SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database throughput'] = """
type: group
short-summary: Manage throughput of SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database throughput show'] = """
type: command
short-summary: Get the throughput of the SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database throughput update'] = """
type: command
short-summary: Update the throughput of the SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb table'] = """
type: group
short-summary: Manage Table resources of Azure Cosmos DB account.
"""

helps['cosmosdb table create'] = """
type: command
short-summary: Create an Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table delete'] = """
type: command
short-summary: Delete the Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table list'] = """
type: command
short-summary: List the Tables under an Azure Cosmos DB account.
"""

helps['cosmosdb table show'] = """
type: command
short-summary: Show the details of a Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table throughput'] = """
type: group
short-summary: Manage throughput of Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table throughput show'] = """
type: command
short-summary: Get the throughput of the Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table throughput update'] = """
type: command
short-summary: Update the throughput of the Table under an Azure Cosmos DB account.
"""

helps['cosmosdb update'] = """
type: command
short-summary: Update an Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations KEY=VALUE [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
examples:
  - name: Update an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb update --capabilities EnableGremlin --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
  - name: Creates a new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb update -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
"""

helps['deployment'] = """
type: group
short-summary: Manage Azure Resource Manager deployments at subscription scope.
"""

helps['deployment create'] = """
type: command
short-summary: Start a deployment.
parameters:
  - name: --parameters
    short-summary: Supply deployment parameter values.
    long-summary: >
        Parameters may be supplied from a file using the `@{path}` syntax, a JSON string, or as <KEY=VALUE> pairs. Parameters are evaluated in order, so when a value is assigned twice, the latter value will be used.
        It is recommended that you supply your parameters file first, and then override selectively using KEY=VALUE syntax.
examples:
  - name: Create a deployment from a remote template file, using parameters from a local JSON file.
    text: >
        az deployment create --location WestUS --template-uri https://myresource/azuredeploy.json --parameters @myparameters.json
  - name: Create a deployment from a local template file, using parameters from a JSON string.
    text: |
        az deployment create --location WestUS --template-file azuredeploy.json --parameters '{
                "policyName": {
                    "value": "policy2"
                }
            }'
  - name: Create a deployment from a local template, using a parameter file, a remote parameter file, and selectively overriding key/value pairs.
    text: >
        az deployment create --location WestUS --template-file azuredeploy.json  \\
            --parameters @params.json --parameters https://mysite/params.json --parameters MyValue=This MyArray=@array.json
"""

helps['deployment export'] = """
type: command
short-summary: Export the template used for a deployment.
examples:
  - name: Export the template used for a deployment. (autogenerated)
    text: az deployment export --name MyDeployment
    crafted: true
"""

helps['deployment operation'] = """
type: group
short-summary: Manage deployment operations.
"""

helps['deployment validate'] = """
type: command
short-summary: Validate whether a template is syntactically correct.
parameters:
  - name: --parameters
    short-summary: Supply deployment parameter values.
    long-summary: >
        Parameters may be supplied from a file using the `@{path}` syntax, a JSON string, or as <KEY=VALUE> pairs. Parameters are evaluated in order, so when a value is assigned twice, the latter value will be used.
        It is recommended that you supply your parameters file first, and then override selectively using KEY=VALUE syntax.
examples:
  - name: Validate whether a template is syntactically correct. (autogenerated)
    text: az deployment validate --location westus2 --template-file {template-file}
    crafted: true
"""

helps['deployment wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a deployment condition is met.
"""

helps['deploymentmanager'] = """
type: group
short-summary: Create and manage rollouts for your service.
long-summary: To deploy your service across many regions and make sure it is running as expected in each region, you can use deployment manager to coordinate a staged rollout of the service. For more details, visit https://docs.microsoft.com/azure/azure-resource-manager/deployment-manager-overview
"""

helps['deploymentmanager artifact-source'] = """
type: group
short-summary: Manage artifact sources.
long-summary: Artifact sources can be used for creating service topologies and rollouts.
"""

helps['deploymentmanager artifact-source create'] = """
type: command
short-summary: Creates an artifact source.
examples:
  - name: Create a new artifact source.
    text: az deploymentmanager artifact-source create -g rg1 -n contosoServiceArtifactSource -l location --sas-uri https://myStorageAct.blob.azure.com/artifacts?st=2019-04-10T22%3A12Z&se=2019-04-11T09%3A12Z&sp=rl&sv=2018-03-28&sr=c&sig=f6Nx8en4sIJQryYFVVj%2B5BdU7bho96jAgOzLO40Twkg%3D
"""

helps['deploymentmanager artifact-source delete'] = """
type: command
short-summary: Deletes an artifact source.
examples:
  - name: Deletes an artifact source
    text: >
        az deploymentmanager artifact-source delete -g rg1 -n contosoServiceArtifactSource
"""

helps['deploymentmanager artifact-source show'] = """
type: command
short-summary: Get the details of an artifact source.
examples:
  - name: Get an artifact source
    text: >
        az deploymentmanager artifact-source show -g rg1 -n contosoServiceArtifactSource
"""

helps['deploymentmanager artifact-source update'] = """
type: command
short-summary: Updates an artifact source.
examples:
  - name: Updates an artifact source
    text: >
        az deploymentmanager artifact-source update -g rg1 -n contosoServiceArtifactSource --sas-uri https://dummy.blob.azure.com/updated_sample_sas_uri
"""

helps['deploymentmanager rollout'] = """
type: group
short-summary: Manage the rollouts.
long-summary: View progress, restart a failed rollout, stop a running rollout. Rollouts can be created using the 'az group deployment' command.
"""

helps['deploymentmanager rollout restart'] = """
type: command
short-summary: Restarts the rollout.
examples:
  - name: Restart the rollout
    text: >
        az deploymentmanager rollout restart -g rg1 -n contosoServiceRollout

  - name: Restart the rollout and skip all steps that have succeeded in the previous run
    text: >
        az deploymentmanager rollout restart -g rg1 -n contosoServiceRollout --skip-succeeded
"""

helps['deploymentmanager rollout show'] = """
type: command
short-summary: Gets the rollout.
examples:
  - name: Gets the rollout
    text: >
        az deploymentmanager rollout show -g rg1 -n contosoServiceRollout
  - name: Gets the specific retry attempt of a rollout. Shows the steps run during that attempt.
    text: >
        az deploymentmanager rollout show -g rg1 -n contosoServiceRollout --retry-attempt 1
"""

helps['deploymentmanager rollout stop'] = """
type: command
short-summary: Stop the rollout.
examples:
  - name: Stops the rollout
    text: >
        az deploymentmanager rollout stop -g rg1 -n contosoServiceRollout
"""

helps['deploymentmanager service'] = """
type: group
short-summary: Manage the services in a service topology.
"""

helps['deploymentmanager service create'] = """
type: command
short-summary: Creates a service under the specified service topology.
examples:
  - name: Create a new service under a service topology. Specify the service by its name, service topology it is in and the resource group name.
    text: >
        az deploymentmanager service create -g rg1 -l serviceLocation --service-topology-name contosoServiceTopology -n contosoService1 --target-location "East US" --target-subscription-id XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
"""

helps['deploymentmanager service delete'] = """
type: command
short-summary: Deletes the service topology.
examples:
  - name: Deletes a service topology.
    text: >
        az deploymentmanager service delete -g rg1 --service-topology-name contosoServiceTopology -n contosoService1
"""

helps['deploymentmanager service show'] = """
type: command
short-summary: Get the details of a service.
examples:
  - name: Get the service under a service topology.
    text: >
        az deploymentmanager service show -g rg1 --service-topology-name contosoServiceTopology -n contosoService1
"""

helps['deploymentmanager service update'] = """
type: command
short-summary: Updates the service.
examples:
  - name: Updates the service.
    text: >
        az deploymentmanager service update -g rg1 --service-topology-name contosoServiceTopology -n contosoService1 --target-location "West US" --target-subscription-id XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
"""

helps['deploymentmanager service-topology'] = """
type: group
short-summary: Manage service topologies.
"""

helps['deploymentmanager service-topology create'] = """
type: command
short-summary: Creates a service topology.
examples:
  - name: Create a new service topology.
    text: >
        az deploymentmanager service-topology create -g rg1 -l topologyLocation -n contosoServiceTopology --artifact-source /subscriptions/mySub/resourcegroups/rg1/providers/Microsoft.DeploymentManager/artifactSources/contosoWebAppArtifactSource
"""

helps['deploymentmanager service-topology delete'] = """
type: command
short-summary: Deletes the service topology.
examples:
  - name: Deletes a service topology.
    text: >
        az deploymentmanager service-topology delete -g rg1 -n contosoServiceTopology
"""

helps['deploymentmanager service-topology show'] = """
type: command
short-summary: Get the details of a service topology.
examples:
  - name: Get the service topology.
    text: >
        az deploymentmanager service-topology show -g rg1 -n contosoServiceTopology
"""

helps['deploymentmanager service-topology update'] = """
type: command
short-summary: Updates the service topology.
examples:
  - name: Updates the service topology.
    text: >
        az deploymentmanager service-topology update -g rg1 -n contosoServiceTopology --artifact-source /subscriptions/mySub/resourcegroups/rg1/providers/Microsoft.DeploymentManager/artifactSources/contosoWebAppArtifactSource
"""

helps['deploymentmanager service-unit'] = """
type: group
short-summary: Manage the service units.
long-summary: Service units combine to form a service in a service topology.
"""

helps['deploymentmanager service-unit create'] = """
type: command
short-summary: Creates a service unit under the specified service and service topology.
examples:
  - name: Create a new service unit using relative paths into the artifact source.
    description: Specify the service unit by its name, the service and service topology it is in. The template and parameters files are defined as relative paths into the artifact source location referenced in the specified service topology. The resources defined in this template are to be deployed into the target resource group service1ResourceGroup with the deployment mode set to 'Incremental'.
    text: >
        az deploymentmanager service-unit create -g rg1 -l location --service-topology-name contosoServiceTopology --service-name contosoService1 -n ContosoService1Storage --target-resource-group service1ResourceGroup --deployment-mode Incremental --template-path "Templates/Service1.Storage.json" --parameters-path "Parameters/Service1.Storage.Parameters.json"
  - name: Create a new service unit using SAS Uri for template and parameters.
    description: Specify the service unit by its name, the service and service topology it is in. The template and parameters files are defined as SAS Uri's. The resources defined in this template are to be deployed into the target resource group service1ResourceGroup with the deployment mode set to 'Incremental'.
    text: >
        az deploymentmanager service-unit create -g rg1 -l location --service-topology-name contosoServiceTopology --service-name contosoService1 -n ContosoService1Storage \\
            --target-resource-group service1ResourceGroup --deployment-mode Incremental \\
            --template-path "https://ContosoStorage.blob.core.windows.net/ContosoArtifacts/Templates/Service2.Storage.json?sasParameters" \\
            --parameters-path "https://ContosoStorage.blob.core.windows.net/ContosoArtifacts/Parameters/Service2Storage.Parameters.json?sasParameters"
"""

helps['deploymentmanager service-unit delete'] = """
type: command
short-summary: Deletes the service unit.
examples:
  - name: Deletes a service unit.
    text: >
        az deploymentmanager service-unit delete -g rg1 --service-topology-name contosoServiceTopology --service-name contosoService1 -n ContosoService1Storage
"""

helps['deploymentmanager service-unit show'] = """
type: command
short-summary: Get the details of a service unit.
examples:
  - name: Get the service unit.
    text: >
        az deploymentmanager service-unit show -g rg1 --service-topology-name contosoServiceTopology --service-name contosoService1 -n ContosoService1Storage
"""

helps['deploymentmanager service-unit update'] = """
type: command
short-summary: Updates the service unit.
examples:
  - name: Updates the service unit.
    text: >
        az deploymentmanager service-unit update -g rg1 --service-topology-name contosoServiceTopology --service-name contosoService1 -n ContosoService1Storage --target-resource-group service1ResourceGroupUpdated
"""

helps['deploymentmanager step'] = """
type: group
short-summary: Manage the steps.
long-summary: Allows you to manage the steps that can be used in rollouts.
"""

helps['deploymentmanager step create'] = """
type: command
short-summary: Creates the step.
examples:
  - name: Creates a step.
    text: >
        az deploymentmanager step create -g rg1 -l location -n contosoServiceWaitStep --duration PT30M
"""

helps['deploymentmanager step show'] = """
type: command
short-summary: Get the details of the step.
examples:
  - name: Get the step.
    text: >
        az deploymentmanager step show -g rg1 -n contosoServiceWaitStep
"""

helps['deploymentmanager step update'] = """
type: command
short-summary: Updates the step.
examples:
  - name: Updates a step.
    text: >
        az deploymentmanager step update -g rg1 -n contosoServiceWaitStep --duration PT20M
"""

helps['disk'] = """
type: group
short-summary: Manage Azure Managed Disks.
long-summary: >4

    Azure Virtual Machines use disks as a place to store an operating system, applications, and data.
    All Azure virtual machines have at least two disks: An operating system disk, and a temporary disk.
    The operating system disk is created from an image, and both the operating system disk and the image are actually virtual hard disks (VHDs)
    stored in an Azure storage account. Virtual machines also can have one or more data disks, that are also stored as VHDs.


    Azure Managed and Unmanaged Data Disks have a maximum size of 4095 GB (with the exception of larger disks in preview). Azure Unmanaged Disks also have a maximum capacity of 4095 GB.


    For more information, see:

    - Azure Disks - https://docs.microsoft.com/azure/virtual-machines/linux/about-disks-and-vhds and https://docs.microsoft.com/azure/virtual-machines/windows/about-disks-and-vhds.

    - Larger Managed Disks in Public Preview - https://azure.microsoft.com/blog/introducing-the-public-preview-of-larger-managed-disks-sizes/

    - Ultra SSD Managed Disks in Public Preview - https://docs.microsoft.com/azure/virtual-machines/windows/disks-ultra-ssd


"""

helps['disk create'] = """
type: command
short-summary: Create a managed disk.
examples:
  - name: Create a managed disk by importing from a blob uri.
    text: >
        az disk create -g MyResourceGroup -n MyDisk --source https://vhd1234.blob.core.windows.net/vhds/osdisk1234.vhd
  - name: Create an empty managed disk.
    text: >
        az disk create -g MyResourceGroup -n MyDisk --size-gb 10
  - name: Create a managed disk by copying an existing disk or snapshot.
    text: >
        az disk create -g MyResourceGroup -n MyDisk2 --source MyDisk
  - name: Create a disk in an availability zone in the region of "East US 2"
    text: >
        az disk create -n MyDisk -g MyResourceGroup --size-gb 10 --location eastus2 --zone 1
"""

helps['disk delete'] = """
type: command
short-summary: Delete a managed disk.
examples:
  - name: Delete a managed disk. (autogenerated)
    text: az disk delete --name MyManagedDisk --resource-group MyResourceGroup
    crafted: true
"""

helps['disk grant-access'] = """
type: command
short-summary: Grant a resource access to a managed disk.
examples:
  - name: Grant a resource read access to a managed disk. (autogenerated)
    text: az disk grant-access --duration-in-seconds 3600 --name MyManagedDisk --resource-group MyResourceGroup
    crafted: true
"""

helps['disk list'] = """
type: command
short-summary: List managed disks.
"""

helps['disk revoke-access'] = """
type: command
short-summary: Revoke a resource's read access to a managed disk.
examples:
  - name: Revoke a resource's read access to a managed disk. (autogenerated)
    text: az disk revoke-access --ids $id
    crafted: true
"""

helps['disk update'] = """
type: command
short-summary: Update a managed disk.
examples:
  - name: Update a managed disk. (autogenerated)
    text: az disk update --name MyManagedDisk --resource-group MyResourceGroup --size-gb 20
    crafted: true
"""

helps['disk wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a managed disk is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a managed disk is met. (autogenerated)
    text: az disk wait --created --name MyManagedDisk --resource-group MyResourceGroup
    crafted: true
"""

helps['dla'] = """
type: group
short-summary: Manage Data Lake Analytics accounts, jobs, and catalogs.
"""

helps['dla account'] = """
type: group
short-summary: Manage Data Lake Analytics accounts.
"""

helps['dla account blob-storage'] = """
type: group
short-summary: Manage links between Data Lake Analytics accounts and Azure Storage.
"""

helps['dla account blob-storage add'] = """
type: command
short-summary: Links an Azure Storage account to the specified Data Lake Analytics account.
"""

helps['dla account blob-storage update'] = """
type: command
short-summary: Updates an Azure Storage account linked to the specified Data Lake Analytics account.
"""

helps['dla account compute-policy'] = """
type: group
short-summary: Manage Data Lake Analytics account compute policies.
"""

helps['dla account compute-policy create'] = """
type: command
short-summary: Create a compute policy in the Data Lake Analytics account.
parameters:
  - name: --max-dop-per-job
    type: int
    short-summary: The maximum degree of parallelism allowed per job for this policy. At least one of `--min-priority-per-job` and `--max-dop-per-job` must be specified.
  - name: --min-priority-per-job
    type: int
    short-summary: The minimum priority allowed per job for this policy. At least one of `--min-priority-per-job` and `--max-dop-per-job` must be specified.
  - name: --compute-policy-name
    type: string
    short-summary: The name of the compute policy to create.
  - name: --object-id
    type: string
    short-summary: The Azure Active Directory object ID of the user, group, or service principal to apply the policy to.
  - name: --object-type
    type: string
    short-summary: The Azure Active Directory object type associated with the supplied object ID.
"""

helps['dla account compute-policy delete'] = """
type: command
short-summary: Delete a compute policy in a Data Lake Analytics account.
"""

helps['dla account compute-policy list'] = """
type: command
short-summary: List compute policies in the a Lake Analytics account.
"""

helps['dla account compute-policy show'] = """
type: command
short-summary: Retrieve a compute policy in a Data Lake Analytics account.
"""

helps['dla account compute-policy update'] = """
type: command
short-summary: Update a compute policy in the Data Lake Analytics account.
parameters:
  - name: --max-dop-per-job
    type: int
    short-summary: The maximum degree of parallelism allowed per job for this policy. At least one of `--min-priority-per-job` and `--max-dop-per-job` must be specified.
  - name: --min-priority-per-job
    type: int
    short-summary: The minimum priority allowed per job for this policy. At least one of `--min-priority-per-job` and `--max-dop-per-job` must be specified.
  - name: --compute-policy-name
    type: string
    short-summary: The name of the compute policy to update.
"""

helps['dla account create'] = """
type: command
short-summary: Create a Data Lake Analytics account.
parameters:
  - name: --default-data-lake-store
    type: string
    short-summary: The default Data Lake Store account to associate with the created account.
  - name: --max-degree-of-parallelism
    type: int
    short-summary: The maximum degree of parallelism for this account.
  - name: --max-job-count
    type: int
    short-summary: The maximum number of concurrent jobs for this account.
  - name: --query-store-retention
    type: int
    short-summary: The number of days to retain job metadata.
"""

helps['dla account data-lake-store'] = """
type: group
short-summary: Manage links between Data Lake Analytics and Data Lake Store accounts.
"""

helps['dla account delete'] = """
type: command
short-summary: Delete a Data Lake Analytics account.
"""

helps['dla account firewall'] = """
type: group
short-summary: Manage Data Lake Analytics account firewall rules.
"""

helps['dla account firewall create'] = """
type: command
short-summary: Create a firewall rule in a Data Lake Analytics account.
parameters:
  - name: --end-ip-address
    type: string
    short-summary: The end of the valid IP range for the firewall rule.
  - name: --start-ip-address
    type: string
    short-summary: The start of the valid IP range for the firewall rule.
  - name: --firewall-rule-name
    type: string
    short-summary: The name of the firewall rule.
"""

helps['dla account firewall delete'] = """
type: command
short-summary: Delete a firewall rule in a Data Lake Analytics account.
"""

helps['dla account firewall list'] = """
type: command
short-summary: List firewall rules in a Data Lake Analytics account.
"""

helps['dla account firewall show'] = """
type: command
short-summary: Retrieve a firewall rule in a Data Lake Analytics account.
"""

helps['dla account firewall update'] = """
type: command
short-summary: Update a firewall rule in a Data Lake Analytics account.
"""

helps['dla account list'] = """
type: command
short-summary: List available Data Lake Analytics accounts.
"""

helps['dla account show'] = """
type: command
short-summary: Get the details of a Data Lake Analytics account.
"""

helps['dla account update'] = """
type: command
short-summary: Update a Data Lake Analytics account.
parameters:
  - name: --max-degree-of-parallelism
    type: int
    short-summary: The maximum degree of parallelism for this account.
  - name: --max-job-count
    type: int
    short-summary: The maximum number of concurrent jobs for this account.
  - name: --query-store-retention
    type: int
    short-summary: The number of days to retain job metadata.
  - name: --firewall-state
    type: string
    short-summary: Enable or disable existing firewall rules.
  - name: --allow-azure-ips
    type: string
    short-summary: Allow or block IPs originating from Azure through the firewall.
"""

helps['dla catalog'] = """
type: group
short-summary: Manage Data Lake Analytics catalogs.
"""

helps['dla catalog assembly'] = """
type: group
short-summary: Manage Data Lake Analytics catalog assemblies.
"""

helps['dla catalog credential'] = """
type: group
short-summary: Manage Data Lake Analytics catalog credentials.
"""

helps['dla catalog credential create'] = """
type: command
short-summary: Create a new catalog credential for use with an external data source.
parameters:
  - name: --credential-name
    type: string
    short-summary: The name of the credential.
  - name: --database-name
    type: string
    short-summary: The name of the database in which to create the credential.
  - name: --user-name
    type: string
    short-summary: The user name that will be used when authenticating with this credential.
"""

helps['dla catalog credential delete'] = """
type: command
short-summary: Delete a catalog credential.
"""

helps['dla catalog credential list'] = """
type: command
short-summary: List catalog credentials.
"""

helps['dla catalog credential show'] = """
type: command
short-summary: Retrieve a catalog credential.
"""

helps['dla catalog credential update'] = """
type: command
short-summary: Update a catalog credential for use with an external data source.
parameters:
  - name: --credential-name
    type: string
    short-summary: The name of the credential to update.
  - name: --database-name
    type: string
    short-summary: The name of the database in which the credential exists.
  - name: --user-name
    type: string
    short-summary: The user name associated with the credential that will have its password updated.
"""

helps['dla catalog database'] = """
type: group
short-summary: Manage Data Lake Analytics catalog databases.
"""

helps['dla catalog external-data-source'] = """
type: group
short-summary: Manage Data Lake Analytics catalog external data sources.
"""

helps['dla catalog package'] = """
type: group
short-summary: Manage Data Lake Analytics catalog packages.
"""

helps['dla catalog procedure'] = """
type: group
short-summary: Manage Data Lake Analytics catalog stored procedures.
"""

helps['dla catalog schema'] = """
type: group
short-summary: Manage Data Lake Analytics catalog schemas.
"""

helps['dla catalog table'] = """
type: group
short-summary: Manage Data Lake Analytics catalog tables.
"""

helps['dla catalog table list'] = """
type: command
short-summary: List tables in a database or schema.
parameters:
  - name: --database-name
    type: string
    short-summary: The name of the database.
  - name: --schema-name
    type: string
    short-summary: The schema assocated with the tables to list.
"""

helps['dla catalog table-partition'] = """
type: group
short-summary: Manage Data Lake Analytics catalog table partitions.
"""

helps['dla catalog table-stats'] = """
type: group
short-summary: Manage Data Lake Analytics catalog table statistics.
"""

helps['dla catalog table-stats list'] = """
type: command
short-summary: List table statistics in a database, table, or schema.
parameters:
  - name: --database-name
    type: string
    short-summary: The name of the database.
  - name: --schema-name
    type: string
    short-summary: The schema associated with the tables to list.
  - name: --table-name
    type: string
    short-summary: The table to list statistics for. `--schema-name` must also be specified.
"""

helps['dla catalog table-type'] = """
type: group
short-summary: Manage Data Lake Analytics catalog table types.
"""

helps['dla catalog tvf'] = """
type: group
short-summary: Manage Data Lake Analytics catalog table valued functions.
"""

helps['dla catalog tvf list'] = """
type: command
short-summary: List table valued functions in a database or schema.
parameters:
  - name: --database-name
    type: string
    short-summary: The name of the database.
  - name: --schema-name
    type: string
    short-summary: The name of the schema assocated with table valued functions to list.
"""

helps['dla catalog view'] = """
type: group
short-summary: Manage Data Lake Analytics catalog views.
"""

helps['dla catalog view list'] = """
type: command
short-summary: List views in a database or schema.
parameters:
  - name: --database-name
    type: string
    short-summary: The name of the database.
  - name: --schema-name
    type: string
    short-summary: The name of the schema associated with the views to list.
"""

helps['dla job'] = """
type: group
short-summary: Manage Data Lake Analytics jobs.
"""

helps['dla job cancel'] = """
type: command
short-summary: Cancel a Data Lake Analytics job.
"""

helps['dla job list'] = """
type: command
short-summary: List Data Lake Analytics jobs.
"""

helps['dla job pipeline'] = """
type: group
short-summary: Manage Data Lake Analytics job pipelines.
"""

helps['dla job pipeline list'] = """
type: command
short-summary: List job pipelines in a Data Lake Analytics account.
"""

helps['dla job pipeline show'] = """
type: command
short-summary: Retrieve a job pipeline in a Data Lake Analytics account.
"""

helps['dla job recurrence'] = """
type: group
short-summary: Manage Data Lake Analytics job recurrences.
"""

helps['dla job recurrence list'] = """
type: command
short-summary: List job recurrences in a Data Lake Analytics account.
"""

helps['dla job recurrence show'] = """
type: command
short-summary: Retrieve a job recurrence in a Data Lake Analytics account.
"""

helps['dla job show'] = """
type: command
short-summary: Get information for a Data Lake Analytics job.
"""

helps['dla job submit'] = """
type: command
short-summary: Submit a job to a Data Lake Analytics account.
parameters:
  - name: --job-name
    type: string
    short-summary: Name for the submitted job.
  - name: --script
    type: string
    short-summary: Script to submit. This may be '@{file}' to load from a file.
  - name: --runtime-version
    short-summary: The runtime version to use.
    long-summary: This parameter is used for explicitly overwriting the default runtime. It should only be done if you know what you are doing.
  - name: --degree-of-parallelism
    short-summary: The degree of parallelism for the job.
    long-summary: Higher values equate to more parallelism and will usually yield faster running jobs, at the cost of more AUs.
  - name: --priority
    short-summary: The priority of the job.
    long-summary: Lower values increase the priority, with the lowest value being 1. This determines the order jobs are run in.
"""

helps['dla job wait'] = """
type: command
short-summary: Wait for a Data Lake Analytics job to finish.
long-summary: This command exits when the job completes.
parameters:
  - name: --job-id
    type: string
    short-summary: 'Job ID to poll for completion.'
"""

helps['dls'] = """
type: group
short-summary: Manage Data Lake Store accounts and filesystems.
"""

helps['dls account'] = """
type: group
short-summary: Manage Data Lake Store accounts.
"""

helps['dls account create'] = """
type: command
short-summary: Creates a Data Lake Store account.
parameters:
  - name: --key-vault-id
    type: string
    short-summary: 'Key vault for the user-assigned encryption type.'
  - name: --key-name
    type: string
    short-summary: 'Key name for the user-assigned encryption type.'
examples:
  - name: Creates a Data Lake Store account. (autogenerated)
    text: az dls account create --account mydatalakestoragegen1 --resource-group MyResourceGroup
    crafted: true
"""

helps['dls account delete'] = """
type: command
short-summary: Delete a Data Lake Store account.
examples:
  - name: Delete a Data Lake Store account. (autogenerated)
    text: az dls account delete --account mydatalakestoragegen1
    crafted: true
"""

helps['dls account enable-key-vault'] = """
type: command
short-summary: Enable the use of Azure Key Vault for encryption of a Data Lake Store account.
examples:
  - name: Enable the use of Azure Key Vault for encryption of a Data Lake Store account. (autogenerated)
    text: az dls account enable-key-vault --account mydatalakestoragegen1
    crafted: true
"""

helps['dls account firewall'] = """
type: group
short-summary: Manage Data Lake Store account firewall rules.
"""

helps['dls account firewall create'] = """
type: command
short-summary: Creates a firewall rule in a Data Lake Store account.
parameters:
  - name: --end-ip-address
    type: string
    short-summary: 'The end of the valid ip range for the firewall rule.'
  - name: --start-ip-address
    type: string
    short-summary: 'The start of the valid ip range for the firewall rule.'
  - name: --firewall-rule-name
    type: string
    short-summary: 'The name of the firewall rule.'
"""

helps['dls account firewall delete'] = """
type: command
short-summary: Deletes a firewall rule in a Data Lake Store account.
"""

helps['dls account firewall list'] = """
type: command
short-summary: Lists firewall rules in a Data Lake Store account.
examples:
  - name: Lists firewall rules in a Data Lake Store account. (autogenerated)
    text: az dls account firewall list --account mydatalakestoragegen1 --subscription MySubscription
    crafted: true
"""

helps['dls account firewall show'] = """
type: command
short-summary: Get the details of a firewall rule in a Data Lake Store account.
"""

helps['dls account firewall update'] = """
type: command
short-summary: Updates a firewall rule in a Data Lake Store account.
"""

helps['dls account list'] = """
type: command
short-summary: Lists available Data Lake Store accounts.
examples:
  - name: Lists available Data Lake Store accounts. (autogenerated)
    text: az dls account list --resource-group MyResourceGroup
    crafted: true
"""

helps['dls account network-rule'] = """
type: group
short-summary: Manage Data Lake Store account virtual network rules.
"""

helps['dls account network-rule create'] = """
type: command
short-summary: Creates a virtual network rule in a Data Lake Store account.
parameters:
  - name: --subnet
    type: string
    short-summary: 'The subnet name or id for the virtual network rule.'
  - name: --vnet-name
    type: string
    short-summary: 'The name of the virtual network rule.'
"""

helps['dls account network-rule delete'] = """
type: command
short-summary: Deletes a virtual network rule in a Data Lake Store account.
"""

helps['dls account network-rule list'] = """
type: command
short-summary: Lists virtual network rules in a Data Lake Store account.
"""

helps['dls account network-rule show'] = """
type: command
short-summary: Get the details of a virtual network rule in a Data Lake Store account.
"""

helps['dls account network-rule update'] = """
type: command
short-summary: Updates a virtual network rule in a Data Lake Store account.
"""

helps['dls account show'] = """
type: command
short-summary: Get the details of a Data Lake Store account.
examples:
  - name: Get the details of a Data Lake Store account. (autogenerated)
    text: az dls account show --account mydatalakestoragegen1
    crafted: true
"""

helps['dls account trusted-provider'] = """
type: group
short-summary: Manage Data Lake Store account trusted identity providers.
"""

helps['dls account update'] = """
type: command
short-summary: Updates a Data Lake Store account.
examples:
  - name: Updates a Data Lake Store account. (autogenerated)
    text: az dls account update --account mydatalakestoragegen1 --allow-azure-ips Enabled --firewall-state Enabled --resource-group MyResourceGroup --subscription MySubscription --tags key=value
    crafted: true
"""

helps['dls fs'] = """
type: group
short-summary: Manage a Data Lake Store filesystem.
"""

helps['dls fs access'] = """
type: group
short-summary: Manage Data Lake Store filesystem access and permissions.
"""

helps['dls fs access remove-all'] = """
type: command
short-summary: Remove the access control list for a file or folder.
examples:
  - name: Remove the access control list for a file or folder. (autogenerated)
    text: az dls fs access remove-all --account dpreptestfiles --path / --subscription MySubscription
    crafted: true
"""

helps['dls fs access remove-entry'] = """
type: command
short-summary: Remove entries for the access control list of a file or folder.
examples:
  - name: Remove entries for the access control list of a file or folder. (autogenerated)
    text: az dls fs access remove-entry --account dpreptestfiles --acl-spec user:00000000-0000-0000-0000-000000000000:-w- --path /
    crafted: true
"""

helps['dls fs access set'] = """
type: command
short-summary: Replace the existing access control list for a file or folder.
examples:
  - name: Replace the existing access control list for a file or folder. (autogenerated)
    text: az dls fs access set --account dpreptestfiles --acl-spec user:00000000-0000-0000-0000-000000000000:-w- --path / --subscription MySubscription
    crafted: true
"""

helps['dls fs access set-entry'] = """
type: command
short-summary: Update the access control list for a file or folder.
examples:
  - name: Update the access control list for a file or folder. (autogenerated)
    text: az dls fs access set-entry --account dpreptestfiles --acl-spec user:00000000-0000-0000-0000-000000000000:-w- --path /
    crafted: true
"""

helps['dls fs access set-owner'] = """
type: command
short-summary: Set the owner information for a file or folder in a Data Lake Store account.
parameters:
  - name: --owner
    type: string
    short-summary: The user Azure Active Directory object ID or user principal name to set as the owner.
  - name: --group
    type: string
    short-summary: The group Azure Active Directory object ID or user principal name to set as the owning group.
"""

helps['dls fs access set-permission'] = """
type: command
short-summary: Set the permissions for a file or folder in a Data Lake Store account.
parameters:
  - name: --permission
    type: int
    short-summary: The octal representation of the permissions for user, group and mask.
example:
  - name: Set full permissions for a user, read-execute permissions for a group, and execute permissions for all.
    text: az fs access set-permission --path /path/to/file.txt --permission 751
examples:
  - name: Set the permissions for a file or folder in a Data Lake Store account. (autogenerated)
    text: az dls fs access set-permission --account dpreptestfiles --path / --permission 777 --subscription MySubscription
    crafted: true
"""

helps['dls fs access show'] = """
type: command
short-summary: Display the access control list (ACL).
examples:
  - name: Display the access control list (ACL). (autogenerated)
    text: az dls fs access show --account {account} --path {path}
    crafted: true
"""

helps['dls fs append'] = """
type: command
short-summary: Append content to a file in a Data Lake Store account.
parameters:
  - name: --content
    type: string
    short-summary: 'Content to be appended to the file.'
"""

helps['dls fs create'] = """
type: command
short-summary: Creates a file or folder in a Data Lake Store account.
parameters:
  - name: --content
    type: string
    short-summary: 'Content for the file to contain upon creation.'
examples:
  - name: Creates a file or folder in a Data Lake Store account. (autogenerated)
    text: az dls fs create --account {account} --folder  --path {path}
    crafted: true
"""

helps['dls fs delete'] = """
type: command
short-summary: Delete a file or folder in a Data Lake Store account.
examples:
  - name: Delete a file or folder in a Data Lake Store account. (autogenerated)
    text: az dls fs delete --account {account} --path {path}
    crafted: true
"""

helps['dls fs download'] = """
type: command
short-summary: Download a file or folder from a Data Lake Store account to the local machine.
parameters:
  - name: --source-path
    type: string
    short-summary: The full path in the Data Lake Store filesystem to download the file or folder from.
  - name: --destination-path
    type: string
    short-summary: The local path where the file or folder will be downloaded to.
  - name: --thread-count
    type: int
    short-summary: 'Parallelism of the download. Default: The number of cores in the local machine.'
  - name: --chunk-size
    type: int
    short-summary: Size of a chunk, in bytes.
    long-summary: Large files are split into chunks. Files smaller than this size will always be transferred in a single thread.
  - name: --buffer-size
    type: int
    short-summary: Size of the transfer buffer, in bytes.
    long-summary: A buffer cannot be bigger than a chunk and cannot be smaller than a block.
  - name: --block-size
    type: int
    short-summary: Size of a block, in bytes.
    long-summary: Within each chunk, a smaller block is written for each API call. A block cannot be bigger than a chunk and must be bigger than a buffer.
examples:
  - name: Download a file or folder from a Data Lake Store account to the local machine. (autogenerated)
    text: az dls fs download --account {account} --destination-path {destination-path} --source-path {source-path}
    crafted: true
"""

helps['dls fs join'] = """
type: command
short-summary: Join files in a Data Lake Store account into one file.
parameters:
  - name: --source-paths
    type: list
    short-summary: The space-separated list of files in the Data Lake Store account to join.
  - name: --destination-path
    type: string
    short-summary: The destination path in the Data Lake Store account.
"""

helps['dls fs list'] = """
type: command
short-summary: List the files and folders in a Data Lake Store account.
examples:
  - name: List the files and folders in a Data Lake Store account. (autogenerated)
    text: az dls fs list --account {account} --path {path}
    crafted: true
"""

helps['dls fs move'] = """
type: command
short-summary: Move a file or folder in a Data Lake Store account.
parameters:
  - name: --source-path
    type: list
    short-summary: The file or folder to move.
  - name: --destination-path
    type: string
    short-summary: The destination path in the Data Lake Store account.
examples:
  - name: Move a file or folder in a Data Lake Store account. (autogenerated)
    text: az dls fs move --account {account} --destination-path {destination-path} --source-path {source-path}
    crafted: true
"""

helps['dls fs preview'] = """
type: command
short-summary: Preview the content of a file in a Data Lake Store account.
parameters:
  - name: --length
    type: long
    short-summary: The amount of data to preview in bytes.
    long-summary: If not specified, attempts to preview the full file. If the file is > 1MB `--force` must be specified.
  - name: --offset
    type: long
    short-summary: The position in bytes to start the preview from.
"""

helps['dls fs remove-expiry'] = """
type: command
short-summary: Remove the expiration time for a file.
"""

helps['dls fs set-expiry'] = """
type: command
short-summary: Set the expiration time for a file.
"""

helps['dls fs show'] = """
type: command
short-summary: Get file or folder information in a Data Lake Store account.
examples:
  - name: Get file or folder information in a Data Lake Store account. (autogenerated)
    text: az dls fs show --account {account} --path {path}
    crafted: true
"""

helps['dls fs test'] = """
type: command
short-summary: Test for the existence of a file or folder in a Data Lake Store account.
examples:
  - name: Test for the existence of a file or folder in a Data Lake Store account. (autogenerated)
    text: az dls fs test --account {account} --path {path}
    crafted: true
"""

helps['dls fs upload'] = """
type: command
short-summary: Upload a file or folder to a Data Lake Store account.
parameters:
  - name: --source-path
    type: string
    short-summary: The path to the file or folder to upload.
  - name: --destination-path
    type: string
    short-summary: The full path in the Data Lake Store filesystem to upload the file or folder to.
  - name: --thread-count
    type: int
    short-summary: 'Parallelism of the upload. Default: The number of cores in the local machine.'
  - name: --chunk-size
    type: int
    short-summary: Size of a chunk, in bytes.
    long-summary: Large files are split into chunks. Files smaller than this size will always be transferred in a single thread.
  - name: --buffer-size
    type: int
    short-summary: Size of the transfer buffer, in bytes.
    long-summary: A buffer cannot be bigger than a chunk and cannot be smaller than a block.
  - name: --block-size
    type: int
    short-summary: Size of a block, in bytes.
    long-summary: Within each chunk, a smaller block is written for each API call. A block cannot be bigger than a chunk and must be bigger than a buffer.

examples:
  - name: Upload a file or folder to a Data Lake Store account. (autogenerated)
    text: az dls fs upload --account {account} --destination-path {destination-path} --overwrite  --source-path {source-path}
    crafted: true
"""

helps['dms'] = """
type: group
short-summary: Manage Azure Data Migration Service (DMS) instances.
"""

helps['dms check-name'] = """
type: command
short-summary: Check if a given DMS instance name is available in a given region as well as the name's validity.
parameters:
  - name: --name -n
    type: string
    short-summary: >
        The Service name to check.
"""

helps['dms check-status'] = """
type: command
short-summary: Perform a health check and return the status of the service and virtual machine size.
"""

helps['dms create'] = """
type: command
short-summary: Create an instance of the Data Migration Service.
parameters:
  - name: --sku-name
    type: string
    short-summary: >
        The name of the CPU SKU on which the service's Virtual Machine will run. Check the name and the availability of SKUs in your area with "az dms list-skus".
  - name: --subnet
    type: string
    short-summary: >
        The Resource ID of the VNet's Subnet you will use to connect the source and target DBs.
        Use "az network vnet subnet show -h" for help to get your subnet's ID.
examples:
  - name: Create an instance of DMS.
    text: >
        az dms create -l westus -n mydms -g myresourcegroup --sku-name Basic_2vCores --subnet /subscriptions/{vnetSubscriptionId}/resourceGroups/{vnetResourceGroup}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName} --tags tagName1=tagValue1 tagWithNoValue
"""

helps['dms delete'] = """
type: command
short-summary: Delete an instance of the Data Migration Service.
parameters:
  - name: --delete-running-tasks
    type: bool
    short-summary: >
        Cancel any running tasks before deleting the service.
"""

helps['dms list'] = """
type: command
short-summary: List the DMS instances within your currently configured subscription (to set this use "az account set"). If provided, only show the instances within a given resource group.
examples:
  - name: List all the instances in your subscription.
    text: >
        az dms list
  - name: List all the instances in a given resource group.
    text: >
        az dms list -g myresourcegroup
"""

helps['dms list-skus'] = """
type: command
short-summary: List the SKUs that are supported by the Data Migration Service.
"""

helps['dms project'] = """
type: group
short-summary: Manage Projects for an instance of the Data Migration Service.
"""

helps['dms project check-name'] = """
type: command
short-summary: Check if a given Project name is available within a given instance of DMS as well as the name's validity.
parameters:
  - name: --name -n
    type: string
    short-summary: >
        The Project name to check.
"""

helps['dms project create'] = """
type: command
short-summary: Create a migration Project which can contain multiple Tasks.
parameters:
  - name: --source-platform
    type: string
    short-summary: >
        The type of server for the source database. The supported types are: SQL.
  - name: --target-platform
    type: string
    short-summary: >
        The type of service for the target database. The supported types are: SQLDB.
examples:
  - name: Create a Project for a DMS instance.
    text: >
        az dms project create -l westus -n myproject -g myresourcegroup --service-name mydms --source-platform SQL --target-platform SQLDB --tags tagName1=tagValue1 tagWithNoValue
"""

helps['dms project delete'] = """
type: command
short-summary: Delete a Project.
parameters:
  - name: --delete-running-tasks
    type: bool
    short-summary: >
        Cancel any running tasks before deleting the Project.
"""

helps['dms project list'] = """
type: command
short-summary: List the Projects within an instance of DMS.
"""

helps['dms project show'] = """
type: command
short-summary: Show the details of a migration Project.
"""

helps['dms project task'] = """
type: group
short-summary: Manage Tasks for a Data Migration Service instance's Project.
"""

helps['dms project task cancel'] = """
type: command
short-summary: Cancel a Task if it's currently queued or running.
"""

helps['dms project task check-name'] = """
type: command
short-summary: Check if a given Task name is available within a given instance of DMS as well as the name's validity.
parameters:
  - name: --name -n
    type: string
    short-summary: >
        The Task name to check.
"""

helps['dms project task create'] = """
type: command
short-summary: Create and start a migration Task.
parameters:
  - name: --database-options-json
    type: string
    short-summary: >
        Database and table information. This can be either a JSON-formatted string or the location to a file containing the JSON object. See example below for the format.
  - name: --source-connection-json
    type: string
    short-summary: >
        The connection information to the source server. This can be either a JSON-formatted string or the location to a file containing the JSON object. See example below for the format.
  - name: --target-connection-json
    type: string
    short-summary: >
        The connection information to the target server. This can be either a JSON-formatted string or the location to a file containing the JSON object. See example below for the format.
  - name: --enable-data-integrity-validation
    type: bool
    short-summary: >
        Whether to perform a checksum based data integrity validation between source and target for the selected database and tables.
  - name: --enable-query-analysis-validation
    type: bool
    short-summary: >
        Whether to perform a quick and intelligent query analysis by retrieving queries from the source database and
        executing them in the target. The result will have execution statistics for executions in source and target databases
        for the extracted queries.
  - name: --enable-schema-validation
    type: bool
    short-summary: >
        Whether to compare the schema information between source and target.
examples:
  - name: Create and start a Task which performs no validation checks.
    text: >
        az dms project task create --database-options-json "C:\\CLI Files\\databaseOptions.json" -n mytask --project-name myproject -g myresourcegroup --service-name mydms --source-connection-json "{'dataSource': 'myserver', 'authentication': 'SqlAuthentication', 'encryptConnection': 'true', 'trustServerCertificate': 'true'}" --target-connection-json "C:\\CLI Files\\targetConnection.json"
  - name: Create and start a Task which performs all validation checks.
    text: >
        az dms project task create --database-options-json "C:\\CLI Files\\databaseOptions.json" -n mytask --project-name myproject -g myresourcegroup --service-name mydms --source-connection-json "C:\\CLI Files\\sourceConnection.json" --target-connection-json "C:\\CLI Files\\targetConnection.json" --enable-data-integrity-validation --enable-query-analysis-validation --enable-schema-validation
  - name: The format of the database options JSON object.
    text: >
        [
            {
                "name": "source database",
                "target_database_name": "target database",
                "make_source_db_read_only": false|true,
                "table_map": {
                    "schema.SourceTableName1": "schema.TargetTableName1",
                    "schema.SourceTableName2": "schema.TargetTableName2",
                    ...n
                }
            },
            ...n
        ]
  - name: The format of the connection JSON object.
    text: >
        {
            "userName": "user name",    // if this is missing or null, you will be prompted
            "password": null,           // if this is missing or null (highly recommended) you will be prompted
            "dataSource": "server name[,port]",
            "authentication": "SqlAuthentication|WindowsAuthentication",
            "encryptConnection": true,      // highly recommended to leave as true
            "trustServerCertificate": true  // highly recommended to leave as true
        }
"""

helps['dms project task delete'] = """
type: command
short-summary: Delete a migration Task.
parameters:
  - name: --delete-running-tasks
    type: bool
    short-summary: >
        If the Task is currently running, cancel the Task before deleting the Project.
"""

helps['dms project task list'] = """
type: command
short-summary: List the Tasks within a Project. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.
parameters:
  - name: --task-type
    type: string
    short-summary: >
        Filters the list by the type of task. For the list of possible types see "az dms check-status".
examples:
  - name: List all Tasks within a Project.
    text: >
        az dms project task list --project-name myproject -g myresourcegroup --service-name mydms
  - name: List only the SQL to SQL migration tasks within a Project.
    text: >
        az dms project task list --project-name myproject -g myresourcegroup --service-name mydms --task-type Migrate.SqlServer.SqlDb
"""

helps['dms project task show'] = """
type: command
short-summary: Show the details of a migration Task. Use the "--expand" to get more details.
parameters:
  - name: --expand
    type: string
    short-summary: >
        Expand the response to provide more details. Use with "command" to see more details of the Task.
        Use with "output" to see the results of the Task's migration.
"""

helps['dms show'] = """
type: command
short-summary: Show the details for an instance of the Data Migration Service.
"""

helps['dms start'] = """
type: command
short-summary: Start an instance of the Data Migration Service. It can then be used to run data migrations.
"""

helps['dms stop'] = """
type: command
short-summary: Stop an instance of the Data Migration Service. While stopped, it can't be used to run data migrations and the owner won't be billed.
"""

helps['dms wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the DMS instance is met.
"""

helps['eventgrid'] = """
type: group
short-summary: Manage Azure Event Grid topics, event subscriptions, domains and domain topics.
"""

helps['eventgrid domain'] = """
type: group
short-summary: Manage event domains.
"""

helps['eventgrid domain create'] = """
type: command
short-summary: Create a domain.
examples:
  - name: Create a new domain.
    text: az eventgrid domain create -g rg1 --name domain1 -l westus2
"""

helps['eventgrid domain delete'] = """
type: command
short-summary: Delete a domain.
examples:
  - name: Delete a domain.
    text: az eventgrid domain delete -g rg1 --name domain1
"""

helps['eventgrid domain key'] = """
type: group
short-summary: Manage shared access keys of a domain.
"""

helps['eventgrid domain key list'] = """
type: command
short-summary: List shared access keys of a domain.
"""

helps['eventgrid domain key regenerate'] = """
type: command
short-summary: Regenerate a shared access key of a domain.
"""

helps['eventgrid domain list'] = """
type: command
short-summary: List available domains.
examples:
  - name: List all domains in the current Azure subscription.
    text: az eventgrid domain list
  - name: List all domains in a resource group.
    text: az eventgrid domain list -g rg1
  - name: List all domains in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid domain list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all domains in a resource group except the domain with name "name1"
    text: az eventgrid domain list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid domain show'] = """
type: command
short-summary: Get the details of a domain.
examples:
  - name: Show the details of a domain.
    text: az eventgrid domain show -g rg1 -n domain1
  - name: Show the details of a domain based on resource ID.
    text: az eventgrid domain show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1
"""

helps['eventgrid domain topic'] = """
type: group
short-summary: Manage event domain topics.
"""

helps['eventgrid domain topic create'] = """
type: command
short-summary: Create a domain topic under a domain.
examples:
  - name: Create a new domain topic under domain.
    text: az eventgrid domain topic create -g rg1 --domain-name domain1 --name domaintopic1
"""

helps['eventgrid domain topic delete'] = """
type: command
short-summary: Delete a domain topic under a domain.
examples:
  - name: Delete a domain topic.
    text: az eventgrid domain topic delete -g rg1 --domain-name domain1 --name domaintopic1
"""

helps['eventgrid domain topic list'] = """
type: command
short-summary: List available topics in a domain.
examples:
  - name: List all topics in a domain.
    text: az eventgrid domain topic list -g rg1 --domain-name domain1
  - name: List all domain topics in a domain whose name contains the pattern "XYZ"
    text: az eventgrid domain topic list -g rg1 --domain-name domain1 --odata-query "Contains(name, 'XYZ')"
  - name: List all domain topics in a domain except the domain topic with name "name1"
    text: az eventgrid domain topic list -g rg1 --domain-name domain1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid domain topic show'] = """
type: command
short-summary: Get the details of a domain topic.
examples:
  - name: Show the details of a domain topic.
    text: az eventgrid domain topic show -g rg1 --domain-name domain1 --name topic1
"""

helps['eventgrid domain update'] = """
type: command
short-summary: Update a domain.
examples:
  - name: Update the properties of an existing domain.
    text: az eventgrid domain update -g rg1 --name domain1 --tags Dept=IT
"""

helps['eventgrid event-subscription'] = """
type: group
short-summary: Manage event subscriptions.
long-summary: Manage event subscriptions for an Event Grid topic, domain, domain topic, Azure subscription, resource group or for any other Azure resource that supports event notifications.
"""

helps['eventgrid event-subscription create'] = """
type: command
short-summary: Create a new event subscription.
parameters:
  - name: --advanced-filter
    short-summary: An advanced filter enables filtering of events based on a specific event property.
    long-summary: |
        Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
        StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
        StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
        StringContains:            --advanced-filter subject StringContains Blue Red
        StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
        StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
        NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
        NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
        NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
        NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
        NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
        NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
        BoolEquals:                --advanced-filter data.property3 BoolEquals true
        Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource to which the event subscription needs to be created.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
  - name: --deadletter-endpoint
    short-summary: The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    long-summary: |
        Example: --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/containerName
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
    long-summary: The type of the destination endpoint. It is expected that the destination endpoint be created and available for use before executing any Event Grid command.
examples:
  - name: Create a new event subscription for an Event Grid topic, using default filters.
    text: |
        az eventgrid event-subscription create --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for an Azure subscription subscription, using default filters.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for a resource group, using default filters.
    text: |
        az eventgrid event-subscription create --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for a storage account, using default filters.
    text: |
        az eventgrid event-subscription create --name es3 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1"  \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for a storage account, using advanced filters.
    text: |
        az eventgrid event-subscription create  --name es3 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --advanced-filter data.blobType StringIn BlockBlob
            --advanced-filter data.url StringBeginsWith https://myaccount.blob.core.windows.net
  - name: Create a new event subscription for an Azure subscription, with a filter specifying a subject prefix.
    text: |
        az eventgrid event-subscription create --name es4 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --subject-begins-with mysubject_prefix
  - name: Create a new event subscription for a resource group, with a filter specifying a subject suffix.
    text: |
        az eventgrid event-subscription create --name es5 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --subject-ends-with mysubject_suffix
  - name: Create a new event subscription for an Azure subscription, using default filters, and an EventHub as a destination.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint-type eventhub \\
            --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.EventHub/namespaces/n1/eventhubs/EH1
  - name: Create a new event subscription for an Azure subscription, using default filters, and an Azure Storage queue as a destination.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint-type storagequeue \\
            --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/queueservices/default/queues/q1
  - name: Create a new event subscription for an Azure subscription, using default filters, and an Azure ServiceBusQueue as a destination.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint-type servicebusqueue \\
            --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.ServiceBus/namespaces/ns1/queues/queue1
  - name: Create a new event subscription for a storage account, with a deadletter destination and custom retry policy of maximum 10 delivery attempts and an Event TTL of 2 hours (whichever happens earlier).
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/s2/blobServices/default/containers/blobcontainer1 \\
            --max-delivery-attempts 10 --event-ttl 120
  - name: Create a new event subscription for a domain topic.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1/topics/t1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription (for a storage account) with an expiration date.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/sa1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --expiration-date "2018-10-31"
"""

helps['eventgrid event-subscription delete'] = """
type: command
short-summary: Delete an event subscription.
parameters:
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be deleted.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
examples:
  - name: Delete an event subscription for an Event Grid topic.
    text: |
        az eventgrid event-subscription delete --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
  - name: Delete an event subscription for an Event Grid domain topic.
    text: |
        az eventgrid event-subscription delete --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1/topics/topic1
  - name: Delete an event subscription for an Event Grid domain.
    text: |
        az eventgrid event-subscription delete --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1
  - name: Delete an event subscription for an Azure subscription.
    text: |
        az eventgrid event-subscription delete --name es2 \\
            --source-resource-id /subscriptions/{SubID}
  - name: Delete an event subscription for a resource group.
    text: |
        az eventgrid event-subscription delete --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}
  - name: Delete an event subscription for a storage account.
    text: |
        az eventgrid event-subscription delete --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/microsoft.storage/storageaccounts/kalsegblob
"""

helps['eventgrid event-subscription list'] = """
type: command
short-summary: List event subscriptions.
long-summary: |
    Event Grid supports both regional and global event subscriptions: Event subscriptions on regional resources (such as Storage accounts or Event Grid topics) are regional, while event subscriptions on global resources (such as an Azure subscription or resource group) are global.
    Hence, you can list event subscriptions in a few different ways:
    1. To list by the resource ID of the resource whose event subscriptions you want to list, specify the --source-resource-id parameter. No other parameters must be specified.
    2. To list by a topic-type (e.g. storage accounts), specify the --topic-type parameter along with --location (e.g. "westus2") parameter. For global topic types (e.g. "Microsoft.Resources.Subscriptions"), specify the location value as "global".
    3. To list all event subscriptions in a region (across all topic types), specify only the --location parameter.
    4. For both #2 and #3 above, to filter only by a resource group, you can additionally specify the --resource-group parameter.
parameters:
  - name: --topic-type-name
    short-summary: Name of the topic-type whose event subscriptions need to be listed. When this is specified, you must also specify --location.
    long-summary: |
        Example 1: List all Storage event subscriptions in WestUS2
            --resource-group TestRG --topic-type-name Microsoft.Storage.StorageAccounts --location westus2
        Example 2: List all event subscriptions on Azure subscriptions
            --topic-type-name Microsoft.Resources.Subscriptions --location global
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be listed.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
examples:
  - name: List all event subscriptions created for an Event Grid topic.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
  - name: List all event subscriptions created for a storage account.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/kalsegblob
  - name: List all event subscriptions created for an Azure subscription.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}
  - name: List all event subscriptions created for a resource group.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}
  - name: List all event subscriptions for an Event Grid domain.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1
  - name: List all event subscriptions for an Event Grid domain topic.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1/topics/topic1
  - name: List all Storage event subscriptions (under the currently selected Azure subscription) in westus2.
    text: |
        az eventgrid event-subscription list --topic-type Microsoft.Storage.StorageAccounts --location westus2
  - name: List all Storage event subscriptions (under the given resource group) in westus2.
    text: |
        az eventgrid event-subscription list --topic-type Microsoft.Storage.StorageAccounts --location westus2 --resource-group {RG}
  - name: List all regional or global event subscriptions (under the currently selected Azure subscription).
    text: |
        az eventgrid event-subscription list --location westus2
        az eventgrid event-subscription list --location global
  - name: List all regional or global event subscriptions under a specified resource group.
    text: |
        az eventgrid event-subscription list --location westus2 --resource-group {RG}
        az eventgrid event-subscription list --location global --resource-group {RG}
  - name: List all event subscriptions for an Event Grid domain whose name contains the pattern "XYZ"
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1 --odata-query "Contains(name, 'XYZ')"
  - name: List all event subscriptions for an Event Grid domain except the event subscription with name "name1"
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid event-subscription show'] = """
type: command
short-summary: Get the details of an event subscription.
parameters:
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be shown.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
examples:
  - name: Show the details of an event subscription for an Event Grid topic.
    text: |
        az eventgrid event-subscription show --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/topic1
  - name: Show the details of an event subscription for an Azure subscription.
    text: |
        az eventgrid event-subscription show --name es2 \\
            --source-resource-id /subscriptions/{SubID}
  - name: Show the details of an event subscription for a resource group.
    text: |
        az eventgrid event-subscription show --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
  - name: Show the details of an event subscription for a storage account.
    text: |
        az eventgrid event-subscription show --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/microsoft.storage/storageaccounts/kalsegblob
"""

helps['eventgrid event-subscription update'] = """
type: command
short-summary: Update an event subscription.
parameters:
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be updated.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
examples:
  - name: Update an event subscription for an Event Grid topic to specify a new endpoint.
    text: |
        az eventgrid event-subscription update --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Update an event subscription for an Azure subscription to specify a new subject-ends-with filter.
    text: |
        az eventgrid event-subscription update --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --subject-ends-with .jpg
  - name: Update an event subscription for a resource group to specify a new endpoint and a new subject-ends-with filter.
    text: |
        az eventgrid event-subscription update --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
            --subject-ends-with .png \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Update an event subscription for a storage account to specify a new list of included event types.
    text: |
        az eventgrid event-subscription update --name es3 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/microsoft.storage/storageaccounts/kalsegblob" \\
            --included-event-types Microsoft.Storage.BlobCreated Microsoft.Storage.BlobDeleted
  - name: Update an event subscription for a storage account, to include a deadletter destination.
    text: |
        az eventgrid event-subscription update --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/kalsegblob" \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/blobcontainer1
"""

helps['eventgrid topic'] = """
type: group
short-summary: Manage Azure Event Grid topics.
"""

helps['eventgrid topic create'] = """
type: command
short-summary: Create a topic.
examples:
  - name: Create a new topic.
    text: az eventgrid topic create -g rg1 --name topic1 -l westus2
"""

helps['eventgrid topic delete'] = """
type: command
short-summary: Delete a topic.
examples:
  - name: Delete a topic.
    text: az eventgrid topic delete -g rg1 --name topic1
"""

helps['eventgrid topic key'] = """
type: group
short-summary: Manage shared access keys of a topic.
"""

helps['eventgrid topic key list'] = """
type: command
short-summary: List shared access keys of a topic.
"""

helps['eventgrid topic key regenerate'] = """
type: command
short-summary: Regenerate a shared access key of a topic.
"""

helps['eventgrid topic list'] = """
type: command
short-summary: List available topics.
examples:
  - name: List all topics in the current Azure subscription.
    text: az eventgrid topic list
  - name: List all topics in a resource group.
    text: az eventgrid topic list -g rg1
  - name: List all topics in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid topic list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all topics in a resource group except the domain with name "name1"
    text: az eventgrid topic list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid topic show'] = """
type: command
short-summary: Get the details of a topic.
examples:
  - name: Show the details of a topic.
    text: az eventgrid topic show -g rg1 -n topic1
  - name: Show the details of a topic based on resource ID.
    text: az eventgrid topic show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
"""

helps['eventgrid topic update'] = """
type: command
short-summary: Update a topic.
examples:
  - name: Update the properties of an existing topic.
    text: az eventgrid topic update -g rg1 --name topic1 --tags Dept=IT
"""

helps['eventgrid topic-type'] = """
type: group
short-summary: Get details for topic types.
"""

helps['eventgrid topic-type list'] = """
type: command
short-summary: List registered topic types.
"""

helps['eventgrid topic-type list-event-types'] = """
type: command
short-summary: List the event types supported by a topic type.
examples:
  - name: List all event types supported by Azure Storage Accounts.
    text: |
        az eventgrid topic-type list-event-types -n Microsoft.Storage.StorageAccounts
"""

helps['eventgrid topic-type show'] = """
type: command
short-summary: Get the details for a topic type.
"""

helps['eventhubs'] = """
type: group
short-summary: Manage Azure Event Hubs namespaces, eventhubs, consumergroups and geo recovery configurations - Alias
"""

helps['eventhubs eventhub'] = """
type: group
short-summary: Manage Azure EventHubs eventhub and authorization-rule
"""

helps['eventhubs eventhub authorization-rule'] = """
type: group
short-summary: Manage Azure Service Bus Authorizationrule for Eventhub
"""

helps['eventhubs eventhub authorization-rule create'] = """
type: command
short-summary: Creates Authorizationrule for the given Eventhub
examples:
  - name: Creates Authorizationrule
    text: az eventhubs eventhub authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myauthorule --rights Listen
"""

helps['eventhubs eventhub authorization-rule delete'] = """
type: command
short-summary: Deletes the Authorizationrule of Eventhub.
examples:
  - name: Deletes the Authorizationrule of Eventhub.
    text: az eventhubs eventhub authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myauthorule
"""

helps['eventhubs eventhub authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorizationrule connection strings for Eventhub
"""

helps['eventhubs eventhub authorization-rule keys list'] = """
type: command
short-summary: Shows the connection strings of Authorizationrule for the Eventhub.
examples:
  - name: Shows the connection strings of Authorizationrule for the eventhub.
    text: az eventhubs eventhub authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myauthorule
"""

helps['eventhubs eventhub authorization-rule keys renew'] = """
type: command
short-summary: Regenerate the connection strings of Authorizationrule for the namespace.
examples:
  - name: Regenerate the connection strings of Authorizationrule for the namespace.
    text: az eventhubs eventhub authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myauthorule --key PrimaryKey
"""

helps['eventhubs eventhub authorization-rule list'] = """
type: command
short-summary: shows the list of Authorization-rules by Eventhub
examples:
  - name: shows the list of Authorization-rules by Eventhub
    text: az eventhubs eventhub authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub
"""

helps['eventhubs eventhub authorization-rule show'] = """
type: command
short-summary: shows the details of Authorizationrule
examples:
  - name: shows the details of Authorizationrule
    text: az eventhubs eventhub authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myauthorule
"""

helps['eventhubs eventhub authorization-rule update'] = """
type: command
short-summary: Updates Authorizationrule for the given Eventhub
examples:
  - name: Updates Authorizationrule
    text: az eventhubs eventhub authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myauthorule --rights Send
"""

helps['eventhubs eventhub consumer-group'] = """
type: group
short-summary: Manage Azure Event Hubs consumergroup
"""

helps['eventhubs eventhub consumer-group create'] = """
type: command
short-summary: Creates the EventHub ConsumerGroup
examples:
  - name: Create EventHub ConsumerGroup.
    text: az eventhubs eventhub consumer-group create --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myconsumergroup
"""

helps['eventhubs eventhub consumer-group delete'] = """
type: command
short-summary: Deletes the ConsumerGroup
examples:
  - name: Deletes the ConsumerGroup
    text: az eventhubs eventhub consumer-group delete --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myconsumergroup
"""

helps['eventhubs eventhub consumer-group list'] = """
type: command
short-summary: List the ConsumerGroup by Eventhub
examples:
  - name: List the ConsumerGroup by Eventhub.
    text: az eventhubs eventhub consumer-group list --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub
"""

helps['eventhubs eventhub consumer-group show'] = """
type: command
short-summary: Shows the ConsumerGroup Details
examples:
  - name: Shows the ConsumerGroup details.
    text: az eventhubs eventhub consumer-group show --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myconsumergroup
"""

helps['eventhubs eventhub consumer-group update'] = """
type: command
short-summary: Updates the EventHub ConsumerGroup
examples:
  - name: Updates a ConsumerGroup.
    text: az eventhubs eventhub consumer-group update --resource-group myresourcegroup --namespace-name mynamespace --eventhub-name myeventhub --name myconsumergroup --user-metadata MyUserMetadata
"""

helps['eventhubs eventhub create'] = """
type: command
short-summary: Creates the EventHubs Eventhub
examples:
  - name: Create a new Eventhub.
    text: az eventhubs eventhub create --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub --message-retention 4 --partition-count 15
"""

helps['eventhubs eventhub delete'] = """
type: command
short-summary: Deletes the Eventhub
examples:
  - name: Deletes the Eventhub
    text: az eventhubs eventhub delete --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub
"""

helps['eventhubs eventhub list'] = """
type: command
short-summary: List the EventHub by Namepsace
examples:
  - name: Get the Eventhubs by Namespace.
    text: az eventhubs eventhub list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['eventhubs eventhub show'] = """
type: command
short-summary: shows the Eventhub Details
examples:
  - name: Shows the Eventhub details.
    text: az eventhubs eventhub show --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub
"""

helps['eventhubs eventhub update'] = """
type: command
short-summary: Updates the EventHubs Eventhub
examples:
  - name: Updates a new Eventhub.
    text: az eventhubs eventhub update --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub --message-retention 3 --partition-count 12
"""

helps['eventhubs georecovery-alias'] = """
type: group
short-summary: Manage Azure EventHubs Geo Recovery configuration Alias
"""

helps['eventhubs georecovery-alias authorization-rule'] = """
type: group
short-summary: Manage Azure EventHubs Authorizationrule for Geo Recovery configuration Alias
"""

helps['eventhubs georecovery-alias authorization-rule keys'] = """
type: group
short-summary: Manage Azure Event Hubs Authorizationrule connection strings for Geo Recovery configuration Alias
"""

helps['eventhubs georecovery-alias authorization-rule keys list'] = """
type: command
short-summary: Shows the keys and connection strings of Authorizationrule for the EventHubs Namespace
examples:
  - name: Shows the keys and connection strings of Authorizationrule for the namespace.
    text: az eventhubs georecovery-alias authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --alias myaliasname
"""

helps['eventhubs georecovery-alias authorization-rule list'] = """
type: command
short-summary: List of Authorizationrule by EventHubs Namespace
examples:
  - name: List of Authorizationrule by EventHubs Namespace
    text: az eventhubs georecovery-alias authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --alias myaliasname
"""

helps['eventhubs georecovery-alias authorization-rule show'] = """
type: command
short-summary: Show properties of EventHubs Geo-Disaster Recovery Configuration Alias and Namespace Authorizationrule
examples:
  - name: Show properties Authorizationrule by EventHubs Namespace
    text: az eventhubs georecovery-alias authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['eventhubs georecovery-alias break-pair'] = """
type: command
short-summary: Disables Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces
examples:
  - name: Disables Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces
    text: az eventhubs georecovery-alias break-pair --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['eventhubs georecovery-alias delete'] = """
type: command
short-summary: Delete Geo-Disaster Recovery Configuration Alias
examples:
  - name: Delete Geo-Disaster Recovery Configuration Alias
    text: az eventhubs georecovery-alias delete --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['eventhubs georecovery-alias exists'] = """
type: command
short-summary: Check the availability of Geo-Disaster Recovery Configuration Alias Name
examples:
  - name: Check the availability of Geo-Disaster Recovery Configuration Alias Name
    text: az eventhubs georecovery-alias exists --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['eventhubs georecovery-alias fail-over'] = """
type: command
short-summary: Invokes Geo-Disaster Recovery Configuration Alias to point to the secondary namespace
examples:
  - name: Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace
    text: az eventhubs georecovery-alias fail-over --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['eventhubs georecovery-alias set'] = """
type: command
short-summary: Sets a Geo-Disaster Recovery Configuration Alias for the give Namespace
examples:
  - name: Sets Geo-Disaster Recovery Configuration Alias for the give Namespace
    text: az eventhubs georecovery-alias set --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname --partner-namespace resourcearmid
"""

helps['eventhubs georecovery-alias show'] = """
type: command
short-summary: shows properties of Geo-Disaster Recovery Configuration Alias for Primay or Secondary Namespace
examples:
  - name: Shows properties of Geo-Disaster Recovery Configuration Alias of the Primary Namespace
    text: az eventhubs georecovery-alias show --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
  - name: Shows properties of Geo-Disaster Recovery Configuration Alias of the Secondary Namespace
    text: az eventhubs georecovery-alias show --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['eventhubs namespace'] = """
type: group
short-summary: Manage Azure EventHubs namespace and Authorizationrule
"""

helps['eventhubs namespace authorization-rule'] = """
type: group
short-summary: Manage Azure EventHubs Authorizationrule for Namespace
"""

helps['eventhubs namespace authorization-rule create'] = """
type: command
short-summary: Creates Authorizationrule for the given Namespace
examples:
  - name: Creates Authorizationrule
    text: az eventhubs namespace authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send Listen
"""

helps['eventhubs namespace authorization-rule delete'] = """
type: command
short-summary: Deletes the Authorizationrule of the namespace.
examples:
  - name: Deletes the Authorizationrule of the namespace.
    text: az eventhubs namespace authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['eventhubs namespace authorization-rule keys'] = """
type: group
short-summary: Manage Azure EventHubs Authorizationrule connection strings for Namespace
"""

helps['eventhubs namespace authorization-rule keys list'] = """
type: command
short-summary: Shows the connection strings for namespace
examples:
  - name: Shows the connection strings of Authorizationrule for the namespace.
    text: az eventhubs namespace authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['eventhubs namespace authorization-rule keys renew'] = """
type: command
short-summary: Regenerate the connection strings of Authorizationrule for the namespace.
examples:
  - name: Regenerate the connection strings of Authorizationrule for the namespace.
    text: az eventhubs namespace authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --key PrimaryKey
"""

helps['eventhubs namespace authorization-rule list'] = """
type: command
short-summary: Shows the list of Authorizationrule by Namespace
examples:
  - name: Shows the list of Authorizationrule by Namespace
    text: az eventhubs namespace authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['eventhubs namespace authorization-rule show'] = """
type: command
short-summary: Shows the details of Authorizationrule
examples:
  - name: Shows the details of Authorizationrule
    text: az eventhubs namespace authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['eventhubs namespace authorization-rule update'] = """
type: command
short-summary: Updates Authorizationrule for the given Namespace
examples:
  - name: Updates Authorizationrule
    text: az eventhubs namespace authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send
"""

helps['eventhubs namespace create'] = """
type: command
short-summary: Creates the EventHubs Namespace
examples:
  - name: Creates a new namespace.
    text: az eventhubs namespace create --resource-group myresourcegroup --name mynamespace --location westus --tags tag1=value1 tag2=value2 --sku Standard --enable-auto-inflate --maximum-throughput-units 20
"""

helps['eventhubs namespace delete'] = """
type: command
short-summary: Deletes the Namespaces
examples:
  - name: Deletes the Namespace
    text: az eventhubs namespace delete --resource-group myresourcegroup --name mynamespace
"""

helps['eventhubs namespace exists'] = """
type: command
short-summary: check for the availability of the given name for the Namespace
examples:
  - name: Create a new topic.
    text: az eventhubs namespace exists --name mynamespace
"""

helps['eventhubs namespace list'] = """
type: command
short-summary: Lists the EventHubs Namespaces
examples:
  - name: List the Event Hubs Namespaces by resource group.
    text: az eventhubs namespace list --resource-group myresourcegroup
  - name: Get the Namespaces by Subscription.
    text: az eventhubs namespace list
"""

helps['eventhubs namespace network-rule'] = """
type: group
short-summary: Manage Azure EventHubs networkruleset for namespace
"""

helps['eventhubs namespace network-rule add'] = """
type: command
short-summary: Add a network rule for a namespace.
examples:
  - name: add a VirtualNetwork rule in NetworkruleSet for a namespace
    text: az eventhubs namespace network-rule add --resource-group myresourcegroup --namespace-name mynamespace --subnet /subscriptions/{subscriptionid}/resourcegroups/{resourcegroupname}/providers/Microsoft.Network/virtualNetworks/{virtualnetworkname}/subnets/{subnetname} --ignore-missing-endpoint True
  - name: add a IP rule in NetworkruleSet for a namespace
    text: az eventhubs namespace network-rule add --resource-group myresourcegroup --namespace-name mynamespace --ip-address 10.6.0.0/24 --action Allow
"""

helps['eventhubs namespace network-rule list'] = """
type: command
short-summary: Show properties of Network rule of the given Namespace.
examples:
  - name: Show properties of Network rule of the given Namespace
    text: az eventhubs namespace network-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['eventhubs namespace network-rule remove'] = """
type: command
short-summary: Remove network rule for a namespace
examples:
  - name: remove VirtualNetwork rule from NetworkruleSet for a namespace
    text: az eventhubs namespace network-rule remove --resource-group myresourcegroup --namespace-name mynamespace --subnet /subscriptions/{subscriptionid}/resourcegroups/{resourcegroupname}/providers/Microsoft.Network/virtualNetworks/{virtualnetworkname}/subnets/{subnetname}
  - name: remove IP rule from NetworkruleSet for a namespace
    text: az eventhubs namespace network-rule remove --resource-group myresourcegroup --namespace-name mynamespace --ip-address 10.6.0.0/24
"""

helps['eventhubs namespace show'] = """
type: command
short-summary: shows the Event Hubs Namespace Details
examples:
  - name: shows the Namespace details.
    text: az eventhubs namespace show --resource-group myresourcegroup --name mynamespace
"""

helps['eventhubs namespace update'] = """
type: command
short-summary: Updates the EventHubs Namespace
examples:
  - name: Update a new namespace.
    text: az eventhubs namespace update --resource-group myresourcegroup --name mynamespace --tags tag=value --enable-auto-inflate True
"""

helps['extension'] = """
type: group
short-summary: Manage and update CLI extensions.
"""

helps['extension add'] = """
type: command
short-summary: Add an extension.
examples:
  - name: Add extension by name
    text: az extension add --name anextension
  - name: Add extension from URL
    text: az extension add --source https://contoso.com/anextension-0.0.1-py2.py3-none-any.whl
  - name: Add extension from local disk
    text: az extension add --source ~/anextension-0.0.1-py2.py3-none-any.whl
  - name: Add extension from local disk and use pip proxy for dependencies
    text: az extension add --source ~/anextension-0.0.1-py2.py3-none-any.whl --pip-proxy https://user:pass@proxy.server:8080
"""

helps['extension list'] = """
type: command
short-summary: List the installed extensions.
"""

helps['extension list-available'] = """
type: command
short-summary: List publicly available extensions.
examples:
  - name: List all publicly available extensions
    text: az extension list-available
  - name: List details on a particular extension
    text: az extension list-available --show-details --query anextension
"""

helps['extension remove'] = """
type: command
short-summary: Remove an extension.
"""

helps['extension show'] = """
type: command
short-summary: Show an extension.
"""

helps['extension update'] = """
type: command
short-summary: Update an extension.
examples:
  - name: Update an extension by name
    text: az extension update --name anextension
  - name: Update an extension by name and use pip proxy for dependencies
    text: az extension update --name anextension --pip-proxy https://user:pass@proxy.server:8080
"""

helps['feature'] = """
type: group
short-summary: Manage resource provider features.
"""

helps['feature list'] = """
type: command
short-summary: List preview features.
examples:
  - name: List preview features
    text: az feature list
    crafted: true
"""

helps['feature register'] = """
type: command
short-summary: register a preview feature.
examples:
  - name: register the "Shared Image Gallery" feature
    text: az feature register --namespace Microsoft.Compute --name GalleryPreview
"""

helps['feedback'] = """
type: command
short-summary: Send feedback to the Azure CLI Team!
"""

helps['find'] = """
type: command
short-summary: I'm an AI robot, my advice is based on our Azure documentation as well as the usage patterns of Azure CLI and Azure ARM users. Using me improves Azure products and documentation.
examples:
  - name: Give me any Azure CLI group and I’ll show the most popular commands within the group.
    text: |
        az find "az storage"
  - name: Give me any Azure CLI command and I’ll show the most popular parameters and subcommands.
    text: |
        az find "az monitor activity-log list"
  - name: You can also enter a search term, and I'll try to help find the best commands.
    text: |
        az find "arm template"
"""

helps['functionapp'] = """
type: group
short-summary: Manage function apps. To install the Azure Functions Core tools see https://github.com/Azure/azure-functions-core-tools
"""

helps['functionapp config'] = """
type: group
short-summary: Configure a function app.
"""

helps['functionapp config appsettings'] = """
type: group
short-summary: Configure function app settings.
"""

helps['functionapp config appsettings delete'] = """
type: command
short-summary: Delete a function app's settings.
examples:
  - name: Delete a function app's settings. (autogenerated)
    text: az functionapp config appsettings delete --name MyFunctionApp --resource-group MyResourceGroup --setting-names {setting-names}
    crafted: true
"""

helps['functionapp config appsettings list'] = """
type: command
short-summary: Show settings for a function app.
examples:
  - name: Show settings for a function app. (autogenerated)
    text: az functionapp config appsettings list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config appsettings set'] = """
type: command
short-summary: Update a function app's settings.
examples:
  - name: Update a function app's settings.
    text: |
        az functionapp config appsettings set --name MyFunctionApp --resource-group MyResourceGroup --settings "AzureWebJobsStorage=$storageConnectionString"
"""

helps['functionapp config container'] = """
type: group
short-summary: Manage function app container settings.
"""

helps['functionapp config container delete'] = """
type: command
short-summary: Delete a function app container's settings.
"""

helps['functionapp config container set'] = """
type: command
short-summary: Set a function app container's settings.
examples:
  - name: Set a function app container's settings. (autogenerated)
    text: az functionapp config container set --docker-custom-image-name MyDockerCustomImage --docker-registry-server-password StrongPassword --docker-registry-server-url https://{azure-container-registry-name}.azurecr.io --docker-registry-server-user DockerUserId --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config container show'] = """
type: command
short-summary: Get details of a function app container's settings.
examples:
  - name: Get details of a function app container's settings. (autogenerated)
    text: az functionapp config container show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config hostname'] = """
type: group
short-summary: Configure hostnames for a function app.
"""

helps['functionapp config hostname add'] = """
type: command
short-summary: Bind a hostname to a function app.
examples:
  - name: Bind a hostname to a function app. (autogenerated)
    text: az functionapp config hostname add --hostname www.yourdomain.com --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config hostname delete'] = """
type: command
short-summary: Unbind a hostname from a function app.
"""

helps['functionapp config hostname get-external-ip'] = """
type: command
short-summary: Get the external-facing IP address for a function app.
"""

helps['functionapp config hostname list'] = """
type: command
short-summary: List all hostname bindings for a function app.
"""

helps['functionapp config set'] = """
type: command
short-summary: Set the function app's configuration.
"""

helps['functionapp config show'] = """
type: command
short-summary: Get the details of a function app's configuration.
examples:
  - name: Get the details of a web app's configuration. (autogenerated)
    text: az functionapp config show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config ssl'] = """
type: group
short-summary: Configure SSL certificates.
"""

helps['functionapp config ssl bind'] = """
type: command
short-summary: Bind an SSL certificate to a function app.
examples:
  - name: Bind an SSL certificate to a function app. (autogenerated)
    text: az functionapp config ssl bind --certificate-thumbprint {certificate-thumbprint} --name MyFunctionApp --resource-group MyResourceGroup --ssl-type SNI
    crafted: true
"""

helps['functionapp config ssl delete'] = """
type: command
short-summary: Delete an SSL certificate from a function app.
"""

helps['functionapp config ssl list'] = """
type: command
short-summary: List SSL certificates for a function app.
examples:
  - name: List SSL certificates for a function app. (autogenerated)
    text: az functionapp config ssl list --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config ssl unbind'] = """
type: command
short-summary: Unbind an SSL certificate from a function app.
"""

helps['functionapp config ssl upload'] = """
type: command
short-summary: Upload an SSL certificate to a function app.
examples:
  - name: Upload an SSL certificate to a function app. (autogenerated)
    text: az functionapp config ssl upload --certificate-file {certificate-file} --certificate-password {certificate-password} --name MyFunctionApp     --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp cors'] = """
type: group
short-summary: Manage Cross-Origin Resource Sharing (CORS)
"""

helps['functionapp cors add'] = """
type: command
short-summary: Add allowed origins
examples:
  - name: add a new allowed origin
    text: >
        az functionapp cors add -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
"""

helps['functionapp cors remove'] = """
type: command
short-summary: Remove allowed origins
examples:
  - name: remove an allowed origin
    text: >
        az functionapp cors remove -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
  - name: remove all allowed origins
    text: >
        az functionapp cors remove -g {myRG} -n {myAppName} --allowed-origins
"""

helps['functionapp cors show'] = """
type: command
short-summary: show allowed origins
examples:
  - name: show allowed origins (autogenerated)
    text: az functionapp cors show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp create'] = """
type: command
short-summary: Create a function app.
long-summary: The function app's name must be able to produce a unique FQDN as AppName.azurewebsites.net.
examples:
  - name: Create a basic function app.
    text: >
        az functionapp create -g MyResourceGroup  -p MyPlan -n MyUniqueAppName -s MyStorageAccount
  - name: Create a function app. (autogenerated)
    text: az functionapp create --consumption-plan-location westus --name MyUniqueAppName --os-type Windows --resource-group MyResourceGroup --runtime dotnet --storage-account MyStorageAccount
    crafted: true
"""

helps['functionapp delete'] = """
type: command
short-summary: Delete a function app.
examples:
  - name: Delete a function app. (autogenerated)
    text: az functionapp delete --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment'] = """
type: group
short-summary: Manage function app deployments.
"""

helps['functionapp deployment container'] = """
type: group
short-summary: Manage container-based continuous deployment.
"""

helps['functionapp deployment container config'] = """
type: command
short-summary: Configure continuous deployment via containers.
examples:
  - name: Configure continuous deployment via containers (autogenerated)
    text: az functionapp deployment container config --enable-cd true --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment container show-cd-url'] = """
type: command
short-summary: Get the URL which can be used to configure webhooks for continuous deployment.
examples:
  - name: Get the URL which can be used to configure webhooks for continuous deployment. (autogenerated)
    text: az functionapp deployment container show-cd-url --ids {ids}
    crafted: true
"""

helps['functionapp deployment list-publishing-credentials'] = """
type: command
short-summary: Get the details for available function app publishing credentials.
examples:
  - name: Get the details for available function app deployment publishing credentials.
    text: az functionapp deployment list-publishing-credentials --name MyFunctionApp   --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment list-publishing-profiles'] = """
type: command
short-summary: Get the details for available function app deployment profiles.
examples:
  - name: Get the details for available function app deployment profiles. (autogenerated)
    text: az functionapp deployment list-publishing-profiles --name MyFunctionApp   --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment slot'] = """
type: group
short-summary: Manage function app deployment slots.
"""

helps['functionapp deployment slot auto-swap'] = """
type: command
short-summary: Configure deployment slot auto swap.
"""

helps['functionapp deployment slot create'] = """
type: command
short-summary: Create a deployment slot.
examples:
  - name: Create a deployment slot. (autogenerated)
    text: az functionapp deployment slot create --name MyFunctionapp --resource-group MyResourceGroup --slot staging
    crafted: true
"""

helps['functionapp deployment slot delete'] = """
type: command
short-summary: Delete a deployment slot.
examples:
  - name: Delete a deployment slot. (autogenerated)
    text: az functionapp deployment slot delete --name MyFunctionapp --resource-group MyResourceGroup --slot staging
    crafted: true
"""

helps['functionapp deployment slot list'] = """
type: command
short-summary: List all deployment slots.
examples:
  - name: List all deployment slots. (autogenerated)
    text: az functionapp deployment slot list --name MyFunctionapp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment slot swap'] = """
type: command
short-summary: Change deployment slots for a function app.
examples:
  - name: Swap a staging slot into production for the MyUniqueApp function app.
    text: >
        az functionapp deployment slot swap  -g MyResourceGroup -n MyUniqueApp --slot staging \\
            --target-slot production
"""

helps['functionapp deployment source'] = """
type: group
short-summary: Manage function app deployment via source control.
"""

helps['functionapp deployment source config'] = """
type: command
short-summary: Manage deployment from git or Mercurial repositories.
examples:
  - name: Manage deployment from git or Mercurial repositories. (autogenerated)
    text: az functionapp deployment source config --branch master --manual-integration --name MyFunctionApp --repo-url https://github.com/Azure-Samples/function-image-upload-resize --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment source config-local-git'] = """
type: command
short-summary: Get a URL for a git repository endpoint to clone and push to for function app deployment.
examples:
  - name: Get an endpoint and add it as a git remote.
    text: >
        az functionapp deployment source config-local-git \\
            -g MyResourceGroup -n MyUniqueApp

        git remote add azure \\
            https://{deploy_user_name}@MyUniqueApp.scm.azurewebsites.net/MyUniqueApp.git
"""

helps['functionapp deployment source config-zip'] = """
type: command
short-summary: Perform deployment using the kudu zip push deployment for a function app.
long-summary: >
    By default Kudu assumes that zip deployments do not require any build-related actions like
    npm install or dotnet publish. This can be overridden by including an .deployment file in your
    zip file with the following content '[config] SCM_DO_BUILD_DURING_DEPLOYMENT = true',
    to enable Kudu detection logic and build script generation process.
    See https://github.com/projectkudu/kudu/wiki/Configurable-settings#enabledisable-build-actions-preview.
    Alternately the setting can be enabled using the az functionapp config appsettings set command.
examples:
  - name: Perform deployment by using zip file content.
    text: >
        az functionapp deployment source config-zip \\
            -g {myRG}} -n {myAppName} \\
            --src {zipFilePathLocation}
"""

helps['functionapp deployment source delete'] = """
type: command
short-summary: Delete a source control deployment configuration.
"""

helps['functionapp deployment source show'] = """
type: command
short-summary: Get the details of a source control deployment configuration.
examples:
  - name: Get the details of a source control deployment configuration. (autogenerated)
    text: az functionapp deployment source show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment source sync'] = """
type: command
short-summary: Synchronize from the repository. Only needed under manual integration mode.
examples:
  - name: Synchronize from the repository. Only needed under manual integration mode. (autogenerated)
    text: az functionapp deployment source sync --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment user'] = """
type: group
short-summary: Manage user credentials for deployment.
"""

helps['functionapp deployment user set'] = """
type: command
short-summary: Update deployment credentials.
long-summary: All function and web apps in the subscription will be impacted since they share the same deployment credentials.
examples:
  - name: Set FTP and git deployment credentials for all apps.
    text: >
        az functionapp deployment user set --user-name MyUserName
"""

helps['functionapp devops-pipeline'] = """
type: group
short-summary: Azure Function specific integration with Azure DevOps. Please visit https://aka.ms/functions-azure-devops for more information.
"""

helps['functionapp devops-pipeline create'] = """
type: command
short-summary: Create an Azure DevOps pipeline for a function app.
examples:
  - name: create an Azure Pipeline to a function app.
    text: >
        az functionapp devops-pipeline create --functionapp-name FunctionApp
  - name: create an Azure Pipeline from a Github function app repository.
    text: >
        az functionapp devops-pipeline create --github-repository GithubOrganization/GithubRepository --github-pat GithubPersonalAccessToken
  - name: create an Azure Pipeline with specific Azure DevOps organization and project
    text: >
        az functionapp devops-pipeline create --organization-name AzureDevOpsOrganization --project-name AzureDevOpsProject
"""

helps['functionapp hybrid-connection'] = """
type: group
short-summary: methods that list, add and remove hybrid-connections from functionapp
"""

helps['functionapp hybrid-connection add'] = """
type: command
short-summary: add a hybrid-connection to a functionapp
examples:
  - name: add a hybrid-connection to a functionapp
    text: az functionapp hybrid-connection add -g MyResourceGroup -n MyWebapp --namespace [HybridConnectionNamespace] --hybrid-connection [HybridConnectionName] -s [slot]
"""

helps['functionapp hybrid-connection list'] = """
type: command
short-summary: list the hybrid-connections on a functionapp
examples:
  - name: list the hybrid-connections on a functionapp
    text: az functionapp hybrid-connection list -g MyResourceGroup -n MyWebapp -s [slot]
"""

helps['functionapp hybrid-connection remove'] = """
type: command
short-summary: remove a hybrid-connection from a functionapp
examples:
  - name: remove a hybrid-connection from a functionapp
    text: az functionapp hybrid-connection remove -g MyResourceGroup -n MyWebapp --namespace [HybridConnectionNamespace] --hybrid-connection [HybridConnectionName] -s [slot]
"""

helps['functionapp identity'] = """
type: group
short-summary: manage web app's managed service identity
"""

helps['functionapp identity assign'] = """
type: command
short-summary: assign or disable managed service identity to the web app
examples:
  - name: assign local identity and assign a reader role to the current resource group.
    text: >
        az functionapp identity assign -g MyResourceGroup -n MyUniqueApp --role reader --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/MyResourceGroup
  - name: enable identity for the web app.
    text: >
        az functionapp identity assign -g MyResourceGroup -n MyUniqueApp
"""

helps['functionapp identity remove'] = """
type: command
short-summary: Disable web app's managed service identity
"""

helps['functionapp identity show'] = """
type: command
short-summary: display web app's managed service identity
examples:
  - name: display functionapp's managed service identity (autogenerated)
    text: az functionapp identity show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp list'] = """
type: command
short-summary: List function apps.
examples:
  - name: List default host name and state for all function apps.
    text: >
        az functionapp list --query "[].{hostName: defaultHostName, state: state}"
  - name: List all running function apps.
    text: >
        az functionapp list --query "[?state=='Running']"
"""

helps['functionapp list-consumption-locations'] = """
type: command
short-summary: List available locations for running function apps.
"""

helps['functionapp plan'] = """
type: group
short-summary: Manage App Service Plans for an Azure Function
"""

helps['functionapp plan create'] = """
type: command
short-summary: Create an App Service Plan for an Azure Function.
examples:
  - name: Create an elastic premium app service plan with burst out capability up to 10 instances.
    text: >
        az functionapp plan create -g MyResourceGroup -n MyPlan --min-instances 1 --max-burst 10 --sku EP1
  - name: Create a basic app service plan.
    text: >
        az functionapp plan create -g MyResourceGroup -n MyPlan --sku B1
"""

helps['functionapp plan delete'] = """
type: command
short-summary: Delete an App Service Plan.
"""

helps['functionapp plan list'] = """
type: command
short-summary: List App Service Plans.
examples:
  - name: List all Elastic Premium 1 tier App Service plans.
    text: >
        az functionapp plan list --query "[?sku.tier=='EP1']"
"""

helps['functionapp plan show'] = """
type: command
short-summary: Get the App Service Plans for a resource group or a set of resource groups.
examples:
  - name: Get the app service plans for a resource group or a set of resource groups. (autogenerated)
    text: az functionapp plan show --name MyAppServicePlan --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp plan update'] = """
type: command
short-summary: Update an App Service plan for an Azure Function.
examples:
  - name: Update an app service plan to EP2 sku with twenty maximum workers.
    text: >
        az functionapp plan update -g MyResourceGroup -n MyPlan --max-burst 20 --sku EP2
"""

helps['functionapp restart'] = """
type: command
short-summary: Restart a function app.
examples:
  - name: Restart a function app. (autogenerated)
    text: az functionapp restart --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp show'] = """
type: command
short-summary: Get the details of a function app.
examples:
  - name: Get the details of a function app. (autogenerated)
    text: az functionapp show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp start'] = """
type: command
short-summary: Start a function app.
examples:
  - name: Start a function app. (autogenerated)
    text: az functionapp start --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp stop'] = """
type: command
short-summary: Stop a function app.
examples:
  - name: Stop a function app. (autogenerated)
    text: az functionapp stop --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp update'] = """
type: command
short-summary: Update a function app.
examples:
  - name: Update a function app. (autogenerated)
    text: az functionapp update --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp vnet-integration'] = """
type: group
short-summary: methods that list, add, and remove virtual networks integrations from a functionapp
"""

helps['functionapp vnet-integration add'] = """
type: command
short-summary: add a regional virtual network integration to a functionapp
examples:
  - name: add a regional virtual network integration to a functionapp
    text: az functionapp vnet-integration add -g MyResourceGroup -n MyFunctionapp --vnet MyVnetName --subnet MySubnetName -s [slot]
"""

helps['functionapp vnet-integration list'] = """
type: command
short-summary: list the virtual network integrations on a functionapp
examples:
  - name: list the virtual networks integrations on a functionapp
    text: az functionapp vnet-integration list -g MyResourceGroup -n MyFunctionapp -s [slot]
"""

helps['functionapp vnet-integration remove'] = """
type: command
short-summary: remove a regional virtual network integration from functionapp
examples:
  - name: remove a regional virtual network integration from functionapp
    text: az functionapp vnet-integration remove -g MyResourceGroup -n MyFunctionapp -s [slot]
"""

helps['group'] = """
type: group
short-summary: Manage resource groups and template deployments.
"""

helps['group create'] = """
type: command
short-summary: Create a new resource group.
examples:
  - name: Create a new resource group in the West US region.
    text: >
        az group create -l westus -n MyResourceGroup
"""

helps['group delete'] = """
type: command
short-summary: Delete a resource group.
examples:
  - name: Delete a resource group.
    text: >
        az group delete -n MyResourceGroup
"""

helps['group deployment'] = """
type: group
short-summary: Manage Azure Resource Manager deployments.
"""

helps['group deployment create'] = """
type: command
short-summary: Start a deployment.
parameters:
  - name: --parameters
    short-summary: Supply deployment parameter values.
    long-summary: >
        Parameters may be supplied from a file using the `@{path}` syntax, a JSON string, or as <KEY=VALUE> pairs. Parameters are evaluated in order, so when a value is assigned twice, the latter value will be used.
        It is recommended that you supply your parameters file first, and then override selectively using KEY=VALUE syntax.
examples:
  - name: Create a deployment from a remote template file, using parameters from a local JSON file.
    text: >
        az group deployment create -g MyResourceGroup --template-uri https://myresource/azuredeploy.json --parameters @myparameters.json
  - name: Create a deployment from a local template file, using parameters from a JSON string.
    text: |
        az group deployment create -g MyResourceGroup --template-file azuredeploy.json --parameters '{
                "location": {
                    "value": "westus"
                }
            }'
  - name: Create a deployment from a local template, using a local parameter file, a remote parameter file, and selectively overriding key/value pairs.
    text: >
        az group deployment create -g MyResourceGroup --template-file azuredeploy.json \\
            --parameters @params.json --parameters https://mysite/params.json --parameters MyValue=This MyArray=@array.json
"""

helps['group deployment export'] = """
type: command
short-summary: Export the template used for a deployment.
examples:
  - name: Export the template used for a deployment. (autogenerated)
    text: az group deployment export --name MyDeployment --resource-group MyResourceGroup
    crafted: true
"""

helps['group deployment operation'] = """
type: group
short-summary: Manage deployment operations.
"""

helps['group deployment validate'] = """
type: command
short-summary: Validate whether a template is syntactically correct.
parameters:
  - name: --parameters
    short-summary: Supply deployment parameter values.
    long-summary: >
        Parameters may be supplied from a file using the `@{path}` syntax, a JSON string, or as <KEY=VALUE> pairs. Parameters are evaluated in order, so when a value is assigned twice, the latter value will be used.
        It is recommended that you supply your parameters file first, and then override selectively using KEY=VALUE syntax.
examples:
  - name: Validate whether a template is syntactically correct. (autogenerated)
    text: |-
        az group deployment validate --parameters '{
                "location": {
                    "value": "westus"
                }
            }' --resource-group MyResourceGroup --template-file storage.json
    crafted: true
"""

helps['group deployment wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a deployment condition is met.
examples:
  - name: Place the CLI in a waiting state until a deployment condition is met. (autogenerated)
    text: az group deployment wait --name MyDeployment --resource-group MyResourceGroup --updated
    crafted: true
  - name: Place the CLI in a waiting state until a deployment condition is met. (autogenerated)
    text: az group deployment wait --created --name MyDeployment --resource-group MyResourceGroup
    crafted: true
"""

helps['group exists'] = """
type: command
short-summary: Check if a resource group exists.
examples:
  - name: Check if 'MyResourceGroup' exists.
    text: >
        az group exists -n MyResourceGroup
"""

helps['group list'] = """
type: command
short-summary: List resource groups.
examples:
  - name: List all resource groups located in the West US region.
    text: >
        az group list --query "[?location=='westus']"
"""

helps['group lock'] = """
type: group
short-summary: Manage Azure resource group locks.
"""

helps['group lock create'] = """
type: command
short-summary: Create a resource group lock.
examples:
  - name: Create a read-only resource group level lock.
    text: >
        az group lock create --lock-type ReadOnly -n lockName -g MyResourceGroup
"""

helps['group lock delete'] = """
type: command
short-summary: Delete a resource group lock.
examples:
  - name: Delete a resource group lock
    text: >
        az group lock delete --name lockName -g MyResourceGroup
"""

helps['group lock list'] = """
type: command
short-summary: List lock information in the resource-group.
examples:
  - name: List out all locks on the resource group level
    text: >
        az group lock list -g MyResourceGroup
"""

helps['group lock show'] = """
type: command
short-summary: Show the details of a resource group lock
examples:
  - name: Show a resource group level lock
    text: >
        az group lock show -n lockname -g MyResourceGroup
"""

helps['group lock update'] = """
type: command
short-summary: Update a resource group lock.
examples:
  - name: Update a resource group lock with new notes and type
    text: >
        az group lock update --name lockName -g MyResourceGroup --notes newNotesHere --lock-type CanNotDelete
"""

helps['group update'] = """
type: command
short-summary: Update a resource group.
examples:
  - name: Update a resource group. (autogenerated)
    text: |-
        az group update --resource-group MyResourceGroup --set tags.CostCenter='{"Dept":"IT","Environment":"Test"}'
    crafted: true
"""

helps['group wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the resource group is met.
examples:
  - name: Place the CLI in a waiting state until a condition of the resource group is met. (autogenerated)
    text: az group wait --created  --resource-group MyResourceGroup
    crafted: true
  - name: Place the CLI in a waiting state until a condition of the resource group is met. (autogenerated)
    text: az group wait --deleted --resource-group MyResourceGroup
    crafted: true
"""

helps['hdinsight'] = """
type: group
short-summary: Manage HDInsight resources.
"""

helps['hdinsight application'] = """
type: group
short-summary: Manage HDInsight applications.
"""

helps['hdinsight application create'] = """
type: command
short-summary: Create an application for a HDInsight cluster.
examples:
  - name: Create an application with a script URI.
    text: |-
        az hdinsight application create -g MyResourceGroup -n MyApplication \\
        --cluster-name MyCluster \\
        --script-uri https://hdiconfigactions.blob.core.windows.net/linuxhueconfigactionv02/install-hue-uber-v02.sh \\
        --script-action-name MyScriptAction \\
        --script-parameters '"-version latest -port 20000"'
  - name: Create an application with a script URI and specified edge node size.
    text: |-
        az hdinsight application create -g MyResourceGroup -n MyApplication \\
        --cluster-name MyCluster \\
        --script-uri https://hdiconfigactions.blob.core.windows.net/linuxhueconfigactionv02/install-hue-uber-v02.sh \\
        --script-action-name MyScriptAction \\
        --script-parameters "-version latest -port 20000" \\
        --edgenode-size Standard_D4_v2
  - name: Create an application with HTTPS Endpoint.
    text: |-
        az hdinsight application create -g MyResourceGroup -n MyApplication \\
        --cluster-name MyCluster \\
        --script-uri https://hdiconfigactions.blob.core.windows.net/linuxhueconfigactionv02/install-hue-uber-v02.sh \\
        --script-action-name MyScriptAction \\
        --script-parameters "-version latest -port 20000" \\
        --destination-port 8888 \\
        --sub-domain-suffix was
"""

helps['hdinsight application wait'] = """
type: command
short-summary: Place the CLI in a waiting state until an operation is complete.
"""

helps['hdinsight create'] = """
type: command
short-summary: Create a new cluster.
examples:
  - name: Create a cluster with an existing storage account.
    text: |-
        az hdinsight create -t spark -g MyResourceGroup -n MyCluster \\
        -p "HttpPassword1234!" \\
        --storage-account MyStorageAccount
  - name: Create a cluster with the Enterprise Security Package (ESP).
    text: |-
        az hdinsight create --esp -t spark -g MyResourceGroup -n MyCluster \\
        -p "HttpPassword1234!" \\
        --storage-account MyStorageAccount \\
        --subnet "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyRG/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/subnet1" \\
        --domain "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyRG/providers/Microsoft.AAD/domainServices/MyDomain.onmicrosoft.com" \\
        --assign-identity "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/MyMsiRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MyMSI" \\
        --cluster-admin-account MyAdminAccount@MyDomain.onmicrosoft.com \\
        --cluster-users-group-dns MyGroup
  - name: Create a Kafka cluster with disk encryption. See https://docs.microsoft.com/azure/hdinsight/kafka/apache-kafka-byok.
    text: |-
        az hdinsight create -t kafka -g MyResourceGroup -n MyCluster \\
        -p "HttpPassword1234!" --workernode-data-disks-per-node 2 \\
        --storage-account MyStorageAccount \\
        --encryption-key-name kafkaClusterKey \\
        --encryption-key-version 00000000000000000000000000000000 \\
        --encryption-vault-uri https://MyKeyVault.vault.azure.net \\
        --assign-identity MyMSI
  - name: Create a cluster with Azure Data Lake Storage Gen2
    text: |-
        az hdinsight create -t spark -g MyResourceGroup -n MyCluster \\
        -p "HttpPassword1234!" \\
        --storage-account MyStorageAccount \\
        --storage-account-managed-identity MyMSI
  - name: Create a cluster with configuration from JSON string.
    text: |-
        az hdinsight create -t spark -g MyResourceGroup -n MyCluster \\
        -p "HttpPassword1234!" \\
        --storage-account MyStorageAccount \\
        --cluster-configuration {'gateway':{'restAuthCredential.username':'admin'}}
  - name: Create a cluster with configuration from a local file.
    text: |-
        az hdinsight create -t spark -g MyResourceGroup -n MyCluster \\
        -p "HttpPassword1234!" \\
        --storage-account MyStorageAccount \\
        --cluster-configuration @config.json
"""

helps['hdinsight list'] = """
type: command
short-summary: List HDInsight clusters in a resource group or subscription.
"""

helps['hdinsight monitor'] = """
type: group
short-summary: Manage Azure Monitor logs integration on an HDInsight cluster.
"""

helps['hdinsight monitor disable'] = """
type: command
short-summary: Disable the Azure Monitor logs integration on an HDInsight cluster.
"""

helps['hdinsight monitor enable'] = """
type: command
short-summary: Enable the Azure Monitor logs integration on an HDInsight cluster.
"""

helps['hdinsight monitor show'] = """
type: command
short-summary: Get the status of Azure Monitor logs integration on an HDInsight cluster.
"""

helps['hdinsight rotate-disk-encryption-key'] = """
type: command
short-summary: Rotate the disk encryption key of the specified HDInsight cluster.
"""

helps['hdinsight script-action'] = """
type: group
short-summary: Manage HDInsight script actions.
"""

helps['hdinsight script-action execute'] = """
type: command
short-summary: Execute script actions on the specified HDInsight cluster.
examples:
  - name: Execute a script action and persist on success.
    text: |-
        az hdinsight script-action execute -g MyResourceGroup -n MyScriptActionName \\
        --cluster-name MyCluster \\
        --script-uri https://hdiconfigactions.blob.core.windows.net/linuxgiraphconfigactionv01/giraph-installer-v01.sh \\
        --roles headnode workernode \\
        --persist-on-success
"""

helps['hdinsight wait'] = """
type: command
short-summary: Place the CLI in a waiting state until an operation is complete.
"""

helps['identity'] = """
type: group
short-summary: Managed Service Identities
"""

helps['identity list'] = """
type: command
short-summary: List Managed Service Identities
"""

helps['identity list-operations'] = """
type: command
short-summary: Lists available operations for the Managed Identity provider
"""

helps['image'] = """
type: group
short-summary: Manage custom virtual machine images.
"""

helps['image create'] = """
type: command
short-summary: Create a custom Virtual Machine Image from managed disks or snapshots.
examples:
  - name: Create an image from an existing disk.
    text: |
        az image create -g MyResourceGroup -n image1 --os-type Linux \\
            --source /subscriptions/db5eb68e-73e2-4fa8-b18a-0123456789999/resourceGroups/rg1/providers/Microsoft.Compute/snapshots/s1
  - name: Create an image by capturing an existing generalized virtual machine in the same resource group.
    text: az image create -g MyResourceGroup -n image1 --source MyVm1
"""

helps['image list'] = """
type: command
short-summary: List custom VM images.
"""

helps['image template'] = """
type: group
short-summary: Manage and build image builder templates.
"""

helps['image template create'] = """
type: command
short-summary: Create an image builder template.
parameters:
  - name: --image-source -i
    populator-commands:
      - az vm image list
      - az vm image show
examples:
  - name: Create an image builder template from an UbuntuLTS 18.04 image. Distribute it as a managed image and a shared image gallery image version
    text: |
        scripts="https://my-script-url.net/customize_script.sh"
        imagesource="Canonical:UbuntuServer:18.04-LTS:18.04.201903060"

        az image template create --image-source $imagesource -n mytemplate -g my-group \\
            --scripts $scripts --managed-image-destinations image_1=westus \\
            --shared-image-destinations my_shared_gallery/linux_image_def=westus,brazilsouth

  - name: >
        [Advanced] Create an image template with multiple customizers and distributors using the CLI's object cache via --defer. Supports features such as: customizer and output names, powershell exit codes, inline scripts, windows restart, file customizers, artifact tags and vhd output distributors.
    text: |
        script="https://my-script-url.com/customize_script.ps1"
        imagesource="MicrosoftWindowsServer:WindowsServer:2019-Datacenter:2019.0.20190214"

        # create and update template object in local cli cache. Defers put request to ARM
        # Cache object ttl set via az configure.
        az image template create --image-source $imagesource -n mytemplate \\
            -g my-group --scripts $script --defer

        # add customizers
        az image template customizer add -n mytemplate -g my-group  \\
            --customizer-name my-pwsh-script --exit-codes 0 1 --inline-script \\
            "mkdir c:\\buildActions" "echo Azure-Image-Builder-Was-Here \\
             > c:\\buildActions\\Output.txt" --type powershell --defer

        az image template customizer add -n mytemplate -g my-group \\
            --customizer-name my-file-customizer --type file \\
            --file-source "https://my-file-source.net/file.txt"  \\
            --dest-path "c:\\buildArtifacts\\file.txt" --defer

        # add distributors
        az image template output add -n mytemplate -g my-group --is-vhd \\
            --output-name my-win-image-vhd --artifact-tags "is_vhd=True" --defer

        az image template output add -n mytemplate -g my-group \\
            --output-name my-win-image-managed --managed-image winImage \\
            --managed-image-location eastus \\
            --artifact-tags "is_vhd=False" --defer

        # Stop deferring put request to ARM. Create the template from the object cache.
        # Cache object will be deleted.
        az image template update -n mytemplate -g my-group
"""

helps['image template customizer'] = """
type: group
short-summary: Manage image builder template customizers.
"""

helps['image template customizer add'] = """
type: command
short-summary: Add an image builder customizer to an image builder template.
long-summary: Must be used with --defer
examples:
  - name: Add an inline shell customizer to an image template in the cli object cache
    text: |
        az image template customizer add -n mytemplate -g my-group \\
            --inline-script "sudo mkdir /buildArtifacts" \\
                            "sudo cp /tmp/index.html /buildArtifacts/index.html" \\
            --customizer-name shell-script-inline --type shell --defer

  - name: Add a file customizer to an image template in the cli object cache
    text: |
        az image template customizer add -n mytemplate -g my-group \\
            --customizer-name my-file --type file \\
            --file-source "https://my-remote-file.html" --dest-path "/tmp/index.html" --defer

  - name: Add a windows restart customizer to an image template in the cli object cache
    text: |
        az image template customizer add -n mytemplate -g my-group \\
        --customizer-name shell-script-url \\
        --restart-check-command "echo Azure-Image-Builder-Restarted-the-VM  > \\
                                c:\\buildArtifacts\\restart.txt" \\
            --type windows-restart --restart-timeout 10m --defer

"""

helps['image template customizer clear'] = """
type: command
short-summary: Remove all image builder customizers from an image builder template.
long-summary: Must be used with --defer
"""

helps['image template customizer remove'] = """
type: command
short-summary: Remove an image builder customizer from an image builder template.
long-summary: Must be used with --defer
"""

helps['image template delete'] = """
type: command
short-summary: Delete image builder template.
"""

helps['image template list'] = """
type: command
short-summary: List image builder templates.
"""

helps['image template output'] = """
type: group
short-summary: Manage image builder template output distributors.
long-summary: >
    A customized image can be distributed as a managed image,
    a shared image in a shared image gallery (SIG), or as a VHD blob.
"""

helps['image template output add'] = """
type: command
short-summary: Add an image builder output distributor to an image builder template.
long-summary: Must be used with --defer. The output distributor can be a managed image, a gallery image, or as a VHD blob.
examples:
  - name: Add a managed image distributor to an image template in the cli object cache. Specify a run output name.
    text: |
        az image template output add -n mytemplate -g my-group \\
            --managed-image my_desired_image_name --output-name managed_image_run_01 --defer

  - name: Add a shared image gallery distributor to an image template in the cli object cache. Specify its replication regions.
    text: |
        az image template output add -n mytemplate -g my-group --gallery-name my_shared_gallery \\
            --gallery-replication-regions westus brazilsouth \\
            --gallery-image-definition linux_image_def --defer

  - name: Add a VHD distributor to an image template in the cli object cache.
    text: |
        az image template output add -n mytemplate -g my-group \\
            --output-name my_vhd_image --is-vhd  --defer

"""

helps['image template output clear'] = """
type: command
short-summary: Remove all image builder output distributors from an image builder template.
long-summary: Must be used with --defer
"""

helps['image template output remove'] = """
type: command
short-summary: Remove an image builder output distributor from an image builder template.
long-summary: Must be used with --defer
"""

helps['image template run'] = """
type: command
short-summary: Build an image builder template.
examples:
  - name: Start a template build run and then wait for it to finish.
    text: |
        az image template run -n mytemplate -g my-group --no-wait

        az image template wait -n mytemplate -g aibmdi \\
            --custom "lastRunStatus.runState!='running'"

        az image template show -n mytemplate -g my-group
"""

helps['image template show'] = """
type: command
short-summary: Show an image builder template.
"""

helps['image template show-runs'] = """
type: command
short-summary: Show an image builder template's run outputs.
examples:
  - name: Run a template build run and then view its run outputs.
    text: |
        az image template run -n mytemplate -g my-group --no-wait

        az image template wait -n mytemplate -g aibmdi \\
            --custom "lastRunStatus.runState!='running'"

        az image template show-runs -n mytemplate -g my-group
"""

helps['image template update'] = """
type: command
short-summary: Update an image builder template.
long-summary: >
    Updating an image builder templates is currently unsupported. This command can be used in conjunction with --defer
    to update an image template object within the CLI cache. Without --defer it retrieves the specified image template
    from the cache and sends a request to Azure to create the image template.

examples:
  - name: |
        Create a template resource from a template object in the cli cache.
        See "az image template create / output add / customizer add --help" and "az cache -h" for more information
    text: |
        # create and write template object to local cli cache
        az image template create --image-source {image_source} -n mytemplate -g my-group \\
            --scripts {script} --managed-image-destinations image_1=westus --defer

        # add customizers and outputs to local cache template object via az image template output / customizer add
        # one can also update cache object properties through generic update options, such as: --set
        az image template output add -n mytemplate -g my-group --output-name my-win-image-managed \\
            --artifact-tags "is_vhd=False"  --managed-image winImage --managed-image-location eastus --defer

        # send template create request to azure to create template resource
        az image template update -n mytemplate -g my-group
"""

helps['image template wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the template is met.
examples:
  - name: Start a template build run and then wait for it to finish.
    text: |
        az image template run -n mytemplate -g my-group --no-wait

        az image template wait -n mytemplate -g aibmdi \\
            --custom "lastRunStatus.runState!='running'"

        az image template show -n mytemplate -g my-group
"""

helps['image update'] = """
type: command
short-summary: Update custom VM images.
examples:
  - name: Add or update tags.
    text: az image update -n ImageName -g ResourceGroup --tags tag1=val1 tag2=val2
  - name: Remove all tags.
    text: az image update -n ImageName -g resourceGroup --tags
"""

helps['interactive'] = """
type: command
short-summary: Start interactive mode. Installs the Interactive extension if not installed already.
long-summary: >
    For more information on interactive mode, see: https://azure.microsoft.com/blog/welcome-to-azure-cli-shell/
"""

helps['iot'] = """
type: group
short-summary: Manage Internet of Things (IoT) assets.
long-summary: Comprehensive IoT data-plane functionality is available in the Azure IoT CLI Extension. For more info and install guide go to https://github.com/Azure/azure-iot-cli-extension
"""

helps['iot dps'] = """
type: group
short-summary: Manage Azure IoT Hub Device Provisioning Service.
"""

helps['iot dps access-policy'] = """
type: group
short-summary: Manage Azure IoT Hub Device Provisioning Service access policies.
"""

helps['iot dps access-policy create'] = """
type: command
short-summary: Create a new shared access policy in an Azure IoT Hub device provisioning service.
examples:
  - name: Create a new shared access policy in an Azure IoT Hub device provisioning service with EnrollmentRead right
    text: >
        az iot dps access-policy create --dps-name MyDps --resource-group MyResourceGroup --name MyPolicy --rights EnrollmentRead
"""

helps['iot dps access-policy delete'] = """
type: command
short-summary: Delete a shared access policies in an Azure IoT Hub device provisioning service.
examples:
  - name: Delete shared access policy 'MyPolicy' in an Azure IoT Hub device provisioning service
    text: >
        az iot dps access-policy delete --dps-name MyDps --resource-group MyResourceGroup --name MyPolicy
"""

helps['iot dps access-policy list'] = """
type: command
short-summary: List all shared access policies in an Azure IoT Hub device provisioning service.
examples:
  - name: List all shared access policies in MyDps
    text: >
        az iot dps access-policy list --dps-name MyDps --resource-group MyResourceGroup
"""

helps['iot dps access-policy show'] = """
type: command
short-summary: Show details of a shared access policies in an Azure IoT Hub device provisioning service.
examples:
  - name: Show details of shared access policy 'MyPolicy' in an Azure IoT Hub device provisioning service
    text: >
        az iot dps access-policy show --dps-name MyDps --resource-group MyResourceGroup --name MyPolicy
"""

helps['iot dps access-policy update'] = """
type: command
short-summary: Update a shared access policy in an Azure IoT Hub device provisioning service.
examples:
  - name: Update access policy 'MyPolicy' in an Azure IoT Hub device provisioning service with EnrollmentWrite right
    text: >
        az iot dps access-policy update --dps-name MyDps --resource-group MyResourceGroup --name MyPolicy --rights EnrollmentWrite
"""

helps['iot dps certificate'] = """
type: group
short-summary: Manage Azure IoT Hub Device Provisioning Service certificates.
"""

helps['iot dps certificate create'] = """
type: command
short-summary: Create/upload an Azure IoT Hub Device Provisioning Service certificate.
examples:
  - name: Upload a CA certificate PEM file to an Azure IoT Hub device provisioning service.
    text: >
        az iot dps certificate create --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate --path /certificates/Certificate.pem
  - name: Upload a CA certificate CER file to an Azure IoT Hub device provisioning service.
    text: >
        az iot dps certificate create --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate --path /certificates/Certificate.cer
"""

helps['iot dps certificate delete'] = """
type: command
short-summary: Delete an Azure IoT Hub Device Provisioning Service certificate.
examples:
  - name: Delete MyCertificate in an Azure IoT Hub device provisioning service
    text: >
        az iot dps certificate delete --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate --etag AAAAAAAAAAA=
"""

helps['iot dps certificate generate-verification-code'] = """
type: command
short-summary: Generate a verification code for an Azure IoT Hub Device Provisioning Service certificate.
long-summary: This verification code is used to complete the proof of possession step for a certificate. Use this verification code as the CN of a new certificate signed with the root certificates private key.
examples:
  - name: Generate a verification code for MyCertificate
    text: >
        az iot dps certificate generate-verification-code --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate --etag AAAAAAAAAAA=
"""

helps['iot dps certificate list'] = """
type: command
short-summary: List all certificates contained within an Azure IoT Hub device provisioning service
examples:
  - name: List all certificates in MyDps
    text: >
        az iot dps certificate list --dps-name MyDps --resource-group MyResourceGroup
"""

helps['iot dps certificate show'] = """
type: command
short-summary: Show information about a particular Azure IoT Hub Device Provisioning Service certificate.
examples:
  - name: Show details about MyCertificate in an Azure IoT Hub device provisioning service
    text: >
        az iot dps certificate show --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate
"""

helps['iot dps certificate update'] = """
type: command
short-summary: Update an Azure IoT Hub Device Provisioning Service certificate.
long-summary: Upload a new certificate to replace the existing certificate with the same name.
examples:
  - name: Update a CA certificate in an Azure IoT Hub device provisioning service by uploading a new PEM file.
    text: >
        az iot dps certificate update --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate --path /certificates/NewCertificate.pem --etag AAAAAAAAAAA=
  - name: Update a CA certificate in an Azure IoT Hub device provisioning service by uploading a new CER file.
    text: >
        az iot dps certificate update --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate --path /certificates/NewCertificate.cer --etag AAAAAAAAAAA=
"""

helps['iot dps certificate verify'] = """
type: command
short-summary: Verify an Azure IoT Hub Device Provisioning Service certificate.
long-summary: Verify a certificate by uploading a verification certificate containing the verification code obtained by calling generate-verification-code. This is the last step in the proof of possession process.
examples:
  - name: Verify ownership of the MyCertificate private key.
    text: >
        az iot dps certificate verify --dps-name MyDps --resource-group MyResourceGroup --name MyCertificate --path /certificates/Verification.pem --etag AAAAAAAAAAA=
"""

helps['iot dps create'] = """
type: command
short-summary: Create an Azure IoT Hub device provisioning service.
long-summary: For an introduction to Azure IoT Hub Device Provisioning Service, see https://docs.microsoft.com/azure/iot-dps/about-iot-dps
examples:
  - name: Create an Azure IoT Hub device provisioning service with the standard pricing tier S1, in the region of the resource group.
    text: >
        az iot dps create --name MyDps --resource-group MyResourceGroup
  - name: Create an Azure IoT Hub device provisioning service with the standard pricing tier S1, in the 'eastus' region.
    text: >
        az iot dps create --name MyDps --resource-group MyResourceGroup --location eastus
"""

helps['iot dps delete'] = """
type: command
short-summary: Delete an Azure IoT Hub device provisioning service.
examples:
  - name: Delete an Azure IoT Hub device provisioning service 'MyDps'
    text: >
        az iot dps delete --name MyDps --resource-group MyResourceGroup
"""

helps['iot dps linked-hub'] = """
type: group
short-summary: Manage Azure IoT Hub Device Provisioning Service linked IoT hubs.
"""

helps['iot dps linked-hub create'] = """
type: command
short-summary: Create a linked IoT hub in an Azure IoT Hub device provisioning service.
examples:
  - name: Create a linked IoT hub in an Azure IoT Hub device provisioning service
    text: >
        az iot dps linked-hub create --dps-name MyDps --resource-group MyResourceGroup --connection-string HostName=test.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=XNBhoasdfhqRlgGnasdfhivtshcwh4bJwe7c0RIGuWsirW0= --location westus
  - name: Create a linked IoT hub in an Azure IoT Hub device provisioning service which applies allocation weight and weight being 10
    text: >
        az iot dps linked-hub create --dps-name MyDps --resource-group MyResourceGroup --connection-string HostName=test.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=XNBhoasdfhqRlgGnasdfhivtshcwh4bJwe7c0RIGuWsirW0= --location westus --allocation-weight 10 --apply-allocation-policy True
"""

helps['iot dps linked-hub delete'] = """
type: command
short-summary: Update a linked IoT hub in an Azure IoT Hub device provisioning service.
examples:
  - name: Delete linked IoT hub 'MyLinkedHub' in an Azure IoT Hub device provisioning service
    text: >
        az iot dps linked-hub delete --dps-name MyDps --resource-group MyResourceGroup --linked-hub MyLinkedHub
"""

helps['iot dps linked-hub list'] = """
type: command
short-summary: List all linked IoT hubs in an Azure IoT Hub device provisioning service.
examples:
  - name: List all linked IoT hubs in MyDps
    text: >
        az iot dps linked-hub list --dps-name MyDps --resource-group MyResourceGroup
"""

helps['iot dps linked-hub show'] = """
type: command
short-summary: Show details of a linked IoT hub in an Azure IoT Hub device provisioning service.
examples:
  - name: Show details of linked IoT hub 'MyLinkedHub' in an Azure IoT Hub device provisioning service
    text: >
        az iot dps linked-hub show --dps-name MyDps --resource-group MyResourceGroup --linked-hub MyLinkedHub
"""

helps['iot dps linked-hub update'] = """
type: command
short-summary: Update a linked IoT hub in an Azure IoT Hub device provisioning service.
examples:
  - name: Update linked IoT hub 'MyLinkedHub.azure-devices.net' in an Azure IoT Hub device provisioning service
    text: >
        az iot dps linked-hub update --dps-name MyDps --resource-group MyResourceGroup --linked-hub MyLinkedHub.azure-devices.net --allocation-weight 10 --apply-allocation-policy True
"""

helps['iot dps list'] = """
type: command
short-summary: List Azure IoT Hub device provisioning services.
examples:
  - name: List all Azure IoT Hub device provisioning services in a subscription.
    text: >
        az iot dps list
  - name: List all Azure IoT Hub device provisioning services in the resource group 'MyResourceGroup'
    text: >
        az iot dps list --resource-group MyResourceGroup
"""

helps['iot dps show'] = """
type: command
short-summary: Get the details of an Azure IoT Hub device provisioning service.
examples:
  - name: Show details of an Azure IoT Hub device provisioning service 'MyDps'
    text: >
        az iot dps show --name MyDps --resource-group MyResourceGroup
"""

helps['iot dps update'] = """
type: command
short-summary: Update an Azure IoT Hub device provisioning service.
examples:
  - name: Update Allocation Policy to 'GeoLatency' of an Azure IoT Hub device provisioning service 'MyDps'
    text: >
        az iot dps update --name MyDps --resource-group MyResourceGroup --set properties.allocationPolicy="GeoLatency"
"""

helps['iot hub'] = """
type: group
short-summary: Manage Azure IoT hubs.
"""

helps['iot hub certificate'] = """
type: group
short-summary: Manage IoT Hub certificates.
"""

helps['iot hub certificate create'] = """
type: command
short-summary: Create/upload an Azure IoT Hub certificate.
long-summary: For a detailed explanation of CA certificates in Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/iot-hub-x509ca-overview
examples:
  - name: Uploads a CA certificate PEM file to an IoT hub.
    text: >
        az iot hub certificate create --hub-name MyIotHub --name MyCertificate --path /certificates/Certificate.pem
  - name: Uploads a CA certificate CER file to an IoT hub.
    text: >
        az iot hub certificate create --hub-name MyIotHub --name MyCertificate --path /certificates/Certificate.cer
"""

helps['iot hub certificate delete'] = """
type: command
short-summary: Deletes an Azure IoT Hub certificate.
long-summary: For a detailed explanation of CA certificates in Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/iot-hub-x509ca-overview
examples:
  - name: Deletes MyCertificate
    text: >
        az iot hub certificate delete --hub-name MyIotHub --name MyCertificate --etag AAAAAAAAAAA=
"""

helps['iot hub certificate generate-verification-code'] = """
type: command
short-summary: Generates a verification code for an Azure IoT Hub certificate.
long-summary: This verification code is used to complete the proof of possession step for a certificate. Use this verification code as the CN of a new certificate signed with the root certificates private key. For a detailed explanation of CA certificates in Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/iot-hub-x509ca-overview
examples:
  - name: Generates a verification code for MyCertificate
    text: >
        az iot hub certificate generate-verification-code --hub-name MyIotHub --name MyCertificate --etag AAAAAAAAAAA=
"""

helps['iot hub certificate list'] = """
type: command
short-summary: Lists all certificates contained within an Azure IoT Hub
long-summary: For a detailed explanation of CA certificates in Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/iot-hub-x509ca-overview
examples:
  - name: List all certificates in MyIotHub
    text: >
        az iot hub certificate list --hub-name MyIotHub
"""

helps['iot hub certificate show'] = """
type: command
short-summary: Shows information about a particular Azure IoT Hub certificate.
long-summary: For a detailed explanation of CA certificates in Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/iot-hub-x509ca-overview
examples:
  - name: Show details about MyCertificate
    text: >
        az iot hub certificate show --hub-name MyIotHub --name MyCertificate
"""

helps['iot hub certificate update'] = """
type: command
short-summary: Update an Azure IoT Hub certificate.
long-summary: Uploads a new certificate to replace the existing certificate with the same name. For a detailed explanation of CA certificates in Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/iot-hub-x509ca-overview
examples:
  - name: Updates a CA certificate in an IoT hub by uploading a new PEM file.
    text: >
        az iot hub certificate update --hub-name MyIotHub --name MyCertificate --path /certificates/NewCertificate.pem --etag AAAAAAAAAAA=
  - name: Updates a CA certificate in an IoT hub by uploading a new CER file.
    text: >
        az iot hub certificate update --hub-name MyIotHub --name MyCertificate --path /certificates/NewCertificate.cer --etag AAAAAAAAAAA=
"""

helps['iot hub certificate verify'] = """
type: command
short-summary: Verifies an Azure IoT Hub certificate.
long-summary: Verifies a certificate by uploading a verification certificate containing the verification code obtained by calling generate-verification-code. This is the last step in the proof of possession process. For a detailed explanation of CA certificates in Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/iot-hub-x509ca-overview
examples:
  - name: Verifies ownership of the MyCertificate private key.
    text: >
        az iot hub certificate verify --hub-name MyIotHub --name MyCertificate --path /certificates/Verification.pem --etag AAAAAAAAAAA=
"""

helps['iot hub consumer-group'] = """
type: group
short-summary: Manage the event hub consumer groups of an IoT hub.
"""

helps['iot hub consumer-group create'] = """
type: command
short-summary: Create an event hub consumer group.
examples:
  - name: Create a consumer group 'cg1' in the default event hub endpoint.
    text: >
        az iot hub consumer-group create --hub-name MyIotHub --name cg1
  - name: Create a consumer group `cg1` in the operation monitoring event hub endpoint `operationsMonitoringEvents`.
    text: >
        az iot hub consumer-group create --hub-name MyIotHub --event-hub-name operationsMonitoringEvents --name cg1
"""

helps['iot hub consumer-group delete'] = """
type: command
short-summary: Delete an event hub consumer group.
"""

helps['iot hub consumer-group list'] = """
type: command
short-summary: List event hub consumer groups.
"""

helps['iot hub consumer-group show'] = """
type: command
short-summary: Get the details for an event hub consumer group.
"""

helps['iot hub create'] = """
type: command
short-summary: Create an Azure IoT hub.
long-summary: For an introduction to Azure IoT Hub, see https://docs.microsoft.com/azure/iot-hub/
examples:
  - name: Create an IoT Hub with the free pricing tier F1, in the region of the resource group.
    text: >
        az iot hub create --resource-group MyResourceGroup --name MyIotHub
  - name: Create an IoT Hub with the standard pricing tier S1 and 4 partitions, in the 'westus' region.
    text: >
        az iot hub create --resource-group MyResourceGroup --name MyIotHub --sku S1 --location westus --partition-count 4
"""

helps['iot hub delete'] = """
type: command
short-summary: Delete an IoT hub.
examples:
  - name: Delete an IoT hub. (autogenerated)
    text: az iot hub delete --name MyIoTHub --resource-group MyResourceGroup
    crafted: true
"""

helps['iot hub devicestream'] = """
type: group
short-summary: Manage device streams of an IoT hub.
"""

helps['iot hub devicestream show'] = """
type: command
short-summary: Get IoT Hub's device streams endpoints.
long-summary: Get IoT Hub's device streams endpoints.
examples:
  - name: Get all the device streams from "MyIotHub" IoT Hub.
    text: >
        az iot hub devicestream show -n MyIotHub
"""

helps['iot hub job'] = """
type: group
short-summary: Manage jobs in an IoT hub.
"""

helps['iot hub job cancel'] = """
type: command
short-summary: Cancel a job in an IoT hub.
"""

helps['iot hub job list'] = """
type: command
short-summary: List the jobs in an IoT hub.
examples:
  - name: List the jobs in an IoT hub. (autogenerated)
    text: az iot hub job list --hub-name MyHub
    crafted: true
"""

helps['iot hub job show'] = """
type: command
short-summary: Get the details of a job in an IoT hub.
examples:
  - name: Get the details of a job in an IoT hub. (autogenerated)
    text: az iot hub job show --hub-name MyHub --job-id JobId
    crafted: true
"""

helps['iot hub list'] = """
type: command
short-summary: List IoT hubs.
examples:
  - name: List all IoT hubs in a subscription.
    text: >
        az iot hub list
  - name: List all IoT hubs in the resource group 'MyGroup'
    text: >
        az iot hub list --resource-group MyGroup
"""

helps['iot hub list-skus'] = """
type: command
short-summary: List available pricing tiers.
"""

helps['iot hub manual-failover'] = """
type: command
short-summary: Initiate a manual failover for the IoT Hub to the geo-paired disaster recovery region.
examples:
  - name: This fails over “myhub” from East US to West US.
    text: >
        az iot hub manual-failover -n myhub --fr "West US"
"""

helps['iot hub message-enrichment'] = """
type: group
short-summary: Manage message enrichments for endpoints of an IoT Hub.
"""

helps['iot hub message-enrichment create'] = """
type: command
short-summary: Create a message enrichment for chosen endpoints in your IoT Hub
long-summary: Create a message enrichment for chosen endpoints in your IoT Hub
examples:
  - name: Create a message enrichment of {"key":"value"} for the "events" endpoint in your IoT Hub
    text: >
        az iot hub message-enrichment create --key key --value value --endpoints events -n {iothub_name}
"""

helps['iot hub message-enrichment delete'] = """
type: command
short-summary: Delete a message enrichment in your IoT hub (by key)
long-summary: Delete a message enrichment in your IoT hub (by key)
examples:
  - name: Delete a message enrichment with key 'test' from your IoT Hub
    text: >
        az iot hub message-enrichment delete --key test -n {iothub_name}
"""

helps['iot hub message-enrichment list'] = """
type: command
short-summary: Get information on all message enrichments for your IoT Hub
long-summary: Get information on all message enrichments for your IoT Hub
examples:
  - name: List all message enrichments for your IoT Hub
    text: >
        az iot hub message-enrichment list -n {iothub_name}
"""

helps['iot hub message-enrichment update'] = """
type: command
short-summary: Update a message enrichment in your IoT hub (by key)
long-summary: Update a message enrichment in your IoT hub (by key)
examples:
  - name: Update a message enrichment in your IoT hub to apply to a new set of endpoints
    text: >
        az iot hub message-enrichment update --key {key} --value {value} --endpoints NewEndpoint1 NewEndpoint2 -n {iothub_name}
"""

helps['iot hub policy'] = """
type: group
short-summary: Manage shared access policies of an IoT hub.
"""

helps['iot hub policy create'] = """
type: command
short-summary: Create a new shared access policy in an IoT hub.
examples:
  - name: Create a new shared access policy.
    text: >
        az iot hub policy create --hub-name MyIotHub --name new-policy --permissions RegistryWrite ServiceConnect DeviceConnect
"""

helps['iot hub policy delete'] = """
type: command
short-summary: Delete a shared access policy from an IoT hub.
"""

helps['iot hub policy list'] = """
type: command
short-summary: List shared access policies of an IoT hub.
examples:
  - name: List shared access policies of an IoT hub. (autogenerated)
    text: az iot hub policy list --hub-name MyHub --resource-group MyResourceGroup
    crafted: true
"""

helps['iot hub policy renew-key'] = """
type: command
short-summary: Regenerate keys of a shared access policy of an IoT hub.
examples:
  - name: Regenerate primary key of a shared access policy of an IoT hub.
    text: az iot hub policy renew-key --hub-name MyHub --name MySharedAccessPolicy --rk Primary
    crafted: true
"""

helps['iot hub policy show'] = """
type: command
short-summary: Get the details of a shared access policy of an IoT hub.
examples:
  - name: Get the details of a shared access policy of an IoT hub. (autogenerated)
    text: az iot hub policy show --hub-name MyHub --name MySharedAccessPolicy
    crafted: true
"""

helps['iot hub route'] = """
type: group
short-summary: Manage routes of an IoT hub.
"""

helps['iot hub route create'] = """
type: command
short-summary: Create a route in IoT Hub.
long-summary: Create a route to send specific data source and condition to a desired endpoint.
examples:
  - name: Create a new route "R1".
    text: >
        az iot hub route create -g MyResourceGroup --hub-name MyIotHub --endpoint-name E2 --source-type DeviceMessages --route-name R1
  - name: Create a new route "R1" with all parameters.
    text: >
        az iot hub route create -g MyResourceGroup --hub-name MyIotHub --endpoint-name E2 --source-type DeviceMessages --route-name R1 --condition true --enabled true
"""

helps['iot hub route delete'] = """
type: command
short-summary: Delete all or mentioned route for your IoT Hub.
long-summary: Delete a route or all routes for your IoT Hub.
examples:
  - name: Delete route "R1" from "MyIotHub" IoT Hub.
    text: >
        az iot hub route delete -g MyResourceGroup --hub-name MyIotHub --route-name R1
  - name: Delete all the routes of source type "DeviceMessages" from "MyIotHub" IoT Hub.
    text: >
        az iot hub route delete -g MyResourceGroup --hub-name MyIotHub --source-type DeviceMessages
  - name: Delete all the routes from "MyIotHub" IoT Hub.
    text: >
        az iot hub route delete -g MyResourceGroup --hub-name MyIotHub
"""

helps['iot hub route list'] = """
type: command
short-summary: Get all the routes in IoT Hub.
long-summary: Get information on all routes from an IoT Hub.
examples:
  - name: Get all route from "MyIotHub" IoT Hub.
    text: >
        az iot hub route list -g MyResourceGroup --hub-name MyIotHub
  - name: Get all the routes of source type "DeviceMessages" from "MyIotHub" IoT Hub.
    text: >
        az iot hub route list -g MyResourceGroup --hub-name MyIotHub --source-type DeviceMessages
"""

helps['iot hub route show'] = """
type: command
short-summary: Get information about the route in IoT Hub.
long-summary: Get information on a specific route in your IoT Hub.
examples:
  - name: Get an route information from "MyIotHub" IoT Hub.
    text: >
        az iot hub route show -g MyResourceGroup --hub-name MyIotHub --route-name {routeName}
"""

helps['iot hub route test'] = """
type: command
short-summary: Test all routes or mentioned route in IoT Hub.
long-summary: Test all existing routes or mentioned route in your IoT Hub. You can provide a sample message to test your routes.
examples:
  - name: Test the route "R1" from "MyIotHub" IoT Hub.
    text: >
        az iot hub route test -g MyResourceGroup --hub-name MyIotHub --route-name R1
  - name: Test all the route of source type "DeviceMessages" from "MyIotHub" IoT Hub.
    text: >
        az iot hub route test -g MyResourceGroup --hub-name MyIotHub --source-type DeviceMessages
"""

helps['iot hub route update'] = """
type: command
short-summary: Update a route in IoT Hub.
long-summary: Updates a route in IoT Hub. You can change the source, enpoint or query on the route.
examples:
  - name: Update source type of route "R1" from "MyIotHub" IoT Hub.
    text: >
        az iot hub route update -g MyResourceGroup --hub-name MyIotHub --source-type DeviceMessages --route-name R1
"""

helps['iot hub routing-endpoint'] = """
type: group
short-summary: Manage custom endpoints of an IoT hub.
"""

helps['iot hub routing-endpoint create'] = """
type: command
short-summary: Add an endpoint to your IoT Hub.
long-summary: Create a new custom endpoint in your IoT Hub.
examples:
  - name: Add a new endpoint "E2" of type EventHub to "MyIotHub" IoT Hub.
    text: >
        az iot hub routing-endpoint create --resource-group MyResourceGroup --hub-name MyIotHub --endpoint-name E2 --endpoint-type eventhub --endpoint-resource-group {ResourceGroup} --endpoint-subscription-id {SubscriptionId} --connection-string {ConnectionString}
  - name: Add a new endpoint "S1" of type AzureStorageContainer to "MyIotHub" IoT Hub.
    text: |
        az iot hub routing-endpoint create --resource-group MyResourceGroup --hub-name MyIotHub \\
        --endpoint-name S1 --endpoint-type azurestoragecontainer --endpoint-resource-group "[Resource Group]" \\
        --endpoint-subscription-id {SubscriptionId} --connection-string {ConnectionString} \\
        --container-name {ContainerName}
"""

helps['iot hub routing-endpoint delete'] = """
type: command
short-summary: Delete all or mentioned endpoint for your IoT Hub.
long-summary: Delete an endpoint for your IoT Hub. We recommend that you delete any routes to the endpoint, before deleting the endpoint.
examples:
  - name: Delete endpoint "E2" from "MyIotHub" IoT Hub.
    text: >
        az iot hub routing-endpoint delete --resource-group MyResourceGroup --hub-name MyIotHub --endpoint-name E2
  - name: Delete all the endpoints of type "EventHub" from "MyIotHub" IoT Hub.
    text: >
        az iot hub routing-endpoint delete --resource-group MyResourceGroup --hub-name MyIotHub --endpoint-type eventhub
  - name: Delete all the endpoints from "MyIotHub" IoT Hub.
    text: >
        az iot hub routing-endpoint delete --resource-group MyResourceGroup --hub-name MyIotHub
"""

helps['iot hub routing-endpoint list'] = """
type: command
short-summary: Get information on all the endpoints for your IoT Hub.
long-summary: Get information on all endpoints in your IoT Hub. You can also specify which endpoint type you want to get informaiton on.
examples:
  - name: Get all the endpoints from "MyIotHub" IoT Hub.
    text: >
        az iot hub routing-endpoint list -g MyResourceGroup --hub-name MyIotHub
  - name: Get all the endpoints of type "EventHub" from "MyIotHub" IoT Hub.
    text: >
        az iot hub routing-endpoint list -g MyResourceGroup --hub-name MyIotHub --endpoint-type eventhub
"""

helps['iot hub routing-endpoint show'] = """
type: command
short-summary: Get information on mentioned endpoint for your IoT Hub.
long-summary: Get information on a specific endpoint in your IoT Hub
examples:
  - name: Get an endpoint information from "MyIotHub" IoT Hub.
    text: |
        az iot hub routing-endpoint show --resource-group MyResourceGroup --hub-name MyIotHub \\
        --endpoint-name {endpointName}
"""

helps['iot hub show'] = """
type: command
short-summary: Get the details of an IoT hub.
examples:
  - name: Get the details of an IoT hub. (autogenerated)
    text: az iot hub show --name MyIoTHub
    crafted: true
  - name: Show the connection strings for an IoT hub. (autogenerated)
    text: az iot hub show-connection-string --key primary --policy-name MyPolicy
    crafted: true
"""

helps['iot hub show-connection-string'] = """
type: command
short-summary: Show the connection strings for an IoT hub.
examples:
  - name: Show the connection string of an IoT hub using default policy and primary key.
    text: >
        az iot hub show-connection-string --name MyIotHub
  - name: Show the connection string of an IoT Hub using policy 'service' and secondary key.
    text: >
        az iot hub show-connection-string --name MyIotHub --policy-name service --key secondary
  - name: Show the connection strings for all IoT hubs in a resource group.
    text: >
        az iot hub show-connection-string --resource-group MyResourceGroup
  - name: Show the connection strings for all IoT hubs in a subscription.
    text: >
        az iot hub show-connection-string
"""

helps['iot hub show-quota-metrics'] = """
type: command
short-summary: Get the quota metrics for an IoT hub.
examples:
  - name: Get the quota metrics for an IoT hub. (autogenerated)
    text: az iot hub show-quota-metrics --ids {ids}
    crafted: true
  - name: Get the quota metrics for an IoT hub. (autogenerated)
    text: az iot hub show-quota-metrics --name MyIoTHub
    crafted: true
"""

helps['iot hub show-stats'] = """
type: command
short-summary: Get the statistics for an IoT hub.
"""

helps['iot hub update'] = """
type: command
short-summary: Update metadata for an IoT hub.
examples:
  - name: Add a firewall filter rule to accept traffic from the IP mask 127.0.0.0/31.
    text: >
        az iot hub update --name MyIotHub --add properties.ipFilterRules filter_name=test-rule action=Accept ip_mask=127.0.0.0/31
"""

helps['iot pnp'] = """
type: group
short-summary: Manage IoT Plug and Play repositories and repository access keys.
"""

helps['iot pnp key'] = """
type: group
short-summary: Manage access keys to an IoT Plug and Play repository.
"""

helps['iot pnp key create'] = """
type: command
short-summary: Create a key for the given repository.
examples:
  - name: Create a key for the given repository.
    text: >
        az iot pnp key create -r aaaabbbb11112222aaaabbbb1111222 --role Reader
"""

helps['iot pnp key delete'] = """
type: command
short-summary: Delete a key from the given repository.
examples:
  - name: Delete a key from the given repository.
    text: >
        az iot pnp key delete -r aaaabbbb11112222aaaabbbb1111222 -k 12345
"""

helps['iot pnp key list'] = """
type: command
short-summary: List repository's keys.
examples:
  - name: List repository's keys.
    text: >
        az iot pnp key list -r aaaabbbb11112222aaaabbbb1111222
"""

helps['iot pnp key show'] = """
type: command
short-summary: Get the details of a repository key.
examples:
  - name: Get the details of a repository key.
    text: >
        az iot pnp key show -r aaaabbbb11112222aaaabbbb1111222 -k 12345
"""

helps['iot pnp key update'] = """
type: command
short-summary: Update the key for the given repository.
examples:
  - name: Update the key for the given repository.
    text: >
        az iot pnp key update -r aaaabbbb11112222aaaabbbb1111222 -k 12345 --role admin
"""

helps['iot pnp repository'] = """
type: group
short-summary: Manage IoT Plug and Play repositories.
"""

helps['iot pnp repository create'] = """
type: command
short-summary: Create an IoT Plug and Play repository.
examples:
  - name: Create a new IoT Plug and Play repository "myrepo"
    text: >
        az iot pnp repository create -n myrepo
"""

helps['iot pnp repository delete'] = """
type: command
short-summary: Delete an IoT Plug and Play repository.
examples:
  - name: Delete an IoT Plug and Play repository.
    text: >
        az iot pnp repository delete -r aaaabbbb11112222aaaabbbb1111222
"""

helps['iot pnp repository get-provision-status'] = """
type: command
short-summary: Returns the IoT Plug and Play repository provisioning status.
examples:
  - name: Returns the IoT Plug and Play repository provisioning status.
    text: >
        az iot pnp repository get-provision-status -r aaaabbbb11112222aaaabbbb1111222 -s aaaabbbb11112222aaaabbbb1111333
"""

helps['iot pnp repository list'] = """
type: command
short-summary: List IoT Plug and Play repositories.
examples:
  - name: List IoT Plug and Play repositories.
    text: >
        az iot pnp repository list
"""

helps['iot pnp repository show'] = """
type: command
short-summary: Gets the details for an IoT Plug and Play repository.
examples:
  - name: Gets the details for an IoT Plug and Play repository.
    text: >
        az iot pnp repository show -r aaaabbbb11112222aaaabbbb1111222
"""

helps['iot pnp repository update'] = """
type: command
short-summary: Update an IoT Plug and Play repository.
examples:
  - name: Update an IoT Plug and Play repository.
    text: >
        az iot pnp repository update -r aaaabbbb11112222aaaabbbb1111222 -n updatedreponame
"""

helps['iotcentral'] = """
type: group
short-summary: Manage IoT Central assets.
"""

helps['iotcentral app'] = """
type: group
short-summary: Manage IoT Central applications.
"""

helps['iotcentral app create'] = """
type: command
short-summary: Create an IoT Central application.
long-summary: |
    For an introduction to IoT Central, see https://docs.microsoft.com/azure/iot-central/.
    The F1 Sku is no longer supported. Please use the S1 Sku (default) for app creation.
    For more pricing information, please visit https://azure.microsoft.com/pricing/details/iot-central/.
examples:
  - name: Create an IoT Central application in the standard pricing tier S1, in the region of the resource group.
    text: >
        az iotcentral app create --resource-group MyResourceGroup --name my-app-resource --subdomain my-app-subdomain
  - name: Create an IoT Central application with the standard pricing tier S1 in the 'westus' region, with a custom display name, based on the iotc-default template.
    text: >
        az iotcentral app create --resource-group MyResourceGroup --name my-app-resource-name --sku S1 --location westus --subdomain my-app-subdomain --template iotc-default@1.0.0 --display-name 'My Custom Display Name'
"""

helps['iotcentral app delete'] = """
type: command
short-summary: Delete an IoT Central application.
examples:
  - name: Delete an IoT Central application. (autogenerated)
    text: az iotcentral app delete --name MyIoTCentralApplication --resource-group MyResourceGroup
    crafted: true
"""

helps['iotcentral app list'] = """
type: command
short-summary: List IoT Central applications.
examples:
  - name: List all IoT Central applications in a subscription.
    text: >
        az iotcentral app list
  - name: List all IoT Central applications in the resource group 'MyGroup'
    text: >
        az iotcentral app list --resource-group MyGroup
"""

helps['iotcentral app show'] = """
type: command
short-summary: Get the details of an IoT Central application.
examples:
  - name: Show an IoT Central application.
    text: >
        az iotcentral app show --name MyApp
"""

helps['iotcentral app update'] = """
type: command
short-summary: Update metadata for an IoT Central application.
"""

helps['keyvault'] = """
type: group
short-summary: Manage KeyVault keys, secrets, and certificates.
"""

helps['keyvault certificate'] = """
type: group
short-summary: Manage certificates.
"""

helps['keyvault certificate contact'] = """
type: group
short-summary: Manage contacts for certificate management.
"""

helps['keyvault certificate create'] = """
type: command
short-summary: Create a Key Vault certificate.
long-summary: Certificates can be used as a secrets for provisioned virtual machines.
examples:
  - name: Create a self-signed certificate with the default policy and add it to a virtual machine.
    text: |
        az keyvault certificate create --vault-name vaultname -n cert1 \\
          -p "$(az keyvault certificate get-default-policy)"

        secrets=$(az keyvault secret list-versions --vault-name vaultname \\
          -n cert1 --query "[?attributes.enabled].id" -o tsv)

        vm_secrets=$(az vm secret format -s "$secrets")

        az vm create -g group-name -n vm-name --admin-username deploy  \\
          --image debian --secrets "$vm_secrets"
"""

helps['keyvault certificate download'] = """
type: command
short-summary: Download the public portion of a Key Vault certificate.
long-summary: The certificate formatted as either PEM or DER. PEM is the default.
examples:
  - name: Download a certificate as PEM and check its fingerprint in openssl.
    text: |
        az keyvault certificate download --vault-name vault -n cert-name -f cert.pem && \\
        openssl x509 -in cert.pem -inform PEM  -noout -sha1 -fingerprint
  - name: Download a certificate as DER and check its fingerprint in openssl.
    text: |
        az keyvault certificate download --vault-name vault -n cert-name -f cert.crt -e DER && \\
        openssl x509 -in cert.crt -inform DER  -noout -sha1 -fingerprint
"""

helps['keyvault certificate get-default-policy'] = """
type: command
short-summary: Get the default policy for self-signed certificates.
long-summary: |
    This default policy can be used in conjunction with `az keyvault create` to create a self-signed certificate.
    The default policy can also be used as a starting point to create derivative policies.

    For more details, see: https://docs.microsoft.com/rest/api/keyvault/certificates-and-policies
examples:
  - name: Create a self-signed certificate with the default policy
    text: |
        az keyvault certificate create --vault-name vaultname -n cert1 \\
          -p "$(az keyvault certificate get-default-policy)"
"""

helps['keyvault certificate import'] = """
type: command
short-summary: Import a certificate into KeyVault.
long-summary: Certificates can also be used as a secrets in provisioned virtual machines.
examples:
  - name: Create a service principal with a certificate, add the certificate to Key Vault and provision a VM with that certificate.
    text: |
        service_principal=$(az ad sp create-for-rbac --create-cert)

        cert_file=$(echo $service_principal | jq .fileWithCertAndPrivateKey -r)

        az keyvault create -g my-group -n vaultname

        az keyvault certificate import --vault-name vaultname -n cert_name -f cert_file

        secrets=$(az keyvault secret list-versions --vault-name vaultname \\
          -n cert1 --query "[?attributes.enabled].id" -o tsv)

        vm_secrets=$(az vm secret format -s "$secrets")

        az vm create -g group-name -n vm-name --admin-username deploy  \\
          --image debian --secrets "$vm_secrets"
"""

helps['keyvault certificate issuer'] = """
type: group
short-summary: Manage certificate issuer information.
"""

helps['keyvault certificate issuer admin'] = """
type: group
short-summary: Manage admin information for certificate issuers.
"""

helps['keyvault certificate pending'] = """
type: group
short-summary: Manage pending certificate creation operations.
"""

helps['keyvault create'] = """
type: command
short-summary: Create a key vault.
long-summary: Default permissions are created for the current user or service principal unless the `--no-self-perms` flag is specified.
examples:
  - name: Create a key vault. (autogenerated)
    text: az keyvault create --location westus2 --name MyKeyVault --resource-group MyResourceGroup
    crafted: true
"""

helps['keyvault delete'] = """
type: command
short-summary: Delete a key vault.
examples:
  - name: Delete a key vault. (autogenerated)
    text: az keyvault delete --name MyKeyVault --resource-group MyResourceGroup
    crafted: true
"""

helps['keyvault key'] = """
type: group
short-summary: Manage keys.
"""

helps['keyvault list'] = """
type: command
short-summary: List key vaults.
"""

helps['keyvault network-rule'] = """
type: group
short-summary: Manage vault network ACLs.
"""

helps['keyvault recover'] = """
type: command
short-summary: Recover a key vault.
long-summary: Recovers a previously deleted key vault for which soft delete was enabled.
examples:
  - name: Recover a key vault. (autogenerated)
    text: az keyvault recover --location westus2 --name MyKeyVault --resource-group MyResourceGroup
    crafted: true
"""

helps['keyvault secret'] = """
type: group
short-summary: Manage secrets.
"""

helps['keyvault secret set'] = """
type: command
short-summary: Create a secret (if one doesn't exist) or update a secret in a KeyVault.
"""

helps['keyvault show'] = """
type: command
short-summary: Show details of a key vault.
examples:
  - name: Show details of a key vault. (autogenerated)
    text: az keyvault show --name MyKeyVault
    crafted: true
"""

helps['keyvault storage'] = """
type: group
short-summary: Manage storage accounts.
"""

helps['keyvault storage add'] = """
type: command
examples:
  - name: Create a storage account and setup a vault to manage its keys
    text: |
        $id = az storage account create -g resourcegroup -n storageacct --query id

        # assign the Azure Key Vault service the "Storage Account Key Operator Service Role" role.
        az role assignment create --role "Storage Account Key Operator Service Role" --scope $id \\
        --assignee cfa8b339-82a2-471a-a3c9-0fc0be7a4093

        az keyvault storage add --vault-name vault -n storageacct --active-key-name key1    \\
        --auto-regenerate-key --regeneration-period P90D  --resource-id $id
"""

helps['keyvault storage sas-definition'] = """
type: group
short-summary: Manage storage account SAS definitions.
"""

helps['keyvault storage sas-definition create'] = """
type: command
examples:
  - name: Add a sas-definition for an account sas-token
    text: |4

        $sastoken = az storage account generate-sas --expiry 2020-01-01 --permissions rw \\
        --resource-types sco --services bfqt --https-only --account-name storageacct     \\
        --account-key 00000000

        az keyvault storage sas-definition create --vault-name vault --account-name storageacct   \\
        -n rwallserviceaccess --validity-period P2D --sas-type account --template-uri $sastoken
  - name: Add a sas-definition for a blob sas-token
    text: >4

        $sastoken = az storage blob generate-sas --account-name storageacct --account-key 00000000 \\ -c container1 -n blob1 --https-only --permissions rw

        $url = az storage blob url --account-name storageacct -c container1 -n blob1


        az keyvault storage sas-definition create --vault-name vault --account-name storageacct   \\ -n rwblobaccess --validity-period P2D --sas-type service --template-uri $url?$sastoken
"""

helps['keyvault update'] = """
type: command
short-summary: Update the properties of a key vault.
examples:
  - name: Update the properties of a key vault. (autogenerated)
    text: az keyvault update --enabled-for-disk-encryption true --name MyKeyVault --resource-group MyResourceGroup
    crafted: true
"""

helps['kusto'] = """
type: group
short-summary: Manage Azure Kusto resources
"""

helps['kusto cluster'] = """
type: group
short-summary: Manage Azure Kusto clusters.
"""

helps['kusto cluster create'] = """
type: command
short-summary: Create a Kusto cluster.
examples:
  - name: Create a Kusto Cluster.
    text: |-
        az kusto cluster create -l "Central US" -n myclustername -g myrgname --sku D13_v2 --capacity 10
"""

helps['kusto cluster delete'] = """
type: command
short-summary: Delete a Kusto cluster.
"""

helps['kusto cluster list'] = """
type: command
short-summary: List a Kusto cluster.
"""

helps['kusto cluster show'] = """
type: command
short-summary: Get a Kusto cluster.
"""

helps['kusto cluster start'] = """
type: command
short-summary: Start a Kusto cluster.
long-summary: When the cluster is restarted, it takes about ten minutes for it to become available (like when it was originally provisioned). It takes additional time for data to load into the hot cache.
"""

helps['kusto cluster stop'] = """
type: command
short-summary: Stop a Kusto cluster.
long-summary: When the cluster is stopped, data is not available for queries, and you can't ingest new data. Start cluster to enable queries
"""

helps['kusto cluster update'] = """
type: command
short-summary: Update a Kusto cluster.
examples:
  - name: update a Kusto Cluster.
    text: |-
        az kusto cluster update -n myclustername -g myrgname --sku D14_v2 --capacity 4
"""

helps['kusto cluster wait'] = """
type: command
short-summary: Wait for a managed Kusto cluster to reach a desired state.
long-summary: If an operation on a cluster was interrupted or was started with `--no-wait`, use this command to wait for it to complete.
"""

helps['kusto database'] = """
type: group
short-summary: Manage Azure Kusto databases.
"""

helps['kusto database create'] = """
type: command
short-summary: Create a Kusto database.
examples:
  - name: create a Kusto Database.
    text: |-
        az kusto database create --cluster-name myclustername -g myrgname -n mydbname  --soft-delete-period P365D --hot-cache-period P31D
"""

helps['kusto database delete'] = """
type: command
short-summary: Delete a Kusto database.
"""

helps['kusto database list'] = """
type: command
short-summary: List a Kusto database.
"""

helps['kusto database show'] = """
type: command
short-summary: Get a Kusto database.
"""

helps['kusto database update'] = """
type: command
short-summary: Update a Kusto database.
examples:
  - name: create a Kusto Database.
    text: |-
        az kusto database update --cluster-name myclustername -g myrgname -n mydbname  --soft-delete-period P365D --hot-cache-period P30D
"""

helps['kusto database wait'] = """
type: command
short-summary: Wait for a managed Kusto database to reach a desired state.
long-summary: If an operation on a database was interrupted or was started with `--no-wait`, use this command to wait for it to complete.
"""

helps['lab'] = """
type: group
short-summary: Manage Azure DevTest Labs.
"""

helps['lab arm-template'] = """
type: group
short-summary: Manage Azure Resource Manager (ARM) templates in an Azure DevTest Lab.
"""

helps['lab arm-template show'] = """
type: command
short-summary: Get the details of an ARM template in a lab.
parameters:
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --name -n
    short-summary: Name of the Azure Resource Manager template.
  - name: --resource-group -g
    short-summary: Name of lab's resource group.
  - name: --export-parameters
    short-summary: Whether or not to export parameters template.
  - name: --artifact-source-name
    short-summary: Name of the artifact source.
"""

helps['lab artifact'] = """
type: group
short-summary: Manage DevTest Labs artifacts.
"""

helps['lab artifact-source'] = """
type: group
short-summary: Manage DevTest Lab artifact sources.
"""

helps['lab custom-image'] = """
type: group
short-summary: Manage custom images of a DevTest Lab.
"""

helps['lab custom-image create'] = """
type: command
short-summary: Create a custom image in a DevTest Lab.
parameters:
  - name: --name -n
    short-summary: Name of the image.
  - name: --lab-name
    short-summary: Name of the Lab.
  - name: --author
    short-summary: The author of the custom image.
  - name: --description
    short-summary: A detailed description for the custom image.
  - name: --source-vm-id
    short-summary: The resource ID of a virtual machine in the provided lab.
  - name: --os-type
    short-summary: 'Type of the OS on which the custom image is based. Allowed values are: Windows, Linux'
  - name: --os-state
    short-summary: The current state of the virtual machine.
    long-summary: >
        For Windows virtual machines: NonSysprepped, SysprepRequested, SysprepApplied
        For Linux virtual machines: NonDeprovisioned, DeprovisionRequested, DeprovisionApplied
examples:
  - name: Create a custom image in the lab from a running Windows virtual machine without applying sysprep.
    text: |
        az lab custom-image create --lab-name {LabName} -g {ResourceGroup} --name {VMName} \\
            --os-type Windows --os-state NonSysprepped \\
            --source-vm-id "/subscriptions/{SubID}/resourcegroups/{ResourceGroup}/microsoft.devtestlab/labs/{LabName}/virtualmachines/{VMName}"
"""

helps['lab environment'] = """
type: group
short-summary: Manage environments for an Azure DevTest Lab.
"""

helps['lab environment create'] = """
type: command
short-summary: Create an environment in a lab.
parameters:
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --name -n
    short-summary: Name of the environment.
  - name: --resource-group -g
    short-summary: Name of the lab's resource group.
  - name: --arm-template
    short-summary: Name or ID of the ARM template in the lab.
  - name: --artifact-source-name
    short-summary: Name of the artifact source in the lab.
    populator-commands:
      - az lab artifact-source list
  - name: --parameters
    short-summary: JSON encoded list of parameters. Use '@{file}' to load from a file.
  - name: --tags
    short-summary: The tags for the resource.
"""

helps['lab environment delete'] = """
type: command
short-summary: Delete an environment from a lab.
"""

helps['lab environment list'] = """
type: command
short-summary: List environments in a lab.
"""

helps['lab environment show'] = """
type: command
short-summary: Get the details for an environment of a lab.
"""

helps['lab formula'] = """
type: group
short-summary: Manage formulas for an Azure DevTest Lab.
"""

helps['lab formula export-artifacts'] = """
type: command
short-summary: Export artifacts from a formula.
parameters:
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --name -n
    short-summary: Name of the formula.
"""

helps['lab formula show'] = """
type: command
short-summary: Show formulae from an Azure DevTest Lab.
parameters:
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --name -n
    short-summary: Name of the formula.
"""

helps['lab gallery-image'] = """
type: group
short-summary: List Azure Marketplace images allowed for a DevTest Lab.
"""

helps['lab secret'] = """
type: group
short-summary: Manage secrets of an Azure DevTest Lab.
"""

helps['lab secret set'] = """
type: command
short-summary: Set a secret for a lab.
parameters:
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --name -n
    short-summary: Name of the secret.
  - name: --value
    short-summary: Value of the secret.
"""

helps['lab vm'] = """
type: group
short-summary: Manage VMs in an Azure DevTest Lab.
"""

helps['lab vm apply-artifacts'] = """
type: command
short-summary: Apply artifacts to a virtual machine in Azure DevTest Lab.
parameters:
  - name: --resource-group -g
    short-summary: Name of lab's resource group.
  - name: --lab-name
    short-summary: Name of the Lab.
  - name: --name -n
    short-summary: Name of the virtual machine.
  - name: --artifacts
    short-summary: JSON encoded array of artifacts to be applied. Use '@{file}' to load from a file.
"""

helps['lab vm claim'] = """
type: command
short-summary: Claim a virtual machine from the Lab.
parameters:
  - name: --resource-group -g
    short-summary: Name of lab's resource group.
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --name -n
    short-summary: Name of the virtual machine to claim.
examples:
  - name: Claim any available virtual machine in the lab.
    text: >
        az lab vm claim -g {ResourceGroup} --lab-name {LabName}
  - name: Claim a specific virtual machine in the lab.
    text: >
        az lab vm claim -g {ResourceGroup} --lab-name {LabName} --name {VMName}
  - name: Claim multiple virtual machines in the lab by IDs.
    text: |
        az lab vm claim --ids \\
            /subscriptions/{SubID}/resourcegroups/{ResourceGroup}/providers/microsoft.devtestlab/labs/{LabName}/virtualmachines/{VMName1} \\
            /subscriptions/{SubID}/resourcegroups/{ResourceGroup}/providers/microsoft.devtestlab/labs/{LabName}/virtualmachines/{VMName2}
"""

helps['lab vm create'] = """
type: command
short-summary: Create a VM in a lab.
parameters:
  - name: --name -n
    short-summary: Name of the virtual machine.
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --notes
    short-summary: Notes for the virtual machine.
  - name: --image
    short-summary: The name of the operating system image (gallery image name or custom image name/ID).
    long-summary: Use `az lab gallery-image list` for available gallery images or `az lab custom-image list` for available custom images.
  - name: --image-type
    short-summary: 'Type of the image. Allowed values are: gallery, custom'
  - name: --formula
    short-summary: Name of the formula. Use `az lab formula list` for available formulas.
    long-summary: >
        Use `az lab formula` with the `--export-artifacts` flag to export and update artifacts, then pass
        the results via the `--artifacts` argument.
  - name: --size
    short-summary: 'The size of the VM to be created. See https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.'
  - name: --admin-username
    short-summary: Username for the VM admin.
  - name: --admin-password
    short-summary: Password for the VM admin.
  - name: --ssh-key
    short-summary: The SSH public key or public key file path. Use `--generate-ssh-keys` to generate SSH keys.
  - name: --authentication-type
    short-summary: 'Type of authentication allowed for the VM. Allowed values are: password, ssh.'
  - name: --saved-secret
    short-summary: Name of the saved secret to be used for authentication.
    long-summary: When this value is provided, it is used in the place of other authentication methods.
  - name: --vnet-name
    short-summary: Name of the virtual network to add the VM to.
  - name: --subnet
    short-summary: Name of the subnet to add the VM to.
  - name: --ip-configuration
    short-summary: 'Type of IP configuration to use for the VM. Allowed values are: shared, public, private.'
    long-summary: If omitted, will be selected based on the VM's vnet.
  - name: --artifacts
    short-summary: JSON encoded array of artifacts to be applied. Use '@{file}' to load from a file.
  - name: --tags
    short-summary: Space-separated tags in `key[=value]` format.
    long-summary: Tags may be cleared by assigning the empty value "" to them.
  - name: --allow-claim
    short-summary: Flag indicating if the VM should be created as claimable.
  - name: --disk-type
    short-summary: Storage type to use for virtual machine.
  - name: --expiration-date
    short-summary: The expiration date in UTC(yyyy-MM-ddTHH:mm:ss) for the VM.
  - name: --generate-ssh-keys
    short-summary: Generate SSH public and private key files if missing.
examples:
  - name: Create a VM in the lab from a gallery image.
    text: >
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 16.04 LTS" --image-type gallery --size Standard_DS1_v2
  - name: Create a VM in the lab from a gallery image with SSH authentication.
    text: >
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 16.04 LTS" --image-type gallery --size Standard_DS1_v2 --authentication-type ssh
  - name: Create a claimable VM in the lab from a gallery image with password authentication.
    text: >
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 16.04 LTS" --image-type gallery --size Standard_DS1_v2 --allow-claim
  - name: Create a windows VM in the lab from a gallery image with password authentication.
    text: >
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Windows Server 2008 R2 SP1" --image-type gallery --size Standard_DS1_v2
  - name: Create a VM in the lab from a custom image.
    text: >
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "jenkins_custom" --image-type custom --size Standard_DS1_v2
  - name: Create a VM in the lab with a public IP.
    text: >
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 16.04 LTS" --image-type gallery --size Standard_DS1_v2 --ip-configuration public
  - name: Create a VM from a formula.
    text: >
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --formula MyFormula --artifacts '@artifacts.json'
"""

helps['lab vm list'] = """
type: command
short-summary: List the VMs in an Azure DevTest Lab.
parameters:
  - name: --lab-name
    short-summary: Name of the lab.
  - name: --order-by
    short-summary: The ordering expression for the results using OData notation.
  - name: --top
    short-summary: The maximum number of resources to return.
  - name: --filters
    short-summary: The filter to apply.
  - name: --expand
    short-summary: The expand query.
  - name: --claimable
    short-summary: List only claimable virtual machines in the lab. Cannot be used with `--filters`.
  - name: --all
    short-summary: List all virtual machines in the lab. Cannot be used with `--filters`
  - name: --environment
    short-summary: Name or ID of the environment to list virtual machines in. Cannot be used with `--filters`.
  - name: --object-id
    short-summary: Object ID of the owner to list VMs for.
"""

helps['lab vnet'] = """
type: group
short-summary: Manage virtual networks of an Azure DevTest Lab.
"""

helps['lock'] = """
type: group
short-summary: Manage Azure locks.
"""

helps['lock create'] = """
type: command
short-summary: Create a lock.
long-summary: 'Locks can exist at three different scopes: subscription, resource group and resource.'
examples:
  - name: Create a read-only subscription level lock.
    text: >
        az lock create --name lockName --resource-group group --lock-type ReadOnly
"""

helps['lock delete'] = """
type: command
short-summary: Delete a lock.
examples:
  - name: Delete a resource group-level lock
    text: >
        az lock delete --name lockName --resource-group group
"""

helps['lock list'] = """
type: command
short-summary: List lock information.
examples:
  - name: List out the locks on a vnet resource. Includes locks in the associated group and subscription.
    text: >
        az lock list --resource myvnet --resource-type Microsoft.Network/virtualNetworks -g group
  - name: List out all locks on the subscription level
    text: >
        az lock list
"""

helps['lock show'] = """
type: command
short-summary: Show the properties of a lock
examples:
  - name: Show a subscription level lock
    text: >
        az lock show -n lockname
  - name: Show the properties of a lock (autogenerated)
    text: az lock show --name lockname --resource-group MyResourceGroup --resource-name MyResource --resource-type Microsoft.Network/virtualNetworks
    crafted: true
"""

helps['lock update'] = """
type: command
short-summary: Update a lock.
examples:
  - name: Update a resource group level lock with new notes and type
    text: >
        az lock update --name lockName --resource-group group --notes newNotesHere --lock-type CanNotDelete
"""

helps['login'] = """
type: command
short-summary: Log in to Azure.
examples:
  - name: Log in interactively.
    text: >
        az login
  - name: Log in with user name and password. This doesn't work with Microsoft accounts or accounts that have two-factor authentication enabled.
    text: >
        az login -u johndoe@contoso.com -p VerySecret
  - name: Log in with a service principal using client secret.
    text: >
        az login --service-principal -u http://azure-cli-2016-08-05-14-31-15 -p VerySecret --tenant contoso.onmicrosoft.com
  - name: Log in with a service principal using client certificate.
    text: >
        az login --service-principal -u http://azure-cli-2016-08-05-14-31-15 -p ~/mycertfile.pem --tenant contoso.onmicrosoft.com
  - name: Log in using a VM's system assigned identity
    text: >
        az login --identity
  - name: Log in using a VM's user assigned identity. Client or object ids of the service identity also work
    text: >
        az login --identity -u /subscriptions/<subscriptionId>/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
"""

helps['managedapp'] = """
type: group
short-summary: Manage template solutions provided and maintained by Independent Software Vendors (ISVs).
"""

helps['managedapp create'] = """
type: command
short-summary: Create a managed application.
examples:
  - name: Create a managed application of kind 'ServiceCatalog'. This requires a valid managed application definition ID.
    text: |
        az managedapp create -g MyResourceGroup -n MyManagedApp -l westcentralus --kind ServiceCatalog \\
            -m "/subscriptions/{SubID}/resourceGroups/{ManagedResourceGroup}" \\
            -d "/subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Solutions/applianceDefinitions/{ApplianceDefinition}"
  - name: Create a managed application of kind 'MarketPlace'. This requires a valid plan, containing details about existing marketplace package like plan name, version, publisher and product.
    text: |
        az managedapp create -g MyResourceGroup -n MyManagedApp -l westcentralus --kind MarketPlace \\
            -m "/subscriptions/{SubID}/resourceGroups/{ManagedResourceGroup}" \\
            --plan-name ContosoAppliance --plan-version "1.0" --plan-product "contoso-appliance" --plan-publisher Contoso
"""

helps['managedapp definition'] = """
type: group
short-summary: Manage Azure Managed Applications.
"""

helps['managedapp definition create'] = """
type: command
short-summary: Create a managed application definition.
examples:
  - name: Create a managed application defintion.
    text: >
        az managedapp definition create -g MyResourceGroup -n MyManagedAppDef -l eastus --display-name "MyManagedAppDef" \\
            --description "My Managed App Def description" -a "myPrincipalId:myRoleId" --lock-level None \\
            --package-file-uri "https://path/to/myPackage.zip"
  - name: Create a managed application defintion with inline values for createUiDefinition and mainTemplate.
    text: >
        az managedapp definition create -g MyResourceGroup -n MyManagedAppDef -l eastus --display-name "MyManagedAppDef" \\
            --description "My Managed App Def description" -a "myPrincipalId:myRoleId" --lock-level None \\
            --create-ui-definition @myCreateUiDef.json --main-template @myMainTemplate.json
"""

helps['managedapp definition delete'] = """
type: command
short-summary: Delete a managed application definition.
examples:
  - name: Delete a managed application definition. (autogenerated)
    text: az managedapp definition delete --name MyManagedApplicationDefinition --resource-group MyResourceGroup
    crafted: true
"""

helps['managedapp definition list'] = """
type: command
short-summary: List managed application definitions.
examples:
  - name: List managed application definitions. (autogenerated)
    text: az managedapp definition list --resource-group MyResourceGroup
    crafted: true
"""

helps['managedapp delete'] = """
type: command
short-summary: Delete a managed application.
examples:
  - name: Delete a managed application. (autogenerated)
    text: az managedapp delete --name MyManagedApplication --resource-group MyResourceGroup
    crafted: true
"""

helps['managedapp list'] = """
type: command
short-summary: List managed applications.
examples:
  - name: List managed applications. (autogenerated)
    text: az managedapp list --resource-group MyResourceGroup
    crafted: true
"""

helps['managedservices'] = """
type: group
short-summary: Manage the registration assignments and definitions in Azure.
"""

helps['managedservices assignment'] = """
type: group
short-summary: Manage the registration assignments in Azure.
"""

helps['managedservices assignment create'] = """
type: command
short-summary: Creates a new registration assignment.
parameters:
  - name: --definition
    short-summary: |
        The fully qualified resource id of the registration definition.
  - name: --assignment-id
    short-summary: |
        Can be used to override the generated registration assignment id.
examples:
  - name: Create an assignment under the default subscription scope.
    text: az managedservices assignment create --definition "/subscriptions/a62076fa-768a-403c-9d9d-6a9919aae441/providers/Microsoft.ManagedServices/registrationDefinitions/0c3e9687-b461-4615-b6e4-74d54998d6e4"
  - name: Create an assignment under a given resource group scope.
    text: az managedservices assignment create --definition "/subscriptions/a62076fa-768a-403c-9d9d-6a9919aae441/providers/Microsoft.ManagedServices/registrationDefinitions/0c3e9687-b461-4615-b6e4-74d54998d6e4" --resource-group mygroup
"""

helps['managedservices assignment delete'] = """
type: command
short-summary: Deletes the registration assignment.
examples:
  - name: Deletes an assignment given its identifier under the default subscription scope.
    text: az managedservices assignment delete --assignment d3087cf0-e180-4cca-b147-54ae00c7b504
  - name: Deletes an assignment given its fully qualified resource id.
    text: az managedservices assignment delete --assignment /subscriptions/a62076fa-768a-403c-9d9d-6a9919aae441/providers/Microsoft.ManagedServices/registrationAssignments/0c3e9687-b461-4615-b6e4-74d54998d6e4
"""

helps['managedservices assignment list'] = """
type: command
short-summary: List all the registration assignments.
examples:
  - name: Lists all the registration assignments under the default scope.
    text: az managedservices assignment list
  - name: Lists all the registration assignments under the given resource group.
    text: az managedservices assignment list --resource-group mygroup
  - name: Lists all the registration assignments under the default scope along with the associated registration definition details.
    text: az managedservices assignment list --include-definition true
"""

helps['managedservices assignment show'] = """
type: command
short-summary: Gets a registration assignment.
examples:
  - name: Get an assignment given its identifier under the default subscription scope.
    text: az managedservices assignment show --assignment d3087cf0-e180-4cca-b147-54ae00c7b504
  - name: Get an assignment given its fully qualified resource id.
    text: az managedservices assignment show --assignment /subscriptions/a62076fa-768a-403c-9d9d-6a9919aae441/providers/Microsoft.ManagedServices/registrationAssignments/0c3e9687-b461-4615-b6e4-74d54998d6e4
  - name: Get an assignment given its identifier under the default subscription scope with the registration definition details.
    text: az managedservices assignment show --assignment d3087cf0-e180-4cca-b147-54ae00c7b504 --include-definition true
"""

helps['managedservices definition'] = """
type: group
short-summary: Manage the registration definitions in Azure.
"""

helps['managedservices definition create'] = """
type: command
short-summary: Creates a new registration definition.
parameters:
  - name: --name
    short-summary: |
        The name of the registration definition.
  - name: --tenant-id
    short-summary: |
        The managed by tenant id.
  - name: --principal-id
    short-summary: |
        The principal id.
  - name: --role-definition-id
    short-summary: |
        The role definition id.
  - name: --description
    short-summary: |
        The friendly description.
  - name: --plan-name
    short-summary: |
        The plan name.
  - name: --plan-product
    short-summary: |
        The plan product.
  - name: --plan-publisher
    short-summary: |
        The plan publisher.
  - name: --plan-version
    short-summary: |
        The plan version.
  - name: --definition-id
    short-summary: |
        Can be used to override the generated registration definition id.
examples:
  - name: Creates a registration definition under the default subscription scope with the required parameters.
    text: az managedservices definition create --name mydef --tenant-id dab3375b-6197-4a15-a44b-16c41faa91d7 --principal-id b6f6c88a-5b7a-455e-ba40-ce146d4d3671 --role-definition-id ccdd72a7-3385-48ef-bd42-f606fba81ae7
"""

helps['managedservices definition delete'] = """
type: command
short-summary: Deletes a registration.
examples:
  - name: Deletes the registration definition given its identifier under the default subscription scope.
    text: az managedservices definition delete --definition af8772a0-fd9c-4ddc-8ad0-7d4b3913d7dd
  - name: Deletes the registration definition given its fully qualified resource id.
    text: az managedservices definition delete --definition /subscriptions/39033314-9b39-4c7b-84fd-0e26e55f15dc/providers/Microsoft.ManagedServices/registrationDefinitions/1d693e4f-9e79-433a-b3a2-afce1f8b61ec
"""

helps['managedservices definition list'] = """
type: command
short-summary: List all the registration definitions under the default scope or under the subscription provided.
examples:
  - name: Lists all the registration definitions under the default subscription scope.
    text: az managedservices definition list
"""

helps['managedservices definition show'] = """
type: command
short-summary: Gets a registration definition.
examples:
  - name: Gets the registration definition given its identifier under the default subscription scope.
    text: az managedservices definition show --definition af8772a0-fd9c-4ddc-8ad0-7d4b3913d7dd
  - name: Gets the registration definition given its fully qualified resource id.
    text: az managedservices definition show --definition /subscriptions/39033314-9b39-4c7b-84fd-0e26e55f15dc/providers/Microsoft.ManagedServices/registrationDefinitions/1d693e4f-9e79-433a-b3a2-afce1f8b61ec
"""

helps['maps'] = """
type: group
short-summary: Manage Azure Maps.
"""

helps['maps account'] = """
type: group
short-summary: Manage Azure Maps accounts.
"""

helps['maps account create'] = """
type: command
short-summary: Create a maps account.
parameters:
  - name: --accept-tos
    short-summary: Accept the Terms of Service, and do not prompt for confirmation.
    long-summary: |
        By creating an Azure Maps account, you agree that you have read and agree to the
        License (https://azure.microsoft.com/support/legal/) and
        Privacy Statement (https://privacy.microsoft.com/privacystatement).

"""

helps['maps account delete'] = """
type: command
short-summary: Delete a maps account.
"""

helps['maps account keys'] = """
type: group
short-summary: Manage Azure Maps account keys.
"""

helps['maps account keys list'] = """
type: command
short-summary: List the keys to use with the Maps APIs.
long-summary: |
    A key is used to authenticate and authorize access to the Maps REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.
"""

helps['maps account keys renew'] = """
type: command
short-summary: Renew either the primary or secondary key for use with the Maps APIs.
long-summary: |
    This command immediately invalidates old API keys. Only the renewed keys can be used to connect to maps.
"""

helps['maps account list'] = """
type: command
short-summary: Show all maps accounts in a subscription or in a resource group.
"""

helps['maps account show'] = """
type: command
short-summary: Show the details of a maps account.
"""

helps['maps account update'] = """
type: command
short-summary: Update the properties of a maps account.
"""

helps['mariadb'] = """
type: group
short-summary: Manage Azure Database for MariaDB servers.
"""

helps['mariadb db'] = """
type: group
short-summary: Manage MariaDB databases on a server.
"""

helps['mariadb db create'] = """
type: command
short-summary: Create a MariaDB database.
examples:
  - name: Create database 'testdb' in the server 'testsvr' with the default parameters.
    text: az mariadb db create -g testgroup -s testsvr -n testdb
  - name: Create database 'testdb' in server 'testsvr' with a given character set and collation rules.
    text: az mariadb db create -g testgroup -s testsvr -n testdb --charset {valid_charset} --collation {valid_collation}
"""

helps['mariadb db delete'] = """
type: command
short-summary: Delete a database.
examples:
  - name: Delete database 'testdb' in the server 'testsvr'.
    text: az mariadb db delete -g testgroup -s testsvr -n testdb
"""

helps['mariadb db list'] = """
type: command
short-summary: List the databases for a server.
examples:
  - name: List databases in the server 'testsvr'.
    text: az mariadb db list -g testgroup -s testsvr
"""

helps['mariadb db show'] = """
type: command
short-summary: Show the details of a database.
examples:
  - name: Show database 'testdb' in the server 'testsvr'.
    text: az mariadb db show -g testgroup -s testsvr -n testdb
"""

helps['mariadb server'] = """
type: group
short-summary: Manage MariaDB servers.
"""

helps['mariadb server configuration'] = """
type: group
short-summary: Manage configuration values for a server.
"""

helps['mariadb server configuration list'] = """
type: command
short-summary: List the configuration values for a server.
"""

helps['mariadb server configuration set'] = """
type: command
short-summary: Update the configuration of a server.
examples:
  - name: Set a new configuration value.
    text: az mariadb server configuration set -g testgroup -s testsvr -n {config_name} --value {config_value}
  - name: Set a configuration value to its default.
    text: az mariadb server configuration set -g testgroup -s testsvr -n {config_name}
"""

helps['mariadb server configuration show'] = """
type: command
short-summary: Get the configuration for a server."
"""

helps['mariadb server create'] = """
type: command
short-summary: Create a server.
examples:
  - name: Create a MariaDB server in North Europe with sku GP_Gen5_2 (General Purpose, Gen 5 hardware, 2 vCores).
    text: az mariadb server create -l northeurope -g testgroup -n testsvr -u username -p password \\ --sku-name GP_Gen5_2
  - name: Create a MariaDB server with all paramaters set.
    text: az mariadb server create -l northeurope -g testgroup -n testsvr -u username -p password \\ --sku-name B_Gen5_1 --ssl-enforcement Disabled \\ --backup-retention 10 --geo-redundant-backup Enabled --storage-size 51200 --tags "key=value" --version {server-version}
"""

helps['mariadb server delete'] = """
type: command
short-summary: Delete a server.
examples:
  - name: Delete a server.
    text: az mariadb server delete -g testgroup -n testsvr
"""

helps['mariadb server firewall-rule'] = """
type: group
short-summary: Manage firewall rules for a server.
"""

helps['mariadb server firewall-rule create'] = """
type: command
short-summary: Create a new firewall rule for a server.
examples:
  - name: Create a firewall rule allowing connections from a specific IP address.
    text: az mariadb server firewall-rule create -g testgroup -s testsvr -n allowip --start-ip-address 107.46.14.221 --end-ip-address 107.46.14.221
  - name: Create a firewall rule allowing connections from an IP address range.
    text: az mariadb server firewall-rule create -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.0 --end-ip-address 107.46.14.221
"""

helps['mariadb server firewall-rule delete'] = """
type: command
short-summary: Delete a firewall rule.
"""

helps['mariadb server firewall-rule list'] = """
type: command
short-summary: List all firewall rules for a server.
"""

helps['mariadb server firewall-rule show'] = """
type: command
short-summary: Get the details of a firewall rule.
"""

helps['mariadb server firewall-rule update'] = """
type: command
short-summary: Update a firewall rule.
examples:
  - name: Update a firewall rule's start IP address.
    text: az mariadb server firewall-rule update -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.1
  - name: Update a firewall rule's start and end IP address.
    text: az mariadb server firewall-rule update -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.2 --end-ip-address 107.46.14.218
"""

helps['mariadb server georestore'] = """
type: command
short-summary: Geo-restore a server from backup.
examples:
  - name: Geo-restore 'testsvr' into a new server 'testsvrnew' located in West US 2.
    text: az mariadb server georestore -g testgroup -n testsvrnew --source-server testsvr -l westus2
  - name: Geo-restore 'testsvr' into a new server 'testsvrnew' located in West US 2 with sku GP_Gen5_2.
    text: az mariadb server georestore -g testgroup -n testsvrnew --source-server testsvr -l westus2 --sku-name GP_Gen5_2
  - name: Geo-restore 'testsvr2' into a new server 'testsvrnew', where 'testsvrnew' is in a different resource group from 'testsvr2'.
    text: |
        az mariadb server georestore -g testgroup -n testsvrnew \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforMariaDB/servers/testsvr2" \\
            -l westus2
"""

helps['mariadb server list'] = """
type: command
short-summary: List available servers.
examples:
  - name: List all MariaDB servers in a subscription.
    text: az mariadb server list
  - name: List all MariaDB servers in a resource group.
    text: az mariadb server list -g testgroup
"""

helps['mariadb server replica'] = """
type: group
short-summary: Manage read replicas.
"""

helps['mariadb server replica create'] = """
type: command
short-summary: Create a read replica for a server.
examples:
  - name: Create a read replica 'testreplsvr' for 'testsvr'.
    text: az mariadb server replica create -n testreplsvr -g testgroup -s testsvr
  - name: Create a read replica 'testreplsvr' for 'testsvr2', where 'testreplsvr' is in a different resource group.
    text: |
        az mariadb server replica create -n testreplsvr -g testgroup \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforMariaDB/servers/testsvr2"
"""

helps['mariadb server replica list'] = """
type: command
short-summary: List all read replicas for a given server.
examples:
  - name: List all read replicas for master server 'testsvr'.
    text: az mariadb server replica list -g testgroup -s testsvr
"""

helps['mariadb server replica stop'] = """
type: command
short-summary: Stop replication to a read replica and make it a read/write server.
examples:
  - name: Stop replication to 'testreplsvr' and make it a read/write server.
    text: az mariadb server replica stop -g testgroup -n testreplsvr
"""

helps['mariadb server restart'] = """
type: command
short-summary: Restart a server.
examples:
  - name: Restart a server.
    text: az mariadb server restart -g testgroup -n testsvr
"""

helps['mariadb server restore'] = """
type: command
short-summary: Restore a server from backup.
examples:
  - name: Restore 'testsvr' to a specific point-in-time as a new server 'testsvrnew'.
    text: az mariadb server restore -g testgroup -n testsvrnew --source-server testsvr --restore-point-in-time "2017-06-15T13:10:00Z"
  - name: Restore 'testsvr2' to 'testsvrnew', where 'testsvrnew' is in a different resource group from 'testsvr2'.
    text: |
        az mariadb server restore -g testgroup -n testsvrnew \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforMariaDB/servers/testsvr2" \\
            --restore-point-in-time "2017-06-15T13:10:00Z"
"""

helps['mariadb server show'] = """
type: command
short-summary: Get the details of a server.
examples:
  - name: Get the details of a server. (autogenerated)
    text: az mariadb server show --name MyServer --resource-group MyResourceGroup
    crafted: true
"""

helps['mariadb server update'] = """
type: command
short-summary: Update a server.
examples:
  - name: Update a server's sku.
    text: az mariadb server update -g testgroup -n testsvrnew --sku-name GP_Gen5_4
  - name: Update a server's tags.
    text: az mariadb server update -g testgroup -n testsvrnew --tags "k1=v1" "k2=v2"
"""

helps['mariadb server vnet-rule'] = """
type: group
short-summary: Manage a server's virtual network rules.
"""

helps['mariadb server vnet-rule create'] = """
type: command
short-summary: Create a virtual network rule to allows access to a MariaDB server.
examples:
  - name: Create a virtual network rule by providing the subnet id.
    text: az mariadb server vnet-rule create -g testgroup -s testsvr -n vnetRuleName --subnet /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/vnetName/subnets/subnetName
  - name: Create a vnet rule by providing the vnet and subnet name. The subnet id is created by taking the resource group name and subscription id of the server.
    text: az mariadb server vnet-rule create -g testgroup -s testsvr -n vnetRuleName --subnet subnetName --vnet-name vnetName
"""

helps['mariadb server vnet-rule update'] = """
type: command
short-summary: Update a virtual network rule.
"""

helps['mariadb server wait'] = """
type: command
short-summary: Wait for server to satisfy certain conditions.
"""

helps['mariadb server-logs'] = """
type: group
short-summary: Manage server logs.
"""

helps['mariadb server-logs download'] = """
type: command
short-summary: Download log files.
examples:
  - name: Download log files f1 and f2 to the current directory from the server 'testsvr'.
    text: az mariadb server-logs download -g testgroup -s testsvr -n f1.log f2.log
"""

helps['mariadb server-logs list'] = """
type: command
short-summary: List log files for a server.
examples:
  - name: List log files for 'testsvr' modified in the last 72 hours (default value).
    text: az mariadb server-logs list -g testgroup -s testsvr
  - name: List log files for 'testsvr' modified in the last 10 hours.
    text: az mariadb server-logs list -g testgroup -s testsvr --file-last-written 10
  - name: List log files for 'testsvr' less than 30Kb in size.
    text: az mariadb server-logs list -g testgroup -s testsvr --max-file-size 30
"""

helps['monitor'] = """
type: group
short-summary: Manage the Azure Monitor Service.
"""

helps['monitor action-group'] = """
type: group
short-summary: Manage action groups
"""

helps['monitor action-group create'] = """
type: command
short-summary: Create a new action group
parameters:
  - name: --action -a
    short-summary: Add receivers to the action group during the creation
    long-summary: |
        Usage:   --action TYPE NAME [ARG ...]
        Email:   --action email bob bob@contoso.com
        SMS:     --action sms charli 1 5551234567
        Webhook: --action webhook alert_hook https://www.contoso.com/alert
        Multiple actions can be specified by using more than one `--action` argument.
  - name: --short-name
    short-summary: The short name of the action group
examples:
  - name: Create a new action group (autogenerated)
    text: az monitor action-group create --action webhook https://alerts.contoso.com apiKey={APIKey} type=HighCPU --name MyActionGroup --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor action-group list'] = """
type: command
short-summary: List action groups under a resource group or the current subscription
parameters:
  - name: --resource-group -g
    type: string
    short-summary: >
        Name of the resource group under which the action groups are being listed. If it is omitted, all the action groups under
        the current subscription are listed.
"""

helps['monitor action-group show'] = """
type: command
short-summary: Show the details of an action group
examples:
  - name: Show the details of an action group (commonly used with --output and --query). (autogenerated)
    text: az monitor action-group show --name MyActionGroup --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor action-group update'] = """
type: command
short-summary: Update an action group
parameters:
  - name: --short-name
    short-summary: Update the group short name of the action group
  - name: --add-action -a
    short-summary: Add receivers to the action group
    long-summary: |
        Usage:   --add-action TYPE NAME [ARG ...]
        Email:   --add-action email bob bob@contoso.com
        SMS:     --add-action sms charli 1 5551234567
        Webhook: --add-action https://www.contoso.com/alert
        Multiple actions can be specified by using more than one `--add-action` argument.
  - name: --remove-action -r
    short-summary: Remove receivers from the action group. Accept space-separated list of receiver names.
"""

helps['monitor activity-log'] = """
type: group
short-summary: Manage activity logs.
"""

helps['monitor activity-log alert'] = """
type: group
short-summary: Manage activity log alerts
"""

helps['monitor activity-log alert action-group'] = """
type: group
short-summary: Manage action groups for activity log alerts
"""

helps['monitor activity-log alert action-group add'] = """
type: command
short-summary: Add action groups to this activity log alert. It can also be used to overwrite existing webhook properties of particular action groups.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alerts
  - name: --action-group -a
    short-summary: The names or the resource ids of the action groups to be added.
  - name: --reset
    short-summary: Remove all the existing action groups before add new conditions.
  - name: --webhook-properties -w
    short-summary: >
        Space-separated webhook properties in 'key[=value]' format. These properties will be associated with
        the action groups added in this command.
    long-summary: >
        For any webhook receiver in these action group, these data are appended to the webhook payload.
        To attach different webhook properties to different action groups, add the action groups in separate update-action commands.
  - name: --strict
    short-summary: Fails the command if an action group to be added will change existing webhook properties.
examples:
  - name: Add an action group and specify webhook properties.
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} \\
          --action /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup} \\
          --webhook-properties usage=test owner=jane
  - name: Overwite an existing action group's webhook properties.
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} \\
          -a /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup} \\
          --webhook-properties usage=test owner=john
  - name: Remove webhook properties from an existing action group.
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} \\
          -a /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup}
  - name: Add new action groups but prevent the command from accidently overwrite existing webhook properties
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} --strict \\
          --action-group {ResourceIDList}
"""

helps['monitor activity-log alert action-group remove'] = """
type: command
short-summary: Remove action groups from this activity log alert
parameters:
  - name: --name -n
    short-summary: Name of the activity log alerts
  - name: --action-group -a
    short-summary: The names or the resource ids of the action groups to be added.
"""

helps['monitor activity-log alert create'] = """
type: command
short-summary: Create a default activity log alert
long-summary: This command will create a default activity log with one condition which compares if the activities logs 'category' field equals to 'ServiceHealth'. The newly created activity log alert does not have any action groups attached to it.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alerts
  - name: --scope -s
    short-summary: A list of strings that will be used as prefixes.
    long-summary: >
        The alert will only apply to activity logs with resourceIDs that fall under one of these prefixes.
        If not provided, the path to the resource group will be used.
  - name: --disable
    short-summary: Disable the activity log alert after it is created.
  - name: --description
    short-summary: A description of this activity log alert
  - name: --condition -c
    short-summary: The condition that will cause the alert to activate. The format is FIELD=VALUE[ and FIELD=VALUE...].
    long-summary: >
        The possible values for the field are 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup',
        'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties.'.
  - name: --action-group -a
    short-summary: >
        Add an action group. Accepts space-separated action group identifiers. The identifier can be the action group's name
        or its resource ID.
  - name: --webhook-properties -w
    short-summary: >
        Space-separated webhook properties in 'key[=value]' format. These properties are associated with the action groups
        added in this command.
    long-summary: >
        For any webhook receiver in these action group, this data is appended to the webhook payload. To attach different webhook
        properties to different action groups, add the action groups in separate update-action commands.
examples:
  - name: Create an alert with default settings.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup}
  - name: Create an alert with condition about error level service health log.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup} \\
          --condition category=ServiceHealth and level=Error
  - name: Create an alert with an action group and specify webhook properties.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup} \\
          -a /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup} \\
          -w usage=test owner=jane
  - name: Create an alert which is initially disabled.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup} --disable
"""

helps['monitor activity-log alert list'] = """
type: command
short-summary: List activity log alerts under a resource group or the current subscription.
parameters:
  - name: --resource-group -g
    short-summary: Name of the resource group under which the activity log alerts are being listed. If it is omitted, all the activity log alerts under the current subscription are listed.
"""

helps['monitor activity-log alert scope'] = """
type: group
short-summary: Manage scopes for activity log alerts
"""

helps['monitor activity-log alert scope add'] = """
type: command
short-summary: Add scopes to this activity log alert.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alerts
  - name: --scope -s
    short-summary: The scopes to add
  - name: --reset
    short-summary: Remove all the existing scopes before add new scopes.
"""

helps['monitor activity-log alert scope remove'] = """
type: command
short-summary: Removes scopes from this activity log alert.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alerts
  - name: --scope -s
    short-summary: The scopes to remove
"""

helps['monitor activity-log alert update'] = """
type: command
short-summary: Update the details of this activity log alert
parameters:
  - name: --description
    short-summary: A description of this activity log alert.
  - name: --condition -c
    short-summary: The conditional expression that will cause the alert to activate. The format is FIELD=VALUE[ and FIELD=VALUE...].
    long-summary: >
        The possible values for the field are 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup',
        'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties.'.
examples:
  - name: Update the condition
    text: >
        az monitor activity-log alert update -n {AlertName} -g {ResourceGroup} \\
          --condition category=ServiceHealth and level=Error
  - name: Disable an alert
    text: >
        az monitor activity-log alert update -n {AlertName} -g {ResourceGroup} --enable false
"""

helps['monitor activity-log list'] = """
type: command
short-summary: List and query activity log events.
parameters:
  - name: --correlation-id
    short-summary: Correlation ID to query.
  - name: --resource-id
    short-summary: ARM ID of a resource.
  - name: --namespace
    short-summary: Resource provider namespace.
  - name: --caller
    short-summary: Caller to query for, such as an e-mail address or service principal ID.
  - name: --status
    short-summary: >
        Status to query for (ex: Failed)
  - name: --max-events
    short-summary: Maximum number of records to return.
  - name: --select
    short-summary: Space-separated list of properties to return.
  - name: --offset
    short-summary: >
        Time offset of the query range, in ##d##h format.
    long-summary: >
        Can be used with either --start-time or --end-time. If used with --start-time, then
        the end time will be calculated by adding the offset. If used with --end-time (default), then
        the start time will be calculated by subtracting the offset. If --start-time and --end-time are
        provided, then --offset will be ignored.
examples:
  - name: List all events from July 1st, looking forward one week.
    text: az monitor activity-log list --start-time 2018-07-01 --offset 7d
  - name: List events within the past six hours based on a correlation ID.
    text: az monitor activity-log list --correlation-id b5eac9d2-e829-4c9a-9efb-586d19417c5f
  - name: List events within the past hour based on resource group.
    text: az monitor activity-log list -g {ResourceGroup} --offset 1h
"""

helps['monitor activity-log list-categories'] = """
type: command
short-summary: List the event categories of activity logs.
"""

helps['monitor alert'] = """
type: group
short-summary: Manage classic metric-based alert rules.
"""

helps['monitor alert create'] = """
type: command
short-summary: Create a classic metric-based alert rule.
parameters:
  - name: --action -a
    short-summary: Add an action to fire when the alert is triggered.
    long-summary: |
        Usage:   --action TYPE KEY [ARG ...]
        Email:   --action email bob@contoso.com ann@contoso.com
        Webhook: --action webhook https://www.contoso.com/alert apiKey=value
        Webhook: --action webhook https://www.contoso.com/alert?apiKey=value
        Multiple actions can be specified by using more than one `--action` argument.
  - name: --description
    short-summary: Free-text description of the rule. Defaults to the condition expression.
  - name: --disabled
    short-summary: Create the rule in a disabled state.
  - name: --condition
    short-summary: The condition which triggers the rule.
    long-summary: >
        The form of a condition is "METRIC {>,>=,<,<=} THRESHOLD {avg,min,max,total,last} PERIOD".
        Values for METRIC and appropriate THRESHOLD values can be obtained from `az monitor metric` commands,
        and PERIOD is of the form "##h##m##s".
  - name: --email-service-owners
    short-summary: Email the service owners if an alert is triggered.
examples:
  - name: Create a high CPU usage alert on a VM with no actions.
    text: >
        az monitor alert create -n rule1 -g {ResourceGroup} --target {VirtualMachineID} --condition "Percentage CPU > 90 avg 5m"
  - name: Create a high CPU usage alert on a VM with email and webhook actions.
    text: |
        az monitor alert create -n rule1 -g {ResourceGroup} --target {VirtualMachineID} \\
            --condition "Percentage CPU > 90 avg 5m" \\
            --action email bob@contoso.com ann@contoso.com --email-service-owners \\
            --action webhook https://www.contoso.com/alerts?type=HighCPU \\
            --action webhook https://alerts.contoso.com apiKey={APIKey} type=HighCPU
"""

helps['monitor alert delete'] = """
type: command
short-summary: Delete an alert rule.
"""

helps['monitor alert list'] = """
type: command
short-summary: List alert rules in a resource group.
examples:
  - name: List alert rules in a resource group. (autogenerated)
    text: az monitor alert list --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor alert list-incidents'] = """
type: command
short-summary: List all incidents for an alert rule.
"""

helps['monitor alert show'] = """
type: command
short-summary: Show an alert rule.
"""

helps['monitor alert show-incident'] = """
type: command
short-summary: Get the details of an alert rule incident.
"""

helps['monitor alert update'] = """
type: command
short-summary: Update a classic metric-based alert rule.
parameters:
  - name: --description
    short-summary: Description of the rule.
  - name: --condition
    short-summary: The condition which triggers the rule.
    long-summary: >
        The form of a condition is "METRIC {>,>=,<,<=} THRESHOLD {avg,min,max,total,last} PERIOD".
        Values for METRIC and appropriate THRESHOLD values can be obtained from `az monitor metric` commands,
        and PERIOD is of the form "##h##m##s".
  - name: --add-action -a
    short-summary: Add an action to fire when the alert is triggered.
    long-summary: |
        Usage:   --add-action TYPE KEY [ARG ...]
        Email:   --add-action email bob@contoso.com ann@contoso.com
        Webhook: --add-action webhook https://www.contoso.com/alert apiKey=value
        Webhook: --add-action webhook https://www.contoso.com/alert?apiKey=value
        Multiple actions can be specified by using more than one `--add-action` argument.
  - name: --remove-action -r
    short-summary: Remove one or more actions.
    long-summary: |
        Usage:   --remove-action TYPE KEY [KEY ...]
        Email:   --remove-action email bob@contoso.com ann@contoso.com
        Webhook: --remove-action webhook https://contoso.com/alert https://alerts.contoso.com
  - name: --email-service-owners
    short-summary: Email the service owners if an alert is triggered.
  - name: --metric
    short-summary: Name of the metric to base the rule on.
    populator-commands:
      - az monitor metrics list-definitions
  - name: --operator
    short-summary: How to compare the metric against the threshold.
  - name: --threshold
    short-summary: Numeric threshold at which to trigger the alert.
  - name: --aggregation
    short-summary: Type of aggregation to apply based on --period.
  - name: --period
    short-summary: >
        Time span over which to apply --aggregation, in nDnHnMnS shorthand or full ISO8601 format.
"""

helps['monitor autoscale'] = """
type: group
short-summary: Manage autoscale settings.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
"""

helps['monitor autoscale create'] = """
type: command
short-summary: Create new autoscale settings.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --action -a
    short-summary: Add an action to fire when a scaling event occurs.
    long-summary: |
        Usage:   --action TYPE KEY [ARG ...]
        Email:   --action email bob@contoso.com ann@contoso.com
        Webhook: --action webhook https://www.contoso.com/alert apiKey=value
        Webhook: --action webhook https://www.contoso.com/alert?apiKey=value
        Multiple actions can be specified by using more than one `--action` argument.
examples:
  - name: Create autoscale settings to scale between 2 and 5 instances (3 as default). Email the administrator when scaling occurs.
    text: |
        az monitor autoscale create -g {myrg} --resource {resource-id} --min-count 2 --max-count 5 \\
          --count 3 --email-administrator

        az monitor autoscale rule create -g {myrg} --autoscale-name {resource-name} --scale out 1 \\
          --condition "Percentage CPU > 75 avg 5m"

        az monitor autoscale rule create -g {myrg} --autoscale-name {resource-name} --scale in 1 \\
          --condition "Percentage CPU < 25 avg 5m"
  - name: Create autoscale settings for exactly 4 instances.
    text: >
        az monitor autoscale create -g {myrg} --resource {resource-id} --count 4
  - name: Create new autoscale settings. (autogenerated)
    text: az monitor autoscale create --count 3 --max-count 5 --min-count 2 --name MyAutoscaleSettings --resource myScaleSet --resource-group MyResourceGroup --resource-type Microsoft.Compute/virtualMachineScaleSets
    crafted: true
"""

helps['monitor autoscale profile'] = """
type: group
short-summary: Manage autoscaling profiles.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
"""

helps['monitor autoscale profile create'] = """
type: command
short-summary: Create a fixed or recurring autoscale profile.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --timezone
    short-summary: Timezone name.
    populator-commands:
      - az monitor autoscale profile list-timezones
  - name: --recurrence -r
    short-summary: When the profile recurs. If omitted, a fixed (non-recurring) profile is created.
    long-summary: |
        Usage:     --recurrence {week} [ARG ARG ...]
        Weekly:    --recurrence week Sat Sun
  - name: --start
    short-summary: When the autoscale profile begins. Format depends on the type of profile.
    long-summary: |
        Fixed:  --start yyyy-mm-dd [hh:mm:ss]
        Weekly: [--start hh:mm]
  - name: --end
    short-summary: When the autoscale profile ends. Format depends on the type of profile.
    long-summary: |
        Fixed:  --end yyyy-mm-dd [hh:mm:ss]
        Weekly: [--end hh:mm]
examples:
  - name: Create a fixed date profile, inheriting the default scaling rules but changing the capacity.
    text: |
        az monitor autoscale create -g {myrg} --resource {resource-id} --min-count 2 --count 3 \\
          --max-count 5

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale out 1 \\
          --condition "Percentage CPU > 75 avg 5m"

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale in 1 \\
          --condition "Percentage CPU < 25 avg 5m"

        az monitor autoscale profile create -g {myrg} --autoscale-name {name} -n Christmas \\
          --copy-rules default --min-count 3 --count 6 --max-count 10 --start 2018-12-24 \\
          --end 2018-12-26 --timezone "Pacific Standard Time"
  - name: Create a recurring weekend profile, inheriting the default scaling rules but changing the capacity.
    text: |
        az monitor autoscale create -g {myrg} --resource {resource-id} --min-count 2 --count 3 \\
          --max-count 5

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale out 1 \\
          --condition "Percentage CPU > 75 avg 5m"

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale in 1 \\
          --condition "Percentage CPU < 25 avg 5m"

        az monitor autoscale profile create -g {myrg} --autoscale-name {name} -n weeekend \\
          --copy-rules default --min-count 1 --count 2 --max-count 2 \\
          --recurrence week sat sun --timezone "Pacific Standard Time"
"""

helps['monitor autoscale profile delete'] = """
type: command
short-summary: Delete an autoscale profile.
"""

helps['monitor autoscale profile list'] = """
type: command
short-summary: List autoscale profiles.
"""

helps['monitor autoscale profile list-timezones'] = """
type: command
short-summary: Look up time zone information.
"""

helps['monitor autoscale profile show'] = """
type: command
short-summary: Show details of an autoscale profile.
"""

helps['monitor autoscale rule'] = """
type: group
short-summary: Manage autoscale scaling rules.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
"""

helps['monitor autoscale rule copy'] = """
type: command
short-summary: Copy autoscale rules from one profile to another.
"""

helps['monitor autoscale rule create'] = """
type: command
short-summary: Add a new autoscale rule.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --condition
    short-summary: The condition which triggers the scaling action.
    long-summary: >
        The form of a condition is "METRIC {==,!=,>,>=,<,<=} THRESHOLD {avg,min,max,total,count} PERIOD".
        Values for METRIC and appropriate THRESHOLD values can be obtained from the `az monitor metric` command.
        Format of PERIOD is "##h##m##s".
  - name: --scale
    short-summary: The direction and amount to scale.
    long-summary: |
        Usage:          --scale {to,in,out} VAL[%]
        Fixed Count:    --scale to 5
        In by Count:    --scale in 2
        Out by Percent: --scale out 10%
  - name: --timegrain
    short-summary: >
        The way metrics are polled across instances.
    long-summary: >
        The form of the timegrain is {avg,min,max,sum} VALUE. Values can be obtained from the `az monitor metric` command.
        Format of VALUE is "##h##m##s".
examples:
  - name: Scale to 5 instances when the CPU Percentage across instances is greater than 75 averaged over 10 minutes.
    text: |
        az monitor autoscale rule create -g {myrg} --autoscale-name {myvmss} \\
          --scale to 5 --condition "Percentage CPU > 75 avg 10m"
  - name: Scale up 2 instances when the CPU Percentage across instances is greater than 75 averaged over 5 minutes.
    text: |
        az monitor autoscale rule create -g {myrg} --autoscale-name {myvmss} \\
          --scale out 2 --condition "Percentage CPU > 75 avg 5m"
  - name: Scale down 50% when the CPU Percentage across instances is less than 25 averaged over 15 minutes.
    text: |
        az monitor autoscale rule create -g {myrg} --autoscale-name {myvmss} \\
          --scale in 50% --condition "Percentage CPU < 25 avg 15m"
"""

helps['monitor autoscale rule delete'] = """
type: command
short-summary: Remove autoscale rules from a profile.
"""

helps['monitor autoscale rule list'] = """
type: command
short-summary: List autoscale rules for a profile.
"""

helps['monitor autoscale show'] = """
type: command
short-summary: Show autoscale setting details.
examples:
  - name: Show autoscale setting details. (autogenerated)
    text: az monitor autoscale show --name MyAutoscaleSettings --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor autoscale update'] = """
type: command
short-summary: Update autoscale settings.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --add-action -a
    short-summary: Add an action to fire when a scaling event occurs.
    long-summary: |
        Usage:   --add-action TYPE KEY [ARG ...]
        Email:   --add-action email bob@contoso.com ann@contoso.com
        Webhook: --add-action webhook https://www.contoso.com/alert apiKey=value
        Webhook: --add-action webhook https://www.contoso.com/alert?apiKey=value
        Multiple actions can be specified by using more than one `--add-action` argument.
  - name: --remove-action -r
    short-summary: Remove one or more actions.
    long-summary: |
        Usage:   --remove-action TYPE KEY [KEY ...]
        Email:   --remove-action email bob@contoso.com ann@contoso.com
        Webhook: --remove-action webhook https://contoso.com/alert https://alerts.contoso.com
examples:
  - name: Update autoscale settings to use a fixed 3 instances by default.
    text: |
        az monitor autoscale update -g {myrg} -n {autoscale-name} --count 3
  - name: Update autoscale settings to remove an email notification.
    text: |
        az monitor autoscale update -g {myrg} -n {autoscale-name} \\
          --remove-action email bob@contoso.com
"""

helps['monitor autoscale-settings'] = """
type: group
short-summary: Manage autoscale settings.
"""

helps['monitor autoscale-settings update'] = """
type: command
short-summary: Updates an autoscale setting.
examples:
  - name: Updates an autoscale setting. (autogenerated)
    text: az monitor autoscale-settings update --name MyAutoscaleSetting --resource-group MyResourceGroup --set retentionPolicy.days=365
    crafted: true
"""

helps['monitor diagnostic-settings'] = """
type: group
short-summary: Manage service diagnostic settings.
"""

helps['monitor diagnostic-settings categories'] = """
type: group
short-summary: Retrieve service diagnostic settings categories.
"""

helps['monitor diagnostic-settings create'] = """
type: command
short-summary: Create diagnostic settings for the specified resource.
long-summary: >
    For more information, visit: https://docs.microsoft.com/rest/api/monitor/diagnosticsettings/createorupdate#metricsettings
parameters:
  - name: --name -n
    short-summary: The name of the diagnostic settings.
  - name: --resource-group -g
    type: string
    short-summary: Name of the resource group for the Log Analytics and Storage Account when the name of the service instead of a full resource ID is given.
  - name: --logs
    type: string
    short-summary: JSON encoded list of logs settings. Use '@{file}' to load from a file.
  - name: --metrics
    type: string
    short-summary: JSON encoded list of metric settings. Use '@{file}' to load from a file.
  - name: --storage-account
    type: string
    short-summary: Name or ID of the storage account to send diagnostic logs to.
  - name: --workspace
    type: string
    short-summary: Name or ID of the Log Analytics workspace to send diagnostic logs to.
  - name: --event-hub
    type: string
    short-summary: >
        Name or ID an event hub. If none is specified, the default event hub will be selected.
  - name: --event-hub-rule
    short-summary: Name or ID of the event hub authorization rule.
examples:
  - name: Create diagnostic settings with EventHub.
    text: |
        az monitor diagnostic-settings create --resource {ID} -n {name}
           --event-hub-rule {eventHubRuleID} --storage-account {storageAccount}
           --logs '[
             {
               "category": "WorkflowRuntime",
               "enabled": true,
               "retentionPolicy": {
                 "enabled": false,
                 "days": 0
               }
             }
           ]'
           --metrics '[
             {
               "category": "WorkflowRuntime",
               "enabled": true,
               "retentionPolicy": {
                 "enabled": false,
                 "days": 0
               }
             }
           ]'
"""

helps['monitor diagnostic-settings update'] = """
type: command
short-summary: Update diagnostic settings.
"""

helps['monitor log-profiles'] = """
type: group
short-summary: Manage log profiles.
"""

helps['monitor log-profiles create'] = """
type: command
short-summary: Create a log profile.
parameters:
  - name: --name -n
    short-summary: The name of the log profile.
  - name: --locations
    short-summary: Space-separated list of regions for which Activity Log events should be stored.
  - name: --categories
    short-summary: Space-separated categories of the logs. These categories are created as is convenient to the user. Some values are Write, Delete, and/or Action.
  - name: --storage-account-id
    short-summary: The resource id of the storage account to which you would like to send the Activity Log.
  - name: --service-bus-rule-id
    short-summary: The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format '{service bus resource ID}/authorizationrules/{key name}'.
  - name: --days
    short-summary: The number of days for the retention in days. A value of 0 will retain the events indefinitely
  - name: --enabled
    short-summary: Whether the retention policy is enabled.
examples:
  - name: Create a log profile. (autogenerated)
    text: |
        az monitor log-profiles create --categories "Delete" --days 0 --enabled true --location westus2 --locations westus --name MyLogProfile --service-bus-rule-id "/subscriptions/{YOUR SUBSCRIPTION ID}/resourceGroups/{RESOURCE GROUP NAME}/providers/Microsoft.EventHub/namespaces/{EVENT HUB NAME SPACE}/authorizationrules/RootManageSharedAccessKey"
    crafted: true
"""

helps['monitor log-profiles update'] = """
type: command
short-summary: Update a log profile.
examples:
  - name: Update a log profile. (autogenerated)
    text: az monitor log-profiles update --name MyLogProfile --set retentionPolicy.days=365
    crafted: true
"""

helps['monitor metrics'] = """
type: group
short-summary: View Azure resource metrics.
"""

helps['monitor metrics alert'] = """
type: group
short-summary: Manage near-realtime metric alert rules.
"""

helps['monitor metrics alert create'] = """
type: command
short-summary: Create a metric-based alert rule.
parameters:
  - name: --action -a
    short-summary: Add an action group and optional webhook properties to fire when the alert is triggered.
    long-summary: |
        Usage:   --action ACTION_GROUP_NAME_OR_ID [KEY=VAL [KEY=VAL ...]]

        Multiple action groups can be specified by using more than one `--action` argument.
  - name: --disabled
    short-summary: Create the rule in a disabled state.
  - name: --condition
    short-summary: The condition which triggers the rule.
    long-summary: |
        Usage:  --conditon {avg,min,max,total,count} [NAMESPACE.]METRIC {=,!=,>,>=,<,<=} THRESHOLD
                           [where DIMENSION {includes,excludes} VALUE [or VALUE ...]
                           [and   DIMENSION {includes,excludes} VALUE [or VALUE ...] ...]]

        Dimensions can be queried by adding the 'where' keyword and multiple dimensions can be queried by combining them with the 'and' keyword.

        Values for METRIC, DIMENSION and appropriate THRESHOLD values can be obtained from `az monitor metrics list-definition` command.

        Multiple conditons can be specified by using more than one `--condition` argument.
examples:
  - name: Create a high CPU usage alert on a VM with no actions.
    text: >
        az monitor metrics alert create -n alert1 -g {ResourceGroup} --scopes {VirtualMachineID} --condition "avg Percentage CPU > 90" --description "High CPU"
  - name: Create a high CPU usage alert on a VM with email and webhook actions.
    text: |
        az monitor metrics alert create -n alert1 -g {ResourceGroup} --scopes {VirtualMachineID} \\
            --condition "avg Percentage CPU > 90" --window-size 5m --evaluation-frequency 1m \\
            --action {actionGroupId} apiKey={APIKey} type=HighCPU --description "High CPU"
  - name: Create an alert when a storage account shows a high number of slow transactions, using multi-dimensional filters.
    text: |
        az monitor metrics alert create -g {ResourceGroup} -n alert1 --scopes {StorageAccountId} \\
            --description "Storage Slow Transactions" \\
            --condition "total transactions > 5 where ResponseType includes Success" \\
            --condition "avg SuccessE2ELatency > 250 where ApiName includes GetBlob or PutBlob"
"""

helps['monitor metrics alert delete'] = """
type: command
short-summary: Delete a metrics-based alert rule.
examples:
  - name: Delete a metrics-based alert rule. (autogenerated)
    text: az monitor metrics alert delete --name MyAlertRule --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor metrics alert list'] = """
type: command
short-summary: List metric-based alert rules.
examples:
  - name: List metric-based alert rules. (autogenerated)
    text: az monitor metrics alert list --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor metrics alert show'] = """
type: command
short-summary: Show a metrics-based alert rule.
examples:
  - name: Show a metrics-based alert rule. (autogenerated)
    text: az monitor metrics alert show --name MyAlertRule --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor metrics alert update'] = """
type: command
short-summary: Update a metric-based alert rule.
parameters:
  - name: --add-condition
    short-summary: Add a condition which triggers the rule.
    long-summary: |
        Usage:  --add-conditon {avg,min,max,total,count} [NAMESPACE.]METRIC {=,!=,>,>=,<,<=} THRESHOLD
                               [where DIMENSION {includes,excludes} VALUE [or VALUE ...]
                               [and   DIMENSION {includes,excludes} VALUE [or VALUE ...] ...]]

        Dimensions can be queried by adding the 'where' keyword and multiple dimensions can be queried by combining them with the 'and' keyword.

        Values for METRIC, DIMENSION and appropriate THRESHOLD values can be obtained from `az monitor metrics list-definition` command.

        Multiple conditons can be specified by using more than one `--condition` argument.
  - name: --remove-conditions
    short-summary: Space-separated list of condition names to remove.
  - name: --add-action
    short-summary: Add an action group and optional webhook properties to fire when the alert is triggered.
    long-summary: |
        Usage:   --add-action ACTION_GROUP_NAME_OR_ID [KEY=VAL [KEY=VAL ...]]

        Multiple action groups can be specified by using more than one `--action` argument.
  - name: --remove-actions
    short-summary: Space-separated list of action group names to remove.
examples:
  - name: Update a metric-based alert rule. (autogenerated)
    text: az monitor metrics alert update --enabled true --name MyAlertRule --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor metrics list'] = """
type: command
short-summary: List the metric values for a resource.
parameters:
  - name: --aggregation
    short-summary: The list of aggregation types (space-separated) to retrieve.
    populator-commands:
      - az monitor metrics list-definitions
  - name: --interval
    short-summary: >
        The interval over which to aggregate metrics, in ##h##m format.
  - name: --filter
    short-summary: A string used to reduce the set of metric data returned. eg. "BlobType eq '*'"
    long-summary: 'For a full list of filters, see the filter string reference at https://docs.microsoft.com/rest/api/monitor/metrics/list'
  - name: --metadata
    short-summary: Returns the metadata values instead of metric data
  - name: --dimension
    short-summary: The list of dimensions (space-separated) the metrics are queried into.
    populator-commands:
      - az monitor metrics list-definitions
  - name: --namespace
    short-summary: Namespace to query metric definitions for.
    populator-commands:
      - az monitor metrics list-definitions
  - name: --offset
    short-summary: >
        Time offset of the query range, in ##d##h format.
    long-summary: >
        Can be used with either --start-time or --end-time. If used with --start-time, then
        the end time will be calculated by adding the offset. If used with --end-time (default), then
        the start time will be calculated by subtracting the offset. If --start-time and --end-time are
        provided, then --offset will be ignored.
  - name: --metrics
    short-summary: >
        Space-separated list of metric names to retrieve.
    populator-commands:
      - az monitor metrics list-definitions

examples:
  - name: List a VM's CPU usage for the past hour
    text: >
        az monitor metrics list --resource {ResourceName} --metric "Percentage CPU"
  - name: List success E2E latency of a storage account and split the data series based on API name
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --dimension ApiName
  - name: List success E2E latency of a storage account and split the data series based on both API name and geo type
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --dimension ApiName GeoType
  - name: List success E2E latency of a storage account and split the data series based on both API name and geo type using "--filter" parameter
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --filter "ApiName eq '*' and GeoType eq '*'"
  - name: List success E2E latency of a storage account and split the data series based on both API name and geo type. Limits the api name to 'DeleteContainer'
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --filter "ApiName eq 'DeleteContainer' and GeoType eq '*'"
  - name: List transactions of a storage account per day since 2017-01-01
    text: >
        az monitor metrics list --resource {ResourceName} --metric Transactions \\
                                --start-time 2017-01-01T00:00:00Z \\
                                --interval PT24H
  - name: List the metadata values for a storage account under transaction metric's api name dimension since 2017
    text: >
        az monitor metrics list --resource {ResourceName} --metric Transactions \\
                                --filter "ApiName eq '*'" \\
                                --start-time 2017-01-01T00:00:00Z
"""

helps['monitor metrics list-definitions'] = """
type: command
short-summary: Lists the metric definitions for the resource.
examples:
  - name: Lists the metric definitions for the resource. (autogenerated)
    text: az monitor metrics list-definitions --resource /subscriptions/{subscriptionID}/resourceGroups/Space1999/providers/Microsoft.Network/networkSecurityGroups/ADDS-NSG
    crafted: true
"""

helps['mysql'] = """
type: group
short-summary: Manage Azure Database for MySQL servers.
"""

helps['mysql db'] = """
type: group
short-summary: Manage MySQL databases on a server.
"""

helps['mysql db create'] = """
type: command
short-summary: Create a MySQL database.
examples:
  - name: Create database 'testdb' in the server 'testsvr' with the default parameters.
    text: az mysql db create -g testgroup -s testsvr -n testdb
  - name: Create database 'testdb' in server 'testsvr' with a given character set and collation rules.
    text: az mysql db create -g testgroup -s testsvr -n testdb --charset {valid_charset} --collation {valid_collation}
"""

helps['mysql db delete'] = """
type: command
short-summary: Delete a database.
examples:
  - name: Delete database 'testdb' in the server 'testsvr'.
    text: az mysql db delete -g testgroup -s testsvr -n testdb
"""

helps['mysql db list'] = """
type: command
short-summary: List the databases for a server.
examples:
  - name: List databases in the server 'testsvr'.
    text: az mysql db list -g testgroup -s testsvr
"""

helps['mysql db show'] = """
type: command
short-summary: Show the details of a database.
examples:
  - name: Show database 'testdb' in the server 'testsvr'.
    text: az mysql db show -g testgroup -s testsvr -n testdb
"""

helps['mysql server'] = """
type: group
short-summary: Manage MySQL servers.
"""

helps['mysql server configuration'] = """
type: group
short-summary: Manage configuration values for a server.
"""

helps['mysql server configuration list'] = """
type: command
short-summary: List the configuration values for a server.
examples:
  - name: List the configuration values for a server. (autogenerated)
    text: az mysql server configuration list --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['mysql server configuration set'] = """
type: command
short-summary: Update the configuration of a server.
examples:
  - name: Set a new configuration value.
    text: az mysql server configuration set -g testgroup -s testsvr -n {config_name} --value {config_value}
  - name: Set a configuration value to its default.
    text: az mysql server configuration set -g testgroup -s testsvr -n {config_name}
"""

helps['mysql server configuration show'] = """
type: command
short-summary: Get the configuration for a server."
examples:
  - name: Get the configuration for a server." (autogenerated)
    text: az mysql server configuration show --name MyServerConfiguration --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['mysql server create'] = """
type: command
short-summary: Create a server.
examples:
  - name: Create a MySQL server in North Europe with sku GP_Gen5_2 (General Purpose, Gen 5 hardware, 2 vCores).
    text: az mysql server create -l northeurope -g testgroup -n testsvr -u username -p password \\ --sku-name GP_Gen5_2
  - name: Create a MySQL server with all paramaters set.
    text: az mysql server create -l northeurope -g testgroup -n testsvr -u username -p password \\ --sku-name B_Gen5_1 --ssl-enforcement Disabled \\ --backup-retention 10 --geo-redundant-backup Enabled --storage-size 51200 --tags "key=value" --version {server-version}
"""

helps['mysql server delete'] = """
type: command
short-summary: Delete a server.
examples:
  - name: Delete a server.
    text: az mysql server delete -g testgroup -n testsvr
"""

helps['mysql server firewall-rule'] = """
type: group
short-summary: Manage firewall rules for a server.
"""

helps['mysql server firewall-rule create'] = """
type: command
short-summary: Create a new firewall rule for a server.
examples:
  - name: Create a firewall rule allowing connections from a specific IP address.
    text: az mysql server firewall-rule create -g testgroup -s testsvr -n allowip --start-ip-address 107.46.14.221 --end-ip-address 107.46.14.221
  - name: Create a firewall rule allowing connections from an IP address range.
    text: az mysql server firewall-rule create -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.0 --end-ip-address 107.46.14.221
"""

helps['mysql server firewall-rule delete'] = """
type: command
short-summary: Delete a firewall rule.
examples:
  - name: Delete a firewall rule. (autogenerated)
    text: az mysql server firewall-rule delete --name MyFirewallRule --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['mysql server firewall-rule list'] = """
type: command
short-summary: List all firewall rules for a server.
examples:
  - name: List all firewall rules for a server. (autogenerated)
    text: az mysql server firewall-rule list --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['mysql server firewall-rule show'] = """
type: command
short-summary: Get the details of a firewall rule.
"""

helps['mysql server firewall-rule update'] = """
type: command
short-summary: Update a firewall rule.
examples:
  - name: Update a firewall rule's start IP address.
    text: az mysql server firewall-rule update -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.1
  - name: Update a firewall rule's start and end IP address.
    text: az mysql server firewall-rule update -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.2 --end-ip-address 107.46.14.218
"""

helps['mysql server georestore'] = """
type: command
short-summary: Geo-restore a server from backup.
examples:
  - name: Geo-restore 'testsvr' into a new server 'testsvrnew' located in West US 2.
    text: az mysql server georestore -g testgroup -n testsvrnew --source-server testsvr -l westus2
  - name: Geo-restore 'testsvr' into a new server 'testsvrnew' located in West US 2 with sku GP_Gen5_2.
    text: az mysql server georestore -g testgroup -n testsvrnew --source-server testsvr -l westus2 --sku-name GP_Gen5_2
  - name: Geo-restore 'testsvr2' into a new server 'testsvrnew', where 'testsvrnew' is in a different resource group from 'testsvr2'.
    text: |
        az mysql server georestore -g testgroup -n testsvrnew \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforMySQL/servers/testsvr2" \\
            -l westus2
"""

helps['mysql server list'] = """
type: command
short-summary: List available servers.
examples:
  - name: List all MySQL servers in a subscription.
    text: az mysql server list
  - name: List all MySQL servers in a resource group.
    text: az mysql server list -g testgroup
"""

helps['mysql server replica'] = """
type: group
short-summary: Manage read replicas.
"""

helps['mysql server replica create'] = """
type: command
short-summary: Create a read replica for a server.
examples:
  - name: Create a read replica 'testreplsvr' for 'testsvr'.
    text: az mysql server replica create -n testreplsvr -g testgroup -s testsvr
  - name: Create a read replica 'testreplsvr' for 'testsvr2', where 'testreplsvr' is in a different resource group.
    text: |
        az mysql server replica create -n testreplsvr -g testgroup \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforMySQL/servers/testsvr2"
"""

helps['mysql server replica list'] = """
type: command
short-summary: List all read replicas for a given server.
examples:
  - name: List all read replicas for master server 'testsvr'.
    text: az mysql server replica list -g testgroup -s testsvr
"""

helps['mysql server replica stop'] = """
type: command
short-summary: Stop replication to a read replica and make it a read/write server.
examples:
  - name: Stop replication to 'testreplsvr' and make it a read/write server.
    text: az mysql server replica stop -g testgroup -n testreplsvr
"""

helps['mysql server restart'] = """
type: command
short-summary: Restart a server.
examples:
  - name: Restart a server.
    text: az mysql server restart -g testgroup -n testsvr
"""

helps['mysql server restore'] = """
type: command
short-summary: Restore a server from backup.
examples:
  - name: Restore 'testsvr' to a specific point-in-time as a new server 'testsvrnew'.
    text: az mysql server restore -g testgroup -n testsvrnew --source-server testsvr --restore-point-in-time "2017-06-15T13:10:00Z"
  - name: Restore 'testsvr2' to 'testsvrnew', where 'testsvrnew' is in a different resource group from 'testsvr2'.
    text: |
        az mysql server restore -g testgroup -n testsvrnew \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforMySQL/servers/testsvr2" \\
            --restore-point-in-time "2017-06-15T13:10:00Z"
"""

helps['mysql server show'] = """
type: command
short-summary: Get the details of a server.
examples:
  - name: Get the details of a server
    text: az mysql server show --name MyServer --resource-group MyResourceGroup
    crafted: true
"""

helps['mysql server update'] = """
type: command
short-summary: Update a server.
examples:
  - name: Update a server's sku.
    text: az mysql server update -g testgroup -n testsvrnew --sku-name GP_Gen5_4
  - name: Update a server's tags.
    text: az mysql server update -g testgroup -n testsvrnew --tags "k1=v1" "k2=v2"
"""

helps['mysql server vnet-rule'] = """
type: group
short-summary: Manage a server's virtual network rules.
"""

helps['mysql server vnet-rule create'] = """
type: command
short-summary: Create a virtual network rule to allows access to a MySQL server.
examples:
  - name: Create a virtual network rule by providing the subnet id.
    text: az mysql server vnet-rule create -g testgroup -s testsvr -n vnetRuleName --subnet /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/vnetName/subnets/subnetName
  - name: Create a vnet rule by providing the vnet and subnet name. The subnet id is created by taking the resource group name and subscription id of the server.
    text: az mysql server vnet-rule create -g testgroup -s testsvr -n vnetRuleName --subnet subnetName --vnet-name vnetName
"""

helps['mysql server vnet-rule update'] = """
type: command
short-summary: Update a virtual network rule.
"""

helps['mysql server wait'] = """
type: command
short-summary: Wait for server to satisfy certain conditions.
"""

helps['mysql server-logs'] = """
type: group
short-summary: Manage server logs.
"""

helps['mysql server-logs download'] = """
type: command
short-summary: Download log files.
examples:
  - name: Download log files f1 and f2 to the current directory from the server 'testsvr'.
    text: az mysql server-logs download -g testgroup -s testsvr -n f1.log f2.log
"""

helps['mysql server-logs list'] = """
type: command
short-summary: List log files for a server.
examples:
  - name: List log files for 'testsvr' modified in the last 72 hours (default value).
    text: az mysql server-logs list -g testgroup -s testsvr
  - name: List log files for 'testsvr' modified in the last 10 hours.
    text: az mysql server-logs list -g testgroup -s testsvr --file-last-written 10
  - name: List log files for 'testsvr' less than 30Kb in size.
    text: az mysql server-logs list -g testgroup -s testsvr --max-file-size 30
"""

helps['netappfiles'] = """
type: group
short-summary: Manage Azure NetApp Files (ANF) Resources.
"""

helps['netappfiles account'] = """
type: group
short-summary: Manage Azure NetApp Files (ANF) Account Resources.
"""

helps['netappfiles account ad'] = """
type: group
short-summary: Manage Azure NetApp Files (ANF) Account active directories.
"""

helps['netappfiles account ad add'] = """
type: command
short-summary: Add an active directory to the account.
parameters:
  - name: --account-name --name -a -n
    short-summary: The name of the ANF account
  - name: --username
    short-summary: Username of Active Directory domain administrator
  - name: --password
    short-summary: Plain text password of Active Directory domain administrator
  - name: --domain
    short-summary: Name of the Active Directory domain
  - name: --dns
    short-summary: Comma separated list of DNS server IP addresses for the Active Directory domain
  - name: --smb-server-name
    short-summary: NetBIOS name of the SMB server. This name will be registered as a computer account in the AD and used to mount volumes. Must be 10 characters or less
  - name: --organizational-unit
    short-summary: The Organizational Unit (OU) within the Windows Active Directory
examples:
  - name: Add an active directory to the account
    text: >
        az netappfiles account ad add -g mygroup --name myname --username aduser --password aduser --smb-server-name SMBSERVER --dns 1.2.3.4 --domain westcentralus
"""

helps['netappfiles account ad list'] = """
type: command
short-summary: List the active directories of an account.
parameters:
  - name: --account-name --name -a -n
    short-summary: The name of the ANF account
examples:
  - name: Add an active directory to the account
    text: >
        az netappfiles account ad list -g mygroup --name myname
"""

helps['netappfiles account ad remove'] = """
type: command
short-summary: Remove an active directory from the account.
parameters:
  - name: --account-name --name -a -n
    short-summary: The name of the ANF account
  - name: --active-directory
    short-summary: The id of the active directory
examples:
  - name: Remove an active directory from the account
    text: >
        az netappfiles account ad remove -g mygroup --name myname --active-directory 13641da9-c0e9-4b97-84fc-4f8014a93848
"""

helps['netappfiles account create'] = """
type: command
short-summary: Create a new Azure NetApp Files (ANF) account. Note that active directories are added using the subgroup commands.
parameters:
  - name: --account-name --name -a -n
    short-summary: The name of the ANF account
  - name: --tags
    short-summary: Space-separated tags in `key[=value]` format
examples:
  - name: Create an ANF account
    text: >
        az netappfiles account create -g mygroup --name myname -l location --tags testtag1=mytag1 testtag3=mytagg
"""

helps['netappfiles account delete'] = """
type: command
short-summary: Delete the specified ANF account.
parameters:
  - name: --account-name --name -a -n
    short-summary: The name of the ANF account
examples:
  - name: Delete an ANF account
    text: >
        az netappfiles account delete -g mygroup --name myname
"""

helps['netappfiles account list'] = """
type: command
short-summary: List ANF accounts.
examples:
  - name: List ANF accounts within a resource group
    text: >
        az netappfiles account list -g mygroup
"""

helps['netappfiles account show'] = """
type: command
short-summary: Get the specified ANF account.
parameters:
  - name: --account-name --name -a -n
    short-summary: The name of the ANF account
examples:
  - name: Get an ANF account
    text: >
        az netappfiles account show -g mygroup --name myname
"""

helps['netappfiles account update'] = """
type: command
short-summary: Set/modify the tags for a specified ANF account.
parameters:
  - name: --account-name --name -a -n
    short-summary: The name of the ANF account
  - name: --tags
    short-summary: Space-separated tags in `key[=value]` format
examples:
  - name: Update the tags of an ANF account
    text: >
        az netappfiles account update -g mygroup --name myname --tags testtag2=mytagb
"""

helps['netappfiles list-mount-targets'] = """
type: command
short-summary: List the mount targets of an Azure NetApp Files (ANF) volume.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --volume-name -v
    short-summary: The name of the ANF pool
examples:
  - name: list the mount targets of an ANF volume
    text: >
        az netappfiles list-mount-targets -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname
"""

helps['netappfiles pool'] = """
type: group
short-summary: Manage Azure NetApp Files (ANF) Pool Resources.
"""

helps['netappfiles pool create'] = """
type: command
short-summary: Create a new Azure NetApp Files (ANF) pool.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --name --pool-name -n -p
    short-summary: The name of the ANF pool
  - name: --size
    short-summary: The size for the ANF pool. Must be an integer number of tebibytes in multiples of 4
  - name: --service-level
    short-summary: The service level for the ANF pool
  - name: --tags
    short-summary: Space-separated tags in `key[=value]` format
examples:
  - name: Create an ANF pool
    text: >
        az netappfiles pool create -g mygroup --account-name myaccountname --name mypoolname -l westus2 --size 8 --service-level premium
"""

helps['netappfiles pool delete'] = """
type: command
short-summary: Delete the specified ANF pool.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --name --pool-name -n -p
    short-summary: The name of the ANF pool
examples:
  - name: Delete an ANF pool
    text: >
        az netappfiles pool delete -g mygroup --account-name myaccname --name mypoolname
"""

helps['netappfiles pool list'] = """
type: command
short-summary: L:ist the ANF pools for the specified account.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
examples:
  - name: List the pools for the ANF account
    text: >
        az netappfiles pool list -g mygroup --account-name myname
"""

helps['netappfiles pool show'] = """
type: command
short-summary: Get the specified ANF pool.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --name --pool-name -n -p
    short-summary: The name of the ANF pool
examples:
  - name: Get an ANF pool
    text: >
        az netappfiles pool show -g mygroup --account-name myaccname --name mypoolname
"""

helps['netappfiles pool update'] = """
type: command
short-summary: Update the tags of the specified ANF pool.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --name --pool-name -n -p
    short-summary: The name of the ANF pool
  - name: --size
    short-summary: The size for the ANF pool. Must be an integer number of tebibytes in multiples of 4
  - name: --service-level
    short-summary: The service level for the ANF pool
  - name: --tags
    short-summary: Space-separated tags in `key[=value]` format
examples:
  - name: Update specific values for an ANF pool
    text: >
        az netappfiles pool update -g mygroup --account-name myaccname --name mypoolname --service-level ultra --tags mytag1=abcd mytag2=efgh
"""

helps['netappfiles snapshot'] = """
type: group
short-summary: Manage Azure NetApp Files (ANF) Snapshot Resources.
"""

helps['netappfiles snapshot create'] = """
type: command
short-summary: Create a new Azure NetApp Files (ANF) snapshot.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --volume-name -v
    short-summary: The name of the ANF volume
  - name: --name --snapshot-name -n -s
    short-summary: The name of the ANF snapshot
  - name: --file-system-id
    short-summary: The uuid of the volume
examples:
  - name: Create an ANF snapshot
    text: >
        az netappfiles snapshot create -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname --name mysnapname -l eastus --file-system-id 13641da9-c0e9-4b97-84fc-4f8014a93848
"""

helps['netappfiles snapshot delete'] = """
type: command
short-summary: Delete the specified ANF snapshot.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --volume-name -v
    short-summary: The name of the ANF volume
  - name: --name --snapshot-name -n -s
    short-summary: The name of the ANF snapshot
examples:
  - name: Delete an ANF snapshot
    text: >
        az netappfiles snapshot delete -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname --name mysnapname
"""

helps['netappfiles snapshot list'] = """
type: command
short-summary: List the snapshots of an ANF volume.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --volume-name -v
    short-summary: The name of the ANF volume
examples:
  - name: list the snapshots of an ANF volume
    text: >
        az netappfiles snapshot list -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname
"""

helps['netappfiles snapshot show'] = """
type: command
short-summary: Get the specified ANF snapshot.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --volume-name -v
    short-summary: The name of the ANF volume
  - name: --name --snapshot-name -n -s
    short-summary: The name of the ANF snapshot
examples:
  - name: Return the specified ANF snapshot
    text: >
        az netappfiles snapshot show -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname --name mysnapname
"""

helps['netappfiles volume'] = """
type: group
short-summary: Manage Azure NetApp Files (ANF) Volume Resources.
"""

helps['netappfiles volume create'] = """
type: command
short-summary: Create a new Azure NetApp Files (ANF) volume. Export policies are applied with the subgroup commands but note that volumes are always created with a default export policy
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --name --volume-name -n -v
    short-summary: The name of the ANF volume
  - name: --service-level
    short-summary: The service level
  - name: --usage-threshold
    short-summary: The maximum storage quota allowed for a file system as integer number of GiB. Min 100 GiB, max 100TiB"
  - name: --creation-token
    short-summary: A 1-80 character long alphanumeric string value that identifies a unique file share or mount point in the target subnet
  - name: --vnet
    short-summary: The ARM Id or name of the vnet for the volume
  - name: --subnet
    short-summary: The ARM Id or name of the subnet for the vnet. If omitted 'default' will be used
  - name: --protocol-types
    short-summary: Space seperated list of protocols that the volume can use
  - name: --tags
    short-summary: Space-separated tags in `key[=value]` format
examples:
  - name: Create an ANF volume
    text: >
        az netappfiles volume create -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname -l westus2 --service-level premium --usage-threshold 100 --creation-token "unique-file-path" --vnet myvnet --subnet mysubnet --protocol-types NFSv3 NFSv4
"""

helps['netappfiles volume delete'] = """
type: command
short-summary: Delete the specified ANF volume.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --name --volume-name -n -v
    short-summary: The name of the ANF volume
examples:
  - name: Delete an ANF volume
    text: >
        az netappfiles volume delete -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname
"""

helps['netappfiles volume export-policy'] = """
type: group
short-summary: Manage Azure NetApp Files (ANF) Volume export policies.
"""

helps['netappfiles volume export-policy add'] = """
type: command
short-summary: Add a new rule to the export policy for a volume.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --name --volume-name -n -v
    short-summary: The name of the ANF volume
  - name: --rule-index
    short-summary: Order index. No number can be repeated. Max 6 rules.
  - name: --unix-read-only
    short-summary: Indication of read only access
  - name: --unix-read-write
    short-summary: Indication of read and write access
  - name: --cifs
    short-summary: Indication that CIFS protocol is allowed
  - name: --nfsv3
    short-summary: Indication that NFSv3 protocol is allowed
  - name: --nfsv4
    short-summary: Indication that NFSv4 protocol is allowed
  - name: --allowed-clients
    short-summary: Client ingress specification as comma separated string with IPv4 CIDRs, IPv4 host addresses and host names)
examples:
  - name: Add an export policy rule for the ANF volume
    text: >
        az netappfiles volume export-policy add -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname --allowed-clients "1.2.3.0/24" --rule-index 2 --unix-read-only true --unix-read-write false --cifs false --nfsv3 true --nfsv4 false
"""

helps['netappfiles volume export-policy list'] = """
type: command
short-summary: List the export policy rules for a volume.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --name --volume-name -n -v
    short-summary: The name of the ANF volume
examples:
  - name: List the export policy rules for an ANF volume
    text: >
        az netappfiles volume export-policy list -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname
"""

helps['netappfiles volume export-policy remove'] = """
type: command
short-summary: Remove a rule from the export policy for a volume by rule index. The current rules can be obtained by performing the subgroup list command.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --name --volume-name -n -v
    short-summary: The name of the ANF volume
  - name: --rule-index
    short-summary: Order index. Range 1 to 6.
examples:
  - name: Remove an export policy rule for an ANF volume
    text: >
        az netappfiles volume export-policy remove -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname --rule-index 4
"""

helps['netappfiles volume list'] = """
type: command
short-summary: List the ANF Pools for the specified account.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
examples:
  - name: List the ANF volumes of the pool
    text: >
        az netappfiles volume list -g mygroup --account-name myaccname --pool-name mypoolname
"""

helps['netappfiles volume show'] = """
type: command
short-summary: Get the specified ANF volume.
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --name --volume-name -n -v
    short-summary: The name of the ANF pool
examples:
  - name: Returns the properties of the given ANF volume
    text: >
        az netappfiles volume show -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname
"""

helps['netappfiles volume update'] = """
type: command
short-summary: Update the specified ANF volume with the values provided. Unspecified values will remain unchanged. Export policies are amended/created with the subgroup commands
parameters:
  - name: --account-name -a
    short-summary: The name of the ANF account
  - name: --pool-name -p
    short-summary: The name of the ANF pool
  - name: --name --volume-name -n -v
    short-summary: The name of the ANF volume
  - name: --service-level
    short-summary: The service level
  - name: --usage-threshold
    short-summary: The maximum storage quota allowed for a file system as integer number of GiB. Min 100 GiB, max 100TiB"
  - name: --tags
    short-summary: Space-separated tags in `key[=value]` format
examples:
  - name: Update an ANF volume
    text: >
        az netappfiles volume update -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname --service-level ultra --usage-threshold 100 --tags mytag=specialvol
"""

helps['network'] = """
type: group
short-summary: Manage Azure Network resources.
"""

helps['network application-gateway'] = """
type: group
short-summary: Manage application-level routing and load balancing services.
long-summary: To learn more about Application Gateway, visit https://docs.microsoft.com/azure/application-gateway/application-gateway-create-gateway-cli
"""

helps['network application-gateway address-pool'] = """
type: group
short-summary: Manage address pools of an application gateway.
"""

helps['network application-gateway address-pool create'] = """
type: command
short-summary: Create an address pool.
examples:
  - name: Create an address pool with two endpoints.
    text: |
        az network application-gateway address-pool create -g MyResourceGroup \\
            --gateway-name MyAppGateway -n MyAddressPool --servers 10.0.0.4 10.0.0.5
"""

helps['network application-gateway address-pool delete'] = """
type: command
short-summary: Delete an address pool.
examples:
  - name: Delete an address pool.
    text: az network application-gateway address-pool delete -g MyResourceGroup --gateway-name MyAppGateway -n MyAddressPool
"""

helps['network application-gateway address-pool list'] = """
type: command
short-summary: List address pools.
examples:
  - name: List address pools.
    text: az network application-gateway address-pool list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway address-pool show'] = """
type: command
short-summary: Get the details of an address pool.
examples:
  - name: Get the details of an address pool.
    text: az network application-gateway address-pool show -g MyResourceGroup --gateway-name MyAppGateway -n MyAddressPool
"""

helps['network application-gateway address-pool update'] = """
type: command
short-summary: Update an address pool.
examples:
  - name: Update an address pool, add server.
    text: az network application-gateway address-pool update -g MyResourceGroup --gateway-name MyAppGateway \\ -n MyAddressPool --servers 10.0.0.4 10.0.0.5 10.0.0.6
"""

helps['network application-gateway auth-cert'] = """
type: group
short-summary: Manage authorization certificates of an application gateway.
"""

helps['network application-gateway auth-cert create'] = """
type: command
short-summary: Create an authorization certificate.
examples:
  - name: Create an authorization certificate.
    text: |
        az network application-gateway auth-cert create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyAuthCert --cert-file /path/to/cert/file
"""

helps['network application-gateway auth-cert delete'] = """
type: command
short-summary: Delete an authorization certificate.
examples:
  - name: Delete an authorization certificate.
    text: az network application-gateway auth-cert delete -g MyResourceGroup --gateway-name MyAppGateway -n MyAuthCert
"""

helps['network application-gateway auth-cert list'] = """
type: command
short-summary: List authorization certificates.
examples:
  - name: List authorization certificates.
    text: az network application-gateway auth-cert list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway auth-cert show'] = """
type: command
short-summary: Show an authorization certificate.
examples:
  - name: Show an authorization certificate.
    text: az network application-gateway auth-cert show -g MyResourceGroup --gateway-name MyAppGateway -n MyAuthCert
"""

helps['network application-gateway auth-cert update'] = """
type: command
short-summary: Update an authorization certificate.
examples:
  - name: Update authorization certificates to use a new cert file.
    text: az network application-gateway auth-cert update -g MyResourceGroup --gateway-name MyAppGateway \\ -n MyAuthCert --cert-file /path/to/new/cert/file
"""

helps['network application-gateway create'] = """
type: command
short-summary: Create an application gateway.
examples:
  - name: Create an application gateway with VMs as backend servers.
    text: |
        az network application-gateway create -g MyResourceGroup -n MyAppGateway --capacity 2 --sku Standard_Medium \\
            --vnet-name MyVNet --subnet MySubnet --http-settings-cookie-based-affinity Enabled \\
            --public-ip-address MyAppGatewayPublicIp --servers 10.0.0.4 10.0.0.5
  - name: Create an application gateway. (autogenerated)
    text: az network application-gateway create --capacity 2 --frontend-port MyFrontendPort --http-settings-cookie-based-affinity Enabled --http-settings-port 80 --http-settings-protocol Http --location westus2 --name MyAppGateway --public-ip-address MyAppGatewayPublicIp --resource-group MyResourceGroup --sku Standard_Small --subnet MySubnet --vnet-name MyVNet
    crafted: true
"""

helps['network application-gateway delete'] = """
type: command
short-summary: Delete an application gateway.
examples:
  - name: Delete an application gateway.
    text: az network application-gateway delete -g MyResourceGroup -n MyAppGateway
"""

helps['network application-gateway frontend-ip'] = """
type: group
short-summary: Manage frontend IP addresses of an application gateway.
"""

helps['network application-gateway frontend-ip create'] = """
type: command
short-summary: Create a frontend IP address.
examples:
  - name: Create a frontend IP address.
    text: |
        az network application-gateway frontend-ip create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyFrontendIp --public-ip-address MyPublicIpAddress
"""

helps['network application-gateway frontend-ip delete'] = """
type: command
short-summary: Delete a frontend IP address.
examples:
  - name: Delete a frontend IP address.
    text: az network application-gateway frontend-ip delete -g MyResourceGroup --gateway-name MyAppGateway -n MyFrontendIp
"""

helps['network application-gateway frontend-ip list'] = """
type: command
short-summary: List frontend IP addresses.
examples:
  - name: List frontend IP addresses.
    text: az network application-gateway frontend-ip list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway frontend-ip show'] = """
type: command
short-summary: Get the details of a frontend IP address.
examples:
  - name: Get the details of a frontend IP address.
    text: az network application-gateway frontend-ip show -g MyResourceGroup --gateway-name MyAppGateway -n MyFrontendIp
"""

helps['network application-gateway frontend-ip update'] = """
type: command
short-summary: Update a frontend IP address.
examples:
  - name: Update a frontend IP address to use a new IP address.
    text: az network application-gateway frontend-ip update -g MyResourceGroup --gateway-name MyAppGateway \\ -n MyFrontendIp --public-ip-address MyNewPublicIpAddress
"""

helps['network application-gateway frontend-port'] = """
type: group
short-summary: Manage frontend ports of an application gateway.
"""

helps['network application-gateway frontend-port create'] = """
type: command
short-summary: Create a frontend port.
examples:
  - name: Create a frontend port.
    text: |
        az network application-gateway frontend-port create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyFrontendPort --port 8080
"""

helps['network application-gateway frontend-port delete'] = """
type: command
short-summary: Delete a frontend port.
examples:
  - name: Delete a frontend port.
    text: az network application-gateway frontend-port delete -g MyResourceGroup --gateway-name MyAppGateway -n MyFrontendPort
"""

helps['network application-gateway frontend-port list'] = """
type: command
short-summary: List frontend ports.
examples:
  - name: List frontend ports.
    text: az network application-gateway frontend-port list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway frontend-port show'] = """
type: command
short-summary: Get the details of a frontend port.
examples:
  - name: Get the details of a frontend port.
    text: az network application-gateway frontend-port show -g MyResourceGroup --gateway-name MyAppGateway -n MyFrontendPort
"""

helps['network application-gateway frontend-port update'] = """
type: command
short-summary: Update a frontend port.
examples:
  - name: Update a frontend port to use a different port.
    text: |
        az network application-gateway frontend-port update -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyFrontendPort --port 8081
"""

helps['network application-gateway http-listener'] = """
type: group
short-summary: Manage HTTP listeners of an application gateway.
"""

helps['network application-gateway http-listener create'] = """
type: command
short-summary: Create an HTTP listener.
examples:
  - name: Create an HTTP listener.
    text: |
        az network application-gateway http-listener create -g MyResourceGroup --gateway-name MyAppGateway \\
            --frontend-port MyFrontendPort -n MyHttpListener --frontend-ip MyAppGatewayPublicIp
"""

helps['network application-gateway http-listener delete'] = """
type: command
short-summary: Delete an HTTP listener.
examples:
  - name: Delete an HTTP listener.
    text: az network application-gateway http-listener delete -g MyResourceGroup --gateway-name MyAppGateway -n MyHttpListener
"""

helps['network application-gateway http-listener list'] = """
type: command
short-summary: List HTTP listeners.
examples:
  - name: List HTTP listeners.
    text: az network application-gateway http-listener list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway http-listener show'] = """
type: command
short-summary: Get the details of an HTTP listener.
examples:
  - name: Get the details of an HTTP listener.
    text: az network application-gateway http-listener show -g MyResourceGroup --gateway-name MyAppGateway -n MyHttpListener
"""

helps['network application-gateway http-listener update'] = """
type: command
short-summary: Update an HTTP listener.
examples:
  - name: Update an HTTP listener to use a different hostname.
    text: |
        az network application-gateway http-listener update -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyHttpListener --host-name www.mynewhost.com
"""

helps['network application-gateway http-settings'] = """
type: group
short-summary: Manage HTTP settings of an application gateway.
"""

helps['network application-gateway http-settings create'] = """
type: command
short-summary: Create HTTP settings.
examples:
  - name: Create HTTP settings.
    text: |
        az network application-gateway http-settings create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyHttpSettings --port 80 --protocol Http --cookie-based-affinity Disabled --timeout 30
"""

helps['network application-gateway http-settings delete'] = """
type: command
short-summary: Delete HTTP settings.
examples:
  - name: Delete HTTP settings.
    text: az network application-gateway http-settings delete -g MyResourceGroup --gateway-name MyAppGateway -n MyHttpSettings
"""

helps['network application-gateway http-settings list'] = """
type: command
short-summary: List HTTP settings.
examples:
  - name: List HTTP settings.
    text: az network application-gateway http-settings list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway http-settings show'] = """
type: command
short-summary: Get the details of a gateway's HTTP settings.
examples:
  - name: Get the details of a gateway's HTTP settings.
    text: az network application-gateway http-settings show -g MyResourceGroup --gateway-name MyAppGateway -n MyHttpSettings
"""

helps['network application-gateway http-settings update'] = """
type: command
short-summary: Update HTTP settings.
examples:
  - name: Update HTTP settings to use a new probe.
    text: |
        az network application-gateway http-settings update -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyHttpSettings --probe MyNewProbe
"""

helps['network application-gateway list'] = """
type: command
short-summary: List application gateways.
examples:
  - name: List application gateways.
    text: az network application-gateway list -g MyResourceGroup
"""

helps['network application-gateway probe'] = """
type: group
short-summary: Manage probes to gather and evaluate information on a gateway.
"""

helps['network application-gateway probe create'] = """
type: command
short-summary: Create a probe.
examples:
  - name: Create an application gateway probe.
    text: |
        az network application-gateway probe create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyProbe --protocol https --host 127.0.0.1 --path /path/to/probe
"""

helps['network application-gateway probe delete'] = """
type: command
short-summary: Delete a probe.
examples:
  - name: Delete a probe.
    text: az network application-gateway probe delete -g MyResourceGroup --gateway-name MyAppGateway -n MyProbe
"""

helps['network application-gateway probe list'] = """
type: command
short-summary: List probes.
examples:
  - name: List probes.
    text: az network application-gateway probe list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway probe show'] = """
type: command
short-summary: Get the details of a probe.
examples:
  - name: Get the details of a probe.
    text: az network application-gateway probe show -g MyResourceGroup --gateway-name MyAppGateway -n MyProbe
"""

helps['network application-gateway probe update'] = """
type: command
short-summary: Update a probe.
examples:
  - name: Update an application gateway probe with a timeout of 60 seconds.
    text: |
        az network application-gateway probe update -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyProbe --timeout 60
"""

helps['network application-gateway redirect-config'] = """
type: group
short-summary: Manage redirect configurations.
"""

helps['network application-gateway redirect-config create'] = """
type: command
short-summary: Create a redirect configuration.
examples:
  - name: Create a redirect configuration to a http-listener called MyBackendListener.
    text: |
        az network application-gateway redirect-config create -g MyResourceGroup \\
            --gateway-name MyAppGateway -n MyRedirectConfig --type Permanent \\
            --include-path true --include-query-string true --target-listener MyBackendListener
"""

helps['network application-gateway redirect-config delete'] = """
type: command
short-summary: Delete a redirect configuration.
examples:
  - name: Delete a redirect configuration.
    text: az network application-gateway redirect-config delete -g MyResourceGroup \\ --gateway-name MyAppGateway -n MyRedirectConfig
"""

helps['network application-gateway redirect-config list'] = """
type: command
short-summary: List redirect configurations.
examples:
  - name: List redirect configurations.
    text: az network application-gateway redirect-config list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway redirect-config show'] = """
type: command
short-summary: Get the details of a redirect configuration.
examples:
  - name: Get the details of a redirect configuration.
    text: az network application-gateway redirect-config show -g MyResourceGroup --gateway-name MyAppGateway -n MyRedirectConfig
"""

helps['network application-gateway redirect-config update'] = """
type: command
short-summary: Update a redirect configuration.
examples:
  - name: Update a redirect configuration to a different http-listener.
    text: |
        az network application-gateway redirect-config update -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyRedirectConfig --type Permanent --target-listener MyNewBackendListener
  - name: Update a redirect configuration. (autogenerated)
    text: az network application-gateway redirect-config update --gateway-name MyAppGateway --include-query-string true --name MyRedirectConfig --resource-group MyResourceGroup
    crafted: true
"""

helps['network application-gateway rewrite-rule'] = """
short-summary: Manage rewrite rules of an application gateway.
type: group
"""

helps['network application-gateway rewrite-rule condition'] = """
short-summary: Manage rewrite rule conditions of an application gateway.
type: group
"""

helps['network application-gateway rewrite-rule condition create'] = """
short-summary: Create a rewrite rule condition.
type: command
parameters:
  - name: --variable
    populator-commands:
      - az network application-gateway rewrite-rule condition list-server-variables
"""

helps['network application-gateway rewrite-rule condition delete'] = """
short-summary: Delete a rewrite rule condition.
type: command
"""

helps['network application-gateway rewrite-rule condition list'] = """
short-summary: List rewrite rule conditions.
type: command
"""

helps['network application-gateway rewrite-rule condition show'] = """
short-summary: Get the details of a rewrite rule condition.
type: command
"""

helps['network application-gateway rewrite-rule condition update'] = """
short-summary: Update a rewrite rule condition.
type: command
parameters:
  - name: --variable
    populator-commands:
      - az network application-gateway rewrite-rule condition list-server-variables
"""

helps['network application-gateway rewrite-rule create'] = """
short-summary: Create a rewrite rule.
type: command
parameters:
  - name: --request-headers
    populator-commands:
      - az network application-gateway rewrite-rule list-request-headers
  - name: --response-headers
    populator-commands:
      - az network application-gateway rewrite-rule list-response-headers
"""

helps['network application-gateway rewrite-rule delete'] = """
short-summary: Delete a rewrite rule.
type: command
"""

helps['network application-gateway rewrite-rule list'] = """
short-summary: List rewrite rules.
type: command
"""

helps['network application-gateway rewrite-rule set'] = """
short-summary: Manage rewrite rule sets of an application gateway.
type: group
"""

helps['network application-gateway rewrite-rule set create'] = """
short-summary: Create a rewrite rule set.
type: command
"""

helps['network application-gateway rewrite-rule set delete'] = """
short-summary: Delete a rewrite rule set.
type: command
"""

helps['network application-gateway rewrite-rule set list'] = """
short-summary: List rewrite rule sets.
type: command
"""

helps['network application-gateway rewrite-rule set show'] = """
short-summary: Get the details of a rewrite rule set.
type: command
"""

helps['network application-gateway rewrite-rule set update'] = """
short-summary: Update a rewrite rule set.
type: command
"""

helps['network application-gateway rewrite-rule show'] = """
short-summary: Get the details of a rewrite rule.
type: command
"""

helps['network application-gateway rewrite-rule update'] = """
short-summary: Update a rewrite rule.
type: command
parameters:
  - name: --request-headers
    populator-commands:
      - az network application-gateway rewrite-rule list-request-headers
  - name: --response-headers
    populator-commands:
      - az network application-gateway rewrite-rule list-response-headers
"""

helps['network application-gateway root-cert'] = """
type: group
short-summary: Manage trusted root certificates of an application gateway.
"""

helps['network application-gateway root-cert create'] = """
type: command
short-summary: Upload a trusted root certificate.
examples:
  - name: Upload a trusted root certificate. (autogenerated)
    text: az network application-gateway root-cert create --cert-file /path/to/cert/file --gateway-name MyGateway --name MyTrustedRootCertificate --resource-group MyResourceGroup
    crafted: true
"""

helps['network application-gateway root-cert delete'] = """
type: command
short-summary: Delete a trusted root certificate.
examples:
  - name: Delete a trusted root certificate.
    text: az network application-gateway root-cert delete -g MyResourceGroup --gateway-name MyAppGateway -n MyRootCert
"""

helps['network application-gateway root-cert list'] = """
type: command
short-summary: List trusted root certificates.
examples:
  - name: List trusted root certificates.
    text: az network application-gateway root-cert list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway root-cert show'] = """
type: command
short-summary: Get the details of a trusted root certificate.
examples:
  - name: Get the details of a trusted root certificate.
    text: az network application-gateway root-cert show -g MyResourceGroup --gateway-name MyAppGateway -n MyRootCert
"""

helps['network application-gateway root-cert update'] = """
type: command
short-summary: Update a trusted root certificate.
"""

helps['network application-gateway rule'] = """
type: group
short-summary: Evaluate probe information and define routing rules.
long-summary: >
    For more information, visit, https://docs.microsoft.com/azure/application-gateway/application-gateway-customize-waf-rules-cli
"""

helps['network application-gateway rule create'] = """
type: command
short-summary: Create a rule.
long-summary: Rules are executed in the order in which they are created.
examples:
  - name: Create a basic rule.
    text: |
        az network application-gateway rule create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyRule --http-listener MyBackendListener --rule-type Basic --address-pool MyAddressPool --http-settings MyHttpSettings
"""

helps['network application-gateway rule delete'] = """
type: command
short-summary: Delete a rule.
examples:
  - name: Delete a rule.
    text: az network application-gateway rule delete -g MyResourceGroup --gateway-name MyAppGateway -n MyRule
"""

helps['network application-gateway rule list'] = """
type: command
short-summary: List rules.
examples:
  - name: List rules.
    text: az network application-gateway rule list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway rule show'] = """
type: command
short-summary: Get the details of a rule.
examples:
  - name: Get the details of a rule.
    text: az network application-gateway rule show -g MyResourceGroup --gateway-name MyAppGateway -n MyRule
"""

helps['network application-gateway rule update'] = """
type: command
short-summary: Update a rule.
examples:
  - name: Update a rule use a new HTTP listener.
    text: |
        az network application-gateway rule update -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyRule --http-listener MyNewBackendListener
  - name: Update a rule. (autogenerated)
    text: az network application-gateway rule update --address-pool MyAddressPool --gateway-name MyAppGateway --name MyRule --resource-group MyResourceGroup
    crafted: true
"""

helps['network application-gateway show'] = """
type: command
short-summary: Get the details of an application gateway.
examples:
  - name: Get the details of an application gateway.
    text: az network application-gateway show -g MyResourceGroup -n MyAppGateway
"""

helps['network application-gateway show-backend-health'] = """
type: command
short-summary: Get information on the backend health of an application gateway.
examples:
  - name: Show backend health of an application gateway.
    text: az network application-gateway show-backend-health -g MyResourceGroup -n MyAppGateway
"""

helps['network application-gateway ssl-cert'] = """
type: group
short-summary: Manage SSL certificates of an application gateway.
long-summary: For more information visit https://docs.microsoft.com/azure/application-gateway/application-gateway-ssl-cli
"""

helps['network application-gateway ssl-cert create'] = """
type: command
short-summary: Upload an SSL certificate.
examples:
  - name: Upload an SSL certificate.
    text: |
        az network application-gateway ssl-cert create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MySslCert --cert-file \\path\\to\\cert\\file --cert-password Abc123
"""

helps['network application-gateway ssl-cert delete'] = """
type: command
short-summary: Delete an SSL certificate.
examples:
  - name: Delete an SSL certificate.
    text: az network application-gateway ssl-cert delete -g MyResourceGroup --gateway-name MyAppGateway -n MySslCert
"""

helps['network application-gateway ssl-cert list'] = """
type: command
short-summary: List SSL certificates.
examples:
  - name: List SSL certificates.
    text: az network application-gateway ssl-cert list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway ssl-cert show'] = """
type: command
short-summary: Get the details of an SSL certificate.
examples:
  - name: Get the details of an SSL certificate.
    text: az network application-gateway ssl-cert show -g MyResourceGroup --gateway-name MyAppGateway -n MySslCert
"""

helps['network application-gateway ssl-cert update'] = """
type: command
short-summary: Update an SSL certificate.
examples:
  - name: Change a gateway SSL certificate and password.
    text: |
        az network application-gateway ssl-cert update -g MyResourceGroup --gateway-name MyAppGateway -n MySslCert \\
            --cert-file \\path\\to\\new\\cert\\file --cert-password Abc123Abc123
"""

helps['network application-gateway ssl-policy'] = """
type: group
short-summary: Manage the SSL policy of an application gateway.
"""

helps['network application-gateway ssl-policy list-options'] = """
type: command
short-summary: Lists available SSL options for configuring SSL policy.
examples:
  - name: List available SSL options for configuring SSL policy.
    text: az network application-gateway ssl-policy list-options
"""

helps['network application-gateway ssl-policy predefined'] = """
type: group
short-summary: Get information on predefined SSL policies.
"""

helps['network application-gateway ssl-policy predefined list'] = """
type: command
short-summary: Lists all SSL predefined policies for configuring SSL policy.
examples:
  - name: Lists all SSL predefined policies for configuring SSL policy.
    text: az network application-gateway ssl-policy predefined list
"""

helps['network application-gateway ssl-policy predefined show'] = """
type: command
short-summary: Gets SSL predefined policy with the specified policy name.
examples:
  - name: Gets SSL predefined policy with the specified policy name.
    text: az network application-gateway ssl-policy predefined show -n AppGwSslPolicy20170401
"""

helps['network application-gateway ssl-policy set'] = """
type: command
short-summary: Update or clear SSL policy settings.
long-summary: To view the predefined policies, use `az network application-gateway ssl-policy predefined list`.
parameters:
  - name: --cipher-suites
    populator-commands:
      - az network application-gateway ssl-policy list-options
  - name: --disabled-ssl-protocols
    populator-commands:
      - az network application-gateway ssl-policy list-options
  - name: --min-protocol-version
    populator-commands:
      - az network application-gateway ssl-policy list-options
examples:
  - name: Set a predefined SSL policy.
    text: |
        az network application-gateway ssl-policy set -g MyResourceGroup --gateway-name MyAppGateway \\
            -n AppGwSslPolicy20170401S --policy-type Predefined
  - name: Set a custom SSL policy with TLSv1_2 and the cipher suites below.
    text: |
        az network application-gateway ssl-policy set -g MyResourceGroup --gateway-name MyAppGateway \\
            --policy-type Custom --min-protocol-version TLSv1_2 \\
            --cipher-suites TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 TLS_RSA_WITH_AES_128_GCM_SHA256
"""

helps['network application-gateway ssl-policy show'] = """
type: command
short-summary: Get the details of gateway's SSL policy settings.
examples:
  - name: Get the details of a gateway's SSL policy settings.
    text: az network application-gateway ssl-policy show -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway start'] = """
type: command
short-summary: Start an application gateway.
examples:
  - name: Start an application gateway.
    text: az network application-gateway start -g MyResourceGroup -n MyAppGateway
"""

helps['network application-gateway stop'] = """
type: command
short-summary: Stop an application gateway.
examples:
  - name: Stop an application gateway.
    text: az network application-gateway stop -g MyResourceGroup -n MyAppGateway
"""

helps['network application-gateway update'] = """
type: command
short-summary: Update an application gateway.
examples:
  - name: Update an application gateway. (autogenerated)
    text: az network application-gateway update --name MyApplicationGateway --resource-group MyResourceGroup
    crafted: true
"""

helps['network application-gateway url-path-map'] = """
type: group
short-summary: Manage URL path maps of an application gateway.
"""

helps['network application-gateway url-path-map create'] = """
type: command
short-summary: Create a URL path map.
long-summary: >
    The map must be created with at least one rule. This command requires the creation of the
    first rule at the time the map is created. To learn more
    visit https://docs.microsoft.com/azure/application-gateway/application-gateway-create-url-route-cli
examples:
  - name: Create a URL path map with a rule.
    text: |
        az network application-gateway url-path-map create -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyUrlPathMap --rule-name MyUrlPathMapRule1 --paths /mypath1/* --address-pool MyAddressPool \\
            --default-address-pool MyAddressPool --http-settings MyHttpSettings --default-http-settings MyHttpSettings
"""

helps['network application-gateway url-path-map delete'] = """
type: command
short-summary: Delete a URL path map.
examples:
  - name: Delete a URL path map.
    text: az network application-gateway url-path-map delete -g MyResourceGroup --gateway-name MyAppGateway -n MyUrlPathMap
"""

helps['network application-gateway url-path-map list'] = """
type: command
short-summary: List URL path maps.
examples:
  - name: List URL path maps.
    text: az network application-gateway url-path-map list -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway url-path-map rule'] = """
type: group
short-summary: Manage the rules of a URL path map.
"""

helps['network application-gateway url-path-map rule create'] = """
type: command
short-summary: Create a rule for a URL path map.
examples:
  - name: Create a rule for a URL path map.
    text: |
        az network application-gateway url-path-map rule create -g MyResourceGroup \\
            --gateway-name MyAppGateway -n MyUrlPathMapRule2 --path-map-name MyUrlPathMap \\
            --paths /mypath2/* --address-pool MyAddressPool --http-settings MyHttpSettings
"""

helps['network application-gateway url-path-map rule delete'] = """
type: command
short-summary: Delete a rule of a URL path map.
examples:
  - name: Delete a rule of a URL path map.
    text: |
        az network application-gateway url-path-map rule delete -g MyResourceGroup --gateway-name MyAppGateway \\
            --path-map-name MyUrlPathMap -n MyUrlPathMapRule2
"""

helps['network application-gateway url-path-map show'] = """
type: command
short-summary: Get the details of a URL path map.
examples:
  - name: Get the details of a URL path map.
    text: az network application-gateway url-path-map show -g MyResourceGroup --gateway-name MyAppGateway -n MyUrlPathMap
"""

helps['network application-gateway url-path-map update'] = """
type: command
short-summary: Update a URL path map.
examples:
  - name: Update a URL path map to use new default HTTP settings.
    text: |
        az network application-gateway url-path-map update -g MyResourceGroup --gateway-name MyAppGateway \\
            -n MyUrlPathMap --default-http-settings MyNewHttpSettings
  - name: Update a URL path map. (autogenerated)
    text: az network application-gateway url-path-map update --default-address-pool MyAddressPool --default-http-settings MyNewHttpSettings --gateway-name MyAppGateway --name MyUrlPathMap --resource-group MyResourceGroup
    crafted: true
"""

helps['network application-gateway waf-config'] = """
type: group
short-summary: Configure the settings of a web application firewall.
long-summary: >
    These commands are only applicable to application gateways with an SKU type of WAF. To learn
    more, visit https://docs.microsoft.com/azure/application-gateway/application-gateway-web-application-firewall-cli
"""

helps['network application-gateway waf-config list-rule-sets'] = """
type: command
short-summary: Get information on available WAF rule sets, rule groups, and rule IDs.
parameters:
  - name: --group
    short-summary: >
        List rules for the specified rule group. Use `*` to list rules for all groups.
        Omit to suppress listing individual rules.
  - name: --type
    short-summary: Rule set type to list. Omit to list all types.
  - name: --version
    short-summary: Rule set version to list. Omit to list all versions.
examples:
  - name: List available rule groups in OWASP type rule sets.
    text: az network application-gateway waf-config list-rule-sets --type OWASP
  - name: List available rules in the OWASP 3.0 rule set.
    text: az network application-gateway waf-config list-rule-sets --group '*' --type OWASP --version 3.0
  - name: List available rules in the `crs_35_bad_robots` rule group.
    text: az network application-gateway waf-config list-rule-sets --group crs_35_bad_robots
  - name: List available rules in table format.
    text: az network application-gateway waf-config list-rule-sets -o table
"""

helps['network application-gateway waf-config set'] = """
type: command
short-summary: Update the firewall configuration of a web application.
long-summary: >
    This command is only applicable to application gateways with an SKU type of WAF. To learn
    more, visit https://docs.microsoft.com/azure/application-gateway/application-gateway-web-application-firewall-cli
parameters:
  - name: --rule-set-type
    short-summary: Rule set type.
    populator-commands:
      - az network application-gateway waf-config list-rule-sets
  - name: --rule-set-version
    short-summary: Rule set version.
    populator-commands:
      - az network application-gateway waf-config list-rule-sets
  - name: --disabled-rule-groups
    short-summary: Space-separated list of rule groups to disable. To disable individual rules, use `--disabled-rules`.
    populator-commands:
      - az network application-gateway waf-config list-rule-sets
  - name: --disabled-rules
    short-summary: Space-separated list of rule IDs to disable.
    populator-commands:
      - az network application-gateway waf-config list-rule-sets
  - name: --exclusion
    short-summary: Add an exclusion expression to the WAF check.
    long-summary: |
        Usage:   --exclusion VARIABLE OPERATOR VALUE

        Multiple exclusions can be specified by using more than one `--exclusion` argument.
examples:
  - name: Configure WAF on an application gateway in detection mode with default values
    text: |
        az network application-gateway waf-config set -g MyResourceGroup --gateway-name MyAppGateway \\
            --enabled true --firewall-mode Detection --rule-set-version 3.0
  - name: Disable rules for validation of request body parsing and SQL injection.
    text: |
        az network application-gateway waf-config set -g MyResourceGroup --gateway-name MyAppGateway \\
            --enabled true --rule-set-type OWASP --rule-set-version 3.0 \\
            --disabled-rule-groups REQUEST-942-APPLICATION-ATTACK-SQLI \\
            --disabled-rules 920130 920140
  - name: Configure WAF on an application gateway with exclusions.
    text: |
        az network application-gateway waf-config set -g MyResourceGroup --gateway-name MyAppGateway \\
            --enabled true --firewall-mode Detection --rule-set-version 3.0 \\
            --exclusion "RequestHeaderNames StartsWith x-header" \\
            --exclusion "RequestArgNames Equals IgnoreThis"
"""

helps['network application-gateway waf-config show'] = """
type: command
short-summary: Get the firewall configuration of a web application.
examples:
  - name: Get the firewall configuration of a web application.
    text: az network application-gateway waf-config show -g MyResourceGroup --gateway-name MyAppGateway
"""

helps['network application-gateway waf-policy'] = """
type: group
short-summary: Manage application gateway web application firewall (WAF) policies.
"""

helps['network application-gateway waf-policy create'] = """
type: command
short-summary: Create an application gateway WAF policy.
"""

helps['network application-gateway waf-policy delete'] = """
type: command
short-summary: Delete an application gateway WAF policy.
"""

helps['network application-gateway waf-policy list'] = """
type: command
short-summary: List application gateway WAF policies.
"""

helps['network application-gateway waf-policy rule'] = """
type: group
short-summary: Manage application gateway web application firewall (WAF) policy custom rules.
"""

helps['network application-gateway waf-policy rule create'] = """
type: command
short-summary: Create an application gateway WAF policy custom rule.
"""

helps['network application-gateway waf-policy rule delete'] = """
type: command
short-summary: Delete an application gateway WAF policy custom rule.
"""

helps['network application-gateway waf-policy rule list'] = """
type: command
short-summary: List application gateway WAF policy custom rules.
"""

helps['network application-gateway waf-policy rule match-condition'] = """
type: group
short-summary: Manage application gateway web application firewall (WAF) policies.
"""

helps['network application-gateway waf-policy rule match-condition add'] = """
type: command
short-summary: A match condition to an application gateway WAF policy custom rule.
"""

helps['network application-gateway waf-policy rule match-condition list'] = """
type: command
short-summary: List application gateway WAF policy custom rule match conditions.
"""

helps['network application-gateway waf-policy rule match-condition remove'] = """
type: command
short-summary: Remove a match condition from an application gateway WAF policy custom rule.
"""

helps['network application-gateway waf-policy rule show'] = """
type: command
short-summary: Get the details of an application gateway WAF policy custom rule.
"""

helps['network application-gateway waf-policy rule update'] = """
type: command
short-summary: Update an application gateway WAF policy custom rule.
"""

helps['network application-gateway waf-policy show'] = """
type: command
short-summary: Get the details of an application gateway WAF policy.
"""

helps['network application-gateway waf-policy update'] = """
type: command
short-summary: Update an application gateway WAF policy.
"""

helps['network application-gateway waf-policy wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the application gateway WAF policy is met.
"""

helps['network application-gateway wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the application gateway is met.
examples:
  - name: Place the CLI in a waiting state until the application gateway is created.
    text: az network application-gateway wait -g MyResourceGroup -n MyAppGateway --created
"""

helps['network asg'] = """
type: group
short-summary: Manage application security groups (ASGs).
long-summary: >
    You can configure network security as a natural extension of an application's structure, ASG allows
    you to group virtual machines and define network security policies based on those groups. You can specify an
    application security group as the source and destination in a NSG security rule. For more information
    visit https://docs.microsoft.com/azure/virtual-network/create-network-security-group-preview
"""

helps['network asg create'] = """
type: command
short-summary: Create an application security group.
parameters:
  - name: --name -n
    short-summary: Name of the new application security group resource.
examples:
  - name: Create an application security group.
    text: az network asg create -g MyResourceGroup -n MyAsg --tags MyWebApp, CostCenter=Marketing
"""

helps['network asg delete'] = """
type: command
short-summary: Delete an application security group.
examples:
  - name: Delete an application security group.
    text: az network asg delete -g MyResourceGroup -n MyAsg
"""

helps['network asg list'] = """
type: command
short-summary: List all application security groups in a subscription.
examples:
  - name: List all application security groups in a subscription.
    text: az network asg list
"""

helps['network asg show'] = """
type: command
short-summary: Get details of an application security group.
examples:
  - name: Get details of an application security group.
    text: az network asg show -g MyResourceGroup -n MyAsg
"""

helps['network asg update'] = """
type: command
short-summary: Update an application security group.
long-summary: >
    This command can only be used to update the tags for an application security group.
    Name and resource group are immutable and cannot be updated.
examples:
  - name: Update an application security group with a modified tag value.
    text: az network asg update -g MyResourceGroup -n MyAsg --set tags.CostCenter=MyBusinessGroup
"""

helps['network ddos-protection'] = """
type: group
short-summary: Manage DDoS Protection Plans.
"""

helps['network ddos-protection create'] = """
type: command
short-summary: Create a DDoS protection plan.
parameters:
  - name: --vnets
    long-summary: >
        This parameter can only be used if all the VNets are within the same subscription as
        the DDoS protection plan. If this is not the case, set the protection plan on the VNet
        directly using the `az network vnet update` command.
examples:
  - name: Create a DDoS protection plan.
    text: az network ddos-protection create -g MyResourceGroup -n MyDdosPlan
  - name: Create a DDoS protection plan. (autogenerated)
    text: az network ddos-protection create --location westus2 --name MyDdosPlan --resource-group MyResourceGroup
    crafted: true
"""

helps['network ddos-protection delete'] = """
type: command
short-summary: Delete a DDoS protection plan.
examples:
  - name: Delete a DDoS protection plan.
    text: az network ddos-protection delete -g MyResourceGroup -n MyDdosPlan
"""

helps['network ddos-protection list'] = """
type: command
short-summary: List DDoS protection plans.
examples:
  - name: List DDoS protection plans
    text: az network ddos-protection list
"""

helps['network ddos-protection show'] = """
type: command
short-summary: Show details of a DDoS protection plan.
examples:
  - name: Show details of a DDoS protection plan.
    text: az network ddos-protection show -g MyResourceGroup -n MyDdosPlan
"""

helps['network ddos-protection update'] = """
type: command
short-summary: Update a DDoS protection plan.
parameters:
  - name: --vnets
    long-summary: >
        This parameter can only be used if all the VNets are within the same subscription as
        the DDoS protection plan. If this is not the case, set the protection plan on the VNet
        directly using the `az network vnet update` command.
examples:
  - name: Add a Vnet to a DDoS protection plan in the same subscription.
    text: az network ddos-protection update -g MyResourceGroup -n MyDdosPlan --vnets MyVnet
"""

helps['network dns'] = """
type: group
short-summary: Manage DNS domains in Azure.
"""

helps['network dns record-set'] = """
type: group
short-summary: Manage DNS records and record sets.
"""

helps['network dns record-set a'] = """
type: group
short-summary: Manage DNS A records.
"""

helps['network dns record-set a add-record'] = """
type: command
short-summary: Add an A record.
examples:
  - name: Add an A record.
    text: |
        az network dns record-set a add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv4Address
"""

helps['network dns record-set a create'] = """
type: command
short-summary: Create an empty A record set.
examples:
  - name: Create an empty A record set.
    text: az network dns record-set a create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
  - name: Create an empty A record set. (autogenerated)
    text: az network dns record-set a create --name MyRecordSet --resource-group MyResourceGroup --ttl 30 --zone-name www.mysite.com
    crafted: true
"""

helps['network dns record-set a delete'] = """
type: command
short-summary: Delete an A record set and all associated records.
examples:
  - name: Delete an A record set and all associated records.
    text: az network dns record-set a delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set a list'] = """
type: command
short-summary: List all A record sets in a zone.
examples:
  - name: List all A record sets in a zone.
    text: az network dns record-set a list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set a remove-record'] = """
type: command
short-summary: Remove an A record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an A record from its record set.
    text: |
        az network dns record-set a remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv4Address
"""

helps['network dns record-set a show'] = """
type: command
short-summary: Get the details of an A record set.
examples:
  - name: Get the details of an A record set.
    text: az network dns record-set a show -g MyResourceGroup -n MyRecordSet -z www.mysite.com
"""

helps['network dns record-set a update'] = """
type: command
short-summary: Update an A record set.
examples:
  - name: Update an A record set.
    text: |
        az network dns record-set a update -g MyResourceGroup -n MyRecordSet \\
            -z www.mysite.com --metadata owner=WebTeam
  - name: Update an A record set. (autogenerated)
    text: az network dns record-set a update --name MyRecordSet --resource-group MyResourceGroup --set tags.CostCenter=MyBusinessGroup --zone-name www.mysite.com
    crafted: true
"""

helps['network dns record-set aaaa'] = """
type: group
short-summary: Manage DNS AAAA records.
"""

helps['network dns record-set aaaa add-record'] = """
type: command
short-summary: Add an AAAA record.
examples:
  - name: Add an AAAA record.
    text: |
        az network dns record-set aaaa add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv6Address
"""

helps['network dns record-set aaaa create'] = """
type: command
short-summary: Create an empty AAAA record set.
examples:
  - name: Create an empty AAAA record set.
    text: az network dns record-set aaaa create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set aaaa delete'] = """
type: command
short-summary: Delete an AAAA record set and all associated records.
examples:
  - name: Delete an AAAA record set and all associated records.
    text: az network dns record-set aaaa delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set aaaa list'] = """
type: command
short-summary: List all AAAA record sets in a zone.
examples:
  - name: List all AAAA record sets in a zone.
    text: az network dns record-set aaaa list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set aaaa remove-record'] = """
type: command
short-summary: Remove AAAA record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an AAAA record from its record set.
    text: |
        az network dns record-set aaaa remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv6Address
"""

helps['network dns record-set aaaa show'] = """
type: command
short-summary: Get the details of an AAAA record set.
examples:
  - name: Get the details of an AAAA record set.
    text: az network dns record-set aaaa show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set aaaa update'] = """
type: command
short-summary: Update an AAAA record set.
examples:
  - name: Update an AAAA record set.
    text: |
        az network dns record-set aaaa update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network dns record-set caa'] = """
type: group
short-summary: Manage DNS CAA records.
"""

helps['network dns record-set caa add-record'] = """
type: command
short-summary: Add a CAA record.
examples:
  - name: Add a CAA record.
    text: |
        az network dns record-set caa add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --flags 0 --tag "issue" --value "ca.contoso.com"
"""

helps['network dns record-set caa create'] = """
type: command
short-summary: Create an empty CAA record set.
examples:
  - name: Create an empty CAA record set.
    text: az network dns record-set caa create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set caa delete'] = """
type: command
short-summary: Delete a CAA record set and all associated records.
examples:
  - name: Delete a CAA record set and all associated records.
    text: az network dns record-set caa delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set caa list'] = """
type: command
short-summary: List all CAA record sets in a zone.
examples:
  - name: List all CAA record sets in a zone.
    text: az network dns record-set caa list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set caa remove-record'] = """
type: command
short-summary: Remove a CAA record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a CAA record from its record set.
    text: |
        az network dns record-set caa remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --flags 0 --tag "issue" --value "ca.contoso.com"
"""

helps['network dns record-set caa show'] = """
type: command
short-summary: Get the details of a CAA record set.
examples:
  - name: Get the details of a CAA record set.
    text: az network dns record-set caa show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set caa update'] = """
type: command
short-summary: Update a CAA record set.
examples:
  - name: Update a CAA record set.
    text: |
        az network dns record-set caa update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network dns record-set cname'] = """
type: group
short-summary: Manage DNS CNAME records.
"""

helps['network dns record-set cname create'] = """
type: command
short-summary: Create an empty CNAME record set.
examples:
  - name: Create an empty CNAME record set.
    text: az network dns record-set cname create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set cname delete'] = """
type: command
short-summary: Delete a CNAME record set and its associated record.
examples:
  - name: Delete a CNAME record set and its associated record.
    text: az network dns record-set cname delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set cname list'] = """
type: command
short-summary: List the CNAME record set in a zone.
examples:
  - name: List the CNAME record set in a zone.
    text: az network dns record-set cname list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set cname remove-record'] = """
type: command
short-summary: Remove a CNAME record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a CNAME record from its record set.
    text: |
        az network dns record-set cname remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -c www.contoso.com
"""

helps['network dns record-set cname set-record'] = """
type: command
short-summary: Set the value of a CNAME record.
examples:
  - name: Set the value of a CNAME record.
    text: |
        az network dns record-set cname set-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -c www.contoso.com
"""

helps['network dns record-set cname show'] = """
type: command
short-summary: Get the details of a CNAME record set.
examples:
  - name: Get the details of a CNAME record set.
    text: az network dns record-set cname show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set list'] = """
type: command
short-summary: List all record sets within a DNS zone.
examples:
  - name: List all "@" record sets within this zone.
    text: az network dns record-set list -g MyResourceGroup -z www.mysite.com --query "[?name=='@']"
"""

helps['network dns record-set mx'] = """
type: group
short-summary: Manage DNS MX records.
"""

helps['network dns record-set mx add-record'] = """
type: command
short-summary: Add an MX record.
examples:
  - name: Add an MX record.
    text: |
        az network dns record-set mx add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -e mail.mysite.com -p 10
"""

helps['network dns record-set mx create'] = """
type: command
short-summary: Create an empty MX record set.
examples:
  - name: Create an empty MX record set.
    text: az network dns record-set mx create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set mx delete'] = """
type: command
short-summary: Delete an MX record set and all associated records.
examples:
  - name: Delete an MX record set and all associated records.
    text: az network dns record-set mx delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set mx list'] = """
type: command
short-summary: List all MX record sets in a zone.
examples:
  - name: List all MX record sets in a zone.
    text: az network dns record-set mx list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set mx remove-record'] = """
type: command
short-summary: Remove an MX record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an MX record from its record set.
    text: |
        az network dns record-set mx remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -e mail.mysite.com -p 10
"""

helps['network dns record-set mx show'] = """
type: command
short-summary: Get the details of an MX record set.
examples:
  - name: Get the details of an MX record set.
    text: az network dns record-set mx show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set mx update'] = """
type: command
short-summary: Update an MX record set.
examples:
  - name: Update an MX record set.
    text: |
        az network dns record-set mx update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
  - name: Update an MX record set. (autogenerated)
    text: az network dns record-set mx update --name MyRecordSet --resource-group MyResourceGroup --set tags.CostCenter=MyBusinessGroup --zone-name www.mysite.com
    crafted: true
"""

helps['network dns record-set ns'] = """
type: group
short-summary: Manage DNS NS records.
"""

helps['network dns record-set ns add-record'] = """
type: command
short-summary: Add an NS record.
examples:
  - name: Add an NS record.
    text: |
        az network dns record-set ns add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d ns.mysite.com
"""

helps['network dns record-set ns create'] = """
type: command
short-summary: Create an empty NS record set.
examples:
  - name: Create an empty NS record set.
    text: az network dns record-set ns create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set ns delete'] = """
type: command
short-summary: Delete an NS record set and all associated records.
examples:
  - name: Delete an NS record set and all associated records.
    text: az network dns record-set ns delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set ns list'] = """
type: command
short-summary: List all NS record sets in a zone.
examples:
  - name: List all NS record sets in a zone.
    text: az network dns record-set ns list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set ns remove-record'] = """
type: command
short-summary: Remove an NS record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an NS record from its record set.
    text: |
        az network dns record-set ns remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d ns.mysite.com
"""

helps['network dns record-set ns show'] = """
type: command
short-summary: Get the details of an NS record set.
examples:
  - name: Get the details of an NS record set.
    text: az network dns record-set ns show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set ns update'] = """
type: command
short-summary: Update an NS record set.
examples:
  - name: Update an NS record set.
    text: |
        az network dns record-set ns update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
  - name: Update an NS record set. (autogenerated)
    text: az network dns record-set ns update --name MyRecordSet --resource-group MyResourceGroup --set tags.CostCenter=MyBusinessGroup --zone-name www.mysite.com
    crafted: true
"""

helps['network dns record-set ptr'] = """
type: group
short-summary: Manage DNS PTR records.
"""

helps['network dns record-set ptr add-record'] = """
type: command
short-summary: Add a PTR record.
examples:
  - name: Add a PTR record.
    text: |
        az network dns record-set ptr add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d another.site.com
"""

helps['network dns record-set ptr create'] = """
type: command
short-summary: Create an empty PTR record set.
examples:
  - name: Create an empty PTR record set.
    text: az network dns record-set ptr create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set ptr delete'] = """
type: command
short-summary: Delete a PTR record set and all associated records.
examples:
  - name: Delete a PTR record set and all associated records.
    text: az network dns record-set ptr delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set ptr list'] = """
type: command
short-summary: List all PTR record sets in a zone.
examples:
  - name: List all PTR record sets in a zone.
    text: az network dns record-set ptr list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set ptr remove-record'] = """
type: command
short-summary: Remove a PTR record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a PTR record from its record set.
    text: |
        az network dns record-set ptr remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d another.site.com
"""

helps['network dns record-set ptr show'] = """
type: command
short-summary: Get the details of a PTR record set.
examples:
  - name: Get the details of a PTR record set.
    text: az network dns record-set ptr show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set ptr update'] = """
type: command
short-summary: Update a PTR record set.
examples:
  - name: Update a PTR record set.
    text: |
        az network dns record-set ptr update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network dns record-set soa'] = """
type: group
short-summary: Manage a DNS SOA record.
"""

helps['network dns record-set soa show'] = """
type: command
short-summary: Get the details of an SOA record.
examples:
  - name: Get the details of an SOA record.
    text: az network dns record-set soa show -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set soa update'] = """
type: command
short-summary: Update properties of an SOA record.
examples:
  - name: Update properties of an SOA record.
    text: |
        az network dns record-set soa update -g MyResourceGroup -z www.mysite.com \\
            -e myhostmaster.mysite.com
"""

helps['network dns record-set srv'] = """
type: group
short-summary: Manage DNS SRV records.
"""

helps['network dns record-set srv add-record'] = """
type: command
short-summary: Add an SRV record.
examples:
  - name: Add an SRV record.
    text: |
        az network dns record-set srv add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -t webserver.mysite.com -r 8081 -p 10 -w 10
"""

helps['network dns record-set srv create'] = """
type: command
short-summary: Create an empty SRV record set.
examples:
  - name: Create an empty SRV record set.
    text: |
        az network dns record-set srv create -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet
"""

helps['network dns record-set srv delete'] = """
type: command
short-summary: Delete an SRV record set and all associated records.
examples:
  - name: Delete an SRV record set and all associated records.
    text: az network dns record-set srv delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set srv list'] = """
type: command
short-summary: List all SRV record sets in a zone.
examples:
  - name: List all SRV record sets in a zone.
    text: az network dns record-set srv list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set srv remove-record'] = """
type: command
short-summary: Remove an SRV record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an SRV record from its record set.
    text: |
        az network dns record-set srv remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -t webserver.mysite.com -r 8081 -p 10 -w 10
"""

helps['network dns record-set srv show'] = """
type: command
short-summary: Get the details of an SRV record set.
examples:
  - name: Get the details of an SRV record set.
    text: az network dns record-set srv show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set srv update'] = """
type: command
short-summary: Update an SRV record set.
examples:
  - name: Update an SRV record set.
    text: |
        az network dns record-set srv update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network dns record-set txt'] = """
type: group
short-summary: Manage DNS TXT records.
"""

helps['network dns record-set txt add-record'] = """
type: command
short-summary: Add a TXT record.
examples:
  - name: Add a TXT record.
    text: |
        az network dns record-set txt add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -v Owner=WebTeam
"""

helps['network dns record-set txt create'] = """
type: command
short-summary: Create an empty TXT record set.
examples:
  - name: Create an empty TXT record set.
    text: az network dns record-set txt create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
  - name: Create an empty TXT record set. (autogenerated)
    text: az network dns record-set txt create --name MyRecordSet --resource-group MyResourceGroup --ttl 30 --zone-name www.mysite.com
    crafted: true
"""

helps['network dns record-set txt delete'] = """
type: command
short-summary: Delete a TXT record set and all associated records.
examples:
  - name: Delete a TXT record set and all associated records.
    text: az network dns record-set txt delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set txt list'] = """
type: command
short-summary: List all TXT record sets in a zone.
examples:
  - name: List all TXT record sets in a zone.
    text: az network dns record-set txt list -g MyResourceGroup -z www.mysite.com
"""

helps['network dns record-set txt remove-record'] = """
type: command
short-summary: Remove a TXT record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a TXT record from its record set.
    text: |
        az network dns record-set txt remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -v Owner=WebTeam
"""

helps['network dns record-set txt show'] = """
type: command
short-summary: Get the details of a TXT record set.
examples:
  - name: Get the details of a TXT record set.
    text: az network dns record-set txt show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network dns record-set txt update'] = """
type: command
short-summary: Update a TXT record set.
examples:
  - name: Update a TXT record set.
    text: |
        az network dns record-set txt update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
  - name: Update a TXT record set. (autogenerated)
    text: az network dns record-set txt update --name MyRecordSet --resource-group MyResourceGroup --set tags.CostCenter=MyBusinessGroup --zone-name www.mysite.com
    crafted: true
"""

helps['network dns zone'] = """
type: group
short-summary: Manage DNS zones.
"""

helps['network dns zone create'] = """
type: command
short-summary: Create a DNS zone.
parameters:
  - name: --if-none-match
    short-summary: Only create a DNS zone if one doesn't exist that matches the given name.
examples:
  - name: Create a DNS zone using a fully qualified domain name.
    text: >
        az network dns zone create -g MyResourceGroup -n www.mysite.com
  - name: Create a DNS zone with delegation in the parent within the same subscription and resource group
    text: >
        az network dns zone create -g MyResourceGroup -n books.mysite.com -p mysite.com
  - name: Create a DNS zone with delegation in the parent in different subscription
    text: >
        az network dns zone create -g MyResourceGroup -n books.mysite.com -p "/subscriptions/**67e2/resourceGroups/OtherRg/providers/Microsoft.Network/dnszones/mysite.com"
"""

helps['network dns zone delete'] = """
type: command
short-summary: Delete a DNS zone and all associated records.
examples:
  - name: Delete a DNS zone using a fully qualified domain name.
    text: >
        az network dns zone delete -g MyResourceGroup -n www.mysite.com
"""

helps['network dns zone export'] = """
type: command
short-summary: Export a DNS zone as a DNS zone file.
examples:
  - name: Export a DNS zone as a DNS zone file.
    text: >
        az network dns zone export -g MyResourceGroup -n www.mysite.com -f mysite_com_zone.txt
"""

helps['network dns zone import'] = """
type: command
short-summary: Create a DNS zone using a DNS zone file.
examples:
  - name: Import a local zone file into a DNS zone resource.
    text: >
        az network dns zone import -g MyResourceGroup -n MyZone -f /path/to/zone/file
"""

helps['network dns zone list'] = """
type: command
short-summary: List DNS zones.
examples:
  - name: List DNS zones in a resource group.
    text: >
        az network dns zone list -g MyResourceGroup
"""

helps['network dns zone show'] = """
type: command
short-summary: Get a DNS zone parameters. Does not show DNS records within the zone.
examples:
  - name: List DNS zones in a resource group.
    text: >
        az network dns zone show -g MyResourceGroup -n www.mysite.com
"""

helps['network dns zone update'] = """
type: command
short-summary: Update a DNS zone properties. Does not modify DNS records within the zone.
parameters:
  - name: --if-match
    short-summary: Update only if the resource with the same ETAG exists.
examples:
  - name: Update a DNS zone properties to change the user-defined value of a previously set tag.
    text: >
        az network dns zone update -g MyResourceGroup -n www.mysite.com --tags CostCenter=Marketing
"""

helps['network express-route'] = """
type: group
short-summary: Manage dedicated private network fiber connections to Azure.
long-summary: >
    To learn more about ExpressRoute circuits visit
    https://docs.microsoft.com/azure/expressroute/howto-circuit-cli
"""

helps['network express-route auth'] = """
type: group
short-summary: Manage authentication of an ExpressRoute circuit.
long-summary: >
    To learn more about ExpressRoute circuit authentication visit
    https://docs.microsoft.com/azure/expressroute/howto-linkvnet-cli#connect-a-virtual-network-in-a-different-subscription-to-a-circuit
"""

helps['network express-route auth create'] = """
type: command
short-summary: Create a new link authorization for an ExpressRoute circuit.
examples:
  - name: Create a new link authorization for an ExpressRoute circuit.
    text: >
        az network express-route auth create --circuit-name MyCircuit -g MyResourceGroup -n MyAuthorization
"""

helps['network express-route auth delete'] = """
type: command
short-summary: Delete a link authorization of an ExpressRoute circuit.
examples:
  - name: Delete a link authorization of an ExpressRoute circuit.
    text: >
        az network express-route auth delete --circuit-name MyCircuit -g MyResourceGroup -n MyAuthorization
"""

helps['network express-route auth list'] = """
type: command
short-summary: List link authorizations of an ExpressRoute circuit.
examples:
  - name: List link authorizations of an ExpressRoute circuit.
    text: >
        az network express-route auth list -g MyResourceGroup --circuit-name MyCircuit
  - name: List link authorizations of an ExpressRoute circuit. (autogenerated)
    text: az network express-route auth list --circuit-name MyCircuit --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['network express-route auth show'] = """
type: command
short-summary: Get the details of a link authorization of an ExpressRoute circuit.
examples:
  - name: Get the details of a link authorization of an ExpressRoute circuit.
    text: >
        az network express-route auth show -g MyResourceGroup --circuit-name MyCircuit -n MyAuthorization
"""

helps['network express-route create'] = """
type: command
short-summary: Create an ExpressRoute circuit.
parameters:
  - name: --bandwidth
    populator-commands:
      - az network express-route list-service-providers
  - name: --peering-location
    populator-commands:
      - az network express-route list-service-providers
  - name: --provider
    populator-commands:
      - az network express-route list-service-providers
examples:
  - name: Create an ExpressRoute circuit.
    text: >
        az network express-route create --bandwidth 200 -n MyCircuit --peering-location "Silicon Valley" -g MyResourceGroup --provider "Equinix" -l "West US" --sku-family MeteredData --sku-tier Standard
"""

helps['network express-route delete'] = """
type: command
short-summary: Delete an ExpressRoute circuit.
examples:
  - name: Delete an ExpressRoute circuit.
    text: >
        az network express-route delete -n MyCircuit -g MyResourceGroup
"""

helps['network express-route gateway'] = """
type: group
short-summary: Manage ExpressRoute gateways.
"""

helps['network express-route gateway connection'] = """
type: group
short-summary: Manage ExpressRoute gateway connections.
"""

helps['network express-route gateway connection create'] = """
type: command
short-summary: Create an ExpressRoute gateway connection.
"""

helps['network express-route gateway connection delete'] = """
type: command
short-summary: Delete an ExpressRoute gateway connection.
examples:
  - name: Delete an ExpressRoute gateway connection. (autogenerated)
    text: az network express-route gateway connection delete --gateway-name MyGateway --name MyExpressRouteConnection --resource-group MyResourceGroup
    crafted: true
"""

helps['network express-route gateway connection list'] = """
type: command
short-summary: List ExpressRoute gateway connections.
examples:
  - name: List ExpressRoute gateway connections. (autogenerated)
    text: az network express-route gateway connection list --gateway-name MyGateway --resource-group MyResourceGroup
    crafted: true
"""

helps['network express-route gateway connection show'] = """
type: command
short-summary: Get the details of an ExpressRoute gateway connection.
examples:
  - name: Get the details of an ExpressRoute gateway connection. (autogenerated)
    text: az network express-route gateway connection show --gateway-name MyGateway --name MyExpressRouteConnection --resource-group MyResourceGroup
    crafted: true
"""

helps['network express-route gateway connection update'] = """
type: command
short-summary: Update an ExpressRoute gateway connection.
"""

helps['network express-route gateway create'] = """
type: command
short-summary: Create an ExpressRoute gateway.
"""

helps['network express-route gateway delete'] = """
type: command
short-summary: Delete an ExpressRoute gateway.
examples:
  - name: Delete an ExpressRoute gateway. (autogenerated)
    text: az network express-route gateway delete --name MyExpressRouteGateway --resource-group MyResourceGroup
    crafted: true
"""

helps['network express-route gateway list'] = """
type: command
short-summary: List ExpressRoute gateways.
"""

helps['network express-route gateway show'] = """
type: command
short-summary: Get the details of an ExpressRoute gateway.
examples:
  - name: Get the details of an ExpressRoute gateway. (autogenerated)
    text: az network express-route gateway show --name MyExpressRouteGateway --resource-group MyResourceGroup
    crafted: true
"""

helps['network express-route gateway update'] = """
type: command
short-summary: Update settings of an ExpressRoute gateway.
"""

helps['network express-route get-stats'] = """
type: command
short-summary: Get the statistics of an ExpressRoute circuit.
examples:
  - name: Get the statistics of an ExpressRoute circuit.
    text: >
        az network express-route get-stats -g MyResourceGroup -n MyCircuit
"""

helps['network express-route list'] = """
type: command
short-summary: List all ExpressRoute circuits for the current subscription.
examples:
  - name: List all ExpressRoute circuits for the current subscription.
    text: >
        az network express-route list -g MyResourceGroup
"""

helps['network express-route list-arp-tables'] = """
type: command
short-summary: Show the current Address Resolution Protocol (ARP) table of an ExpressRoute circuit.
examples:
  - name: Show the current Address Resolution Protocol (ARP) table of an ExpressRoute circuit.
    text: |
        az network express-route list-arp-tables -g MyResourceGroup -n MyCircuit \\
            --path primary --peering-name AzurePrivatePeering
"""

helps['network express-route list-route-tables'] = """
type: command
short-summary: Show the current routing table of an ExpressRoute circuit peering.
examples:
  - name: Show the current routing table of an ExpressRoute circuit peering.
    text: |
        az network express-route list-route-tables -g MyResourceGroup -n MyCircuit \\
            --path primary --peering-name AzurePrivatePeering
"""

helps['network express-route list-service-providers'] = """
type: command
short-summary: List available ExpressRoute service providers.
examples:
  - name: List available ExpressRoute service providers.
    text: az network express-route list-service-providers
"""

helps['network express-route peering'] = """
type: group
short-summary: Manage ExpressRoute peering of an ExpressRoute circuit.
"""

helps['network express-route peering connection'] = """
type: group
short-summary: Manage ExpressRoute circuit connections.
"""

helps['network express-route peering connection create'] = """
type: command
short-summary: Create connections between two ExpressRoute circuits.
examples:
  - name: Create connection between two ExpressRoute circuits with AzurePrivatePeering settings.
    text: |
        az network express-route peering connection create -g MyResourceGroup --circuit-name \\
            MyCircuit --peering-name AzurePrivatePeering -n myConnection --peer-circuit \\
            MyOtherCircuit --address-prefix 104.0.0.0/29
"""

helps['network express-route peering connection delete'] = """
type: command
short-summary: Delete an ExpressRoute circuit connection.
"""

helps['network express-route peering connection show'] = """
type: command
short-summary: Get the details of an ExpressRoute circuit connection.
"""

helps['network express-route peering create'] = """
type: command
short-summary: Create peering settings for an ExpressRoute circuit.
examples:
  - name: Create Microsoft Peering settings with IPv4 configuration.
    text: |
        az network express-route peering create -g MyResourceGroup --circuit-name MyCircuit \\
            --peering-type MicrosoftPeering --peer-asn 10002 --vlan-id 103 \\
            --primary-peer-subnet 101.0.0.0/30 --secondary-peer-subnet 102.0.0.0/30 \\
            --advertised-public-prefixes 101.0.0.0/30
"""

helps['network express-route peering delete'] = """
type: command
short-summary: Delete peering settings.
examples:
  - name: Delete private peering.
    text: >
        az network express-route peering delete -g MyResourceGroup --circuit-name MyCircuit -n AzurePrivatePeering
"""

helps['network express-route peering list'] = """
type: command
short-summary: List peering settings of an ExpressRoute circuit.
examples:
  - name: List peering settings of an ExpressRoute circuit.
    text: >
        az network express-route peering list -g MyResourceGroup --circuit-name MyCircuit
"""

helps['network express-route peering show'] = """
type: command
short-summary: Get the details of an express route peering.
examples:
  - name: Get private peering details of an ExpressRoute circuit.
    text: >
        az network express-route peering show -g MyResourceGroup --circuit-name MyCircuit -n AzurePrivatePeering
"""

helps['network express-route peering update'] = """
type: command
short-summary: Update peering settings of an ExpressRoute circuit.
examples:
  - name: Add IPv6 Microsoft Peering settings to existing IPv4 config.
    text: |
        az network express-route peering update -g MyResourceGroup --circuit-name MyCircuit \\
            --ip-version ipv6 --primary-peer-subnet 2002:db00::/126 \\
            --secondary-peer-subnet 2003:db00::/126 --advertised-public-prefixes 2002:db00::/126
    supported-profiles: latest
"""

helps['network express-route port'] = """
type: group
short-summary: Manage ExpressRoute ports.
"""

helps['network express-route port create'] = """
type: command
short-summary: Create an ExpressRoute port.
examples:
  - name: Create an ExpressRoute port. (autogenerated)
    text: az network express-route port create --bandwidth 200 --encapsulation Dot1Q --location westus2 --name MyExpressRoutePort --peering-location westus --resource-group MyResourceGroup
    crafted: true
"""

helps['network express-route port delete'] = """
type: command
short-summary: Delete an ExpressRoute port.
examples:
  - name: Delete an ExpressRoute port. (autogenerated)
    text: az network express-route port delete --name MyExpressRoutePort --resource-group MyResourceGroup
    crafted: true
"""

helps['network express-route port link'] = """
type: group
short-summary: View ExpressRoute links.
"""

helps['network express-route port link list'] = """
type: command
short-summary: List ExpressRoute links.
"""

helps['network express-route port link show'] = """
type: command
short-summary: Get the details of an ExpressRoute link.
"""

helps['network express-route port list'] = """
type: command
short-summary: List ExpressRoute ports.
"""

helps['network express-route port location'] = """
type: group
short-summary: View ExpressRoute port location information.
"""

helps['network express-route port location list'] = """
type: command
short-summary: List ExpressRoute port locations.
"""

helps['network express-route port location show'] = """
type: command
short-summary: Get the details of an ExpressRoute port location.
examples:
  - name: Get the details of an ExpressRoute port location. (autogenerated)
    text: az network express-route port location show --location westus2
    crafted: true
"""

helps['network express-route port show'] = """
type: command
short-summary: Get the details of an ExpressRoute port.
"""

helps['network express-route port update'] = """
type: command
short-summary: Update settings of an ExpressRoute port.
"""

helps['network express-route show'] = """
type: command
short-summary: Get the details of an ExpressRoute circuit.
examples:
  - name: Get the details of an ExpressRoute circuit.
    text: >
        az network express-route show -n MyCircuit -g MyResourceGroup
"""

helps['network express-route update'] = """
type: command
short-summary: Update settings of an ExpressRoute circuit.
examples:
  - name: Change the SKU of an ExpressRoute circuit from Standard to Premium.
    text: >
        az network express-route update -n MyCircuit -g MyResourceGroup --sku-tier Premium
"""

helps['network express-route wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the ExpressRoute is met.
examples:
  - name: Pause executing next line of CLI script until the ExpressRoute circuit is successfully provisioned.
    text: az network express-route wait -n MyCircuit -g MyResourceGroup --created
"""

helps['network lb'] = """
type: group
short-summary: Manage and configure load balancers.
long-summary: To learn more about Azure Load Balancer visit https://docs.microsoft.com/azure/load-balancer/load-balancer-get-started-internet-arm-cli
"""

helps['network lb address-pool'] = """
type: group
short-summary: Manage address pools of a load balancer.
"""

helps['network lb address-pool create'] = """
type: command
short-summary: Create an address pool.
examples:
  - name: Create an address pool.
    text: az network lb address-pool create -g MyResourceGroup --lb-name MyLb -n MyAddressPool
"""

helps['network lb address-pool delete'] = """
type: command
short-summary: Delete an address pool.
examples:
  - name: Delete an address pool.
    text: az network lb address-pool delete -g MyResourceGroup --lb-name MyLb -n MyAddressPool
"""

helps['network lb address-pool list'] = """
type: command
short-summary: List address pools.
examples:
  - name: List address pools.
    text: az network lb address-pool list -g MyResourceGroup --lb-name MyLb -o table
"""

helps['network lb address-pool show'] = """
type: command
short-summary: Get the details of an address pool.
examples:
  - name: Get the details of an address pool.
    text: az network lb address-pool show -g MyResourceGroup --lb-name MyLb -n MyAddressPool
"""

helps['network lb create'] = """
type: command
short-summary: Create a load balancer.
examples:
  - name: Create a basic load balancer.
    text: >
        az network lb create -g MyResourceGroup -n MyLb --sku Basic
  - name: Create a basic load balancer on a specific virtual network and subnet. If a virtual network with the same name is found in the same resource group, the load balancer will utilize this virtual network.  If one is not found a new one will be created.
    text: >
        az network lb create -g MyResourceGroup -n MyLb --sku Basic --vnet-name MyVnet --subnet MySubnet
  - name: Create a basic load balancer on a subnet of a pre-existing virtual network.
    text: >
        az network lb create -g MyResourceGroup -n MyLb --sku Basic --subnet {subnetID}
  - name: Create a basic zone flavored internal load balancer, through provisioning a zonal public ip.
    text: >
        az network lb create -g MyResourceGroup -n MyLb --sku Basic --public-ip-zone 2
  - name: >
        Create a standard zone flavored public-facing load balancer, through provisioning a zonal frontend ip configuration and Vnet.
    text: >
        az network lb create -g MyResourceGroup -n MyLb --sku Standard --frontend-ip-zone 1 --vnet-name MyVnet --subnet MySubnet
"""

helps['network lb delete'] = """
type: command
short-summary: Delete a load balancer.
examples:
  - name: Delete a load balancer.
    text: az network lb delete -g MyResourceGroup -n MyLb
"""

helps['network lb frontend-ip'] = """
type: group
short-summary: Manage frontend IP addresses of a load balancer.
"""

helps['network lb frontend-ip create'] = """
type: command
short-summary: Create a frontend IP address.
examples:
  - name: Create a frontend ip address for a public load balancer.
    text: az network lb frontend-ip create -g MyResourceGroup -n MyFrontendIp --lb-name MyLb --public-ip-address MyFrontendIp
  - name: Create a frontend ip address for an internal load balancer.
    text: |
        az network lb frontend-ip create -g MyResourceGroup -n MyFrontendIp --lb-name MyLb \\
            --private-ip-address 10.10.10.100 --subnet MySubnet --vnet-name MyVnet
"""

helps['network lb frontend-ip delete'] = """
type: command
short-summary: Delete a frontend IP address.
examples:
  - name: Delete a frontend IP address.
    text: az network lb frontend-ip delete -g MyResourceGroup --lb-name MyLb -n MyFrontendIp
"""

helps['network lb frontend-ip list'] = """
type: command
short-summary: List frontend IP addresses.
examples:
  - name: List frontend IP addresses.
    text: az network lb frontend-ip list -g MyResourceGroup --lb-name MyLb
"""

helps['network lb frontend-ip show'] = """
type: command
short-summary: Get the details of a frontend IP address.
examples:
  - name: Get the details of a frontend IP address.
    text: az network lb frontend-ip show -g MyResourceGroup --lb-name MyLb -n MyFrontendIp
  - name: Get the details of a frontend IP address (autogenerated)
    text: az network lb frontend-ip show --lb-name MyLb --name MyFrontendIp --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['network lb frontend-ip update'] = """
type: command
short-summary: Update a frontend IP address.
examples:
  - name: Update the frontend IP address of a public load balancer.
    text: az network lb frontend-ip update -g MyResourceGroup --lb-name MyLb -n MyFrontendIp --public-ip-address MyNewPublicIp
  - name: Update the frontend IP address of an internal load balancer.
    text: az network lb frontend-ip update -g MyResourceGroup --lb-name MyLb -n MyFrontendIp --private-ip-address 10.10.10.50
  - name: Update a frontend IP address. (autogenerated)
    text: az network lb frontend-ip update --lb-name MyLb --name MyFrontendIp --resource-group MyResourceGroup --set tags.CostCenter=MyBusinessGroup
    crafted: true
"""

helps['network lb inbound-nat-pool'] = """
type: group
short-summary: Manage inbound NAT address pools of a load balancer.
"""

helps['network lb inbound-nat-pool create'] = """
type: command
short-summary: Create an inbound NAT address pool.
examples:
  - name: Create an inbound NAT address pool.
    text: |
        az network lb inbound-nat-pool create -g MyResourceGroup --lb-name MyLb \\
        -n MyNatPool --protocol Tcp --frontend-port-range-start 80 --frontend-port-range-end 89 \\
        --backend-port 80 --frontend-ip-name MyFrontendIp
"""

helps['network lb inbound-nat-pool delete'] = """
type: command
short-summary: Delete an inbound NAT address pool.
examples:
  - name: Delete an inbound NAT address pool.
    text: az network lb inbound-nat-pool delete -g MyResourceGroup --lb-name MyLb -n MyNatPool
"""

helps['network lb inbound-nat-pool list'] = """
type: command
short-summary: List inbound NAT address pools.
examples:
  - name: List inbound NAT address pools.
    text: az network lb inbound-nat-pool list -g MyResourceGroup --lb-name MyLb -o table
"""

helps['network lb inbound-nat-pool show'] = """
type: command
short-summary: Get the details of an inbound NAT address pool.
examples:
  - name: Get the details of an inbound NAT address pool.
    text: az network lb inbound-nat-pool show -g MyResourceGroup --lb-name MyLb -n MyNatPool
"""

helps['network lb inbound-nat-pool update'] = """
type: command
short-summary: Update an inbound NAT address pool.
examples:
  - name: Update an inbound NAT address pool to a different backend port.
    text: |
        az network lb inbound-nat-pool update -g MyResourceGroup --lb-name MyLb -n MyNatPool \\
            --protocol Tcp --backend-port 8080
  - name: Update an inbound NAT address pool. (autogenerated)
    text: az network lb inbound-nat-pool update --backend-port 8080 --enable-tcp-reset true --frontend-port-range-end 89 --frontend-port-range-start 80 --lb-name MyLb --name MyNatPool --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb inbound-nat-rule'] = """
type: group
short-summary: Manage inbound NAT rules of a load balancer.
"""

helps['network lb inbound-nat-rule create'] = """
type: command
short-summary: Create an inbound NAT rule.
examples:
  - name: Create a basic inbound NAT rule for port 80.
    text: |
        az network lb inbound-nat-rule create -g MyResourceGroup --lb-name MyLb -n MyNatRule \\
            --protocol Tcp --frontend-port 80 --backend-port 80
  - name: Create a basic inbound NAT rule for a specific frontend IP and enable floating IP for NAT Rule.
    text: |
        az network lb inbound-nat-rule create -g MyResourceGroup --lb-name MyLb -n MyNatRule --protocol Tcp \\
            --frontend-port 5432 --backend-port 3389 --frontend-ip-name MyFrontendIp --floating-ip true
"""

helps['network lb inbound-nat-rule delete'] = """
type: command
short-summary: Delete an inbound NAT rule.
examples:
  - name: Delete an inbound NAT rule.
    text: az network lb inbound-nat-rule delete -g MyResourceGroup --lb-name MyLb -n MyNatRule
"""

helps['network lb inbound-nat-rule list'] = """
type: command
short-summary: List inbound NAT rules.
examples:
  - name: List inbound NAT rules.
    text: az network lb inbound-nat-rule list -g MyResourceGroup --lb-name MyLb -o table
"""

helps['network lb inbound-nat-rule show'] = """
type: command
short-summary: Get the details of an inbound NAT rule.
examples:
  - name: Get the details of an inbound NAT rule.
    text: az network lb inbound-nat-rule show -g MyResourceGroup --lb-name MyLb -n MyNatRule
"""

helps['network lb inbound-nat-rule update'] = """
type: command
short-summary: Update an inbound NAT rule.
examples:
  - name: Update an inbound NAT rule to disable floating IP and modify idle timeout duration.
    text: |
        az network lb inbound-nat-rule update -g MyResourceGroup --lb-name MyLb -n MyNatRule \\
            --floating-ip false --idle-timeout 5
  - name: Update an inbound NAT rule. (autogenerated)
    text: az network lb inbound-nat-rule update --backend-port 3389 --frontend-port 5432 --lb-name MyLb --name MyNatRule --protocol Udp --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb list'] = """
type: command
short-summary: List load balancers.
examples:
  - name: List load balancers.
    text: az network lb list -g MyResourceGroup
"""

helps['network lb outbound-rule'] = """
type: group
short-summary: Manage outbound rules of a load balancer.
"""

helps['network lb outbound-rule create'] = """
type: command
short-summary: Create an outbound-rule.
examples:
  - name: Create an outbound-rule. (autogenerated)
    text: az network lb outbound-rule create --address-pool MyAddressPool --frontend-ip-configs myfrontendoutbound --idle-timeout 5 --lb-name MyLb --name MyOutboundRule --outbound-ports 10000 --protocol Udp --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb outbound-rule delete'] = """
type: command
short-summary: Delete an outbound-rule.
examples:
  - name: Delete an outbound-rule. (autogenerated)
    text: az network lb outbound-rule delete --lb-name MyLb --name MyOutboundRule --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb outbound-rule list'] = """
type: command
short-summary: List outbound rules.
examples:
  - name: List outbound rules. (autogenerated)
    text: az network lb outbound-rule list --lb-name MyLb --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb outbound-rule show'] = """
type: command
short-summary: Get the details of an outbound rule.
examples:
  - name: Get the details of an outbound rule. (autogenerated)
    text: az network lb outbound-rule show --lb-name MyLb --name MyOutboundRule --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb outbound-rule update'] = """
type: command
short-summary: Update an outbound-rule.
examples:
  - name: Update an outbound-rule. (autogenerated)
    text: az network lb outbound-rule update --lb-name MyLb --name MyOutboundRule --outbound-ports 10000 --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb probe'] = """
type: group
short-summary: Evaluate probe information and define routing rules.
"""

helps['network lb probe create'] = """
type: command
short-summary: Create a probe.
examples:
  - name: Create a probe on a load balancer over HTTP and port 80.
    text: |
        az network lb probe create -g MyResourceGroup --lb-name MyLb -n MyProbe \\
            --protocol http --port 80 --path /
  - name: Create a probe on a load balancer over TCP on port 443.
    text: |
        az network lb probe create -g MyResourceGroup --lb-name MyLb -n MyProbe \\
            --protocol tcp --port 443
"""

helps['network lb probe delete'] = """
type: command
short-summary: Delete a probe.
examples:
  - name: Delete a probe.
    text: az network lb probe delete -g MyResourceGroup --lb-name MyLb -n MyProbe
"""

helps['network lb probe list'] = """
type: command
short-summary: List probes.
examples:
  - name: List probes.
    text: az network lb probe list -g MyResourceGroup --lb-name MyLb -o table
"""

helps['network lb probe show'] = """
type: command
short-summary: Get the details of a probe.
examples:
  - name: Get the details of a probe.
    text: az network lb probe show -g MyResourceGroup --lb-name MyLb -n MyProbe
"""

helps['network lb probe update'] = """
type: command
short-summary: Update a probe.
examples:
  - name: Update a probe with a different port and interval.
    text: az network lb probe update -g MyResourceGroup --lb-name MyLb -n MyProbe --port 81 --interval 10
"""

helps['network lb rule'] = """
type: group
short-summary: Manage load balancing rules.
"""

helps['network lb rule create'] = """
type: command
short-summary: Create a load balancing rule.
examples:
  - name: >
        Create a load balancing rule that assigns a front-facing IP configuration and port to an address pool and port.
    text: |
        az network lb rule create -g MyResourceGroup --lb-name MyLb -n MyLbRule --protocol Tcp \\
            --frontend-ip-name MyFrontEndIp --frontend-port 80 \\
            --backend-pool-name MyAddressPool --backend-port 80
  - name: >
        Create a load balancing rule that assigns a front-facing IP configuration and port to an address pool and port with the floating ip feature.
    text: |
        az network lb rule create -g MyResourceGroup --lb-name MyLb -n MyLbRule --protocol Tcp \\
            --frontend-ip-name MyFrontEndIp --backend-pool-name MyAddressPool  \\
            --floating-ip true --frontend-port 80 --backend-port 80
  - name: >
        Create an HA ports load balancing rule that assigns a frontend IP and port to use all available backend IPs in a pool on the same port.
    text: |
        az network lb rule create -g MyResourceGroup --lb-name MyLb -n MyHAPortsRule \\
            --protocol All --frontend-port 0 --backend-port 0 --frontend-ip-name MyFrontendIp \\
            --backend-pool-name MyAddressPool
"""

helps['network lb rule delete'] = """
type: command
short-summary: Delete a load balancing rule.
examples:
  - name: Delete a load balancing rule.
    text: az network lb rule delete -g MyResourceGroup --lb-name MyLb -n MyLbRule
"""

helps['network lb rule list'] = """
type: command
short-summary: List load balancing rules.
examples:
  - name: List load balancing rules.
    text: az network lb rule list -g MyResourceGroup --lb-name MyLb -o table
"""

helps['network lb rule show'] = """
type: command
short-summary: Get the details of a load balancing rule.
examples:
  - name: Get the details of a load balancing rule.
    text: az network lb rule show -g MyResourceGroup --lb-name MyLb -n MyLbRule
"""

helps['network lb rule update'] = """
type: command
short-summary: Update a load balancing rule.
examples:
  - name: Update a load balancing rule to change the protocol to UDP.
    text: az network lb rule update -g MyResourceGroup --lb-name MyLb -n MyLbRule --protocol Udp
    examples:
  - name: Update a load balancing rule to support HA ports.
    text: az network lb rule update -g MyResourceGroup --lb-name MyLb -n MyLbRule \\ --protocol All --frontend-port 0 --backend-port 0
  - name: Update a load balancing rule. (autogenerated)
    text: az network lb rule update --disable-outbound-snat true --lb-name MyLb --name MyLbRule --resource-group MyResourceGroup
    crafted: true
"""

helps['network lb show'] = """
type: command
short-summary: Get the details of a load balancer.
examples:
  - name: Get the details of a load balancer.
    text: az network lb show -g MyResourceGroup -n MyLb
"""

helps['network lb update'] = """
type: command
short-summary: Update a load balancer.
long-summary: >
    This command can only be used to update the tags for a load balancer. Name and resource group are immutable and cannot be updated.
examples:
  - name: Update the tags of a load balancer.
    text: az network lb update -g MyResourceGroup -n MyLb --set tags.CostCenter=MyBusinessGroup
"""

helps['network list-usages'] = """
type: command
short-summary: List the number of network resources in a region that are used against a subscription quota.
examples:
  - name: List the provisioned network resources in East US region within a subscription.
    text: az network list-usages --location eastus -o table
"""

helps['network local-gateway'] = """
type: group
short-summary: Manage local gateways.
long-summary: >
    For more information on local gateways, visit: https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-cli#localnet
"""

helps['network local-gateway create'] = """
type: command
short-summary: Create a local VPN gateway.
examples:
  - name: Create a Local Network Gateway to represent your on-premises site.
    text: |
        az network local-gateway create -g MyResourceGroup -n MyLocalGateway \\
            --gateway-ip-address 23.99.221.164 --local-address-prefixes 10.0.0.0/24 20.0.0.0/24
"""

helps['network local-gateway delete'] = """
type: command
short-summary: Delete a local VPN gateway.
long-summary: >
    In order to delete a Local Network Gateway, you must first delete ALL Connection objects in Azure
    that are connected to the Gateway. After deleting the Gateway, proceed to delete other resources now not in use.
    For more information, follow the order of instructions on this page: https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-delete-vnet-gateway-portal
examples:
  - name: Create a Local Network Gateway to represent your on-premises site.
    text: az network local-gateway delete -g MyResourceGroup -n MyLocalGateway
  - name: Delete a local VPN gateway. (autogenerated)
    text: az network local-gateway delete --name MyLocalGateway --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['network local-gateway list'] = """
type: command
short-summary: List all local VPN gateways in a resource group.
examples:
  - name: List all local VPN gateways in a resource group.
    text: az network local-gateway list -g MyResourceGroup
"""

helps['network local-gateway show'] = """
type: command
short-summary: Get the details of a local VPN gateway.
examples:
  - name: Get the details of a local VPN gateway.
    text: az network local-gateway show -g MyResourceGroup -n MyLocalGateway
"""

helps['network local-gateway update'] = """
type: command
short-summary: Update a local VPN gateway.
examples:
  - name: Update a Local Network Gateway provisioned with a 10.0.0.0/24 address prefix with additional prefixes.
    text: |
        az network local-gateway update -g MyResourceGroup -n MyLocalGateway \\
            --local-address-prefixes 10.0.0.0/24 20.0.0.0/24 30.0.0.0/24
  - name: Update a local VPN gateway. (autogenerated)
    text: az network local-gateway update --gateway-ip-address 23.99.221.164 --name MyLocalGateway --resource-group MyResourceGroup
    crafted: true
"""

helps['network local-gateway wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the local gateway is met.
examples:
  - name: Wait for Local Network Gateway to return as created.
    text: |
        az network local-gateway wait -g MyResourceGroup -n MyLocalGateway --created
"""

helps['network nat'] = """
type: group
short-summary: Commands to manage NAT resources.
"""

helps['network nat gateway'] = """
type: group
short-summary: Commands to manage NAT gateways.
"""

helps['network nat gateway create'] = """
type: command
short-summary: Create a NAT gateway.
examples:
  - name: Create a NAT gateway.
    text: az network nat gateway create --resource-group MyResourceGroup --name MyNatGateway --location MyLocation --public-ip-addresses  MyPublicIp --public-ip-prefixes  MyPublicIpPrefix --idle-timeout 4 --zone 2
"""

helps['network nat gateway delete'] = """
type: command
short-summary: Delete a NAT gateway.
examples:
  - name: Delete a NAT gateway.
    text: az network nat gateway delete --resource-group MyResourceGroup --name MyNatGateway
"""

helps['network nat gateway list'] = """
type: command
short-summary: List NAT gateways.
examples:
  - name: List NAT gateways.
    text: az network nat gateway list -g MyResourceGroup
"""

helps['network nat gateway show'] = """
type: command
short-summary: Show details of a NAT gateway.
examples:
  - name: Show details of a NAT gateway.
    text: az network nat gateway show --resource-group MyResourceGroup --name MyNatGateway
  - name: Show NAT gateway using ID.
    text: az network nat gateway show --ids {GatewayId}
"""

helps['network nat gateway update'] = """
type: command
short-summary: Update a NAT gateway.
examples:
  - name: Update a NAT gateway.
    text: az network nat gateway update -g MyResourceGroup --name MyNatGateway --idle-timeout 5
"""

helps['network nat gateway wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the NAT gateway is met.
"""

helps['network nic'] = """
type: group
short-summary: Manage network interfaces.
long-summary: >
    To learn more about network interfaces in Azure visit https://docs.microsoft.com/azure/virtual-network/virtual-network-network-interface
"""

helps['network nic create'] = """
type: command
short-summary: Create a network interface.
examples:
  - name: Create a network interface for a specified subnet on a specified virtual network.
    text: >
        az network nic create -g MyResourceGroup --vnet-name MyVnet --subnet MySubnet -n MyNic
  - name: >
        Create a network interface for a specified subnet on a virtual network which allows
            IP forwarding subject to a network security group.
    text: |
        az network nic create -g MyResourceGroup --vnet-name MyVnet --subnet MySubnet -n MyNic \\
            --ip-forwarding --network-security-group MyNsg
  - name: >
        Create a network interface for a specified subnet on a virtual network with network security group and application security groups.
    text: |
        az network nic create -g MyResourceGroup --vnet-name MyVnet --subnet MySubnet -n MyNic \\
            --network-security-group MyNsg --application-security-groups Web App
"""

helps['network nic delete'] = """
type: command
short-summary: Delete a network interface.
examples:
  - name: Delete a network interface.
    text: >
        az network nic delete -g MyResourceGroup -n MyNic
"""

helps['network nic ip-config'] = """
type: group
short-summary: Manage IP configurations of a network interface.
"""

helps['network nic ip-config address-pool'] = """
type: group
short-summary: Manage address pools in an IP configuration.
"""

helps['network nic ip-config address-pool add'] = """
type: command
short-summary: Add an address pool to an IP configuration.
examples:
  - name: Add an address pool to an IP configuration.
    text: |
        az network nic ip-config address-pool add -g MyResourceGroup --nic-name MyNic \\
            -n MyIpConfig --address-pool MyAddressPool
  - name: Add an address pool to an IP configuration. (autogenerated)
    text: az network nic ip-config address-pool add --address-pool MyAddressPool --ip-config-name MyIpConfig --lb-name MyLb --nic-name MyNic --resource-group MyResourceGroup
    crafted: true
"""

helps['network nic ip-config address-pool remove'] = """
type: command
short-summary: Remove an address pool of an IP configuration.
examples:
  - name: Remove an address pool of an IP configuration.
    text: |
        az network nic ip-config address-pool remove -g MyResourceGroup --nic-name MyNic \\
            -n MyIpConfig --address-pool MyAddressPool
  - name: Remove an address pool of an IP configuration. (autogenerated)
    text: az network nic ip-config address-pool remove --address-pool MyAddressPool --ip-config-name MyIpConfig --lb-name MyLb --nic-name MyNic --resource-group MyResourceGroup
    crafted: true
"""

helps['network nic ip-config create'] = """
type: command
short-summary: Create an IP configuration.
long-summary: >
    You must have the Microsoft.Network/AllowMultipleIpConfigurationsPerNic feature enabled for your subscription.
    Only one configuration may be designated as the primary IP configuration per NIC, using the `--make-primary` flag.
examples:
  - name: Create a primary IP configuration for a NIC.
    text: az network nic ip-config create -g MyResourceGroup -n MyIpConfig --nic-name MyNic --make-primary
  - name: Create an IP configuration. (autogenerated)
    text: az network nic ip-config create --name MyIpConfig --nic-name MyNic --private-ip-address 10.0.0.9 --resource-group MyResourceGroup
    crafted: true
"""

helps['network nic ip-config delete'] = """
type: command
short-summary: Delete an IP configuration.
long-summary: A NIC must have at least one IP configuration.
examples:
  - name: Delete an IP configuration.
    text: az network nic ip-config delete -g MyResourceGroup -n MyIpConfig --nic-name MyNic
"""

helps['network nic ip-config inbound-nat-rule'] = """
type: group
short-summary: Manage inbound NAT rules of an IP configuration.
"""

helps['network nic ip-config inbound-nat-rule add'] = """
type: command
short-summary: Add an inbound NAT rule to an IP configuration.
examples:
  - name: Add an inbound NAT rule to an IP configuration.
    text: |
        az network nic ip-config inbound-nat-rule add -g MyResourceGroup --nic-name MyNic \\
            -n MyIpConfig --inbound-nat-rule MyNatRule
  - name: Add an inbound NAT rule to an IP configuration. (autogenerated)
    text: az network nic ip-config inbound-nat-rule add --inbound-nat-rule MyNatRule --ip-config-name MyIpConfig --lb-name MyLb --nic-name MyNic --resource-group MyResourceGroup
    crafted: true
"""

helps['network nic ip-config inbound-nat-rule remove'] = """
type: command
short-summary: Remove an inbound NAT rule of an IP configuration.
examples:
  - name: Remove an inbound NAT rule of an IP configuration.
    text: |
        az network nic ip-config inbound-nat-rule remove -g MyResourceGroup --nic-name MyNic \\
            -n MyIpConfig --inbound-nat-rule MyNatRule
"""

helps['network nic ip-config list'] = """
type: command
short-summary: List the IP configurations of a NIC.
examples:
  - name: List the IP configurations of a NIC.
    text: az network nic ip-config list -g MyResourceGroup --nic-name MyNic
"""

helps['network nic ip-config show'] = """
type: command
short-summary: Show the details of an IP configuration.
examples:
  - name: Show the details of an IP configuration of a NIC.
    text: az network nic ip-config show -g MyResourceGroup -n MyIpConfig --nic-name MyNic
"""

helps['network nic ip-config update'] = """
type: command
short-summary: Update an IP configuration.
examples:
  - name: Update a NIC to use a new private IP address.
    text: |
        az network nic ip-config update -g MyResourceGroup --nic-name MyNic \\
            -n MyIpConfig --private-ip-address 10.0.0.9
  - name: Make an IP configuration the default for the supplied NIC.
    text: |
        az network nic ip-config update -g MyResourceGroup --nic-name MyNic \\
            -n MyIpConfig --make-primary
  - name: Update an IP configuration. (autogenerated)
    text: az network nic ip-config update --name MyIpConfig --nic-name MyNic --public-ip-address MyAppGatewayPublicIp --resource-group MyResourceGroup
    crafted: true
"""

helps['network nic list'] = """
type: command
short-summary: List network interfaces.
long-summary: >
    To list network interfaces attached to VMs in VM scale sets use 'az vmss nic list' or 'az vmss nic list-vm-nics'.
examples:
  - name: List all NICs by internal DNS suffix.
    text: >
        az network nic list --query "[?dnsSettings.internalDomainNameSuffix=`{dnsSuffix}`]"
"""

helps['network nic list-effective-nsg'] = """
type: command
short-summary: List all effective network security groups applied to a network interface.
long-summary: >
    To learn more about troubleshooting using effective security rules visit https://docs.microsoft.com/azure/virtual-network/virtual-network-nsg-troubleshoot-portal
examples:
  - name: List the effective security groups associated with a NIC.
    text: az network nic list-effective-nsg -g MyResourceGroup -n MyNic
"""

helps['network nic show'] = """
type: command
short-summary: Get the details of a network interface.
examples:
  - name: Get the internal domain name suffix of a NIC.
    text: az network nic show -g MyResourceGroup -n MyNic --query "dnsSettings.internalDomainNameSuffix"
"""

helps['network nic show-effective-route-table'] = """
type: command
short-summary: Show the effective route table applied to a network interface.
long-summary: >
    To learn more about troubleshooting using the effective route tables visit
    https://docs.microsoft.com/azure/virtual-network/virtual-network-routes-troubleshoot-portal#using-effective-routes-to-troubleshoot-vm-traffic-flow
examples:
  - name: Show the effective routes applied to a network interface.
    text: az network nic show-effective-route-table -g MyResourceGroup -n MyNic
"""

helps['network nic update'] = """
type: command
short-summary: Update a network interface.
examples:
  - name: Update a network interface to use a different network security group.
    text: az network nic update -g MyResourceGroup -n MyNic --network-security-group MyNewNsg
  - name: Update a network interface. (autogenerated)
    text: az network nic update --accelerated-networking true --name MyNic --resource-group MyResourceGroup
    crafted: true
"""

helps['network nic wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the network interface is met.
examples:
  - name: Pause CLI until the network interface is created.
    text: az network nic wait -g MyResourceGroup -n MyNic --created
"""

helps['network nsg'] = """
type: group
short-summary: Manage Azure Network Security Groups (NSGs).
long-summary: >
    You can control network traffic to resources in a virtual network using a network security group.
    A network security group contains a list of security rules that allow or deny inbound or
    outbound network traffic based on source or destination IP addresses, Application Security
    Groups, ports, and protocols. For more information visit https://docs.microsoft.com/azure/virtual-network/virtual-networks-create-nsg-arm-cli
"""

helps['network nsg create'] = """
type: command
short-summary: Create a network security group.
examples:
  - name: Create an NSG in a resource group within a region with tags.
    text: az network nsg create -g MyResourceGroup -n MyNsg --tags super_secure no_80 no_22
"""

helps['network nsg delete'] = """
type: command
short-summary: Delete a network security group.
examples:
  - name: Delete an NSG in a resource group.
    text: az network nsg delete -g MyResourceGroup -n MyNsg
"""

helps['network nsg list'] = """
type: command
short-summary: List network security groups.
examples:
  - name: List all NSGs in the 'westus' region.
    text: az network nsg list --query "[?location=='westus']"
"""

helps['network nsg rule'] = """
type: group
short-summary: Manage network security group rules.
"""

helps['network nsg rule create'] = """
type: command
short-summary: Create a network security group rule.
examples:
  - name: Create a basic "Allow" NSG rule with the highest priority.
    text: >
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule --priority 100
  - name: Create a "Deny" rule over TCP for a specific IP address range with the lowest priority.
    text: |
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule --priority 4096 \\
            --source-address-prefixes 208.130.28/24 --source-port-ranges 80 \\
            --destination-address-prefixes '*' --destination-port-ranges 80 8080 --access Deny \\
            --protocol Tcp --description "Deny from specific IP address ranges on 80 and 8080."
  - name: Create a security rule using service tags. For more details visit https://aka.ms/servicetags
    text: |
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRuleWithTags \\
            --priority 400 --source-address-prefixes VirtualNetwork --destination-address-prefixes Storage \\
            --destination-port-ranges * --direction Outbound --access Allow --protocol Tcp --description "Allow VirtualNetwork to Storage."
  - name: Create a security rule using application security groups. https://aka.ms/applicationsecuritygroups
    text: |
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRuleWithAsg \\
            --priority 500 --source-address-prefixes Internet --destination-port-ranges 80 8080 \\
            --destination-asgs Web --access Allow --protocol Tcp --description "Allow Internet to Web ASG on ports 80,8080."
"""

helps['network nsg rule delete'] = """
type: command
short-summary: Delete a network security group rule.
examples:
  - name: Delete a network security group rule.
    text: az network nsg rule delete -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule
"""

helps['network nsg rule list'] = """
type: command
short-summary: List all rules in a network security group.
examples:
  - name: List all rules in a network security group.
    text: az network nsg rule list -g MyResourceGroup --nsg-name MyNsg
"""

helps['network nsg rule show'] = """
type: command
short-summary: Get the details of a network security group rule.
examples:
  - name: Get the details of a network security group rule.
    text: az network nsg rule show -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule
"""

helps['network nsg rule update'] = """
type: command
short-summary: Update a network security group rule.
examples:
  - name: Update an NSG rule with a new wildcard destination address prefix.
    text: az network nsg rule update -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule --destination-address-prefix '*'
  - name: Update a network security group rule. (autogenerated)
    text: az network nsg rule update --name MyNsgRule --nsg-name MyNsg --resource-group MyResourceGroup --source-address-prefixes 208.130.28/24
    crafted: true
"""

helps['network nsg show'] = """
type: command
short-summary: Get information about a network security group.
examples:
  - name: Get basic information about an NSG.
    text: az network nsg show -g MyResourceGroup -n MyNsg
  - name: Get the default security rules of an NSG and format the output as a table.
    text: az network nsg show -g MyResourceGroup -n MyNsg --query "defaultSecurityRules[]" -o table
  - name: Get all default NSG rules with "Allow" access and format the output as a table.
    text: az network nsg show -g MyResourceGroup -n MyNsg --query "defaultSecurityRules[?access=='Allow']" -o table
"""

helps['network nsg update'] = """
type: command
short-summary: Update a network security group.
long-summary: >
    This command can only be used to update the tags of an NSG. Name and resource group are immutable and cannot be updated.
examples:
  - name: Remove a tag of an NSG.
    text: az network nsg update -g MyResourceGroup -n MyNsg --remove tags.no_80
  - name: Update a network security group. (autogenerated)
    text: az network nsg update --name MyNsg --resource-group MyResourceGroup --set tags.CostCenter=MyBusinessGroup
    crafted: true
"""

helps['network private-dns'] = """
type: group
short-summary: Manage Private DNS domains in Azure.
"""

helps['network private-dns link'] = """
type: group
short-summary: Manage Private DNS links.
"""

helps['network private-dns link vnet'] = """
type: group
short-summary: Manage virtual network links to the specified Private DNS zone.
"""

helps['network private-dns link vnet create'] = """
type: command
short-summary: Create a virtual network link to the specified Private DNS zone.
parameters:
  - name: --tags
    short-summary: Resource tags for the virtual network link.
examples:
  - name: Create a virtual network link to the specified Private DNS zone.
    text: |
        az network private-dns link vnet create -g MyResourceGroup -n MyLinkName -z www.mysite.com \\
            -v MyVirtualNetworkId -e False
"""

helps['network private-dns link vnet delete'] = """
type: command
short-summary: Delete a virtual network link to the specified Private DNS zone.
long-summary: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone.
examples:
  - name: Delete a virtual network link to the specified Private DNS zone.
    text: >
        az network private-dns link vnet delete -g MyResourceGroup -z www.mysite.com -n MyLinkName
"""

helps['network private-dns link vnet list'] = """
type: command
short-summary: List the virtual network links to the specified Private DNS zone.
examples:
  - name: List virtual network links to the specified Private DNS zone in a resource group.
    text: >
        az network private-dns link vnet list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns link vnet show'] = """
type: command
short-summary: Get a virtual network link to the specified Private DNS zone.
examples:
  - name: Get a virtual network link to the specified Private DNS zone..
    text: >
        az network private-dns link vnet show -g MyResourceGroup -n MyLinkName -z www.mysite.com
"""

helps['network private-dns link vnet update'] = """
type: command
short-summary: Update a virtual network link's properties. Does not modify virtual network within the link.
parameters:
  - name: --tags
    short-summary: Resource tags for the virtual network link.
examples:
  - name: Update a virtual network link properties to enable registration.
    text: >
        az network private-dns link vnet update -g MyResourceGroup -n MyLinkName -z www.mysite.com -e True
"""

helps['network private-dns link vnet wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the virtual network link to the specified Private DNS zone is met.
examples:
  - name: Pause executing next line of CLI script until the virtual network link to the specified Private DNS zone is successfully provisioned.
    text: az network private-dns link vnet wait -g MyResourceGroup -n MyLinkName -z www.mysite.com --created
"""

helps['network private-dns record-set'] = """
type: group
short-summary: Manage Private DNS records and record sets.
"""

helps['network private-dns record-set a'] = """
type: group
short-summary: Manage Private DNS A records.
"""

helps['network private-dns record-set a add-record'] = """
type: command
short-summary: Add an A record.
examples:
  - name: Add an A record.
    text: |
        az network private-dns record-set a add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv4Address
"""

helps['network private-dns record-set a create'] = """
type: command
short-summary: Create an empty A record set.
examples:
  - name: Create an empty A record set.
    text: az network private-dns record-set a create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set a delete'] = """
type: command
short-summary: Delete an A record set and all associated records.
examples:
  - name: Delete an A record set and all associated records.
    text: az network private-dns record-set a delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set a list'] = """
type: command
short-summary: List all A record sets in a zone.
examples:
  - name: List all A record sets in a zone.
    text: az network private-dns record-set a list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set a remove-record'] = """
type: command
short-summary: Remove an A record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an A record from its record set.
    text: |
        az network private-dns record-set a remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv4Address
"""

helps['network private-dns record-set a show'] = """
type: command
short-summary: Get the details of an A record set.
examples:
  - name: Get the details of an A record set.
    text: az network private-dns record-set a show -g MyResourceGroup -n MyRecordSet -z www.mysite.com
"""

helps['network private-dns record-set a update'] = """
type: command
short-summary: Update an A record set.
examples:
  - name: Update an A record set.
    text: |
        az network private-dns record-set a update -g MyResourceGroup -n MyRecordSet \\
            -z www.mysite.com --metadata owner=WebTeam
"""

helps['network private-dns record-set aaaa'] = """
type: group
short-summary: Manage Private DNS AAAA records.
"""

helps['network private-dns record-set aaaa add-record'] = """
type: command
short-summary: Add an AAAA record.
examples:
  - name: Add an AAAA record.
    text: |
        az network private-dns record-set aaaa add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv6Address
"""

helps['network private-dns record-set aaaa create'] = """
type: command
short-summary: Create an empty AAAA record set.
examples:
  - name: Create an empty AAAA record set.
    text: az network private-dns record-set aaaa create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set aaaa delete'] = """
type: command
short-summary: Delete an AAAA record set and all associated records.
examples:
  - name: Delete an AAAA record set and all associated records.
    text: az network private-dns record-set aaaa delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set aaaa list'] = """
type: command
short-summary: List all AAAA record sets in a zone.
examples:
  - name: List all AAAA record sets in a zone.
    text: az network private-dns record-set aaaa list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set aaaa remove-record'] = """
type: command
short-summary: Remove AAAA record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an AAAA record from its record set.
    text: |
        az network private-dns record-set aaaa remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv6Address
"""

helps['network private-dns record-set aaaa show'] = """
type: command
short-summary: Get the details of an AAAA record set.
examples:
  - name: Get the details of an AAAA record set.
    text: az network private-dns record-set aaaa show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set aaaa update'] = """
type: command
short-summary: Update an AAAA record set.
examples:
  - name: Update an AAAA record set.
    text: |
        az network private-dns record-set aaaa update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set cname'] = """
type: group
short-summary: Manage Private DNS CNAME records.
"""

helps['network private-dns record-set cname create'] = """
type: command
short-summary: Create an empty CNAME record set.
examples:
  - name: Create an empty CNAME record set.
    text: az network private-dns record-set cname create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set cname delete'] = """
type: command
short-summary: Delete a CNAME record set and its associated record.
examples:
  - name: Delete a CNAME record set and its associated record.
    text: az network private-dns record-set cname delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set cname list'] = """
type: command
short-summary: List the CNAME record set in a zone.
examples:
  - name: List the CNAME record set in a zone.
    text: az network private-dns record-set cname list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set cname remove-record'] = """
type: command
short-summary: Remove a CNAME record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a CNAME record from its record set.
    text: |
        az network private-dns record-set cname remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -c www.contoso.com
"""

helps['network private-dns record-set cname set-record'] = """
type: command
short-summary: Set the value of a CNAME record.
examples:
  - name: Set the value of a CNAME record.
    text: |
        az network private-dns record-set cname set-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -c www.contoso.com
"""

helps['network private-dns record-set cname show'] = """
type: command
short-summary: Get the details of a CNAME record set.
examples:
  - name: Get the details of a CNAME record set.
    text: az network private-dns record-set cname show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set cname update'] = """
type: command
short-summary: Update a CNAME record set.
examples:
  - name: Update a CNAME record set.
    text: |
        az network private-dns record-set cname update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set list'] = """
type: command
short-summary: List all record sets within a Private DNS zone.
examples:
  - name: List all "@" record sets within this zone.
    text: |
        az network private-dns record-set list -g MyResourceGroup -z www.mysite.com \\
            --query "[?name=='@']"
"""

helps['network private-dns record-set mx'] = """
type: group
short-summary: Manage Private DNS MX records.
"""

helps['network private-dns record-set mx add-record'] = """
type: command
short-summary: Add an MX record.
examples:
  - name: Add an MX record.
    text: |
        az network private-dns record-set mx add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -e mail.mysite.com -p 10
"""

helps['network private-dns record-set mx create'] = """
type: command
short-summary: Create an empty MX record set.
examples:
  - name: Create an empty MX record set.
    text: az network private-dns record-set mx create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set mx delete'] = """
type: command
short-summary: Delete an MX record set and all associated records.
examples:
  - name: Delete an MX record set and all associated records.
    text: az network private-dns record-set mx delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set mx list'] = """
type: command
short-summary: List all MX record sets in a zone.
examples:
  - name: List all MX record sets in a zone.
    text: az network private-dns record-set mx list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set mx remove-record'] = """
type: command
short-summary: Remove an MX record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an MX record from its record set.
    text: |
        az network private-dns record-set mx remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -e mail.mysite.com -p 10
"""

helps['network private-dns record-set mx show'] = """
type: command
short-summary: Get the details of an MX record set.
examples:
  - name: Get the details of an MX record set.
    text: az network private-dns record-set mx show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set mx update'] = """
type: command
short-summary: Update an MX record set.
examples:
  - name: Update an MX record set.
    text: |
        az network private-dns record-set mx update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set ptr'] = """
type: group
short-summary: Manage Private DNS PTR records.
"""

helps['network private-dns record-set ptr add-record'] = """
type: command
short-summary: Add a PTR record.
examples:
  - name: Add a PTR record.
    text: |
        az network private-dns record-set ptr add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d another.site.com
"""

helps['network private-dns record-set ptr create'] = """
type: command
short-summary: Create an empty PTR record set.
examples:
  - name: Create an empty PTR record set.
    text: az network private-dns record-set ptr create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set ptr delete'] = """
type: command
short-summary: Delete a PTR record set and all associated records.
examples:
  - name: Delete a PTR record set and all associated records.
    text: az network private-dns record-set ptr delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set ptr list'] = """
type: command
short-summary: List all PTR record sets in a zone.
examples:
  - name: List all PTR record sets in a zone.
    text: az network private-dns record-set ptr list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set ptr remove-record'] = """
type: command
short-summary: Remove a PTR record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a PTR record from its record set.
    text: |
        az network private-dns record-set ptr remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d another.site.com
"""

helps['network private-dns record-set ptr show'] = """
type: command
short-summary: Get the details of a PTR record set.
examples:
  - name: Get the details of a PTR record set.
    text: az network private-dns record-set ptr show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set ptr update'] = """
type: command
short-summary: Update a PTR record set.
examples:
  - name: Update a PTR record set.
    text: |
        az network private-dns record-set ptr update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set soa'] = """
type: group
short-summary: Manage Private DNS SOA record.
"""

helps['network private-dns record-set soa show'] = """
type: command
short-summary: Get the details of an SOA record.
examples:
  - name: Get the details of an SOA record.
    text: az network private-dns record-set soa show -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set soa update'] = """
type: command
short-summary: Update properties of an SOA record.
examples:
  - name: Update properties of an SOA record.
    text: |
        az network private-dns record-set soa update -g MyResourceGroup -z www.mysite.com \\
            -e myhostmaster.mysite.com
"""

helps['network private-dns record-set srv'] = """
type: group
short-summary: Manage Private DNS SRV records.
"""

helps['network private-dns record-set srv add-record'] = """
type: command
short-summary: Add an SRV record.
examples:
  - name: Add an SRV record.
    text: |
        az network private-dns record-set srv add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -t webserver.mysite.com -r 8081 -p 10 -w 10
"""

helps['network private-dns record-set srv create'] = """
type: command
short-summary: Create an empty SRV record set.
examples:
  - name: Create an empty SRV record set.
    text: |
        az network private-dns record-set srv create -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet
"""

helps['network private-dns record-set srv delete'] = """
type: command
short-summary: Delete an SRV record set and all associated records.
examples:
  - name: Delete an SRV record set and all associated records.
    text: az network private-dns record-set srv delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set srv list'] = """
type: command
short-summary: List all SRV record sets in a zone.
examples:
  - name: List all SRV record sets in a zone.
    text: az network private-dns record-set srv list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set srv remove-record'] = """
type: command
short-summary: Remove an SRV record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an SRV record from its record set.
    text: |
        az network private-dns record-set srv remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -t webserver.mysite.com -r 8081 -p 10 -w 10
"""

helps['network private-dns record-set srv show'] = """
type: command
short-summary: Get the details of an SRV record set.
examples:
  - name: Get the details of an SRV record set.
    text: az network private-dns record-set srv show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set srv update'] = """
type: command
short-summary: Update an SRV record set.
examples:
  - name: Update an SRV record set.
    text: |
        az network private-dns record-set srv update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set txt'] = """
type: group
short-summary: Manage Private DNS TXT records.
"""

helps['network private-dns record-set txt add-record'] = """
type: command
short-summary: Add a TXT record.
examples:
  - name: Add a TXT record.
    text: |
        az network private-dns record-set txt add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -v Owner=WebTeam
"""

helps['network private-dns record-set txt create'] = """
type: command
short-summary: Create an empty TXT record set.
examples:
  - name: Create an empty TXT record set.
    text: az network private-dns record-set txt create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set txt delete'] = """
type: command
short-summary: Delete a TXT record set and all associated records.
examples:
  - name: Delete a TXT record set and all associated records.
    text: az network private-dns record-set txt delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set txt list'] = """
type: command
short-summary: List all TXT record sets in a zone.
examples:
  - name: List all TXT record sets in a zone.
    text: az network private-dns record-set txt list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set txt remove-record'] = """
type: command
short-summary: Remove a TXT record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a TXT record from its record set.
    text: |
        az network private-dns record-set txt remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -v Owner=WebTeam
"""

helps['network private-dns record-set txt show'] = """
type: command
short-summary: Get the details of a TXT record set.
examples:
  - name: Get the details of a TXT record set.
    text: az network private-dns record-set txt show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set txt update'] = """
type: command
short-summary: Update a TXT record set.
examples:
  - name: Update a TXT record set.
    text: |
        az network private-dns record-set txt update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns zone'] = """
type: group
short-summary: Manage Private DNS zones.
"""

helps['network private-dns zone create'] = """
type: command
short-summary: Create a Private DNS zone.
parameters:
  - name: --tags
    short-summary: Resource tags for the Private DNS zone.
examples:
  - name: Create a Private DNS zone using a fully qualified domain name.
    text: >
        az network private-dns zone create -g MyResourceGroup -n www.mysite.com
"""

helps['network private-dns zone delete'] = """
type: command
short-summary: Delete a Private DNS zone.
long-summary: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed.
examples:
  - name: Delete a Private DNS zone using a fully qualified domain name.
    text: >
        az network private-dns zone delete -g MyResourceGroup -n www.mysite.com
"""

helps['network private-dns zone list'] = """
type: command
short-summary: List Private DNS zones.
examples:
  - name: List Private DNS zones in a resource group.
    text: >
        az network private-dns zone list -g MyResourceGroup
"""

helps['network private-dns zone show'] = """
type: command
short-summary: Get a Private DNS zone.
examples:
  - name: Get a Private DNS zone using a fully qualified domain name.
    text: >
        az network private-dns zone show -g MyResourceGroup -n www.mysite.com
"""

helps['network private-dns zone update'] = """
type: command
short-summary: Update a Private DNS zone's properties. Does not modify Private DNS records or virtual network links within the zone.
parameters:
  - name: --tags
    short-summary: Resource tags for the Private DNS zone.
examples:
  - name: Update a Private DNS zone properties to change the user-defined value of a previously set tag.
    text: >
        az network private-dns zone update -g MyResourceGroup -n www.mysite.com --tags CostCenter=Marketing
"""

helps['network private-dns zone wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the Private DNS zone is met.
examples:
  - name: Pause executing next line of CLI script until the Private DNS zone is successfully provisioned.
    text: az network private-dns zone wait -g MyResourceGroup -n www.mysite.com --created
"""

helps['network private-endpoint'] = """
type: group
short-summary: Manage private endpoints.
"""

helps['network private-endpoint create'] = """
type: command
short-summary: Create a private endpoint.
examples:
  - name: Create a private endpoint.
    text: az network private-endpoint create -g MyResourceGroup -n MyPE --vnet-name MyVnetName --subnet MySubnet --private-connection-resource-id ""/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.Network/privateLinkServices/MyPLS"" --connection-name tttt -l centralus
"""

helps['network private-endpoint delete'] = """
type: command
short-summary: Delete a private endpoint.
"""

helps['network private-endpoint list'] = """
type: command
short-summary: List private endpoints.
"""

helps['network private-endpoint show'] = """
type: command
short-summary: Get the details of a private endpoint.
"""

helps['network private-endpoint update'] = """
type: command
short-summary: Update a private endpoint.
examples:
  - name: Update a private endpoint.
    text: az network private-endpoint update -g MyResourceGroup -n MyPE --request-message "test" --tags mytag=hello
"""

helps['network private-link-service'] = """
type: group
short-summary: Manage private link services.
"""

helps['network private-link-service connection'] = """
type: group
short-summary: Manage private link service endpoint connections.
"""

helps['network private-link-service connection delete'] = """
type: command
short-summary: Delete a private link service endpoint connection.
"""

helps['network private-link-service connection update'] = """
type: command
short-summary: Update a private link service endpoint connection.
long-summary: >
    To update the connection status, the name of the connection should be provided.
    Please obtain this name by running 'az network private-link-service show -g MyResourceGroup -n MyPLSName'.
    The connection name is under the 'privateEndpointConnections' filed.
examples:
  - name: Update the endpoint connections status of private link service
    text: az network private-link-service connection update -g MyResourceGroup -n MyEndpointName.f072a430-2d82-4470-ab30-d23fcfee58d1 --service-name MyPLSName --connection-status Rejected
"""

helps['network private-link-service create'] = """
type: command
short-summary: Create a private link service.
examples:
  - name: Create a private link service
    text: az network private-link-service create -g MyResourceGroup -n MyPLSName --vnet-name MyVnetName --subnet MySubnet --lb-name MyLBName --lb-frontend-ip-configs LoadBalancerFrontEnd -l centralus
"""

helps['network private-link-service delete'] = """
type: command
short-summary: Delete a private link service.
"""

helps['network private-link-service list'] = """
type: command
short-summary: List private link services.
"""

helps['network private-link-service show'] = """
type: command
short-summary: Get the details of a private link service.
"""

helps['network private-link-service update'] = """
type: command
short-summary: Update a private link service.
examples:
  - name: Update a private link service
    text: az network private-link-service update -g MyResourceGroup -n MyPLSName --visibility SubId1 SubId2 --auto-approval SubId1 SubId2
"""

helps['network profile'] = """
type: group
short-summary: Manage network profiles.
long-summary: >
    To create a network profile, see the create command for the relevant resource. Currently,
    only Azure Container Instances are supported.
"""

helps['network profile delete'] = """
type: command
short-summary: Delete a network profile.
"""

helps['network profile list'] = """
type: command
short-summary: List network profiles.
examples:
  - name: List network profiles (autogenerated)
    text: az network profile list --resource-group MyResourceGroup
    crafted: true
"""

helps['network profile show'] = """
type: command
short-summary: Get the details of a network profile.
examples:
  - name: Get the details of a network profile. (autogenerated)
    text: az network profile show --name MyNetworkProfile --resource-group MyResourceGroup
    crafted: true
"""

helps['network public-ip'] = """
type: group
short-summary: Manage public IP addresses.
long-summary: >
    To learn more about public IP addresses visit https://docs.microsoft.com/azure/virtual-network/virtual-network-public-ip-address
"""

helps['network public-ip create'] = """
type: command
short-summary: Create a public IP address.
examples:
  - name: Create a basic public IP resource.
    text: az network public-ip create -g MyResourceGroup -n MyIp
  - name: Create a static public IP resource for a DNS name label.
    text: az network public-ip create -g MyResourceGroup -n MyIp --dns-name MyLabel --allocation-method Static
  - name: Create a public IP resource in an availability zone in the current resource group region.
    text: az network public-ip create -g MyResourceGroup -n MyIp --zone 2
"""

helps['network public-ip delete'] = """
type: command
short-summary: Delete a public IP address.
examples:
  - name: Delete a public IP address.
    text: az network public-ip delete -g MyResourceGroup -n MyIp
"""

helps['network public-ip list'] = """
type: command
short-summary: List public IP addresses.
examples:
  - name: List all public IPs in a subscription.
    text: az network public-ip list
  - name: List all public IPs in a resource group.
    text: az network public-ip list -g MyResourceGroup
  - name: List all public IPs of a domain name label.
    text: az network public-ip list -g MyResourceGroup --query "[?dnsSettings.domainNameLabel=='MyLabel']"
"""

helps['network public-ip prefix'] = """
type: group
short-summary: Manage public IP prefix resources.
"""

helps['network public-ip prefix create'] = """
type: command
short-summary: Create a public IP prefix resource.
examples:
  - name: Create a public IP prefix resource. (autogenerated)
    text: az network public-ip prefix create --length 28 --location westus2 --name MyPublicIPPrefix --resource-group MyResourceGroup
    crafted: true
"""

helps['network public-ip prefix delete'] = """
type: command
short-summary: Delete a public IP prefix resource.
"""

helps['network public-ip prefix list'] = """
type: command
short-summary: List public IP prefix resources.
"""

helps['network public-ip prefix show'] = """
type: command
short-summary: Get the details of a public IP prefix resource.
examples:
  - name: Get the details of a public IP prefix resource. (autogenerated)
    text: az network public-ip prefix show --name MyPublicIPPrefix --resource-group MyResourceGroup
    crafted: true
"""

helps['network public-ip prefix update'] = """
type: command
short-summary: Update a public IP prefix resource.
examples:
  - name: Update a public IP prefix resource. (autogenerated)
    text: az network public-ip prefix update --name MyPublicIPPrefix --resource-group MyResourceGroup
    crafted: true
"""

helps['network public-ip show'] = """
type: command
short-summary: Get the details of a public IP address.
examples:
  - name: Get information about a public IP resource.
    text: az network public-ip show -g MyResourceGroup -n MyIp
  - name: Get the FQDN and IP address of a public IP resource.
    text: >
        az network public-ip show -g MyResourceGroup -n MyIp --query "{fqdn: dnsSettings.fqdn, address: ipAddress}"
"""

helps['network public-ip update'] = """
type: command
short-summary: Update a public IP address.
examples:
  - name: Update a public IP resource with a DNS name label and static allocation.
    text: az network public-ip update -g MyResourceGroup -n MyIp --dns-name MyLabel --allocation-method Static
"""

helps['network route-filter'] = """
type: group
short-summary: Manage route filters.
long-summary: >
    To learn more about route filters with Microsoft peering with ExpressRoute, visit https://docs.microsoft.com/azure/expressroute/how-to-routefilter-cli
"""

helps['network route-filter create'] = """
type: command
short-summary: Create a route filter.
examples:
  - name: Create a route filter.
    text: az network route-filter create -g MyResourceGroup -n MyRouteFilter
"""

helps['network route-filter delete'] = """
type: command
short-summary: Delete a route filter.
examples:
  - name: Delete a route filter.
    text: az network route-filter delete -g MyResourceGroup -n MyRouteFilter
"""

helps['network route-filter list'] = """
type: command
short-summary: List route filters.
examples:
  - name: List route filters in a resource group.
    text: az network route-filter list -g MyResourceGroup
"""

helps['network route-filter rule'] = """
type: group
short-summary: Manage rules in a route filter.
long-summary: >
    To learn more about route filters with Microsoft peering with ExpressRoute, visit https://docs.microsoft.com/azure/expressroute/how-to-routefilter-cli
"""

helps['network route-filter rule create'] = """
type: command
short-summary: Create a rule in a route filter.
parameters:
  - name: --communities
    short-summary: Space-separated list of border gateway protocol (BGP) community values to filter on.
    populator-commands:
      - az network route-filter rule list-service-communities
examples:
  - name: Create a rule in a route filter to allow Dynamics 365.
    text: |
        az network route-filter rule create -g MyResourceGroup --filter-name MyRouteFilter \\
            -n MyRouteFilterRule --communities 12076:5040 --access Allow
"""

helps['network route-filter rule delete'] = """
type: command
short-summary: Delete a rule from a route filter.
examples:
  - name: Delete a rule from a route filter.
    text: az network route-filter rule delete -g MyResourceGroup --filter-name MyRouteFilter -n MyRouteFilterRule
"""

helps['network route-filter rule list'] = """
type: command
short-summary: List rules in a route filter.
examples:
  - name: List rules in a route filter.
    text: az network route-filter rule list -g MyResourceGroup --filter-name MyRouteFilter
"""

helps['network route-filter rule list-service-communities'] = """
type: command
short-summary: Gets all the available BGP service communities.
examples:
  - name: Gets all the available BGP service communities.
    text: az network route-filter rule list-service-communities -o table
  - name: Get the community value for Exchange.
    text: |
        az network route-filter rule list-service-communities \\
            --query '[].bgpCommunities[?communityName==`Exchange`].[communityValue][][]' -o tsv
"""

helps['network route-filter rule show'] = """
type: command
short-summary: Get the details of a rule in a route filter.
examples:
  - name: Get the details of a rule in a route filter.
    text: az network route-filter rule show -g MyResourceGroup --filter-name MyRouteFilter -n MyRouteFilterRule
"""

helps['network route-filter rule update'] = """
type: command
short-summary: Update a rule in a route filter.
examples:
  - name: Update a rule in a route filter to add Exchange to rule list.
    text: |
        az network route-filter rule update -g MyResourceGroup --filter-name MyRouteFilter \\
            -n MyRouteFilterRule --add communities='12076:5010'
"""

helps['network route-filter show'] = """
type: command
short-summary: Get the details of a route filter.
examples:
  - name: Get the details of a route filter.
    text: az network route-filter show -g MyResourceGroup -n MyRouteFilter
  - name: Get the details of a route filter. (autogenerated)
    text: az network route-filter show --expand peerings --name MyRouteFilter --resource-group MyResourceGroup
    crafted: true
"""

helps['network route-filter update'] = """
type: command
short-summary: Update a route filter.
long-summary: >
    This command can only be used to update the tags for a route filter. Name and resource group are immutable and cannot be updated.
examples:
  - name: Update the tags on a route filter.
    text: az network route-filter update -g MyResourceGroup -n MyRouteFilter --set tags.CostCenter=MyBusinessGroup
"""

helps['network route-table'] = """
type: group
short-summary: Manage route tables.
"""

helps['network route-table create'] = """
type: command
short-summary: Create a route table.
examples:
  - name: Create a route table.
    text: az network route-table create -g MyResourceGroup -n MyRouteTable
"""

helps['network route-table delete'] = """
type: command
short-summary: Delete a route table.
examples:
  - name: Delete a route table.
    text: az network route-table delete -g MyResourceGroup -n MyRouteTable
"""

helps['network route-table list'] = """
type: command
short-summary: List route tables.
examples:
  - name: List all route tables in a subscription.
    text: az network route-table list -g MyResourceGroup
"""

helps['network route-table route'] = """
type: group
short-summary: Manage routes in a route table.
"""

helps['network route-table route create'] = """
type: command
short-summary: Create a route in a route table.
examples:
  - name: Create a route that forces all inbound traffic to a Network Virtual Appliance.
    text: |
        az network route-table route create -g MyResourceGroup --route-table-name MyRouteTable -n MyRoute \\
            --next-hop-type VirtualAppliance --address-prefix 10.0.0.0/16 --next-hop-ip-address 10.0.100.4
"""

helps['network route-table route delete'] = """
type: command
short-summary: Delete a route from a route table.
examples:
  - name: Delete a route from a route table.
    text: az network route-table route delete -g MyResourceGroup --route-table-name MyRouteTable -n MyRoute
"""

helps['network route-table route list'] = """
type: command
short-summary: List routes in a route table.
examples:
  - name: List routes in a route table.
    text: az network route-table route list -g MyResourceGroup --route-table-name MyRouteTable
"""

helps['network route-table route show'] = """
type: command
short-summary: Get the details of a route in a route table.
examples:
  - name: Get the details of a route in a route table.
    text: az network route-table route show -g MyResourceGroup --route-table-name MyRouteTable -n MyRoute -o table
"""

helps['network route-table route update'] = """
type: command
short-summary: Update a route in a route table.
examples:
  - name: Update a route in a route table to change the next hop ip address.
    text: az network route-table route update -g MyResourceGroup --route-table-name MyRouteTable \\ -n MyRoute --next-hop-ip-address 10.0.100.5
"""

helps['network route-table show'] = """
type: command
short-summary: Get the details of a route table.
examples:
  - name: Get the details of a route table.
    text: az network route-table show -g MyResourceGroup -n MyRouteTable
"""

helps['network route-table update'] = """
type: command
short-summary: Update a route table.
examples:
  - name: Update a route table to disable BGP route propogation.
    text: az network route-table update -g MyResourceGroup -n MyRouteTable --disable-bgp-route-propagation true
"""

helps['network service-endpoint'] = """
type: group
short-summary: Manage policies related to service endpoints.
"""

helps['network service-endpoint policy'] = """
type: group
short-summary: Manage service endpoint policies.
"""

helps['network service-endpoint policy create'] = """
type: command
short-summary: Create a service endpoint policy.
"""

helps['network service-endpoint policy delete'] = """
type: command
short-summary: Delete a service endpoint policy.
"""

helps['network service-endpoint policy list'] = """
type: command
short-summary: List service endpoint policies.
examples:
  - name: List service endpoint policies. (autogenerated)
    text: az network service-endpoint policy list --resource-group MyResourceGroup
    crafted: true
"""

helps['network service-endpoint policy show'] = """
type: command
short-summary: Get the details of a service endpoint policy.
"""

helps['network service-endpoint policy update'] = """
type: command
short-summary: Update a service endpoint policy.
"""

helps['network service-endpoint policy-definition'] = """
type: group
short-summary: Manage service endpoint policy definitions.
"""

helps['network service-endpoint policy-definition create'] = """
type: command
short-summary: Create a service endpoint policy definition.
parameters:
  - name: --service
    populator-commands:
      - az network service-endpoint list
"""

helps['network service-endpoint policy-definition delete'] = """
type: command
short-summary: Delete a service endpoint policy definition.
"""

helps['network service-endpoint policy-definition list'] = """
type: command
short-summary: List service endpoint policy definitions.
"""

helps['network service-endpoint policy-definition show'] = """
type: command
short-summary: Get the details of a service endpoint policy definition.
"""

helps['network service-endpoint policy-definition update'] = """
type: command
short-summary: Update a service endpoint policy definition.
"""

helps['network traffic-manager'] = """
type: group
short-summary: Manage the routing of incoming traffic.
"""

helps['network traffic-manager endpoint'] = """
type: group
short-summary: Manage Azure Traffic Manager end points.
"""

helps['network traffic-manager endpoint create'] = """
type: command
short-summary: Create a traffic manager endpoint.
parameters:
  - name: --geo-mapping
    populator-commands:
      - az network traffic-manager endpoint show-geographic-hierarchy
examples:
  - name: Create an endpoint for a performance profile to point to an Azure Web App endpoint.
    text: |
        az network traffic-manager endpoint create -g MyResourceGroup --profile-name MyTmProfile \\
            -n MyEndpoint --type azureEndpoints --target-resource-id $MyWebApp1Id --endpoint-status enabled
"""

helps['network traffic-manager endpoint delete'] = """
type: command
short-summary: Delete a traffic manager endpoint.
examples:
  - name: Delete a traffic manager endpoint.
    text: az network traffic-manager endpoint delete -g MyResourceGroup \\ --profile-name MyTmProfile -n MyEndpoint --type azureEndpoints
  - name: Delete a traffic manager endpoint. (autogenerated)
    text: az network traffic-manager endpoint delete --name MyEndpoint --profile-name MyTmProfile --resource-group MyResourceGroup --subscription MySubscription --type azureEndpoints
    crafted: true
"""

helps['network traffic-manager endpoint list'] = """
type: command
short-summary: List traffic manager endpoints.
examples:
  - name: List traffic manager endpoints.
    text: az network traffic-manager endpoint list -g MyResourceGroup --profile-name MyTmProfile
"""

helps['network traffic-manager endpoint show'] = """
type: command
short-summary: Get the details of a traffic manager endpoint.
examples:
  - name: Get the details of a traffic manager endpoint.
    text: |
        az network traffic-manager endpoint show -g MyResourceGroup \\
            --profile-name MyTmProfile -n MyEndpoint --type azureEndpoints
"""

helps['network traffic-manager endpoint show-geographic-hierarchy'] = """
type: command
short-summary: Get the default geographic hierarchy used by the geographic traffic routing method.
examples:
  - name: Get the default geographic hierarchy used by the geographic traffic routing method.
    text: az network traffic-manager endpoint show-geographic-hierarchy
"""

helps['network traffic-manager endpoint update'] = """
type: command
short-summary: Update a traffic manager endpoint.
examples:
  - name: Update a traffic manager endpoint to change its weight.
    text: az network traffic-manager endpoint update -g MyResourceGroup --profile-name MyTmProfile \\ -n MyEndpoint --weight 20 --type azureEndpoints
  - name: Update a traffic manager endpoint. (autogenerated)
    text: az network traffic-manager endpoint update --name MyEndpoint --profile-name MyTmProfile --resource-group MyResourceGroup --target webserver.mysite.com --type azureEndpoints
    crafted: true
"""

helps['network traffic-manager profile'] = """
type: group
short-summary: Manage Azure Traffic Manager profiles.
"""

helps['network traffic-manager profile check-dns'] = """
type: command
short-summary: Check the availability of a relative DNS name.
long-summary: This checks for the avabilility of dns prefixes for trafficmanager.net.
examples:
  - name: Check the availability of 'mywebapp.trafficmanager.net' in Azure.
    text: az network traffic-manager profile check-dns -n mywebapp
"""

helps['network traffic-manager profile create'] = """
type: command
short-summary: Create a traffic manager profile.
examples:
  - name: Create a traffic manager profile with performance routing.
    text: |
        az network traffic-manager profile create -g MyResourceGroup -n MyTmProfile --routing-method Performance \\
            --unique-dns-name mywebapp --ttl 30 --protocol HTTP --port 80 --path "/"
"""

helps['network traffic-manager profile delete'] = """
type: command
short-summary: Delete a traffic manager profile.
examples:
  - name: Delete a traffic manager profile.
    text: az network traffic-manager profile delete -g MyResourceGroup -n MyTmProfile
"""

helps['network traffic-manager profile list'] = """
type: command
short-summary: List traffic manager profiles.
examples:
  - name: List traffic manager profiles.
    text: az network traffic-manager profile list -g MyResourceGroup
"""

helps['network traffic-manager profile show'] = """
type: command
short-summary: Get the details of a traffic manager profile.
examples:
  - name: Get the details of a traffic manager profile.
    text: az network traffic-manager profile show -g MyResourceGroup -n MyTmProfile
"""

helps['network traffic-manager profile update'] = """
type: command
short-summary: Update a traffic manager profile.
examples:
  - name: Update a traffic manager profile to change the TTL to 300.
    text: az network traffic-manager profile update -g MyResourceGroup -n MyTmProfile --ttl 300
"""

helps['network vnet'] = """
type: group
short-summary: Manage Azure Virtual Networks.
long-summary: To learn more about Virtual Networks visit https://docs.microsoft.com/azure/virtual-network/virtual-network-manage-network
"""

helps['network vnet check-ip-address'] = """
type: command
short-summary: Check if a private IP address is available for use within a virtual network.
examples:
  - name: Check whether 10.0.0.4 is available within MyVnet.
    text: az network vnet check-ip-address -g MyResourceGroup -n MyVnet --ip-address 10.0.0.4
"""

helps['network vnet create'] = """
type: command
short-summary: Create a virtual network.
long-summary: >
    You may also create a subnet at the same time by specifying a subnet name and (optionally) an address prefix.
    To learn about how to create a virtual network visit https://docs.microsoft.com/azure/virtual-network/manage-virtual-network#create-a-virtual-network
examples:
  - name: Create a virtual network.
    text: az network vnet create -g MyResourceGroup -n MyVnet
  - name: Create a virtual network with a specific address prefix and one subnet.
    text: |
        az network vnet create -g MyResourceGroup -n MyVnet --address-prefix 10.0.0.0/16 \\
            --subnet-name MySubnet --subnet-prefix 10.0.0.0/24
"""

helps['network vnet delete'] = """
type: command
short-summary: Delete a virtual network.
examples:
  - name: Delete a virtual network.
    text: az network vnet delete -g MyResourceGroup -n myVNet
"""

helps['network vnet list'] = """
type: command
short-summary: List virtual networks.
examples:
  - name: List all virtual networks in a subscription.
    text: az network vnet list
  - name: List all virtual networks in a resource group.
    text: az network vnet list -g MyResourceGroup
  - name: List virtual networks in a subscription which specify a certain address prefix.
    text: az network vnet list --query "[?contains(addressSpace.addressPrefixes, '10.0.0.0/16')]"
"""

helps['network vnet list-endpoint-services'] = """
type: command
short-summary: List which services support VNET service tunneling in a given region.
long-summary: To learn more about service endpoints visit https://docs.microsoft.com/azure/virtual-network/virtual-network-service-endpoints-configure#azure-cli
examples:
  - name: List the endpoint services available for use in the West US region.
    text: az network vnet list-endpoint-services -l westus -o table
"""

helps['network vnet peering'] = """
type: group
short-summary: Manage peering connections between Azure Virtual Networks.
long-summary: To learn more about virtual network peering visit https://docs.microsoft.com/azure/virtual-network/virtual-network-manage-peering
"""

helps['network vnet peering create'] = """
type: command
short-summary: Create a virtual network peering connection.
long-summary: >
    To successfully peer two virtual networks this command must be called twice with
    the values for --vnet-name and --remote-vnet reversed.
examples:
  - name: Create a peering connection between two virtual networks.
    text: |
        az network vnet peering create -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1 \\
            --remote-vnet MyVnet2Id --allow-vnet-access
"""

helps['network vnet peering delete'] = """
type: command
short-summary: Delete a peering.
examples:
  - name: Delete a virtual network peering connection.
    text: az network vnet peering delete -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1
"""

helps['network vnet peering list'] = """
type: command
short-summary: List peerings.
examples:
  - name: List all peerings of a specified virtual network.
    text: az network vnet peering list -g MyResourceGroup --vnet-name MyVnet1
"""

helps['network vnet peering show'] = """
type: command
short-summary: Show details of a peering.
examples:
  - name: Show all details of the specified virtual network peering.
    text: az network vnet peering show -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1
"""

helps['network vnet peering update'] = """
type: command
short-summary: Update a peering.
examples:
  - name: Change forwarded traffic configuration of a virtual network peering.
    text: >
        az network vnet peering update -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1 --set allowForwardedTraffic=true
  - name: Change virtual network access of a virtual network peering.
    text: >
        az network vnet peering update -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1 --set allowVirtualNetworkAccess=true
  - name: Change gateway transit property configuration of a virtual network peering.
    text: >
        az network vnet peering update -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1 --set allowGatewayTransit=true
  - name: Use remote gateways in virtual network peering.
    text: >
        az network vnet peering update -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1 --set useRemoteGateways=true
"""

helps['network vnet show'] = """
type: command
short-summary: Get the details of a virtual network.
examples:
  - name: Get details for MyVNet.
    text: az network vnet show -g MyResourceGroup -n MyVNet
"""

helps['network vnet subnet'] = """
type: group
short-summary: Manage subnets in an Azure Virtual Network.
long-summary: To learn more about subnets visit https://docs.microsoft.com/azure/virtual-network/virtual-network-manage-subnet
"""

helps['network vnet subnet create'] = """
type: command
short-summary: Create a subnet and associate an existing NSG and route table.
parameters:
  - name: --service-endpoints
    short-summary: Space-separated list of services allowed private access to this subnet.
    populator-commands:
      - az network vnet list-endpoint-services
  - name: --nat-gateway
    short-summary: Attach Nat Gateway to subnet
examples:
  - name: Create new subnet attached to an NSG with a custom route table.
    text: |
        az network vnet subnet create -g MyResourceGroup --vnet-name MyVnet -n MySubnet \\
            --address-prefixes 10.0.0.0/24 --network-security-group MyNsg --route-table MyRouteTable
  - name: Create new subnet attached to a NAT gateway.
    text: az network vnet subnet create -n MySubnet --vnet-name MyVnet -g MyResourceGroup --nat-gateway MyNatGateway --address-prefixes "10.0.0.0/21"
"""

helps['network vnet subnet delete'] = """
type: command
short-summary: Delete a subnet.
examples:
  - name: Delete a subnet.
    text: az network vnet subnet delete -g MyResourceGroup -n MySubnet
  - name: Delete a subnet. (autogenerated)
    text: az network vnet subnet delete --name MySubnet --resource-group MyResourceGroup --vnet-name MyVnet
    crafted: true
"""

helps['network vnet subnet list'] = """
type: command
short-summary: List the subnets in a virtual network.
examples:
  - name: List the subnets in a virtual network.
    text: az network vnet subnet list -g MyResourceGroup --vnet-name MyVNet
"""

helps['network vnet subnet list-available-delegations'] = """
type: command
short-summary: List the services available for subnet delegation.
examples:
  - name: Retrieve the service names for available delegations in the West US region.
    text: az network vnet subnet list-available-delegations -l westus --query [].serviceName
  - name: List the services available for subnet delegation. (autogenerated)
    text: az network vnet subnet list-available-delegations --resource-group MyResourceGroup
    crafted: true
"""

helps['network vnet subnet show'] = """
type: command
short-summary: Show details of a subnet.
examples:
  - name: Show the details of a subnet associated with a virtual network.
    text: az network vnet subnet show -g MyResourceGroup -n MySubnet --vnet-name MyVNet
"""

helps['network vnet subnet update'] = """
type: command
short-summary: Update a subnet.
parameters:
  - name: --service-endpoints
    short-summary: Space-separated list of services allowed private access to this subnet.
    populator-commands:
      - az network vnet list-endpoint-services
  - name: --nat-gateway
    short-summary: Attach Nat Gateway to subnet
examples:
  - name: Associate a network security group to a subnet.
    text: az network vnet subnet update -g MyResourceGroup -n MySubnet --vnet-name MyVNet --network-security-group MyNsg
  - name: Update subnet with NAT gateway.
    text: az network vnet subnet update -n MySubnet --vnet-name MyVnet -g MyResourceGroup --nat-gateway MyNatGateway --address-prefixes "10.0.0.0/21"
  - name: Disable the private endpoint network policies
    text: az network vnet subnet update -n MySubnet --vnet-name MyVnet -g MyResourceGroup --disable-private-endpoint-network-policies
"""

helps['network vnet update'] = """
type: command
short-summary: Update a virtual network.
examples:
  - name: Update a virtual network with the IP address of a DNS server.
    text: az network vnet update -g MyResourceGroup -n MyVNet --dns-servers 10.2.0.8
"""

helps['network vnet-gateway'] = """
type: group
short-summary: Use an Azure Virtual Network Gateway to establish secure, cross-premises connectivity.
long-summary: >
    To learn more about Azure Virtual Network Gateways, visit https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-cli
"""

helps['network vnet-gateway create'] = """
type: command
short-summary: Create a virtual network gateway.
examples:
  - name: Create a basic virtual network gateway for site-to-site connectivity.
    text: |
        az network vnet-gateway create -g MyResourceGroup -n MyVnetGateway --public-ip-address MyGatewayIp \\
            --vnet MyVnet --gateway-type Vpn --sku VpnGw1 --vpn-type RouteBased --no-wait
  - name: >
        Create a basic virtual network gateway that provides point-to-site connectivity with a RADIUS secret that matches what is configured on a RADIUS server.
    text: |
        az network vnet-gateway create -g MyResourceGroup -n MyVnetGateway --public-ip-address MyGatewayIp \\
            --vnet MyVnet --gateway-type Vpn --sku VpnGw1 --vpn-type RouteBased --address-prefixes 40.1.0.0/24 \\
            --client-protocol IkeV2 SSTP --radius-secret 111_aaa --radius-server 30.1.1.15
  - name: Create a virtual network gateway. (autogenerated)
    text: az network vnet-gateway create --gateway-type Vpn --location westus2 --name MyVnetGateway --no-wait --public-ip-addresses myVGPublicIPAddress --resource-group MyResourceGroup --sku Basic --vnet MyVnet --vpn-type PolicyBased
    crafted: true
"""

helps['network vnet-gateway delete'] = """
type: command
short-summary: Delete a virtual network gateway.
long-summary: >
    In order to delete a Virtual Network Gateway, you must first delete ALL Connection objects in Azure that are
     connected to the Gateway. After deleting the Gateway, proceed to delete other resources now not in use.
     For more information, follow the order of instructions on this page:
     https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-delete-vnet-gateway-portal
examples:
  - name: Delete a virtual network gateway.
    text: az network vnet-gateway delete -g MyResourceGroup -n MyVnetGateway
"""

helps['network vnet-gateway ipsec-policy'] = """
type: group
short-summary: Manage virtual network gateway IPSec policies.
"""

helps['network vnet-gateway ipsec-policy add'] = """
type: command
short-summary: Add a virtual network gateway IPSec policy.
long-summary: Set all IPsec policies of a virtual network gateway. If you want to set any IPsec policy, you must set them all.
examples:
  - name: Add specified IPsec policies to a gateway instead of relying on defaults.
    text: |
        az network vnet-gateway ipsec-policy add -g MyResourceGroup --gateway-name MyGateway \\
            --dh-group DHGroup14 --ike-encryption AES256 --ike-integrity SHA384 --ipsec-encryption DES3 \\
            --ipsec-integrity GCMAES256 --pfs-group PFS2048 --sa-lifetime 600 --sa-max-size 1024
"""

helps['network vnet-gateway ipsec-policy clear'] = """
type: command
short-summary: Delete all IPsec policies on a virtual network gateway.
examples:
  - name: Remove all previously specified IPsec policies from a gateway.
    text: az network vnet-gateway ipsec-policy clear -g MyResourceGroup --gateway-name MyConnection
"""

helps['network vnet-gateway ipsec-policy list'] = """
type: command
short-summary: List IPSec policies associated with a virtual network gateway.
examples:
  - name: List the IPsec policies set on a gateway.
    text: az network vnet-gateway ipsec-policy list -g MyResourceGroup --gateway-name MyConnection
"""

helps['network vnet-gateway list'] = """
type: command
short-summary: List virtual network gateways.
examples:
  - name: List virtual network gateways in a resource group.
    text: az network vnet-gateway list -g MyResourceGroup
"""

helps['network vnet-gateway list-advertised-routes'] = """
type: command
short-summary: List the routes of a virtual network gateway advertised to the specified peer.
examples:
  - name: List the routes of a virtual network gateway advertised to the specified peer.
    text: az network vnet-gateway list-advertised-routes -g MyResourceGroup -n MyVnetGateway --peer 23.10.10.9
"""

helps['network vnet-gateway list-bgp-peer-status'] = """
type: command
short-summary: Retrieve the status of BGP peers.
examples:
  - name: Retrieve the status of a BGP peer.
    text: az network vnet-gateway list-bgp-peer-status -g MyResourceGroup -n MyVnetGateway --peer 23.10.10.9
"""

helps['network vnet-gateway list-learned-routes'] = """
type: command
short-summary: This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers.
examples:
  - name: Retrieve a list of learned routes.
    text: az network vnet-gateway list-learned-routes -g MyResourceGroup -n MyVnetGateway
"""

helps['network vnet-gateway reset'] = """
type: command
short-summary: Reset a virtual network gateway.
examples:
  - name: Reset a virtual network gateway.
    text: az network vnet-gateway reset -g MyResourceGroup -n MyVnetGateway
  - name: Reset a virtual network gateway with Active-Active feature enabled.
    text: az network vnet-gateway reset -g MyResourceGroup -n MyVnetGateway --gateway-vip MyGatewayIP
"""

helps['network vnet-gateway revoked-cert'] = """
type: group
short-summary: Manage revoked certificates in a virtual network gateway.
long-summary: Prevent machines using this certificate from accessing Azure through this gateway.
"""

helps['network vnet-gateway revoked-cert create'] = """
type: command
short-summary: Revoke a certificate.
examples:
  - name: Revoke a certificate.
    text: |
        az network vnet-gateway revoked-cert create -g MyResourceGroup -n MyRootCertificate \\
            --gateway-name MyVnetGateway --thumbprint abc123
"""

helps['network vnet-gateway revoked-cert delete'] = """
type: command
short-summary: Delete a revoked certificate.
examples:
  - name: Delete a revoked certificate.
    text: az network vnet-gateway revoked-cert delete -g MyResourceGroup -n MyRootCertificate --gateway-name MyVnetGateway
"""

helps['network vnet-gateway root-cert'] = """
type: group
short-summary: Manage root certificates of a virtual network gateway.
"""

helps['network vnet-gateway root-cert create'] = """
type: command
short-summary: Upload a root certificate.
examples:
  - name: Add a Root Certificate to the list of certs allowed to connect to this Gateway.
    text: |
        az network vnet-gateway root-cert create -g MyResourceGroup -n MyRootCertificate \\
            --gateway-name MyVnetGateway --public-cert-data MyCertificateData
"""

helps['network vnet-gateway root-cert delete'] = """
type: command
short-summary: Delete a root certificate.
examples:
  - name: Remove a certificate from the list of Root Certificates whose children are allowed to access this Gateway.
    text: az network vnet-gateway root-cert delete -g MyResourceGroup -n MyRootCertificate --gateway-name MyVnetGateway
  - name: Delete a root certificate. (autogenerated)
    text: az network vnet-gateway root-cert delete --gateway-name MyVnetGateway --name MyRootCertificate --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['network vnet-gateway show'] = """
type: command
short-summary: Get the details of a virtual network gateway.
examples:
  - name: Get the details of a virtual network gateway.
    text: az network vnet-gateway show -g MyResourceGroup -n MyVnetGateway
"""

helps['network vnet-gateway update'] = """
type: command
short-summary: Update a virtual network gateway.
examples:
  - name: Change the SKU of a virtual network gateway.
    text: az network vnet-gateway update -g MyResourceGroup -n MyVnetGateway --sku VpnGw2
  - name: Update a virtual network gateway. (autogenerated)
    text: az network vnet-gateway update --address-prefixes 40.1.0.0/24 --name MyVnetGateway --resource-group MyResourceGroup
    crafted: true
"""

helps['network vnet-gateway vpn-client'] = """
type: group
short-summary: Download a VPN client configuration required to connect to Azure via point-to-site.
"""

helps['network vnet-gateway vpn-client generate'] = """
type: command
short-summary: Generate VPN client configuration.
long-summary: The command outputs a URL to a zip file for the generated VPN client configuration.
examples:
  - name: Create the VPN client configuration for RADIUS with EAP-MSCHAV2 authentication.
    text: az network vnet-gateway vpn-client generate -g MyResourceGroup -n MyVnetGateway --authentication-method EAPMSCHAPv2
  - name: Create the VPN client configuration for AMD64 architecture.
    text: az network vnet-gateway vpn-client generate -g MyResourceGroup -n MyVnetGateway --processor-architecture Amd64
  - name: Generate VPN client configuration. (autogenerated)
    text: az network vnet-gateway vpn-client generate --name MyVnetGateway --processor-architecture Amd64 --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['network vnet-gateway vpn-client show-url'] = """
type: command
short-summary: Retrieve a pre-generated VPN client configuration.
long-summary: The profile needs to be generated first using vpn-client generate command.
examples:
  - name: Get the pre-generated point-to-site VPN client of the virtual network gateway.
    text: az network vnet-gateway vpn-client show-url -g MyResourceGroup -n MyVnetGateway
"""

helps['network vnet-gateway wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the virtual network gateway is met.
examples:
  - name: Pause CLI until the virtual network gateway is created.
    text: az network vnet-gateway wait -g MyResourceGroup -n MyVnetGateway --created
"""

helps['network vpn-connection'] = """
type: group
short-summary: Manage VPN connections.
long-summary: >
    For more information on site-to-site connections,
    visit https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-cli.
    For more information on Vnet-to-Vnet connections, visit https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-howto-vnet-vnet-cli
"""

helps['network vpn-connection create'] = """
type: command
short-summary: Create a VPN connection.
long-summary: The VPN Gateway and Local Network Gateway must be provisioned before creating the connection between them.
parameters:
  - name: --vnet-gateway1
    short-summary: Name or ID of the source virtual network gateway.
  - name: --vnet-gateway2
    short-summary: Name or ID of the destination virtual network gateway to connect to using a 'Vnet2Vnet' connection.
  - name: --local-gateway2
    short-summary: Name or ID of the destination local network gateway to connect to using an 'IPSec' connection.
  - name: --express-route-circuit2
    short-summary: Name or ID of the destination ExpressRoute to connect to using an 'ExpressRoute' connection.
  - name: --authorization-key
    short-summary: The authorization key for the VPN connection.
  - name: --enable-bgp
    short-summary: Enable BGP for this VPN connection.
  - name: --validate
    short-summary: Display and validate the ARM template but do not create any resources.
examples:
  - name: >
        Create a site-to-site connection between an Azure virtual network and an on-premises local network gateway.
    text: >
        az network vpn-connection create -g MyResourceGroup -n MyConnection --vnet-gateway1 MyVnetGateway --local-gateway2 MyLocalGateway --shared-key Abc123
  - name: Create a VPN connection. (autogenerated)
    text: az network vpn-connection create --location westus2 --name MyConnection --resource-group MyResourceGroup --shared-key Abc123 --vnet-gateway1 MyVnetGateway --vnet-gateway2 /subscriptions/{subscriptionID}/resourceGroups/TestBGPRG1/providers/Microsoft.Network/virtualNetworkGateways/VNet1GW
    crafted: true
"""

helps['network vpn-connection delete'] = """
type: command
short-summary: Delete a VPN connection.
examples:
  - name: Delete a VPN connection.
    text: az network vpn-connection delete -g MyResourceGroup -n MyConnection
"""

helps['network vpn-connection ipsec-policy'] = """
type: group
short-summary: Manage VPN connection IPSec policies.
"""

helps['network vpn-connection ipsec-policy add'] = """
type: command
short-summary: Add a VPN connection IPSec policy.
long-summary: Set all IPsec policies of a VPN connection. If you want to set any IPsec policy, you must set them all.
examples:
  - name: Add specified IPsec policies to a connection instead of relying on defaults.
    text: |
        az network vpn-connection ipsec-policy add -g MyResourceGroup --connection-name MyConnection \\
            --dh-group DHGroup14 --ike-encryption AES256 --ike-integrity SHA384 --ipsec-encryption DES3 \\
            --ipsec-integrity GCMAES256 --pfs-group PFS2048 --sa-lifetime 600 --sa-max-size 1024
"""

helps['network vpn-connection ipsec-policy clear'] = """
type: command
short-summary: Delete all IPsec policies on a VPN connection.
examples:
  - name: Remove all previously specified IPsec policies from a connection.
    text: az network vpn-connection ipsec-policy clear -g MyResourceGroup --connection-name MyConnection
"""

helps['network vpn-connection ipsec-policy list'] = """
type: command
short-summary: List IPSec policies associated with a VPN connection.
examples:
  - name: List the IPsec policies set on a connection.
    text: az network vpn-connection ipsec-policy list -g MyResourceGroup --connection-name MyConnection
"""

helps['network vpn-connection list'] = """
type: command
short-summary: List all VPN connections in a resource group.
examples:
  - name: List all VPN connections in a resource group.
    text: az network vpn-connection list -g MyResourceGroup
"""

helps['network vpn-connection shared-key'] = """
type: group
short-summary: Manage VPN shared keys.
"""

helps['network vpn-connection shared-key reset'] = """
type: command
short-summary: Reset a VPN connection shared key.
examples:
  - name: Reset the shared key on a connection.
    text: az network vpn-connection shared-key reset -g MyResourceGroup --connection-name MyConnection --key-length 128
"""

helps['network vpn-connection shared-key show'] = """
type: command
short-summary: Retrieve a VPN connection shared key.
examples:
  - name: View the shared key of a connection.
    text: az network vpn-connection shared-key show -g MyResourceGroup --connection-name MyConnection
  - name: Retrieve a VPN connection shared key. (autogenerated)
    text: az network vpn-connection shared-key show --connection-name MyConnection --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['network vpn-connection shared-key update'] = """
type: command
short-summary: Update a VPN connection shared key.
examples:
  - name: Change the shared key for the connection to "Abc123".
    text: az network vpn-connection shared-key update -g MyResourceGroup --connection-name MyConnection --value Abc123
"""

helps['network vpn-connection show'] = """
type: command
short-summary: Get the details of a VPN connection.
examples:
  - name: View the details of a VPN connection.
    text: az network vpn-connection show -g MyResourceGroup -n MyConnection
"""

helps['network vpn-connection update'] = """
type: command
short-summary: Update a VPN connection.
examples:
  - name: Add BGP to an existing connection.
    text: az network vpn-connection update -g MyResourceGroup -n MyConnection --enable-bgp True
  - name: Update a VPN connection. (autogenerated)
    text: az network vpn-connection update --name MyConnection --resource-group MyResourceGroup --use-policy-based-traffic-selectors true
    crafted: true
"""

helps['network watcher'] = """
type: group
short-summary: Manage the Azure Network Watcher.
long-summary: >
    Network Watcher assists with monitoring and diagnosing conditions at a network scenario level. To learn more visit https://docs.microsoft.com/azure/network-watcher/
"""

helps['network watcher configure'] = """
type: command
short-summary: Configure the Network Watcher service for different regions.
parameters:
  - name: --enabled
    short-summary: Enabled status of Network Watcher in the specified regions.
  - name: --locations -l
    short-summary: Space-separated list of locations to configure.
  - name: --resource-group -g
    short-summary: Name of resource group. Required when enabling new regions.
    long-summary: >
        When a previously disabled region is enabled to use Network Watcher, a
            Network Watcher resource will be created in this resource group.
examples:
  - name: Configure Network Watcher for the West US region.
    text: az network watcher configure -g NetworkWatcherRG  -l westus --enabled true
"""

helps['network watcher connection-monitor'] = """
type: group
short-summary: Manage connection monitoring between an Azure Virtual Machine and any IP resource.
long-summary: >
    Connection monitor can be used to monitor network connectivity between an Azure virtual machine and an IP address.
     The IP address can be assigned to another Azure resource or a resource on the Internet or on-premises. To learn
     more visit https://aka.ms/connectionmonitordoc
"""

helps['network watcher connection-monitor create'] = """
type: command
short-summary: Create a connection monitor.
parameters:
  - name: --source-resource
    short-summary: >
        Currently only Virtual Machines are supported.
  - name: --dest-resource
    short-summary: >
        Currently only Virtual Machines are supported.
examples:
  - name: Create a connection monitor for a virtual machine.
    text: |
        az network watcher connection-monitor create -g MyResourceGroup -n MyConnectionMonitorName \\
            --source-resource MyVM
"""

helps['network watcher connection-monitor delete'] = """
type: command
short-summary: Delete a connection monitor for the given region.
examples:
  - name: Delete a connection monitor for the given region.
    text: az network watcher connection-monitor delete -l westus -n MyConnectionMonitorName
"""

helps['network watcher connection-monitor list'] = """
type: command
short-summary: List connection monitors for the given region.
examples:
  - name: List a connection monitor for the given region.
    text: az network watcher connection-monitor list -l westus
"""

helps['network watcher connection-monitor query'] = """
type: command
short-summary: Query a snapshot of the most recent connection state of a connection monitor.
examples:
  - name: List a connection monitor for the given region.
    text: az network watcher connection-monitor query -l westus -n MyConnectionMonitorName
"""

helps['network watcher connection-monitor show'] = """
type: command
short-summary: Shows a connection monitor by name.
examples:
  - name: Show a connection monitor for the given name.
    text: az network watcher connection-monitor show -l westus -n MyConnectionMonitorName
"""

helps['network watcher connection-monitor start'] = """
type: command
short-summary: Start the specified connection monitor.
examples:
  - name: Start the specified connection monitor.
    text: az network watcher connection-monitor start -l westus -n MyConnectionMonitorName
"""

helps['network watcher connection-monitor stop'] = """
type: command
short-summary: Stop the specified connection monitor.
examples:
  - name: Stop the specified connection monitor.
    text: az network watcher connection-monitor stop -l westus -n MyConnectionMonitorName
"""

helps['network watcher flow-log'] = """
type: group
short-summary: Manage network security group flow logging.
long-summary: >
    For more information about configuring flow logs visit https://docs.microsoft.com/azure/network-watcher/network-watcher-nsg-flow-logging-cli
"""

helps['network watcher flow-log configure'] = """
type: command
short-summary: Configure flow logging on a network security group.
parameters:
  - name: --nsg
    short-summary: Name or ID of the Network Security Group to target.
  - name: --enabled
    short-summary: Enable logging.
  - name: --retention
    short-summary: Number of days to retain logs.
  - name: --storage-account
    short-summary: Name or ID of the storage account in which to save the flow logs.
examples:
  - name: Enable NSG flow logs.
    text: az network watcher flow-log configure -g MyResourceGroup --enabled true --nsg MyNsg --storage-account MyStorageAccount
  - name: Disable NSG flow logs.
    text: az network watcher flow-log configure -g MyResourceGroup --enabled false --nsg MyNsg
"""

helps['network watcher flow-log show'] = """
type: command
short-summary: Get the flow log configuration of a network security group.
examples:
  - name: Show NSG flow logs.
    text: az network watcher flow-log show -g MyResourceGroup --nsg MyNsg
"""

helps['network watcher list'] = """
type: command
short-summary: List Network Watchers.
examples:
  - name: List all Network Watchers in a subscription.
    text: az network watcher list
"""

helps['network watcher packet-capture'] = """
type: group
short-summary: Manage packet capture sessions on VMs.
long-summary: >
    These commands require that both Azure Network Watcher is enabled for the VMs region and that AzureNetworkWatcherExtension is enabled on the VM.
    For more information visit https://docs.microsoft.com/azure/network-watcher/network-watcher-packet-capture-manage-cli
"""

helps['network watcher packet-capture create'] = """
type: command
short-summary: Create and start a packet capture session.
parameters:
  - name: --capture-limit
    short-summary: The maximum size in bytes of the capture output.
  - name: --capture-size
    short-summary: Number of bytes captured per packet. Excess bytes are truncated.
  - name: --time-limit
    short-summary: Maximum duration of the capture session in seconds.
  - name: --storage-account
    short-summary: Name or ID of a storage account to save the packet capture to.
  - name: --storage-path
    short-summary: Fully qualified URI of an existing storage container in which to store the capture file.
    long-summary: >
        If not specified, the container 'network-watcher-logs' will be
        created if it does not exist and the capture file will be stored there.
  - name: --file-path
    short-summary: >
        Local path on the targeted VM at which to save the packet capture. For Linux VMs, the
        path must start with /var/captures.
  - name: --vm
    short-summary: Name or ID of the VM to target.
  - name: --filters
    short-summary: JSON encoded list of packet filters. Use `@{path}` to load from file.
examples:
  - name: Create a packet capture session on a VM.
    text: az network watcher packet-capture create -g MyResourceGroup -n MyPacketCaptureName --vm MyVm --storage-account MyStorageAccount
  - name: Create a packet capture session on a VM with optional filters for protocols, local IP address and remote IP address ranges and ports.
    text: |
        az network watcher packet-capture create -g MyResourceGroup -n MyPacketCaptureName --vm MyVm \\
            --storage-account MyStorageAccount --filters '[ \\
                { \\
                    "protocol":"TCP", \\
                    "remoteIPAddress":"1.1.1.1-255.255.255", \\
                    "localIPAddress":"10.0.0.3", \\
                    "remotePort":"20" \\
                }, \\
                { \\
                    "protocol":"TCP", \\
                    "remoteIPAddress":"1.1.1.1-255.255.255", \\
                    "localIPAddress":"10.0.0.3", \\
                    "remotePort":"80" \\
                }, \\
                { \\
                    "protocol":"TCP", \\
                    "remoteIPAddress":"1.1.1.1-255.255.255", \\
                    "localIPAddress":"10.0.0.3", \\
                    "remotePort":"443" \\
                }, \\
                { \\
                    "protocol":"UDP" \\
                }]'
"""

helps['network watcher packet-capture delete'] = """
type: command
short-summary: Delete a packet capture session.
examples:
  - name: Delete a packet capture session. This only deletes the session and not the capture file.
    text: az network watcher packet-capture delete -n packetCaptureName -l westcentralus
"""

helps['network watcher packet-capture list'] = """
type: command
short-summary: List all packet capture sessions within a resource group.
examples:
  - name: List all packet capture sessions within a region.
    text: az network watcher packet-capture list -l westus
"""

helps['network watcher packet-capture show'] = """
type: command
short-summary: Show details of a packet capture session.
examples:
  - name: Show a packet capture session.
    text: az network watcher packet-capture show -l westus -n MyPacketCapture
"""

helps['network watcher packet-capture show-status'] = """
type: command
short-summary: Show the status of a packet capture session.
examples:
  - name: Show the status of a packet capture session.
    text: az network watcher packet-capture show-status -l westus -n MyPacketCapture
"""

helps['network watcher packet-capture stop'] = """
type: command
short-summary: Stop a running packet capture session.
examples:
  - name: Stop a running packet capture session.
    text: az network watcher packet-capture stop -l westus -n MyPacketCapture
"""

helps['network watcher run-configuration-diagnostic'] = """
type: command
short-summary: Run a configuration diagnostic on a target resource.
long-summary: >
    Requires that Network Watcher is enabled for the region in which the target is located.
examples:
  - name: Run configuration diagnostic on a VM with a single query.
    text: |
        az network watcher run-configuration-diagnostic --resource {VM_ID}
           --direction Inbound --protocol TCP --source 12.11.12.14 --destination 10.1.1.4 --port 12100
  - name: Run configuration diagnostic on a VM with multiple queries.
    text: |
        az network watcher run-configuration-diagnostic --resource {VM_ID}
            --queries '[
            {
                "direction": "Inbound", "protocol": "TCP", "source": "12.11.12.14",
                "destination": "10.1.1.4", "destinationPort": "12100"
            },
            {
                "direction": "Inbound", "protocol": "TCP", "source": "12.11.12.0/32",
                "destination": "10.1.1.4", "destinationPort": "12100"
            },
            {
                "direction": "Outbound", "protocol": "TCP", "source": "12.11.12.14",
                "destination": "10.1.1.4", "destinationPort": "12100"
            }]'
"""

helps['network watcher show-next-hop'] = """
type: command
short-summary: Get information on the 'next hop' of a VM.
long-summary: >
    Requires that Network Watcher is enabled for the region in which the VM is located.
    For more information about show-next-hop visit https://docs.microsoft.com/azure/network-watcher/network-watcher-check-next-hop-cli
examples:
  - name: Get the next hop from a VMs assigned IP address to a destination at 10.1.0.4.
    text: az network watcher show-next-hop -g MyResourceGroup --vm MyVm --source-ip 10.0.0.4 --dest-ip 10.1.0.4
"""

helps['network watcher show-security-group-view'] = """
type: command
short-summary: Get detailed security information on a VM for the currently configured network security group.
long-summary: >
    For more information on using security group view visit https://docs.microsoft.com/azure/network-watcher/network-watcher-security-group-view-cli
examples:
  - name: Get the network security group information for the specified VM.
    text: az network watcher show-security-group-view -g MyResourceGroup --vm MyVm
"""

helps['network watcher show-topology'] = """
type: command
short-summary: Get the network topology of a resource group, virtual network or subnet.
long-summary: For more information about using network topology visit https://docs.microsoft.com/azure/network-watcher/network-watcher-topology-cli
parameters:
  - name: --resource-group -g
    short-summary: The name of the target resource group to perform topology on.
  - name: --location -l
    short-summary: Location. Defaults to the location of the target resource group.
    long-summary: >
        Topology information is only shown for resources within the target
        resource group that are within the specified region.
examples:
  - name: Use show-topology to get the topology of resources within a resource group.
    text: az network watcher show-topology -g MyResourceGroup
"""

helps['network watcher test-connectivity'] = """
type: command
short-summary: Test if a connection can be established between a Virtual Machine and a given endpoint.
long-summary: >
    To check connectivity between two VMs in different regions, use the VM ids instead of the VM names for the source and destination resource arguments.
    To register for this feature or see additional examples visit https://docs.microsoft.com/azure/network-watcher/network-watcher-connectivity-cli
parameters:
  - name: --source-resource
    short-summary: Name or ID of the resource from which to originate traffic.
    long-summary: Currently only Virtual Machines are supported.
  - name: --source-port
    short-summary: Port number from which to originate traffic.
  - name: --dest-resource
    short-summary: Name or ID of the resource to receive traffic.
    long-summary: Currently only Virtual Machines are supported.
  - name: --dest-port
    short-summary: Port number on which to receive traffic.
  - name: --dest-address
    short-summary: The IP address or URI at which to receive traffic.
examples:
  - name: Check connectivity between two virtual machines in the same resource group over port 80.
    text: az network watcher test-connectivity -g MyResourceGroup --source-resource MyVmName1 --dest-resource MyVmName2 --dest-port 80
  - name: Check connectivity between two virtual machines in the same subscription in two different resource groups over port 80.
    text: az network watcher test-connectivity --source-resource MyVmId1 --dest-resource MyVmId2 --dest-port 80
"""

helps['network watcher test-ip-flow'] = """
type: command
short-summary: Test IP flow to/from a VM given the currently configured network security group rules.
long-summary: >
    Requires that Network Watcher is enabled for the region in which the VM is located.
    For more information visit https://docs.microsoft.com/azure/network-watcher/network-watcher-check-ip-flow-verify-cli
parameters:
  - name: --local
    short-summary: >
        The private IPv4 address for the VMs NIC and the port of the packet in
        X.X.X.X:PORT format. `*` can be used for port when direction is outbound.
  - name: --remote
    short-summary: >
        The IPv4 address and port for the remote side of the packet
        X.X.X.X:PORT format. `*` can be used for port when the direction is inbound.
  - name: --direction
    short-summary: Direction of the packet relative to the VM.
  - name: --protocol
    short-summary: Protocol to test.
examples:
  - name: Run test-ip-flow verify to test logical connectivity from a VM to the specified destination IPv4 address and port.
    text: |
        az network watcher test-ip-flow -g MyResourceGroup --direction Outbound \\
            --protocol TCP --local 10.0.0.4:* --remote 10.1.0.4:80 --vm MyVm
"""

helps['network watcher troubleshooting'] = """
type: group
short-summary: Manage Network Watcher troubleshooting sessions.
long-summary: >
    For more information on configuring troubleshooting visit https://docs.microsoft.com/azure/network-watcher/network-watcher-troubleshoot-manage-cli
"""

helps['network watcher troubleshooting show'] = """
type: command
short-summary: Get the results of the last troubleshooting operation.
examples:
  - name: Show the results or status of a troubleshooting operation for a Vnet Gateway.
    text: az network watcher troubleshooting show -g MyResourceGroup --resource MyVnetGateway --resource-type vnetGateway
"""

helps['network watcher troubleshooting start'] = """
type: command
short-summary: Troubleshoot issues with VPN connections or gateway connectivity.
parameters:
  - name: --resource-type -t
    short-summary: The type of target resource to troubleshoot, if resource ID is not specified.
  - name: --storage-account
    short-summary: Name or ID of the storage account in which to store the troubleshooting results.
  - name: --storage-path
    short-summary: Fully qualified URI to the storage blob container in which to store the troubleshooting results.
examples:
  - name: Start a troubleshooting operation on a VPN Connection.
    text: |
        az network watcher troubleshooting start -g MyResourceGroup --resource MyVPNConnection \\
            --resource-type vpnConnection --storage-account MyStorageAccount \\
            --storage-path https://{storageAccountName}.blob.core.windows.net/{containerName}
"""

helps['policy'] = """
type: group
short-summary: Manage resource policies.
"""

helps['policy assignment'] = """
type: group
short-summary: Manage resource policy assignments.
"""

helps['policy assignment create'] = """
type: command
short-summary: Create a resource policy assignment.
parameters:
  - name: --scope
    type: string
    short-summary: Scope to which this policy assignment applies.
examples:
  - name: Create a resource policy assignment at scope
    text: |
        Valid scopes are management group, subscription, resource group, and resource, for example
           management group:  /providers/Microsoft.Management/managementGroups/MyManagementGroup
           subscription:      /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333
           resource group:    /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup
           resource:          /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM
             az policy assignment create --scope '/providers/Microsoft.Management/managementGroups/MyManagementGroup' --policy {PolicyName} -p '{
                 "allowedLocations": {
                     "value": [
                         "australiaeast",
                         "eastus",
                         "japaneast"
                     ]
                 }
             }'
  - name: Create a resource policy assignment and provide rule parameter values.
    text: |
        az policy assignment create --policy {PolicyName} -p '{
            "allowedLocations": {
                "value": [
                    "australiaeast",
                    "eastus",
                    "japaneast"
                ]
            }
        }'
  - name: Create a resource policy assignment with a system assigned identity.
    text: >
        az policy assignment create --name myPolicy --policy {PolicyName} --assign-identity
  - name: Create a resource policy assignment with a system assigned identity. The identity will have 'Contributor' role access to the subscription.
    text: >
        az policy assignment create --name myPolicy --policy {PolicyName} --assign-identity --identity-scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --role Contributor
"""

helps['policy assignment delete'] = """
type: command
short-summary: Delete a resource policy assignment.
examples:
  - name: Delete a resource policy assignment. (autogenerated)
    text: az policy assignment delete --name MyPolicyAssignment
    crafted: true
"""

helps['policy assignment identity'] = """
type: group
short-summary: Manage a policy assignment's managed identity.
"""

helps['policy assignment identity assign'] = """
type: command
short-summary: Add a system assigned identity to a policy assignment.
examples:
  - name: Add a system assigned managed identity to a policy assignment.
    text: >
        az policy assignment identity assign -g MyResourceGroup -n MyPolicyAssignment
  - name: Add a system assigned managed identity to a policy assignment and grant it the 'Contributor' role for the current resource group.
    text: >
        az policy assignment identity assign -g MyResourceGroup -n MyPolicyAssignment --role Contributor --identity-scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/MyResourceGroup
"""

helps['policy assignment identity remove'] = """
type: command
short-summary: Remove a managed identity from a policy assignment.
"""

helps['policy assignment identity show'] = """
type: command
short-summary: Show a policy assignment's managed identity.
"""

helps['policy assignment list'] = """
type: command
short-summary: List resource policy assignments.
"""

helps['policy assignment show'] = """
type: command
short-summary: Show a resource policy assignment.
examples:
  - name: Show a resource policy assignment. (autogenerated)
    text: az policy assignment show --name MyPolicyAssignment
    crafted: true
"""

helps['policy definition'] = """
type: group
short-summary: Manage resource policy definitions.
"""

helps['policy definition create'] = """
type: command
short-summary: Create a policy definition.
parameters:
  - name: --rules
    type: string
    short-summary: Policy rules in JSON format, or a path to a file containing JSON rules.
  - name: --management-group
    type: string
    short-summary: Name of the management group the new policy definition can be assigned in.
  - name: --subscription
    type: string
    short-summary: Name or id of the subscription the new policy definition can be assigned in.
examples:
  - name: Create a read-only policy.
    text: |
        az policy definition create --name readOnlyStorage --rules '{
            "if":
            {
                "field": "type",
                "equals": "Microsoft.Storage/storageAccounts/write"
            },
            "then":
            {
                "effect": "deny"
            }
        }'
  - name: Create a policy parameter definition.
    text: |
        az policy definition create --name allowedLocations --rules '{
            "if": {
                "allOf": [
                    {
                        "field": "location",
                        "notIn": "[parameters('listOfAllowedLocations')]"
                    },
                    {
                        "field": "location",
                        "notEquals": "global"
                    },
                    {
                        "field": "type",
                        "notEquals": "Microsoft.AzureActiveDirectory/b2cDirectories"
                    }
                ]
            },
            "then": {
                "effect": "deny"
            }
        }' \\
        --params '{
            "allowedLocations": {
                "type": "array",
                "metadata": {
                    "description": "The list of locations that can be specified when deploying resources",
                    "strongType": "location",
                    "displayName": "Allowed locations"
                }
            }
        }'
  - name: Create a read-only policy that can be applied within a management group.
    text: |
        az policy definition create -n readOnlyStorage --management-group 'MyManagementGroup' --rules '{
            "if":
            {
                "field": "type",
                "equals": "Microsoft.Storage/storageAccounts/write"
            },
            "then":
            {
                "effect": "deny"
            }
        }'
"""

helps['policy definition delete'] = """
type: command
short-summary: Delete a policy definition.
examples:
  - name: Delete a policy definition. (autogenerated)
    text: az policy definition delete --name MyPolicyDefinition
    crafted: true
"""

helps['policy definition list'] = """
type: command
short-summary: List policy definitions.
"""

helps['policy definition show'] = """
type: command
short-summary: Show a policy definition.
examples:
  - name: Show a policy definition. (autogenerated)
    text: az policy definition show --name MyPolicyDefinition
    crafted: true
"""

helps['policy definition update'] = """
type: command
short-summary: Update a policy definition.
"""

helps['policy event'] = """
type: group
short-summary: Manage policy events.
"""

helps['policy event list'] = """
type: command
short-summary: List policy events.
examples:
  - name: Get policy events at current subscription scope created in the last day.
    text: >
        az policy event list
  - name: Get policy events at management group scope.
    text: >
        az policy event list -m "myMg"
  - name: Get policy events at resource group scope in current subscription.
    text: >
        az policy event list -g "myRg"
  - name: Get policy events for a resource using resource ID.
    text: >
        az policy event list --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup /providers/Microsoft.EventHub/namespaces/myns1/eventhubs/eh1/consumergroups/cg1"
  - name: Get policy events for a resource using resource name.
    text: >
        az policy event list --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup"
  - name: Get policy events for a nested resource using resource name.
    text: >
        az policy event list --resource "myRule1" --namespace "Microsoft.Network" --resource-type "securityRules" --parent "networkSecurityGroups/mysecuritygroup1" -g "myresourcegroup"
  - name: Get policy events for a policy set definition in current subscription.
    text: >
        az policy event list -s "fff58873-fff8-fff5-fffc-fffbe7c9d697"
  - name: Get policy events for a policy definition in current subscription.
    text: >
        az policy event list -d "fff69973-fff8-fff5-fffc-fffbe7c9d698"
  - name: Get policy events for a policy assignment in current subscription.
    text: >
        az policy event list -a "ddd8ef92e3714a5ea3d208c1"
  - name: Get policy events for a policy assignment in the specified resource group in current subscription.
    text: >
        az policy event list -g "myRg" -a "ddd8ef92e3714a5ea3d208c1"
  - name: Get top 5 policy events in current subscription, selecting a subset of properties and customizing ordering.
    text: >
        az policy event list --top 5 --order-by "timestamp desc, policyAssignmentName asc" --select "timestamp, resourceId, policyAssignmentId, policySetDefinitionId, policyDefinitionId"
  - name: Get policy events in current subscription during a custom time interval.
    text: >
        az policy event list --from "2018-03-08T00:00:00Z" --to "2018-03-15T00:00:00Z"
  - name: Get policy events in current subscription filtering results based on some property values.
    text: >
        az policy event list --filter "(policyDefinitionAction eq 'deny' or policyDefinitionAction eq 'audit') and resourceLocation ne 'eastus'"
  - name: Get number of policy events in current subscription.
    text: >
        az policy event list --apply "aggregate($count as numberOfRecords)"
  - name: Get policy events in current subscription aggregating results based on some properties.
    text: >
        az policy event list --apply "groupby((policyAssignmentId, policyDefinitionId, policyDefinitionAction, resourceId), aggregate($count as numEvents))"
  - name: Get policy events in current subscription grouping results based on some properties.
    text: >
        az policy event list --apply "groupby((policyAssignmentName, resourceId))"
  - name: Get policy events in current subscription aggregating results based on some properties specifying multiple groupings.
    text: >
        az policy event list --apply "groupby((policyAssignmentId, policyDefinitionId, resourceId))/groupby((policyAssignmentId, policyDefinitionId), aggregate($count as numResourcesWithEvents))"
"""

helps['policy remediation'] = """
type: group
short-summary: Manage resource policy remediations.
"""

helps['policy remediation cancel'] = """
type: command
short-summary: Cancel a resource policy remediation.
"""

helps['policy remediation create'] = """
type: command
short-summary: Create a resource policy remediation.
examples:
  - name: Create a remediation at resource group scope for a policy assignment
    text: >
        az policy remediation create -g myRg -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab
  - name: Create a remediation at resource group scope for a policy assignment using the policy assignment resource ID
    text: >
        az policy remediation create -g myRg -n myRemediation --policy-assignment "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/providers/Microsoft.Authorization/policyAssignments/myPa"
  - name: Create a remediation at subscription scope for a policy set assignment
    text: >
        az policy remediation create -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab --definition-reference-id auditVMPolicyReference
  - name: Create a remediation at management group scope for specific resource locations
    text: >
        az policy remediation create -m myMg -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab --location-filters eastus westeurope
  - name: Create a remediation for a specific resource using the resource ID
    text: >
        az policy remediation create --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myRg/providers/Microsoft.Compute/virtualMachines/myVm" -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab
"""

helps['policy remediation delete'] = """
type: command
short-summary: Delete a resource policy remediation.
"""

helps['policy remediation deployment'] = """
type: group
short-summary: Manage resource policy remediation deployments.
"""

helps['policy remediation deployment list'] = """
type: command
short-summary: Lists deployments for a resource policy remediation.
"""

helps['policy remediation list'] = """
type: command
short-summary: List resource policy remediations.
"""

helps['policy remediation show'] = """
type: command
short-summary: Show a resource policy remediation.
"""

helps['policy set-definition'] = """
type: group
short-summary: Manage resource policy set definitions.
"""

helps['policy set-definition create'] = """
type: command
short-summary: Create a policy set definition.
parameters:
  - name: --definitions
    type: string
    short-summary: Policy definitions in JSON format, or a path to a file containing JSON rules.
  - name: --management-group
    type: string
    short-summary: Name of management group the new policy set definition can be assigned in.
  - name: --subscription
    type: string
    short-summary: Name or id of the subscription the new policy set definition can be assigned in.
examples:
  - name: Create a policy set definition.
    text: |
        az policy set-definition create -n readOnlyStorage --definitions '[
                {
                    "policyDefinitionId": "/subscriptions/mySubId/providers/Microsoft.Authorization/policyDefinitions/storagePolicy"
                }
            ]'
  - name: Create a policy set definition to be used by a subscription.
    text: |
        az policy set-definition create -n readOnlyStorage --subscription '0b1f6471-1bf0-4dda-aec3-111122223333' --definitions '[
                {
                    "policyDefinitionId": "/subscriptions/mySubId/providers/Microsoft.Authorization/policyDefinitions/storagePolicy"
                }
            ]'
"""

helps['policy set-definition delete'] = """
type: command
short-summary: Delete a policy set definition.
examples:
  - name: Delete a policy set definition. (autogenerated)
    text: az policy set-definition delete --name MyPolicySetDefinition
    crafted: true
"""

helps['policy set-definition list'] = """
type: command
short-summary: List policy set definitions.
"""

helps['policy set-definition show'] = """
type: command
short-summary: Show a policy set definition.
examples:
  - name: Show a policy set definition. (autogenerated)
    text: az policy set-definition show --name MyPolicySetDefinition
    crafted: true
"""

helps['policy set-definition update'] = """
type: command
short-summary: Update a policy set definition.
examples:
  - name: Update a policy set definition. (autogenerated)
    text: |-
        az policy set-definition update --definitions '[
                {
                    "policyDefinitionId": "/subscriptions/mySubId/providers/Microsoft.Authorization/policyDefinitions/storagePolicy"
                }
            ]' --name MyPolicySetDefinition
    crafted: true
"""

helps['policy state'] = """
type: group
short-summary: Manage policy compliance states.
"""

helps['policy state list'] = """
type: command
short-summary: List policy compliance states.
examples:
  - name: Get latest policy states at current subscription scope.
    text: >
        az policy state list
  - name: Get all policy states at current subscription scope.
    text: >
        az policy state list --all
  - name: Get latest policy states at management group scope.
    text: >
        az policy state list -m "myMg"
  - name: Get latest policy states at resource group scope in current subscription.
    text: >
        az policy state list -g "myRg"
  - name: Get latest policy states for a resource using resource ID.
    text: >
        az policy state list --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup /providers/Microsoft.EventHub/namespaces/myns1/eventhubs/eh1/consumergroups/cg1"
  - name: Get latest policy states for a resource using resource name.
    text: >
        az policy state list --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup"
  - name: Get latest policy states for a nested resource using resource name.
    text: >
        az policy state list --resource "myRule1" --namespace "Microsoft.Network" --resource-type "securityRules" --parent "networkSecurityGroups/mysecuritygroup1" -g "myresourcegroup"
  - name: Get latest policy states for a policy set definition in current subscription.
    text: >
        az policy state list -s "fff58873-fff8-fff5-fffc-fffbe7c9d697"
  - name: Get latest policy states for a policy definition in current subscription.
    text: >
        az policy state list -d "fff69973-fff8-fff5-fffc-fffbe7c9d698"
  - name: Get latest policy states for a policy assignment in current subscription.
    text: >
        az policy state list -a "ddd8ef92e3714a5ea3d208c1"
  - name: Get latest policy states for a policy assignment in the specified resource group in current subscription.
    text: >
        az policy state list -g "myRg" -a "ddd8ef92e3714a5ea3d208c1"
  - name: Get top 5 latest policy states in current subscription, selecting a subset of properties and customizing ordering.
    text: >
        az policy state list --top 5 --order-by "timestamp desc, policyAssignmentName asc" --select "timestamp, resourceId, policyAssignmentId, policySetDefinitionId, policyDefinitionId"
  - name: Get latest policy states in current subscription during a custom time interval.
    text: >
        az policy state list --from "2018-03-08T00:00:00Z" --to "2018-03-15T00:00:00Z"
  - name: Get latest policy states in current subscription filtering results based on some property values.
    text: >
        az policy state list --filter "(policyDefinitionAction eq 'deny' or policyDefinitionAction eq 'audit') and resourceLocation ne 'eastus'"
  - name: Get number of latest policy states in current subscription.
    text: >
        az policy state list --apply "aggregate($count as numberOfRecords)"
  - name: Get latest policy states in current subscription aggregating results based on some properties.
    text: >
        az policy state list --apply "groupby((policyAssignmentId, policySetDefinitionId, policyDefinitionReferenceId, policyDefinitionId), aggregate($count as numStates))"
  - name: Get latest policy states in current subscription grouping results based on some properties.
    text: >
        az policy state list --apply "groupby((policyAssignmentName, resourceId))"
  - name: Get latest policy states in current subscription aggregating results based on some properties specifying multiple groupings.
    text: >
        az policy state list --apply "groupby((policyAssignmentId, policySetDefinitionId, policyDefinitionReferenceId, policyDefinitionId, resourceId))/groupby((policyAssignmentId, policySetDefinitionId, policyDefinitionReferenceId, policyDefinitionId), aggregate($count as numNonCompliantResources))"
  - name: Get latest policy states for a resource including policy evaluation details.
    text: >
        az policy state list --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup" --expand PolicyEvaluationDetails
"""

helps['policy state summarize'] = """
type: command
short-summary: Summarize policy compliance states.
examples:
  - name: Get latest non-compliant policy states summary at current subscription scope.
    text: >
        az policy state summarize
  - name: Get latest non-compliant policy states summary at management group scope.
    text: >
        az policy state summarize -m "myMg"
  - name: Get latest non-compliant policy states summary at resource group scope in current subscription.
    text: >
        az policy state summarize -g "myRg"
  - name: Get latest non-compliant policy states summary for a resource using resource ID.
    text: >
        az policy state summarize --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup /providers/Microsoft.EventHub/namespaces/myns1/eventhubs/eh1/consumergroups/cg1"
  - name: Get latest non-compliant policy states summary for a resource using resource name.
    text: >
        az policy state summarize --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup"
  - name: Get latest non-compliant policy states summary for a nested resource using resource name.
    text: >
        az policy state summarize --resource "myRule1" --namespace "Microsoft.Network" --resource-type "securityRules" --parent "networkSecurityGroups/mysecuritygroup1" -g "myresourcegroup"
  - name: Get latest non-compliant policy states summary for a policy set definition in current subscription.
    text: >
        az policy state summarize -s "fff58873-fff8-fff5-fffc-fffbe7c9d697"
  - name: Get latest non-compliant policy states summary for a policy definition in current subscription.
    text: >
        az policy state summarize -d "fff69973-fff8-fff5-fffc-fffbe7c9d698"
  - name: Get latest non-compliant policy states summary for a policy assignment in current subscription.
    text: >
        az policy state summarize -a "ddd8ef92e3714a5ea3d208c1"
  - name: Get latest non-compliant policy states summary for a policy assignment in the specified resource group in current subscription.
    text: >
        az policy state summarize -g "myRg" -a "ddd8ef92e3714a5ea3d208c1"
  - name: Get latest non-compliant policy states summary in current subscription, limiting the assignments summary to top 5.
    text: >
        az policy state summarize --top 5
  - name: Get latest non-compliant policy states summary in current subscription for a custom time interval.
    text: >
        az policy state summarize --from "2018-03-08T00:00:00Z" --to "2018-03-15T00:00:00Z"
  - name: Get latest non-compliant policy states summary in current subscription filtering results based on some property values.
    text: >
        az policy state summarize --filter "(policyDefinitionAction eq 'deny' or policyDefinitionAction eq 'audit') and resourceLocation ne 'eastus'"
"""

helps['postgres'] = """
type: group
short-summary: Manage Azure Database for PostgreSQL servers.
"""

helps['postgres db'] = """
type: group
short-summary: Manage PostgreSQL databases on a server.
"""

helps['postgres db create'] = """
type: command
short-summary: Create a PostgreSQL database.
examples:
  - name: Create database 'testdb' in the server 'testsvr' with the default parameters.
    text: az postgres db create -g testgroup -s testsvr -n testdb
  - name: Create database 'testdb' in server 'testsvr' with a given character set and collation rules.
    text: az postgres db create -g testgroup -s testsvr -n testdb --charset {valid_charset} --collation {valid_collation}
"""

helps['postgres db delete'] = """
type: command
short-summary: Delete a database.
examples:
  - name: Delete database 'testdb' in the server 'testsvr'.
    text: az postgres db delete -g testgroup -s testsvr -n testdb
"""

helps['postgres db list'] = """
type: command
short-summary: List the databases for a server.
examples:
  - name: List databases in the server 'testsvr'.
    text: az postgres db list -g testgroup -s testsvr
"""

helps['postgres db show'] = """
type: command
short-summary: Show the details of a database.
examples:
  - name: Show database 'testdb' in the server 'testsvr'.
    text: az postgres db show -g testgroup -s testsvr -n testdb
"""

helps['postgres server'] = """
type: group
short-summary: Manage PostgreSQL servers.
"""

helps['postgres server configuration'] = """
type: group
short-summary: Manage configuration values for a server.
"""

helps['postgres server configuration list'] = """
type: command
short-summary: List the configuration values for a server.
examples:
  - name: List the configuration values for a server. (autogenerated)
    text: az postgres server configuration list --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['postgres server configuration set'] = """
type: command
short-summary: Update the configuration of a server.
examples:
  - name: Set a new configuration value.
    text: az postgres server configuration set -g testgroup -s testsvr -n {config_name} --value {config_value}
  - name: Set a configuration value to its default.
    text: az postgres server configuration set -g testgroup -s testsvr -n {config_name}
"""

helps['postgres server configuration show'] = """
type: command
short-summary: Get the configuration for a server."
"""

helps['postgres server create'] = """
type: command
short-summary: Create a server.
examples:
  - name: Create a PostgreSQL server in North Europe with sku GP_Gen5_2 (General Purpose, Gen 5 hardware, 2 vCores).
    text: az postgres server create -l northeurope -g testgroup -n testsvr -u username -p password \\ --sku-name GP_Gen5_2
  - name: Create a PostgreSQL server with all paramaters set.
    text: az postgres server create -l northeurope -g testgroup -n testsvr -u username -p password \\ --sku-name B_Gen5_1 --ssl-enforcement Disabled \\ --backup-retention 10 --geo-redundant-backup Enabled --storage-size 51200 --tags "key=value" --version {server-version}
"""

helps['postgres server delete'] = """
type: command
short-summary: Delete a server.
examples:
  - name: Delete a server.
    text: az postgres server delete -g testgroup -n testsvr
"""

helps['postgres server firewall-rule'] = """
type: group
short-summary: Manage firewall rules for a server.
"""

helps['postgres server firewall-rule create'] = """
type: command
short-summary: Create a new firewall rule for a server.
examples:
  - name: Create a firewall rule allowing connections from a specific IP address.
    text: az postgres server firewall-rule create -g testgroup -s testsvr -n allowip --start-ip-address 107.46.14.221 --end-ip-address 107.46.14.221
  - name: Create a firewall rule allowing connections from an IP address range.
    text: az postgres server firewall-rule create -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.0 --end-ip-address 107.46.14.221
"""

helps['postgres server firewall-rule delete'] = """
type: command
short-summary: Delete a firewall rule.
examples:
  - name: Delete a firewall rule. (autogenerated)
    text: az postgres server firewall-rule delete --name MyFirewallRule --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['postgres server firewall-rule list'] = """
type: command
short-summary: List all firewall rules for a server.
examples:
  - name: List all firewall rules for a server. (autogenerated)
    text: az postgres server firewall-rule list --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['postgres server firewall-rule show'] = """
type: command
short-summary: Get the details of a firewall rule.
examples:
  - name: Get the details of a firewall rule. (autogenerated)
    text: az postgres server firewall-rule show --name MyFirewallRule --resource-group MyResourceGroup --server-name MyServer
    crafted: true
"""

helps['postgres server firewall-rule update'] = """
type: command
short-summary: Update a firewall rule.
examples:
  - name: Update a firewall rule's start IP address.
    text: az postgres server firewall-rule update -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.1
  - name: Update a firewall rule's start and end IP address.
    text: az postgres server firewall-rule update -g testgroup -s testsvr -n allowiprange --start-ip-address 107.46.14.2 --end-ip-address 107.46.14.218
"""

helps['postgres server georestore'] = """
type: command
short-summary: Geo-restore a server from backup.
examples:
  - name: Geo-restore 'testsvr' into a new server 'testsvrnew' located in West US 2.
    text: az postgres server georestore -g testgroup -n testsvrnew --source-server testsvr -l westus2
  - name: Geo-restore 'testsvr' into a new server 'testsvrnew' located in West US 2 with sku GP_Gen5_2.
    text: az postgres server georestore -g testgroup -n testsvrnew --source-server testsvr -l westus2 --sku-name GP_Gen5_2
  - name: Geo-restore 'testsvr2' into a new server 'testsvrnew', where 'testsvrnew' is in a different resource group from 'testsvr2'.
    text: |
        az postgres server georestore -g testgroup -n testsvrnew \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforPostgreSQL/servers/testsvr2" \\
            -l westus2
"""

helps['postgres server list'] = """
type: command
short-summary: List available servers.
examples:
  - name: List all PostgreSQL servers in a subscription.
    text: az postgres server list
  - name: List all PostgreSQL servers in a resource group.
    text: az postgres server list -g testgroup
"""

helps['postgres server replica'] = """
type: group
short-summary: Manage read replicas.
"""

helps['postgres server replica create'] = """
type: command
short-summary: Create a read replica for a server.
examples:
  - name: Create a read replica 'testreplsvr' for 'testsvr'.
    text: az postgres server replica create -n testreplsvr -g testgroup -s testsvr
  - name: Create a read replica 'testreplsvr' for 'testsvr2', where 'testreplsvr' is in a different resource group.
    text: |
        az postgres server replica create -n testreplsvr -g testgroup \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforPostgreSQL/servers/testsvr2"
"""

helps['postgres server replica list'] = """
type: command
short-summary: List all read replicas for a given server.
examples:
  - name: List all read replicas for master server 'testsvr'.
    text: az postgres server replica list -g testgroup -s testsvr
"""

helps['postgres server replica stop'] = """
type: command
short-summary: Stop replication to a read replica and make it a read/write server.
examples:
  - name: Stop replication to 'testreplsvr' and make it a read/write server.
    text: az postgres server replica stop -g testgroup -n testreplsvr
"""

helps['postgres server restart'] = """
type: command
short-summary: Restart a server.
examples:
  - name: Restart a server.
    text: az postgres server restart -g testgroup -n testsvr
"""

helps['postgres server restore'] = """
type: command
short-summary: Restore a server from backup.
examples:
  - name: Restore 'testsvr' to a specific point-in-time as a new server 'testsvrnew'.
    text: az postgres server restore -g testgroup -n testsvrnew --source-server testsvr --restore-point-in-time "2017-06-15T13:10:00Z"
  - name: Restore 'testsvr2' to 'testsvrnew', where 'testsvrnew' is in a different resource group from 'testsvr2'.
    text: |
        az postgres server restore -g testgroup -n testsvrnew \\
            -s "/subscriptions/${SubID}/resourceGroups/${ResourceGroup}/providers/Microsoft.DBforPostgreSQL/servers/testsvr2" \\
            --restore-point-in-time "2017-06-15T13:10:00Z"
"""

helps['postgres server show'] = """
type: command
short-summary: Get the details of a server.
examples:
  - name: Get the details of a server. (autogenerated)
    text: az postgres server show --name MyServer --resource-group MyResourceGroup
    crafted: true
"""

helps['postgres server update'] = """
type: command
short-summary: Update a server.
examples:
  - name: Update a server's sku.
    text: az postgres server update -g testgroup -n testsvrnew --sku-name GP_Gen5_4
  - name: Update a server's tags.
    text: az postgres server update -g testgroup -n testsvrnew --tags "k1=v1" "k2=v2"
"""

helps['postgres server vnet-rule'] = """
type: group
short-summary: Manage a server's virtual network rules.
"""

helps['postgres server vnet-rule create'] = """
type: command
short-summary: Create a virtual network rule to allows access to a PostgreSQL server.
examples:
  - name: Create a virtual network rule by providing the subnet id.
    text: az postgres server vnet-rule create -g testgroup -s testsvr -n vnetRuleName --subnet /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/vnetName/subnets/subnetName
  - name: Create a vnet rule by providing the vnet and subnet name. The subnet id is created by taking the resource group name and subscription id of the server.
    text: az postgres server vnet-rule create -g testgroup -s testsvr -n vnetRuleName --subnet subnetName --vnet-name vnetName
"""

helps['postgres server vnet-rule update'] = """
type: command
short-summary: Update a virtual network rule.
"""

helps['postgres server wait'] = """
type: command
short-summary: Wait for server to satisfy certain conditions.
"""

helps['postgres server-logs'] = """
type: group
short-summary: Manage server logs.
"""

helps['postgres server-logs download'] = """
type: command
short-summary: Download log files.
examples:
  - name: Download log files f1 and f2 to the current directory from the server 'testsvr'.
    text: az postgres server-logs download -g testgroup -s testsvr -n f1.log f2.log
"""

helps['postgres server-logs list'] = """
type: command
short-summary: List log files for a server.
examples:
  - name: List log files for 'testsvr' modified in the last 72 hours (default value).
    text: az postgres server-logs list -g testgroup -s testsvr
  - name: List log files for 'testsvr' modified in the last 10 hours.
    text: az postgres server-logs list -g testgroup -s testsvr --file-last-written 10
  - name: List log files for 'testsvr' less than 30Kb in size.
    text: az postgres server-logs list -g testgroup -s testsvr --max-file-size 30
"""

helps['ppg'] = """
type: group
short-summary: Manage Proximity Placement Groups
"""

helps['ppg create'] = """
type: command
short-summary: Create a proximity placement group
examples:
  - name: Create a proximity placement group (autogenerated)
    text: az ppg create --name MyProximityPlacementGroup --resource-group MyResourceGroup
    crafted: true
"""

helps['ppg list'] = """
type: command
short-summary: List proximity placement groups
examples:
  - name: List proximity placement groups (autogenerated)
    text: az ppg list --resource-group MyResourceGroup
    crafted: true
"""

helps['ppg show'] = """
type: command
short-summary: Get a proximity placement group
"""

helps['ppg update'] = """
type: command
short-summary: Update a proximity placement group
"""

helps['provider'] = """
type: group
short-summary: Manage resource providers.
"""

helps['provider list'] = """
type: command
examples:
  - name: Display all resource types for the network resource provider.
    text: >
        az provider list --query [?namespace=='Microsoft.Network'].resourceTypes[].resourceType
"""

helps['provider operation'] = """
type: group
short-summary: Get provider operations metadatas.
"""

helps['provider operation list'] = """
type: command
short-summary: Get operations from all providers.
"""

helps['provider operation show'] = """
type: command
short-summary: Get an individual provider's operations.
examples:
  - name: Get an individual provider's operations. (autogenerated)
    text: az provider operation show --namespace Microsoft.Storage
    crafted: true
"""

helps['provider register'] = """
type: command
short-summary: Register a provider.
examples:
  - name: Register a provider. (autogenerated)
    text: az provider register --namespace 'Microsoft.PolicyInsights'
    crafted: true
"""

helps['provider unregister'] = """
type: command
short-summary: Unregister a provider.
examples:
  - name: Unregister a provider. (autogenerated)
    text: az provider unregister --namespace Microsoft.Automation
    crafted: true
"""

helps['redis'] = """
type: group
short-summary: Manage dedicated Redis caches for your Azure applications.
"""

helps['redis create'] = """
type: command
short-summary: Create new Redis Cache instance.
"""

helps['redis export'] = """
type: command
short-summary: Export data stored in a Redis cache.
"""

helps['redis firewall-rules'] = """
type: group
short-summary: Manage Redis firewall rules.
"""

helps['redis firewall-rules create'] = """
type: command
short-summary: Create a redis cache firewall rule.
long-summary: Usage example - az redis firewall-rules create --name testCacheName --resource-group testResourceGroup  --start-ip 10.10.10.10 --end-ip 20.20.20.20 --rule-name 10to20
"""

helps['redis firewall-rules update'] = """
type: command
short-summary: Update a redis cache firewall rule.
"""

helps['redis import'] = """
type: command
short-summary: Import data into a Redis cache.
"""

helps['redis list'] = """
type: command
short-summary: List Redis Caches.
long-summary: Lists details about all caches within current Subscription or provided Resource Group.
"""

helps['redis patch-schedule'] = """
type: group
short-summary: Manage Redis patch schedules.
"""

helps['redis patch-schedule create'] = """
type: command
short-summary: Create patching schedule for Redis cache.
long-summary: Usage example - az redis patch-schedule create --name testCacheName --resource-group testResourceGroup --schedule-entries '[{"dayOfWeek":"Tuesday","startHourUtc":"00","maintenanceWindow":"PT5H"}]'
"""

helps['redis patch-schedule update'] = """
type: command
short-summary: Update the patching schedule for Redis cache.
long-summary: Usage example - az redis patch-schedule update --name testCacheName --resource-group testResourceGroup --schedule-entries '[{"dayOfWeek":"Tuesday","startHourUtc":"00","maintenanceWindow":"PT5H"}]'
"""

helps['redis server-link'] = """
type: group
short-summary: Manage Redis server links.
"""

helps['redis server-link create'] = """
type: command
short-summary: Adds a server link to the Redis cache (requires Premium SKU).
long-summary: Usage example - az redis server-link create --name testCacheName --resource-group testResourceGroup --cache-to-link secondTestCacheName --replication-role Secondary
"""

helps['redis update'] = """
type: command
short-summary: Update a Redis cache.
long-summary: Scale or update settings of a Redis cache.
"""

helps['relay'] = """
type: group
short-summary: Manage Azure Relay Service namespaces, WCF relays, hybrid connections, and rules
"""

helps['relay hyco'] = """
type: group
short-summary: Manage Azure Relay Service Hybrid Connection and Authorization Rule
"""

helps['relay hyco authorization-rule'] = """
type: group
short-summary: Manage Azure Relay Service Hybrid Connection Authorization Rule
"""

helps['relay hyco authorization-rule create'] = """
type: command
short-summary: Create Authorization Rule for given Relay Service Hybrid Connection
examples:
  - name: Create Authorization Rule for given Relay Service Hybrid Connection
    text: az relay hyco authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --hybrid-connection-name myhyco --name myauthorule --rights Send Listen
"""

helps['relay hyco authorization-rule delete'] = """
type: command
short-summary: Deletes the Authorization Rule of the given Relay Service Hybrid Connection.
examples:
  - name: Deletes the Authorization Rule of Relay Service Hybrid Connection.
    text: az relay hyco authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --hybrid-connection-name myhyco --name myauthorule
"""

helps['relay hyco authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule keys for Relay Service Hybrid Connection
"""

helps['relay hyco authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for Relay Service Hybrid Connection.
examples:
  - name: List the keys and connection strings of Authorization Rule for Relay Service Hybrid Connection.
    text: az relay hyco authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --hybrid-connection-name myhyco --name myauthorule
"""

helps['relay hyco authorization-rule keys renew'] = """
type: command
short-summary: Regenerate keys of Authorization Rule for Relay Service Hybrid Connection.
examples:
  - name: Regenerate key of Relay Service Hybrid Connection.
    text: az relay hyco authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --hybrid-connection-name myhyco --name myauthorule --key PrimaryKey
"""

helps['relay hyco authorization-rule list'] = """
type: command
short-summary: shows list of Authorization Rule by Relay Service Hybrid Connection
examples:
  - name: shows list of Authorization Rule by Relay Service Hybrid Connection
    text: az relay hyco authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --hybrid-connection-name myhyco
"""

helps['relay hyco authorization-rule show'] = """
type: command
short-summary: Shows the details of Authorization Rule for given Relay Service Hybrid Connection
examples:
  - name: Shows the details of Authorization Rule for given Relay Service Hybrid Connection
    text: az relay hyco authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --hybrid-connection-name myhyco --name myauthorule
"""

helps['relay hyco authorization-rule update'] = """
type: command
short-summary: Create Authorization Rule for given Relay Service Hybrid Connection
examples:
  - name: Create Authorization Rule for given Relay Service Hybrid Connection
    text: az relay hyco authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --hybrid-connection-name myhyco --name myauthorule --rights Send
"""

helps['relay hyco create'] = """
type: command
short-summary: Create the Relay Service Hybrid Connection
examples:
  - name: Create a new Relay Service Hybrid Connection
    text: az relay hyco create --resource-group myresourcegroup --namespace-name mynamespace --name myhyco
"""

helps['relay hyco delete'] = """
type: command
short-summary: Deletes the Relay Service Hybrid Connection
examples:
  - name: Deletes the Relay Service Hybrid Connection
    text: az relay hyco delete --resource-group myresourcegroup --namespace-name mynamespace --name myhyco
"""

helps['relay hyco list'] = """
type: command
short-summary: List the Hybrid Connection by Relay Service Namepsace
examples:
  - name: Get the Hybrid Connections by Namespace.
    text: az relay hyco list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['relay hyco show'] = """
type: command
short-summary: Shows the Relay Service Hybrid Connection Details
examples:
  - name: Shows the Hybrid Connection details.
    text: az relay hyco show --resource-group myresourcegroup --namespace-name mynamespace --name myhyco
"""

helps['relay hyco update'] = """
type: command
short-summary: Updates the Relay Service Hybrid Connection
examples:
  - name: Updates existing Relay Service Hybrid Connection.
    text: az relay hyco update --resource-group myresourcegroup --namespace-name mynamespace --name myhyco
"""

helps['relay namespace'] = """
type: group
short-summary: Manage Azure Relay Service Namespace
"""

helps['relay namespace authorization-rule'] = """
type: group
short-summary: Manage Azure Relay Service Namespace Authorization Rule
"""

helps['relay namespace authorization-rule create'] = """
type: command
short-summary: Create Authorization Rule for the given Relay Service Namespace
examples:
  - name: Create Authorization Rule 'myrule' for the given Relay Service Namespace 'mynamespace' in resourcegroup
    text: az relay namespace authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send Listen
"""

helps['relay namespace authorization-rule delete'] = """
type: command
short-summary: Deletes the Authorization Rule of the Relay Service Namespace.
examples:
  - name: Deletes the Authorization Rule of the Relay Service Namespace.
    text: az relay namespace authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['relay namespace authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule connection strings for Namespace
"""

helps['relay namespace authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for Relay Service Namespace
examples:
  - name: List the keys and connection strings of Authorization Rule for Relay Service Namespace
    text: az relay namespace authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['relay namespace authorization-rule keys renew'] = """
type: command
short-summary: Regenerate keys of Authorization Rule for the Relay Service Namespace.
examples:
  - name: Regenerate keys of Authorization Rule for the Relay Service Namespace.
    text: az relay namespace authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --key PrimaryKey
"""

helps['relay namespace authorization-rule list'] = """
type: command
short-summary: Shows the list of Authorization Rule by Relay Service Namespace
examples:
  - name: Shows the list of Authorization Rule by Relay Service Namespace
    text: az relay namespace authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['relay namespace authorization-rule show'] = """
type: command
short-summary: Shows the details of Relay Service Namespace Authorization Rule
examples:
  - name: Shows the details of Relay Service Namespace Authorization Rule
    text: az relay namespace authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['relay namespace authorization-rule update'] = """
type: command
short-summary: Updates Authorization Rule for the given Relay Service Namespace
examples:
  - name: Updates Authorization Rule 'myrule' for the given Relay Service Namespace 'mynamespace' in resourcegroup
    text: az relay namespace authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send
"""

helps['relay namespace create'] = """
type: command
short-summary: Create a Relay Service Namespace
examples:
  - name: Create a Relay Service Namespace.
    text: az relay namespace create --resource-group myresourcegroup --name mynamespace --location westus --tags tag1=value1 tag2=value2
"""

helps['relay namespace delete'] = """
type: command
short-summary: Deletes the Relay Service Namespace
examples:
  - name: Deletes the Relay Service Namespace
    text: az relay namespace delete --resource-group myresourcegroup --name mynamespace
"""

helps['relay namespace exists'] = """
type: command
short-summary: check for the availability of the given name for the Namespace
examples:
  - name: check for the availability of mynamespace for the Namespace
    text: az relay namespace exists --name mynamespace
"""

helps['relay namespace list'] = """
type: command
short-summary: List the Relay Service Namespaces
examples:
  - name: Get the Relay Service Namespaces by resource group
    text: az relay namespace list --resource-group myresourcegroup
  - name: Get the Relay Service Namespaces by Subscription.
    text: az relay namespace list
"""

helps['relay namespace show'] = """
type: command
short-summary: Shows the Relay Service Namespace details
examples:
  - name: shows the Namespace details.
    text: az relay namespace show --resource-group myresourcegroup --name mynamespace
"""

helps['relay namespace update'] = """
type: command
short-summary: Updates a Relay Service Namespace
examples:
  - name: Updates a Relay Service Namespace.
    text: az relay namespace update --resource-group myresourcegroup --name mynamespace --tags tag=value
"""

helps['relay wcfrelay'] = """
type: group
short-summary: Manage Azure Relay Service WCF Relay and Authorization Rule
"""

helps['relay wcfrelay authorization-rule'] = """
type: group
short-summary: Manage Azure Relay Service WCF Relay Authorization Rule
"""

helps['relay wcfrelay authorization-rule create'] = """
type: command
short-summary: Create Authorization Rule for the given Relay Service WCF Relay.
examples:
  - name: Create Authorization Rule for WCF Relay
    text: az relay wcfrelay authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --relay-name myrelay --name myauthorule --rights Listen
"""

helps['relay wcfrelay authorization-rule delete'] = """
type: command
short-summary: Delete the Authorization Rule of Relay Service WCF Relay
examples:
  - name: Delete the Authorization Rule of Relay Service WCF Relay
    text: az relay wcfrelay authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --relay-name myrelay --name myauthorule
"""

helps['relay wcfrelay authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule keys for Relay Service WCF Relay
"""

helps['relay wcfrelay authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for the given Relay Service WCF Relay
examples:
  - name: List the keys and connection strings of Authorization Rule for the given Relay Service WCF Relay
    text: az relay wcfrelay authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --relay-name myrelay --name myauthorule
"""

helps['relay wcfrelay authorization-rule keys renew'] = """
type: command
short-summary: Regenerate keys of Authorization Rule for Relay Service WCF Relay
examples:
  - name: Regenerate keys of Authorization Rule for Relay Service WCF Relay
    text: az relay wcfrelay authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --relay-name myrelay --name myauthorule --key PrimaryKey
"""

helps['relay wcfrelay authorization-rule list'] = """
type: command
short-summary: List of Authorization Rule by Relay Service WCF Relay.
examples:
  - name: List of Authorization Rule by WCF Relay
    text: az relay wcfrelay authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --relay-name myrelay
"""

helps['relay wcfrelay authorization-rule show'] = """
type: command
short-summary: show properties of Authorization Rule for the given Relay Service WCF Relay.
examples:
  - name: show properties of Authorization Rule
    text: az relay wcfrelay authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --relay-name myrelay --name myauthorule
"""

helps['relay wcfrelay authorization-rule update'] = """
type: command
short-summary: Update Authorization Rule for the given Relay Service WCF Relay.
examples:
  - name: Update Authorization Rule for WCF Relay
    text: az relay wcfrelay authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --relay-name myrelay --name myauthorule --rights Send
"""

helps['relay wcfrelay create'] = """
type: command
short-summary: Create the Relay Service WCF Relay
examples:
  - name: Create Relay Service WCF Relay.
    text: az relay wcfrelay create --resource-group myresourcegroup --namespace-name mynamespace --name myrelay --relay-type NetTcp
"""

helps['relay wcfrelay delete'] = """
type: command
short-summary: Deletes the Relay Service WCF Relay
examples:
  - name: Deletes the wcfrelay
    text: az relay wcfrelay delete --resource-group myresourcegroup --namespace-name mynamespace --name myrelay
"""

helps['relay wcfrelay list'] = """
type: command
short-summary: List the WCF Relay by Relay Service Namepsace
examples:
  - name: Get the WCF Relays by Relay Service Namespace.
    text: az relay wcfrelay list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['relay wcfrelay show'] = """
type: command
short-summary: shows the Relay Service WCF Relay Details
examples:
  - name: Shows the Relay Service WCF Relay Details
    text: az relay wcfrelay show --resource-group myresourcegroup --namespace-name mynamespace --name myrelay
"""

helps['relay wcfrelay update'] = """
type: command
short-summary: Updates existing Relay Service WCF Relay
examples:
  - name: Updates Relay Service WCF Relay.
    text: az relay wcfrelay update --resource-group myresourcegroup --namespace-name mynamespace --name myrelay
"""

helps['reservations'] = """
type: group
short-summary: Manage Azure Reservations.
"""

helps['reservations catalog'] = """
type: group
short-summary: See catalog of available reservations
"""

helps['reservations catalog show'] = """
type: command
short-summary: Get catalog of available reservation.
long-summary: |
    Get the regions and skus that are available for RI purchase for the specified Azure subscription.
parameters:
  - name: --subscription-id
    type: string
    short-summary: Id of the subscription to get the catalog for
  - name: --reserved-resource-type
    type: string
    short-summary: Type of the resource for which the skus should be provided.
"""

helps['reservations reservation'] = """
type: group
short-summary: Manage reservation entities
"""

helps['reservations reservation list'] = """
type: command
short-summary: Get all reservations.
long-summary: |
    List all reservations within a reservation order.
parameters:
  - name: --reservation-order-id
    type: string
    short-summary: Id of container reservation order
"""

helps['reservations reservation list-history'] = """
type: command
short-summary: Get history of a reservation.
parameters:
  - name: --reservation-order-id
    type: string
    short-summary: Order id of the reservation
  - name: --reservation-id
    type: string
    short-summary: Reservation id of the reservation
"""

helps['reservations reservation merge'] = """
type: command
short-summary: Merge two reservations.
parameters:
  - name: --reservation-order-id
    type: string
    short-summary: Reservation order id of the reservations to merge
  - name: --reservation-id-1 -1
    type: string
    short-summary: Id of the first reservation to merge
  - name: --reservation-id-2 -2
    type: string
    short-summary: Id of the second reservation to merge
"""

helps['reservations reservation show'] = """
type: command
short-summary: Get details of a reservation.
parameters:
  - name: --reservation-order-id
    type: string
    short-summary: Order id of reservation to look up
  - name: --reservation-id
    type: string
    short-summary: Reservation id of reservation to look up
"""

helps['reservations reservation split'] = """
type: command
short-summary: Split a reservation.
parameters:
  - name: --reservation-order-id
    type: string
    short-summary: Reservation order id of the reservation to split
  - name: --reservation-id
    type: string
    short-summary: Reservation id of the reservation to split
  - name: --quantity-1 -1
    type: int
    short-summary: Quantity of the first reservation that will be created from split operation
  - name: --quantity-2 -2
    type: int
    short-summary: Quantity of the second reservation that will be created from split operation
"""

helps['reservations reservation update'] = """
type: command
short-summary: Updates the applied scopes of the reservation.
parameters:
  - name: --reservation-order-id
    type: string
    short-summary: Reservation order id of the reservation to update
  - name: --reservation-id
    type: string
    short-summary: Id of the reservation to update
  - name: --applied-scope-type -t
    type: string
    short-summary: Type of the Applied Scope to update the reservation with
  - name: --applied-scopes -s
    type: string
    short-summary: Subscription that the benefit will be applied. Do not specify if AppliedScopeType is Shared.
  - name: --instance-flexibility -i
    type: string
    short-summary: Type of the Instance Flexibility to update the reservation with
"""

helps['reservations reservation-order'] = """
type: group
short-summary: Manage reservation order, which is container for reservations
"""

helps['reservations reservation-order list'] = """
type: command
short-summary: Get all reservation orders
long-summary: |
    List of all the reservation orders that the user has access to in the current tenant.
"""

helps['reservations reservation-order show'] = """
type: command
short-summary: Get a specific reservation order.
long-summary: Get the details of the reservation order.
parameters:
  - name: --reservation-order-id
    type: string
    short-summary: Id of reservation order to look up
"""

helps['reservations reservation-order-id'] = """
type: group
short-summary: See reservation order ids that are applied to subscription
"""

helps['reservations reservation-order-id list'] = """
type: command
short-summary: Get list of applicable reservation order ids.
long-summary: |
    Get applicable reservations that are applied to this subscription.
parameters:
  - name: --subscription-id
    type: string
    short-summary: Id of the subscription to look up applied reservations
"""

helps['resource'] = """
type: group
short-summary: Manage Azure resources.
"""

helps['resource create'] = """
type: command
short-summary: create a resource.
examples:
  - name: Create an API app by providing a full JSON configuration.
    text: |
        az resource create -g myRG -n myApiApp --resource-type Microsoft.web/sites --is-full-object --properties '{
                    "kind": "api",
                    "location": "West US",
                    "properties": {
                        "serverFarmId": "/subscriptions/{SubID}/resourcegroups/{ResourceGroup}/providers/Microsoft.Web/serverfarms/{ServicePlan}"
                    }
                }'
  - name: Create a resource by loading JSON configuration from a file.
    text: >
        az resource create -g myRG -n myApiApp --resource-type Microsoft.web/sites --is-full-object --properties @jsonConfigFile
  - name: Create a web app with the minimum required configuration information.
    text: |
        az resource create -g myRG -n myWeb --resource-type Microsoft.web/sites --properties '{
                "serverFarmId":"/subscriptions/{SubID}/resourcegroups/{ResourceGroup}/providers/Microsoft.Web/serverfarms/{ServicePlan}"
            }'
"""

helps['resource delete'] = """
type: command
short-summary: Delete a resource.
examples:
  - name: Delete a virtual machine named 'MyVm'.
    text: >
        az resource delete -g MyResourceGroup -n MyVm --resource-type "Microsoft.Compute/virtualMachines"
  - name: Delete a web app using a resource identifier.
    text: >
        az resource delete --ids /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Web/sites/MyWebapp
  - name: Delete a subnet using a resource identifier.
    text: >
        az resource delete --ids /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/MySubnet
"""

helps['resource invoke-action'] = """
type: command
short-summary: Invoke an action on the resource.
long-summary: >
    A list of possible actions corresponding to a resource can be found at https://docs.microsoft.com/rest/api/. All POST requests are actions that can be invoked and are specified at the end of the URI path. For instance, to stop a VM, the
    request URI is https://management.azure.com/subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroup}/providers/Microsoft.Compute/virtualMachines/{VM}/powerOff?api-version={APIVersion} and the corresponding action is `powerOff`. This can
    be found at https://docs.microsoft.com/rest/api/compute/virtualmachines/virtualmachines-stop.
examples:
  - name: Power-off a vm, specified by Id.
    text: >
        az resource invoke-action --action powerOff \\
          --ids /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Compute/virtualMachines/{VMName}
  - name: Capture information for a stopped vm.
    text: >
        az resource invoke-action --action capture \\
          --ids /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Compute/virtualMachines/{VMName} \\
          --request-body '{
            "vhdPrefix": "myPrefix",
            "destinationContainerName": "myContainer",
            "overwriteVhds": true
        }'
  - name: Invoke an action on the resource. (autogenerated)
    text: az resource invoke-action --action capture --name MyResource --resource-group MyResourceGroup --resource-type Microsoft.web/sites
    crafted: true
"""

helps['resource link'] = """
type: group
short-summary: Manage links between resources.
long-summary: >
    Linking is a feature of the Resource Manager. It enables declaring relationships between resources even if they do not reside in the same resource group.
    Linking has no impact on resource usage, billing, or role-based access. It allows for managing multiple resources across groups as a single unit.
"""

helps['resource link create'] = """
type: command
short-summary: Create a new link between resources.
parameters:
  - name: --link
    long-summary: >
        Format: /subscriptions/{SubID}/resourceGroups/{ResourceGroupID}/providers/{ProviderNamespace}/{ResourceType}/{ResourceName}/providers/Microsoft.Resources/links/{LinkName}
examples:
  - name: Create a link from {SourceID} to {ResourceID} with notes
    text: >
        az resource link create --link {SourceID} --target {ResourceID} --notes "SourceID depends on ResourceID"
"""

helps['resource link delete'] = """
type: command
short-summary: Delete a link between resources.
parameters:
  - name: --link
    long-summary: >
        Format: /subscriptions/{SubID}/resourceGroups/{ResourceGroupID}/providers/{ProviderNamespace}/{ResourceType}/{ResourceName}/providers/Microsoft.Resources/links/{LinkName}
examples:
  - name: Delete link {LinkID}
    text: >
        az resource link delete --link {LinkID}
"""

helps['resource link list'] = """
type: command
short-summary: List resource links.
examples:
  - name: List links, filtering with {filter-string}
    text: >
        az resource link list --filter {filter-string}
  - name: List all links for resource group {ResourceGroup} in subscription {SubID}
    text: >
        az resource link list --scope /subscriptions/{SubID}/resourceGroups/{ResourceGroup}
"""

helps['resource link update'] = """
type: command
short-summary: Update link between resources.
parameters:
  - name: --link
    long-summary: >
        Format: /subscriptions/{SubID}/resourceGroups/{ResourceGroupID}/providers/{ProviderNamespace}/{ResourceType}/{ResourceName}/providers/Microsoft.Resources/links/{LinkName}
examples:
  - name: Update the notes for {LinkID} notes "some notes to explain this link"
    text: >
        az resource link update --link {LinkID} --notes "some notes to explain this link"
"""

helps['resource list'] = """
type: command
short-summary: List resources.
examples:
  - name: List all resources in the West US region.
    text: >
        az resource list --location westus
  - name: List all resources with the name 'resourceName'.
    text: >
        az resource list --name 'resourceName'
  - name: List all resources with the tag 'test'.
    text: >
        az resource list --tag test
  - name: List all resources with a tag that starts with 'test'.
    text: >
        az resource list --tag 'test*'
  - name: List all resources with the tag 'test' that have the value 'example'.
    text: >
        az resource list --tag test=example
"""

helps['resource lock'] = """
type: group
short-summary: Manage Azure resource level locks.
"""

helps['resource lock create'] = """
type: command
short-summary: Create a resource-level lock.
examples:
  - name: Create a read-only resource level lock on a vnet.
    text: >
        az resource lock create --lock-type ReadOnly -n lockName -g MyResourceGroup --resource myvnet --resource-type Microsoft.Network/virtualNetworks
  - name: Create a read-only resource level lock on a vnet using a vnet id.
    text: >
        az resource lock create --lock-type ReadOnly -n lockName --resource /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/{VNETName}
"""

helps['resource lock delete'] = """
type: command
short-summary: Delete a resource-level lock.
examples:
  - name: Delete a resource level lock
    text: >
        az resource lock delete --name lockName -g MyResourceGroup --resource myvnet --resource-type Microsoft.Network/virtualNetworks
  - name: Delete a resource level lock on a vnet using a vnet id.
    text: >
        az resource lock delete -n lockName --resource /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/{VMName}
"""

helps['resource lock list'] = """
type: command
short-summary: List lock information in the resource-level.
examples:
  - name: List out all locks on a vnet
    text: >
        az resource lock list -g MyResourceGroup --resource myvnet --resource-type Microsoft.Network/virtualNetworks
"""

helps['resource lock show'] = """
type: command
short-summary: Show the details of a resource-level lock
examples:
  - name: Show a resource level lock
    text: >
        az resource lock show -n lockname -g MyResourceGroup --resource myvnet --resource-type Microsoft.Network/virtualNetworks
"""

helps['resource lock update'] = """
type: command
short-summary: Update a resource-level lock.
examples:
  - name: Update a resource level lock with new notes and type
    text: >
        az resource lock update --name lockName -g MyResourceGroup --resource myvnet --resource-type Microsoft.Network/virtualNetworks --notes newNotesHere --lock-type CanNotDelete
"""

helps['resource show'] = """
type: command
short-summary: Get the details of a resource.
examples:
  - name: Show a virtual machine resource named 'MyVm'.
    text: >
        az resource show -g MyResourceGroup -n MyVm --resource-type "Microsoft.Compute/virtualMachines"
  - name: Show a web app using a resource identifier.
    text: >
        az resource show --ids /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Web/sites/MyWebapp
  - name: Show a subnet.
    text: >
        az resource show -g MyResourceGroup -n MySubnet --namespace Microsoft.Network --parent virtualnetworks/MyVnet --resource-type subnets
  - name: Show a subnet using a resource identifier.
    text: >
        az resource show --ids /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/MySubnet
  - name: Show an application gateway path rule.
    text: >
        az resource show -g MyResourceGroup --namespace Microsoft.Network --parent applicationGateways/ag1/urlPathMaps/map1 --resource-type pathRules -n rule1
"""

helps['resource tag'] = """
type: command
short-summary: Tag a resource.
examples:
  - name: Tag the virtual machine 'MyVm' with the key 'vmlist' and value 'vm1'.
    text: >
        az resource tag --tags vmlist=vm1 -g MyResourceGroup -n MyVm --resource-type "Microsoft.Compute/virtualMachines"
  - name: Tag a web app with the key 'vmlist' and value 'vm1', using a resource identifier.
    text: >
        az resource tag --tags vmlist=vm1 --id /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Web/sites/{WebApp}
  - name: Tag a resource. (autogenerated)
    text: az resource tag --ids /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Web/sites/{WebApp} --tags vmlist=vm1
    crafted: true
"""

helps['resource update'] = """
type: command
short-summary: Update a resource.
examples:
  - name: Update a resource. (autogenerated)
    text: az resource update --ids $id --set properties.connectionType=Proxy
    crafted: true
"""

helps['resource wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a resources is met.
"""

helps['rest'] = """
type: command
short-summary: invoke a custom request
examples:
  - name: Get Audit log through Microsoft Graph
    text: >
        az rest --method get --uri https://graph.microsoft.com/beta/auditLogs/directoryAudits
  - name: Update a Azure Active Directory Graph User's display name
    text: >
        az rest --method patch --uri "https://graph.microsoft.com/v1.0/users/johndoe@azuresdkteam.onmicrosoft.com" --body "{\\"displayName\\": \\"jondoe2\\"}"
"""

helps['role'] = """
type: group
short-summary: Manage user roles for access control with Azure Active Directory and service principals.
"""

helps['role assignment'] = """
type: group
short-summary: Manage role assignments.
"""

helps['role assignment create'] = """
type: command
short-summary: Create a new role assignment for a user, group, or service principal.
examples:
  - name: Create role assignment for an assignee.
    text: az role assignment create --assignee sp_name --role a_role
"""

helps['role assignment delete'] = """
type: command
short-summary: Delete role assignments.
examples:
  - name: Delete role assignments. (autogenerated)
    text: |
        az role assignment delete --assignee 00000000-0000-0000-0000-000000000000 --role "Storage Account Key Operator Service Role"
    crafted: true
"""

helps['role assignment list'] = """
type: command
short-summary: List role assignments.
long-summary: By default, only assignments scoped to subscription will be displayed. To view assignments scoped by resource or group, use `--all`.
"""

helps['role assignment list-changelogs'] = """
type: command
short-summary: List changelogs for role assignments.
"""

helps['role definition'] = """
type: group
short-summary: Manage role definitions.
"""

helps['role definition create'] = """
type: command
short-summary: Create a custom role definition.
parameters:
  - name: --role-definition
    type: string
    short-summary: Description of a role as JSON, or a path to a file containing a JSON description.
examples:
  - name: Create a role with read-only access to storage and network resources, and the ability to start or restart VMs.
    text: |
        az role definition create --role-definition '{ \\
            "Name": "Contoso On-call", \\
            "Description": "Perform VM actions and read storage and network information.", \\
            "Actions": [ \\
                "Microsoft.Compute/*/read", \\
                "Microsoft.Compute/virtualMachines/start/action", \\
                "Microsoft.Compute/virtualMachines/restart/action", \\
                "Microsoft.Network/*/read", \\
                "Microsoft.Storage/*/read", \\
                "Microsoft.Authorization/*/read", \\
                "Microsoft.Resources/subscriptions/resourceGroups/read", \\
                "Microsoft.Resources/subscriptions/resourceGroups/resources/read", \\
                "Microsoft.Insights/alertRules/*", \\
                "Microsoft.Support/*" \\
            ], \\
            "DataActions": [ \\
                "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/*" \\
            ], \\
            "NotDataActions": [ \\
                "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write" \\
            ], \\
            "AssignableScopes": ["/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"] \\
        }'
  - name: Create a role from a file containing a JSON description.
    text: >
        az role definition create --role-definition @ad-role.json
"""

helps['role definition delete'] = """
type: command
short-summary: Delete a role definition.
examples:
  - name: Delete a role definition. (autogenerated)
    text: az role definition delete --name MyRole
    crafted: true
"""

helps['role definition list'] = """
type: command
short-summary: List role definitions.
"""

helps['role definition update'] = """
type: command
short-summary: Update a role definition.
parameters:
  - name: --role-definition
    type: string
    short-summary: Description of an existing role as JSON, or a path to a file containing a JSON description.
examples:
  - name: Update a role using the output of "az role definition list"
    text: |
        az role definition update --role-definition '{ \\
            "roleName": "Contoso On-call", \\
            "Description": "Perform VM actions and read storage and network information.", \\
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/providers/Microsoft.Authorization/roleDefinitions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", \\
            "roleType": "CustomRole", \\
            "type": "Microsoft.Authorization/roleDefinitions", \\
            "Actions": [ \\
                "Microsoft.Compute/*/read", \\
                "Microsoft.Compute/virtualMachines/start/action", \\
                "Microsoft.Compute/virtualMachines/restart/action", \\
                "Microsoft.Network/*/read", \\
                "Microsoft.Storage/*/read", \\
                "Microsoft.Authorization/*/read", \\
                "Microsoft.Resources/subscriptions/resourceGroups/read", \\
                "Microsoft.Resources/subscriptions/resourceGroups/resources/read", \\
                "Microsoft.Support/*" \\
            ], \\
            "DataActions": [ \\
                "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/*" \\
            ], \\
            "NotDataActions": [ \\
                "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write" \\
            ], \\
            "AssignableScopes": ["/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"] \\
        }'
"""

helps['search'] = """
type: group
short-summary: Manage Azure Search services, admin keys and query keys.
"""

helps['search admin-key'] = """
type: group
short-summary: Manage Azure Search admin keys.
"""

helps['search query-key'] = """
type: group
short-summary: Manage Azure Search query keys.
"""

helps['search service'] = """
type: group
short-summary: Manage Azure Search services.
"""

helps['search service update'] = """
type: command
short-summary: Update partition and replica of the given search service.
"""

helps['security'] = """
type: group
short-summary: Manage your security posture with Azure Security Center.
"""

helps['security alert'] = """
type: group
short-summary: View security alerts.
"""

helps['security alert list'] = """
type: command
short-summary: List security alerts.
examples:
  - name: Get security alerts on a subscription scope.
    text: >
        az security alert list
  - name: Get security alerts on a resource group scope.
    text: >
        az security alert list -g "myRg"
"""

helps['security alert show'] = """
type: command
short-summary: Shows a security alert.
examples:
  - name: Get a security alert on a subscription scope.
    text: >
        az security alert show --location "centralus" -n "alertName"
  - name: Get a security alert on a resource group scope.
    text: >
        az security alert show -g "myRg" --location "centralus" -n "alertName"
"""

helps['security alert update'] = """
type: command
short-summary: Updates a security alert status.
examples:
  - name: Dismiss a security alert on a subscription scope.
    text: >
        az security alert update --location "centralus" -n "alertName" --status "dismiss"
  - name: Dismiss a security alert on a resource group scope.
    text: >
        az security alert update -g "myRg" --location "centralus" -n "alertName" --status "dismiss"
  - name: Activate a security alert on a subscritpion scope.
    text: >
        az security alert update --location "centralus" -n "alertName" --status "activate"
  - name: Activate a security alert on a resource group scope.
    text: >
        az security alert update -g "myRg" --location "centralus" -n "alertName" --status "activate"
"""

helps['security auto-provisioning-setting'] = """
type: group
short-summary: View your auto provisioning settings.
"""

helps['security auto-provisioning-setting list'] = """
type: command
short-summary: List the auto provisioning settings.
examples:
  - name: Get auto provisioning settings.
    text: >
        az security auto-provisioning-setting list
"""

helps['security auto-provisioning-setting show'] = """
type: command
short-summary: Shows an auto provisioning setting.
examples:
  - name: Get an auto provisioning setting.
    text: >
        az security auto-provisioning-setting show -n "default"
"""

helps['security auto-provisioning-setting update'] = """
type: command
short-summary: Updates your automatic provisioning settings on the subscription.
examples:
  - name: Turns on automatic provisioning on the subscription.
    text: >
        az security auto-provisioning-setting update -n "default" --auto-provision "on"
  - name: Turns off automatic provisioning on the subscription.
    text: >
        az security auto-provisioning-setting update -n "default" --auto-provision "off"
"""

helps['security contact'] = """
type: group
short-summary: View your security contacts.
"""

helps['security contact create'] = """
type: command
short-summary: Creates a security contact.
examples:
  - name: Creates a security contact.
    text: >
        az security contact create -n "default1" --email 'john@contoso.com' --phone '(214)275-4038' --alert-notifications 'on' --alerts-admins 'on'
"""

helps['security contact delete'] = """
type: command
short-summary: Deletes a security contact.
examples:
  - name: Deletes a security contact.
    text: >
        az security contact delete -n "default1"
"""

helps['security contact list'] = """
type: command
short-summary: List security contact.
examples:
  - name: Get security contacts.
    text: >
        az security contact list
"""

helps['security contact show'] = """
type: command
short-summary: Shows a security contact.
examples:
  - name: Get a security contact.
    text: >
        az security contact show -n "default1"
"""

helps['security discovered-security-solution'] = """
type: group
short-summary: View your discovered security solutions
"""

helps['security discovered-security-solution list'] = """
type: command
short-summary: List the discovered security solutions.
examples:
  - name: Get discovered security solutions.
    text: >
        az security discovered-security-solution list
"""

helps['security discovered-security-solution show'] = """
type: command
short-summary: Shows a discovered security solution.
examples:
  - name: Get a discovered security solution.
    text: >
        az security discovered-security-solution show -n ContosoWAF2 -g myService1
"""

helps['security external-security-solution'] = """
type: group
short-summary: View your external security solutions
"""

helps['security external-security-solution list'] = """
type: command
short-summary: List the external security solutions.
examples:
  - name: Get external security solutions.
    text: >
        az security external-security-solution list
"""

helps['security external-security-solution show'] = """
type: command
short-summary: Shows an external security solution.
examples:
  - name: Get an external security solution.
    text: >
        az security external-security-solution show -n aad_defaultworkspace-20ff7fc3-e762-44dd-bd96-b71116dcdc23-eus -g defaultresourcegroup-eus
"""

helps['security jit-policy'] = """
type: group
short-summary: Manage your Just in Time network access policies
"""

helps['security jit-policy list'] = """
type: command
short-summary: List your Just in Time network access policies.
examples:
  - name: Get all the Just in Time network access policies.
    text: >
        az security jit-policy list
"""

helps['security jit-policy show'] = """
type: command
short-summary: Shows a Just in Time network access policy.
examples:
  - name: Get a Just in Time network access policy.
    text: >
        az security jit-policy show -l northeurope -n default -g myService1
"""

helps['security location'] = """
type: group
short-summary: Shows the Azure Security Center Home region location.
"""

helps['security location list'] = """
type: command
short-summary: Shows the Azure Security Center Home region location.
examples:
  - name: Shows the Azure Security Center Home region location.
    text: >
        az security location list
"""

helps['security location show'] = """
type: command
short-summary: Shows the Azure Security Center Home region location.
examples:
  - name: Shows the Azure Security Center Home region location.
    text: >
        az security location show -n centralus
"""

helps['security pricing'] = """
type: group
short-summary: Shows the Azure Security Center Pricing tier for the subscription.
"""

helps['security pricing create'] = """
type: command
short-summary: Updates the Azure Security Center Pricing tier for the subscription.
examples:
  - name: Updates the Azure Security Center Pricing tier for the subscription.
    text: >
        az security pricing create -n default --tier 'standard'
"""

helps['security pricing list'] = """
type: command
short-summary: Shows the Azure Security Center Pricing tier for the subscription.
examples:
  - name: Shows the Azure Security Center Pricing tier for the subscription.
    text: >
        az security pricing list
"""

helps['security pricing show'] = """
type: command
short-summary: Shows the Azure Security Center Pricing tier for the subscription.
examples:
  - name: Shows the Azure Security Center Pricing tier for the subscription.
    text: >
        az security pricing show -n default
"""

helps['security setting'] = """
type: group
short-summary: View your security settings.
"""

helps['security setting list'] = """
type: command
short-summary: List security settings.
examples:
  - name: Get security settings.
    text: >
        az security setting list
"""

helps['security setting show'] = """
type: command
short-summary: Shows a security setting.
examples:
  - name: Get a security setting.
    text: >
        az security setting show -n "MCAS"
"""

helps['security task'] = """
type: group
short-summary: View security tasks (recommendations).
"""

helps['security task list'] = """
type: command
short-summary: List security tasks (recommendations).
examples:
  - name: Get security tasks (recommendations) on a subscription scope.
    text: >
        az security task list
  - name: Get security tasks (recommendations) on a resource group scope.
    text: >
        az security task list -g "myRg"
"""

helps['security task show'] = """
type: command
short-summary: shows a security task (recommendation).
examples:
  - name: Get a security task (recommendation) on a subscription scope.
    text: >
        az security task show -n "taskName"
  - name: Get a security task (recommendation) on a resource group scope.
    text: >
        az security task show -g "myRg" -n "taskName"
"""

helps['security topology'] = """
type: group
short-summary: Shows the network topology in your subscription.
"""

helps['security topology list'] = """
type: command
short-summary: Shows the network topology in your subscription.
examples:
  - name: Shows the network topology in your subscription.
    text: >
        az security topology list
"""

helps['security topology show'] = """
type: command
short-summary: Shows the network topology in your subscription.
examples:
  - name: Shows the network topology in your subscription.
    text: >
        az security topology show -n default -g myService1
"""

helps['security workspace-setting'] = """
type: group
short-summary: Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
"""

helps['security workspace-setting create'] = """
type: command
short-summary: Creates a workspace settings in your subscription - these settings let you control which workspace will hold your security data
examples:
  - name: Creates a workspace settings in your subscription - these settings let you control which workspace will hold your security data
    text: >
        az security workspace-setting create -n default --target-workspace '/subscriptions/20ff7fc3-e762-44dd-bd96-b71116dcdc23/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace'
"""

helps['security workspace-setting delete'] = """
type: command
short-summary: Deletes the workspace settings in your subscription - this will make the security events on the subscription be reported to the default workspace
examples:
  - name: Deletes the workspace settings in your subscription - this will make the security events on the subscription be reported to the default workspace
    text: >
        az security workspace-setting delete -n default
"""

helps['security workspace-setting list'] = """
type: command
short-summary: Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
examples:
  - name: Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
    text: >
        az security workspace-setting list
"""

helps['security workspace-setting show'] = """
type: command
short-summary: Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
examples:
  - name: Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
    text: >
        az security workspace-setting show -n default
"""

helps['self-test'] = """
type: command
short-summary: Runs a self-test of the CLI.
"""

helps['servicebus'] = """
type: group
short-summary: Manage Azure Service Bus namespaces, queues, topics, subscriptions, rules and geo-disaster recovery configuration alias
"""

helps['servicebus georecovery-alias'] = """
type: group
short-summary: Manage Azure Service Bus Geo-Disaster Recovery Configuration Alias
"""

helps['servicebus georecovery-alias authorization-rule'] = """
type: group
short-summary: Manage Azure Service Bus Authorization Rule for Namespace with Geo-Disaster Recovery Configuration Alias
"""

helps['servicebus georecovery-alias authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule keys for Service Bus Namespace
"""

helps['servicebus georecovery-alias authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for the Service Bus Namespace
examples:
  - name: List the keys and connection strings of Authorization Rule for the namespace.
    text: az servicebus georecovery-alias authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --alias myaliasname
"""

helps['servicebus georecovery-alias authorization-rule list'] = """
type: command
short-summary: Shows the list of Authorization Rule by Service Bus Namespace
examples:
  - name: Shows the list of Authorization Rule by Service Bus Namespace
    text: az servicebus georecovery-alias authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias break-pair'] = """
type: command
short-summary: Disables Service Bus Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces
examples:
  - name: Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
    text: az servicebus georecovery-alias break-pair --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias delete'] = """
type: command
short-summary: Deletes Service Bus Geo-Disaster Recovery Configuration Alias request accepted
examples:
  - name: Delete Service Bus Geo-Disaster Recovery Configuration Alias request accepted
    text: az servicebus georecovery-alias delete --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias exists'] = """
type: command
short-summary: Check if Geo Recovery Alias Name is available
examples:
  - name: Check availability of the Geo-Disaster Recovery Configuration Alias Name
    text: az servicebus georecovery-alias exists --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias fail-over'] = """
type: command
short-summary: Invokes Service Bus Geo-Disaster Recovery Configuration Alias failover and re-configure the alias to point to the secondary namespace
examples:
  - name: Invokes Geo-Disaster Recovery Configuration Alias failover and reconfigure the alias to point to the secondary namespace
    text: az servicebus georecovery-alias fail-over --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias set'] = """
type: command
short-summary: Sets Service Bus Geo-Disaster Recovery Configuration Alias for the give Namespace
examples:
  - name: Sets Geo Disaster Recovery configuration - Alias for the give Namespace
    text: az servicebus georecovery-alias set --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname --partner-namespace armresourceid
"""

helps['servicebus georecovery-alias show'] = """
type: command
short-summary: shows properties of Service Bus Geo-Disaster Recovery Configuration Alias for Primay/Secondary Namespace
examples:
  - name: show properties Geo-Disaster Recovery Configuration Alias of the Primary Namespace
    text: az servicebus georecovery-alias show  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
  - name: Get details of Alias (Geo DR Configuration)  of the Secondary Namespace
    text: az servicebus georecovery-alias show  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus migration'] = """
type: group
short-summary: Manage Azure Service Bus Migration of Standard to Premium
"""

helps['servicebus migration abort'] = """
type: command
short-summary: Disable the Service Bus Migration of Standard to Premium namespace
long-summary: abort command stops the replication of entities from standard to premium namespaces. The entities replicated to premium namespace before abort command will be available under premium namespace. The aborted migration can not be resumed, its has to restarted.
examples:
  - name: Disable Service Bus Migration of Standard to Premium namespace
    text: az servicebus migration abort --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration complete'] = """
type: command
short-summary: Completes the Service Bus Migration of Standard to Premium namespace
long-summary: After completing migration, the existing connection strings to standard namespace will connect to premium namespace automatically. Post migration name is the name that can be used to connect to standard namespace after migration is complete.
examples:
  - name: Completes the Service Bus Migration of Standard to Premium namespace
    text: az servicebus migration complete --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration show'] = """
type: command
short-summary: shows properties of properties of Service Bus Migration
examples:
  - name: shows properties of properties of Service Bus Migration
    text: az servicebus migration show --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration start'] = """
type: command
short-summary: Create and Start Service Bus Migration of Standard to Premium namespace.
long-summary: Service Bus Migration requires an empty Premium namespace to replicate entities from Standard namespace.
examples:
  - name: Create and Start Service Bus Migration of Standard to Premium namespace
    text: az servicebus migration start --resource-group myresourcegroup --name standardnamespace --target-namespace ARMIDpremiumnamespace --post-migration-name mypostmigrationname
"""

helps['servicebus namespace'] = """
type: group
short-summary: Manage Azure Service Bus Namespace
"""

helps['servicebus namespace authorization-rule'] = """
type: group
short-summary: Manage Azure Service Bus Namespace Authorization Rule
"""

helps['servicebus namespace authorization-rule create'] = """
type: command
short-summary: Create Authorization Rule for the given Service Bus Namespace
examples:
  - name: Create Authorization Rule 'myauthorule' for the given Service Bus Namespace 'mynamepsace' in resourcegroup
    text: az servicebus namespace authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send Listen
"""

helps['servicebus namespace authorization-rule delete'] = """
type: command
short-summary: Deletes the Authorization Rule of the Service Bus Namespace.
examples:
  - name: Deletes the Authorization Rule of the Service Bus Namespace.
    text: az servicebus namespace authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule connection strings for Namespace
"""

helps['servicebus namespace authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for Service Bus Namespace
examples:
  - name: List the keys and connection strings of Authorization Rule for Service Bus Namespace
    text: az servicebus namespace authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule keys renew'] = """
type: command
short-summary: Regenerate keys of Authorization Rule for the Service Bus Namespace.
examples:
  - name: Regenerate keys of Authorization Rule for the Service Bus Namespace.
    text: az servicebus namespace authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --key PrimaryKey
"""

helps['servicebus namespace authorization-rule list'] = """
type: command
short-summary: Shows the list of Authorization Rule by Service Bus Namespace
examples:
  - name: Shows the list of Authorization Rule by Service Bus Namespace
    text: az servicebus namespace authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace authorization-rule show'] = """
type: command
short-summary: Shows the details of Service Bus Namespace Authorization Rule
examples:
  - name: Shows the details of Service Bus Namespace Authorization Rule
    text: az servicebus namespace authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule update'] = """
type: command
short-summary: Updates Authorization Rule for the given Service Bus Namespace
examples:
  - name: Updates Authorization Rule 'myauthorule' for the given Service Bus Namespace 'mynamepsace' in resourcegroup
    text: az servicebus namespace authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send
"""

helps['servicebus namespace create'] = """
type: command
short-summary: Create a Service Bus Namespace
examples:
  - name: Create a Service Bus Namespace.
    text: az servicebus namespace create --resource-group myresourcegroup --name mynamespace --location westus --tags tag1=value1 tag2=value2 --sku Standard
"""

helps['servicebus namespace delete'] = """
type: command
short-summary: Deletes the Service Bus Namespace
examples:
  - name: Deletes the Service Bus Namespace
    text: az servicebus namespace delete --resource-group myresourcegroup --name mynamespace
"""

helps['servicebus namespace exists'] = """
type: command
short-summary: check for the availability of the given name for the Namespace
examples:
  - name: check for the availability of mynamespace for the Namespace
    text: az servicebus namespace exists --name mynamespace
"""

helps['servicebus namespace list'] = """
type: command
short-summary: List the Service Bus Namespaces
examples:
  - name: Get the Service Bus Namespaces by resource group
    text: az servicebus namespace list --resource-group myresourcegroup
  - name: Get the Service Bus Namespaces by Subscription.
    text: az servicebus namespace list
"""

helps['servicebus namespace network-rule'] = """
type: group
short-summary: Manage Azure ServiceBus networkruleSet for namespace
"""

helps['servicebus namespace network-rule add'] = """
type: command
short-summary: Add a network rule for a namespace.
examples:
  - name: add a VirtualNetwork rule in NetworkruleSet for a namespace
    text: az servicebus namespace network-rule add --resource-group myresourcegroup --namespace-name mynamespace --subnet {subnetId} --ignore-missing-endpoint True
  - name: add a IP rule in NetworkruleSet for a namespace
    text: az servicebus namespace network-rule add --resource-group myresourcegroup --namespace-name mynamespace --ip-address 10.0.0.0/24 --action Allow
"""

helps['servicebus namespace network-rule list'] = """
type: command
short-summary: Show properties of Network rule of the given Namespace.
examples:
  - name: Show properties of Network rule of the given Namespace
    text: az servicebus namespace network-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace network-rule remove'] = """
type: command
short-summary: Remove network rule for a namespace
examples:
  - name: remove VirtualNetwork rule from NetworkruleSet for a namespace
    text: az servicebus namespace network-rule remove --resource-group myresourcegroup --namespace-name mynamespace --subnet {subnetId}
  - name: remove IP rule from NetworkruleSet for a namespace
    text: az servicebus namespace network-rule remove --resource-group myresourcegroup --namespace-name mynamespace --ip-address 10.0.0.0/24
"""

helps['servicebus namespace show'] = """
type: command
short-summary: Shows the Service Bus Namespace details
examples:
  - name: shows the Namespace details.
    text: az servicebus namespace show --resource-group myresourcegroup --name mynamespace
"""

helps['servicebus namespace update'] = """
type: command
short-summary: Updates a Service Bus Namespace
examples:
  - name: Updates a Service Bus Namespace.
    text: az servicebus namespace update --resource-group myresourcegroup --name mynamespace --tags tag=value
"""

helps['servicebus queue'] = """
type: group
short-summary: Manage Azure Service Bus Queue and Authorization Rule
"""

helps['servicebus queue authorization-rule'] = """
type: group
short-summary: Manage Azure Service Bus Queue Authorization Rule
"""

helps['servicebus queue authorization-rule create'] = """
type: command
short-summary: Create Authorization Rule for the given Service Bus Queue.
examples:
  - name: Create Authorization Rule for Queue
    text: az servicebus queue authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule --rights Listen
"""

helps['servicebus queue authorization-rule delete'] = """
type: command
short-summary: Delete the Authorization Rule of Service Bus Queue
examples:
  - name: Delete the Authorization Rule of Service Bus Queue
    text: az servicebus queue authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule
"""

helps['servicebus queue authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule keys for Service Bus Queue
"""

helps['servicebus queue authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for the given Service Bus Queue
examples:
  - name: List the keys and connection strings of Authorization Rule for the given Service Bus Queue
    text: az servicebus queue authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule
"""

helps['servicebus queue authorization-rule keys renew'] = """
type: command
short-summary: Regenerate keys of Authorization Rule for Service Bus Queue
examples:
  - name: Regenerate keys of Authorization Rule for Service Bus Queue
    text: az servicebus queue authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule --key PrimaryKey
"""

helps['servicebus queue authorization-rule list'] = """
type: command
short-summary: List of Authorization Rule by Service Bus Queue.
examples:
  - name: List of Authorization Rule by Queue
    text: az servicebus queue authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue
"""

helps['servicebus queue authorization-rule show'] = """
type: command
short-summary: show properties of Authorization Rule for the given Service Bus Queue.
examples:
  - name: show properties of Authorization Rule
    text: az servicebus queue authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule
"""

helps['servicebus queue authorization-rule update'] = """
type: command
short-summary: Update Authorization Rule for the given Service Bus Queue.
examples:
  - name: Update Authorization Rule for Queue
    text: az servicebus queue authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --queue-name myqueue --name myauthorule --rights Send
"""

helps['servicebus queue create'] = """
type: command
short-summary: Create the Service Bus Queue
examples:
  - name: Create Service Bus Queue.
    text: az servicebus queue create --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue delete'] = """
type: command
short-summary: Deletes the Service Bus Queue
examples:
  - name: Deletes the queue
    text: az servicebus queue delete --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue list'] = """
type: command
short-summary: List the Queue by Service Bus Namepsace
examples:
  - name: Get the Queues by Service Bus Namespace.
    text: az servicebus queue list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus queue show'] = """
type: command
short-summary: shows the Service Bus Queue Details
examples:
  - name: Shows the Service Bus Queue Details
    text: az servicebus queue show --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue update'] = """
type: command
short-summary: Updates existing Service Bus Queue
examples:
  - name: Updates Service Bus Queue.
    text: az servicebus queue update --resource-group myresourcegroup --namespace-name mynamespace --name myqueue --auto-delete-on-idle PT3M
"""

helps['servicebus topic'] = """
type: group
short-summary: Manage Azure Service Bus Topic and Authorization Rule
"""

helps['servicebus topic authorization-rule'] = """
type: group
short-summary: Manage Azure Service Bus Topic Authorization Rule
"""

helps['servicebus topic authorization-rule create'] = """
type: command
short-summary: Create Authorization Rule for given Service Bus Topic
examples:
  - name: Create Authorization Rule for given Service Bus Topic
    text: az servicebus topic authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule --rights Send Listen
"""

helps['servicebus topic authorization-rule delete'] = """
type: command
short-summary: Deletes the Authorization Rule of the given Service Bus Topic.
examples:
  - name: Deletes the Authorization Rule of Service Bus Topic.
    text: az servicebus topic authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule
"""

helps['servicebus topic authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule keys for Service Bus Topic
"""

helps['servicebus topic authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for Service Bus Topic.
examples:
  - name: List the keys and connection strings of Authorization Rule for Service Bus Topic.
    text: az servicebus topic authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule
"""

helps['servicebus topic authorization-rule keys renew'] = """
type: command
short-summary: Regenerate keys of Authorization Rule for Service Bus Topic.
examples:
  - name: Regenerate key of Service Bus Topic.
    text: az servicebus topic authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule --key PrimaryKey
"""

helps['servicebus topic authorization-rule list'] = """
type: command
short-summary: shows list of Authorization Rule by Service Bus Topic
examples:
  - name: shows list of Authorization Rule by Service Bus Topic
    text: az servicebus topic authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic
"""

helps['servicebus topic authorization-rule show'] = """
type: command
short-summary: Shows the details of Authorization Rule for given Service Bus Topic
examples:
  - name: Shows the details of Authorization Rule for given Service Bus Topic
    text: az servicebus topic authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule
"""

helps['servicebus topic authorization-rule update'] = """
type: command
short-summary: Create Authorization Rule for given Service Bus Topic
examples:
  - name: Create Authorization Rule for given Service Bus Topic
    text: az servicebus topic authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule --rights Send
"""

helps['servicebus topic create'] = """
type: command
short-summary: Create the Service Bus Topic
examples:
  - name: Create a new Service Bus Topic
    text: az servicebus topic create --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic delete'] = """
type: command
short-summary: Deletes the Service Bus Topic
examples:
  - name: Deletes the Service Bus Topic
    text: az servicebus topic delete --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic list'] = """
type: command
short-summary: List the Topic by Service Bus Namepsace
examples:
  - name: Get the Topics by Namespace.
    text: az servicebus topic list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus topic show'] = """
type: command
short-summary: Shows the Service Bus Topic Details
examples:
  - name: Shows the Topic details.
    text: az servicebus topic show --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic subscription'] = """
type: group
short-summary: Manage Azure Service Bus Subscription
"""

helps['servicebus topic subscription create'] = """
type: command
short-summary: Create the ServiceBus Subscription
examples:
  - name: Create a new Subscription.
    text: az servicebus topic subscription create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription

"""

helps['servicebus topic subscription delete'] = """
type: command
short-summary: Deletes the Service Bus Subscription
examples:
  - name: Deletes the Subscription
    text: az servicebus topic subscription delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription
"""

helps['servicebus topic subscription list'] = """
type: command
short-summary: List the Subscription by Service Bus Topic
examples:
  - name: Shows the Subscription by Service Bus Topic.
    text: az servicebus topic subscription list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic
"""

helps['servicebus topic subscription rule'] = """
type: group
short-summary: Manage Azure Service Bus Rule
"""

helps['servicebus topic subscription rule create'] = """
type: command
short-summary: Create the ServiceBus Rule for Subscription
examples:
  - name: Create Rule.
    text: az servicebus topic subscription rule create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule --filter-sql-expression myproperty=myvalue
"""

helps['servicebus topic subscription rule delete'] = """
type: command
short-summary: Deletes the ServiceBus Rule
examples:
  - name: Deletes the ServiceBus Rule
    text: az servicebus topic subscription rule delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule
"""

helps['servicebus topic subscription rule list'] = """
type: command
short-summary: List the ServiceBus Rule by Subscription
examples:
  - name: Shows the Rule ServiceBus by Subscription.
    text: az servicebus topic subscription rule list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription
"""

helps['servicebus topic subscription rule show'] = """
type: command
short-summary: Shows ServiceBus Rule Details
examples:
  - name: Shows the ServiceBus Rule details.
    text: az servicebus topic subscription rule show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule
"""

helps['servicebus topic subscription rule update'] = """
type: command
short-summary: Updates the ServiceBus Rule for Subscription
examples:
  - name: Updates Rule.
    text: az servicebus topic subscription rule update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule --filter-sql-expression myproperty=myupdatedvalue
"""

helps['servicebus topic subscription show'] = """
type: command
short-summary: Shows Service Bus Subscription Details
examples:
  - name: Shows the Subscription details.
    text: az servicebus topic subscription show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription
"""

helps['servicebus topic subscription update'] = """
type: command
short-summary: Updates the ServiceBus Subscription
examples:
  - name: Update a new Subscription.
    text: az servicebus topic subscription update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription --lock-duration PT3M
"""

helps['servicebus topic update'] = """
type: command
short-summary: Updates the Service Bus Topic
examples:
  - name: Updates existing Service Bus Topic.
    text: az servicebus topic update --resource-group myresourcegroup --namespace-name mynamespace --name mytopic --enable-ordering True
"""

helps['sf'] = """
type: group
short-summary: Manage and administer Azure Service Fabric clusters.
"""

helps['sf application'] = """
type: group
short-summary: Manage applications running on an Azure Service Fabric cluster.
"""

helps['sf application certificate'] = """
type: group
short-summary: Manage the certificate of an application.
"""

helps['sf application certificate add'] = """
type: command
short-summary: Add a new certificate to the Virtual Machine Scale Sets that make up the cluster to be used by hosted applications.
examples:
  - name: Add an application certificate.
    text: >
        az sf application certificate add -g group-name -n cluster1  --secret-identifier 'https://{KeyVault}.vault.azure.net/secrets/{Secret}'
"""

helps['sf cluster'] = """
type: group
short-summary: Manage an Azure Service Fabric cluster.
"""

helps['sf cluster certificate'] = """
type: group
short-summary: Manage a cluster certificate.
"""

helps['sf cluster certificate add'] = """
type: command
short-summary: Add a secondary cluster certificate to the cluster.
examples:
  - name: Add a certificate to a  cluster using a keyvault secret identifier.
    text: |
        az sf cluster certificate add -g group-name -n cluster1 \\
            --secret-identifier 'https://{KeyVault}.vault.azure.net/secrets/{Secret}'
  - name: Add a self-signed certificate to a cluster.
    text: >
        az sf cluster certificate add -g group-name -n cluster1 --certificate-subject-name test.com

"""

helps['sf cluster certificate remove'] = """
type: command
short-summary: Remove a certificate from a cluster.
examples:
  - name: Remove a certificate by thumbprint.
    text: >
        az sf cluster certificate remove -g group-name -n cluster1 --thumbprint '5F3660C715EBBDA31DB1FFDCF508302348DE8E7A'

"""

helps['sf cluster client-certificate'] = """
type: group
short-summary: Manage the client certificate of a cluster.
"""

helps['sf cluster client-certificate add'] = """
type: command
short-summary: Add a common name or certificate thumbprint to the cluster for client authentication.
examples:
  - name: Add client certificate by thumbprint
    text: >
        az sf cluster client-certificate add -g group-name -n cluster1 --thumbprint '5F3660C715EBBDA31DB1FFDCF508302348DE8E7A'

"""

helps['sf cluster client-certificate remove'] = """
type: command
short-summary: Remove client certificates or subject names used for authentication.
examples:
  - name: Remove a client certificate by thumbprint.
    text: >
        az sf cluster client-certificate remove -g group-name -n cluster1 --thumbprint '5F3660C715EBBDA31DB1FFDCF508302348DE8E7A'

"""

helps['sf cluster create'] = """
type: command
short-summary: Create a new Azure Service Fabric cluster.
examples:
  - name: Create a cluster with a given size and self-signed certificate that is downloaded locally.
    text: >
        az sf cluster create -g group-name -n cluster1 -l westus --cluster-size 4 --vm-password Password#1234 --certificate-output-folder MyCertificates --certificate-subject-name cluster1
  - name: Use a keyvault certificate and custom template to deploy a cluster.
    text: >
        az sf cluster create -g group-name -n cluster1 -l westus --template-file template.json \\
            --parameter-file parameter.json --secret-identifier https://{KeyVault}.vault.azure.net:443/secrets/{MyCertificate}

"""

helps['sf cluster durability'] = """
type: group
short-summary: Manage the durability of a cluster.
"""

helps['sf cluster durability update'] = """
type: command
short-summary: Update the durability tier or VM SKU of a node type in the cluster.
examples:
  - name: Change the cluster durability level to 'Silver'.
    text: >
        az sf cluster durability update -g group-name -n cluster1 --durability-level Silver --node-type nt1

"""

helps['sf cluster list'] = """
type: command
short-summary: List cluster resources.
"""

helps['sf cluster node'] = """
type: group
short-summary: Manage the node instance of a cluster.
"""

helps['sf cluster node add'] = """
type: command
short-summary: Add nodes to a node type in a cluster.
examples:
  - name: Add 2 'nt1' nodes to a cluster.
    text: >
        az sf cluster node add -g group-name -n cluster1 --number-of-nodes-to-add 2 --node-type 'nt1'

"""

helps['sf cluster node remove'] = """
type: command
short-summary: Remove nodes from a node type in a cluster.
examples:
  - name: Remove 2 'nt1' nodes from a cluster.
    text: >
        az sf cluster node remove -g group-name -n cluster1 --node-type 'nt1' --number-of-nodes-to-remove 2

"""

helps['sf cluster node-type'] = """
type: group
short-summary: Manage the node-type of a cluster.
"""

helps['sf cluster node-type add'] = """
type: command
short-summary: Add a new node type to a cluster.
examples:
  - name: Add a new node type to a cluster.
    text: >
        az sf cluster node-type add -g group-name -n cluster1 --node-type 'n2' --capacity 5 --vm-user-name 'adminName' --vm-password User@1234567890

"""

helps['sf cluster reliability'] = """
type: group
short-summary: Manage the reliability of a cluster.
"""

helps['sf cluster reliability update'] = """
type: command
short-summary: Update the reliability tier for the primary node in a cluster.
examples:
  - name: Change the cluster reliability level to 'Silver'.
    text: >
        az sf cluster reliability update -g group-name -n cluster1 --reliability-level Silver

"""

helps['sf cluster setting'] = """
type: group
short-summary: Manage a cluster's settings.
"""

helps['sf cluster setting remove'] = """
type: command
short-summary: Remove settings from a cluster.
examples:
  - name: Remove the `MaxFileOperationTimeout` setting from a cluster.
    text: >
        az sf cluster setting remove -g group-name -n cluster1 --section 'NamingService' --parameter 'MaxFileOperationTimeout'

"""

helps['sf cluster setting set'] = """
type: command
short-summary: Update the settings of a cluster.
examples:
  - name: Set the `MaxFileOperationTimeout` setting for a cluster to 5 seconds.
    text: >
        az sf cluster setting set -g group-name -n cluster1 --section 'NamingService' --parameter 'MaxFileOperationTimeout' --value 5000

"""

helps['sf cluster upgrade-type'] = """
type: group
short-summary: Manage the upgrade type of a cluster.
"""

helps['sf cluster upgrade-type set'] = """
type: command
short-summary: Change the  upgrade type for a cluster.
examples:
  - name: Set a cluster to use the 'Automatic' upgrade mode.
    text: >
        az sf cluster upgrade-type set -g group-name -n cluster1 --upgrade-mode Automatic
"""

helps['sig'] = """
type: group
short-summary: manage shared image gallery
"""

helps['sig create'] = """
type: command
short-summary: create a share image gallery.
examples:
  - name: create a share image gallery. (autogenerated)
    text: az sig create --gallery-name MyGallery --resource-group MyResourceGroup
    crafted: true
"""

helps['sig image-definition'] = """
type: group
short-summary: create an image definition
"""

helps['sig image-definition create'] = """
type: command
short-summary: create a gallery image definition
examples:
  - name: Create a linux image defintion
    text: |
        az sig image-definition create -g MyResourceGroup --gallery-name MyGallery --gallery-image-definition MyImage --publisher GreatPublisher --offer GreatOffer --sku GreatSku --os-type linux
"""

helps['sig image-definition update'] = """
type: command
short-summary: update a share image defintiion.
examples:
  - name: update a share image defintiion. (autogenerated)
    text: az sig image-definition update --gallery-image-definition MyImage --gallery-name MyGallery --resource-group MyResourceGroup
    crafted: true
"""

helps['sig image-version'] = """
type: group
short-summary: create a new version from an image defintion
"""

helps['sig image-version create'] = """
type: command
short-summary: create a new image version
long-summary: this operation might take a long time depending on the replicate region number. Use "--no-wait" is advised.
examples:
  - name: Add a new image version
    text: |
        az sig image-version create -g MyResourceGroup --gallery-name MyGallery --gallery-image-definition MyImage --gallery-image-version 1.0.0 --managed-image /subscriptions/00000000-0000-0000-0000-00000000xxxx/resourceGroups/imageGroups/providers/images/MyManagedImage
  - name: Add a new image version replicated across multiple regions with different replication counts each. Eastus2 will have it's replica count set to the default replica count.
    text: |
        az sig image-version create -g MyResourceGroup --gallery-name MyGallery \\
        --gallery-image-definition MyImage --gallery-image-version 1.0.0 \\
        --managed-image image-name --target-regions eastus2 ukwest=3 southindia=2
  - name: Add a new image version and don't wait on it. Later you can invoke "az sig image-version wait" command when ready to create a vm from the gallery image version
    text: |
        az sig image-version create --no-wait -g MyResourceGroup --gallery-name MyGallery \\
        --gallery-image-definition MyImage --gallery-image-version 1.0.0 \\
        --managed-image imageInTheSameResourceGroup

  - name: Add a new image version with target regions that have different storage account types and replica counts
    text: |
        az sig image-version create -g MyResourceGroup --gallery-image-version 1.0.0 \\
        --target-regions westus=2=standard_lrs eastus=3=standard_zrs \\
        --gallery-name MyGallery --gallery-image-definition MyImage \\
        --managed-image imageInTheSameResourceGroup
"""

helps['sig image-version update'] = """
type: command
short-summary: update a share image version
examples:
  - name: Replicate to a new set of regions
    text: |
        az sig image-version update -g MyResourceGroup --gallery-name MyGallery --gallery-image-definition MyImage --gallery-image-version 1.0.0 --target-regions westcentralus=2 eastus2
  - name: Replicate to one more region
    text: |
        az sig image-version update -g MyResourceGroup --gallery-name MyGallery --gallery-image-definition MyImage --gallery-image-version 1.0.0 --add publishingProfile.targetRegions name=westcentralus

"""

helps['sig image-version wait'] = """
type: command
short-summary: wait for image version related operation
examples:
  - name: wait for an image version gets updated
    text: |
        az sig image-version wait --updated -g MyResourceGroup --gallery-name MyGallery --gallery-image-definition MyImage --gallery-image-version 1.0.0
"""

helps['sig list'] = """
type: command
short-summary: list share image galleries.
"""

helps['sig update'] = """
type: command
short-summary: update a share image gallery.
"""

helps['signalr'] = """
type: group
short-summary: Manage Azure SignalR Service.
"""

helps['signalr cors'] = """
type: group
short-summary: Manage CORS for Azure SignalR Service.
"""

helps['signalr cors add'] = """
type: command
short-summary: Add allowed origins to a SignalR Service
examples:
  - name: Add a list of allowed origins to a SignalR Service
    text: >
        az signalr cors add -n MySignalR -g MyResourceGroup --allowed-origins "http://example1.com" "https://example2.com"
"""

helps['signalr cors list'] = """
type: command
short-summary: List allowed origins of a SignalR Service
"""

helps['signalr cors remove'] = """
type: command
short-summary: Remove allowed origins from a SignalR Service
examples:
  - name: Remove a list of allowed origins from a SignalR Service
    text: >
        az signalr cors remove -n MySignalR -g MyResourceGroup --allowed-origins "http://example1.com" "https://example2.com"
"""

helps['signalr create'] = """
type: command
short-summary: Creates a SignalR Service.
examples:
  - name: Create a SignalR Service with the Standard SKU and serverless mode.
    text: >
        az signalr create -n MySignalR -g MyResourceGroup --sku Standard_S1 --unit-count 1 --service-mode Serverless
"""

helps['signalr delete'] = """
type: command
short-summary: Deletes a SignalR Service.
examples:
  - name: Delete a SignalR Service.
    text: >
        az signalr delete -n MySignalR -g MyResourceGroup
"""

helps['signalr key'] = """
type: group
short-summary: Manage keys for Azure SignalR Service.
"""

helps['signalr key list'] = """
type: command
short-summary: List the access keys for a SignalR Service.
examples:
  - name: Get the primary key for a SignalR Service.
    text: >
        az signalr key list -n MySignalR -g MyResourceGroup --query primaryKey -o tsv
"""

helps['signalr key renew'] = """
type: command
short-summary: Regenerate the access key for a SignalR Service.
examples:
  - name: Renew the secondary key for a SignalR Service.
    text: >
        az signalr key renew -n MySignalR -g MyResourceGroup --key-type secondary
"""

helps['signalr list'] = """
type: command
short-summary: Lists all the SignalR Service under the current subscription.
examples:
  - name: List SignalR Service and show the results in a table.
    text: >
        az signalr list -o table
  - name: List SignalR Service in a resource group and show the results in a table.
    text: >
        az signalr list -g MySignalR -o table
"""

helps['signalr restart'] = """
type: command
short-summary: Restart an existing SignalR Service.
examples:
  - name: Restart a SignalR Service instance.
    text: >
        az signalr restart -n MySignalR -g MyResourceGroup
"""

helps['signalr show'] = """
type: command
short-summary: Get the details of a SignalR Service.
examples:
  - name: Get the sku for a SignalR Service.
    text: >
        az signalr show -n MySignalR -g MyResourceGroup --query sku
"""

helps['signalr update'] = """
type: command
short-summary: Update an existing SignalR Service.
examples:
  - name: Update unit count to scale the service.
    text: >
        az signalr update -n MySignalR -g MyResourceGroup --sku Standard_S1 --unit-count 50
  - name: Update service mode.
    text: >
        az signalr update -n MySignalR -g MyResourceGroup --service-mode Serverless
"""

helps['snapshot'] = """
type: group
short-summary: Manage point-in-time copies of managed disks, native blobs, or other snapshots.
"""

helps['snapshot create'] = """
type: command
short-summary: Create a snapshot.
examples:
  - name: Create a snapshot by importing from a blob uri.
    text: az snapshot create -g MyResourceGroup -n MySnapshot --source https://vhd1234.blob.core.windows.net/vhds/osdisk1234.vhd
  - name: Create an empty snapshot.
    text: az snapshot create -g MyResourceGroup -n MySnapshot --size-gb 10
  - name: Create a snapshot by copying an existing disk in the same resource group.
    text: az snapshot create -g MyResourceGroup -n MySnapshot2 --source MyDisk
  - name: Create a snapshot from an existing disk in another resource group.
    text: az snapshot create -g MyResourceGroup -n MySnapshot2 --source "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.Compute/disks/MyDisk"
"""

helps['snapshot grant-access'] = """
type: command
short-summary: Grant read access to a snapshot.
examples:
  - name: Grant read access to a snapshot. (autogenerated)
    text: az snapshot grant-access --duration-in-seconds 3600 --name MySnapshot --resource-group MyResourceGroup
    crafted: true
"""

helps['snapshot list'] = """
type: command
short-summary: List snapshots.
"""

helps['snapshot revoke-access'] = """
type: command
short-summary: Revoke read access to a snapshot.
examples:
  - name: Revoke read access to a snapshot. (autogenerated)
    text: az snapshot revoke-access --name MySnapshot --resource-group MyResourceGroup
    crafted: true
"""

helps['snapshot update'] = """
type: command
short-summary: Update a snapshot.
"""

helps['snapshot wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a snapshot is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a snapshot is met. (autogenerated)
    text: az snapshot wait --exists --name MySnapshot --resource-group MyResourceGroup
    crafted: true
"""

helps['sql'] = """
type: group
short-summary: Manage Azure SQL Databases and Data Warehouses.
"""

helps['sql db'] = """
type: group
short-summary: Manage databases.
"""

helps['sql db audit-policy'] = """
type: group
short-summary: Manage a database's auditing policy.
"""

helps['sql db audit-policy update'] = """
type: command
short-summary: Update a database's auditing policy.
long-summary: If the policy is being enabled, `--storage-account` or both `--storage-endpoint` and `--storage-key` must be specified.
examples:
  - name: Enable by storage account name.
    text: az sql db audit-policy update -g mygroup -s myserver -n mydb --state Enabled --storage-account mystorage
  - name: Enable by storage endpoint and key.
    text: |
        az sql db audit-policy update -g mygroup -s myserver -n mydb --state Enabled \\
            --storage-endpoint https://mystorage.blob.core.windows.net --storage-key MYKEY==
  - name: Set the list of audit actions.
    text: |
        az sql db audit-policy update -g mygroup -s myserver -n mydb \\
            --actions FAILED_DATABASE_AUTHENTICATION_GROUP 'UPDATE on database::mydb by public'
  - name: Add an audit action.
    text: |
        az sql db audit-policy update -g mygroup -s myserver -n mydb \\
            --add auditActionsAndGroups FAILED_DATABASE_AUTHENTICATION_GROUP
  - name: Remove an audit action by list index.
    text: az sql db audit-policy update -g mygroup -s myserver -n mydb --remove auditActionsAndGroups 0
  - name: Disable an auditing policy.
    text: az sql db audit-policy update -g mygroup -s myserver -n mydb --state Disabled
"""

helps['sql db copy'] = """
type: command
short-summary: Create a copy of a database.
long-summary: A full list of performance level options can be seen by executing `az sql db list-editions -a -o table -l LOCATION`. The copy destination database must have the same edition as the source database, but you can change the edition after the copy has completed.
examples:
  - name: Create a database with performance level S0 as a copy of an existing Standard database.
    text: az sql db copy -g mygroup -s myserver -n originalDb --dest-name newDb --service-objective S0
  - name: Create a database with GeneralPurpose edition, Gen4 hardware, and 1 vcore as a copy of an existing GeneralPurpose database.
    text: az sql db copy -g mygroup -s myserver -n originalDb --dest-name newDb -f Gen4 -c 1
"""

helps['sql db create'] = """
type: command
short-summary: Create a database.
long-summary: A full list of performance level options can be seen by executing `az sql db list-editions -a -o table -l LOCATION`.
examples:
  - name: Create a Standard S0 database.
    text: az sql db create -g mygroup -s myserver -n mydb --service-objective S0
  - name: Create a database with GeneralPurpose edition, Gen4 hardware and 1 vcore
    text: az sql db create -g mygroup -s myserver -n mydb -e GeneralPurpose -f Gen4 -c 1
  - name: Create a database with zone redundancy enabled
    text: az sql db create -g mygroup -s myserver -n mydb -z
  - name: Create a database with zone redundancy explicitly disabled
    text: az sql db create -g mygroup -s myserver -n mydb -z false
"""

helps['sql db delete'] = """
type: command
short-summary: Delete a database.
"""

helps['sql db export'] = """
type: command
short-summary: Export a database to a bacpac.
examples:
  - name: Get an SAS key for use in export operation.
    text: |
        az storage blob generate-sas --account-name myAccountName -c myContainer -n myBacpac.bacpac \\
            --permissions w --expiry 2018-01-01T00:00:00Z
  - name: Export bacpac using an SAS key.
    text: |
        az sql db export -s myserver -n mydatabase -g mygroup -p password -u login \\
            --storage-key "?sr=b&sp=rw&se=2018-01-01T00%3A00%3A00Z&sig=mysignature&sv=2015-07-08" \\
            --storage-key-type SharedAccessKey \\
            --storage-uri https://myAccountName.blob.core.windows.net/myContainer/myBacpac.bacpac
  - name: Export bacpac using a storage account key.
    text: |
        az sql db export -s myserver -n mydatabase -g mygroup -p password -u login \\
            --storage-key MYKEY== --storage-key-type StorageAccessKey \\
            --storage-uri https://myAccountName.blob.core.windows.net/myContainer/myBacpac.bacpac
"""

helps['sql db import'] = """
type: command
short-summary: Imports a bacpac into an existing database.
examples:
  - name: Get an SAS key for use in import operation.
    text: |
        az storage blob generate-sas --account-name myAccountName -c myContainer -n myBacpac.bacpac \\
            --permissions r --expiry 2018-01-01T00:00:00Z
  - name: Import bacpac into an existing database using an SAS key.
    text: |
        az sql db import -s myserver -n mydatabase -g mygroup -p password -u login \\
            --storage-key "?sr=b&sp=rw&se=2018-01-01T00%3A00%3A00Z&sig=mysignature&sv=2015-07-08" \\
            --storage-key-type SharedAccessKey \\
            --storage-uri https://myAccountName.blob.core.windows.net/myContainer/myBacpac.bacpac
  - name: Import bacpac into an existing database using a storage account key.
    text: |
        az sql db import -s myserver -n mydatabase -g mygroup -p password -u login --storage-key MYKEY== \\
            --storage-key-type StorageAccessKey \\
            --storage-uri https://myAccountName.blob.core.windows.net/myContainer/myBacpac.bacpac
"""

helps['sql db list'] = """
type: command
short-summary: List databases a server or elastic pool.
"""

helps['sql db list-editions'] = """
type: command
short-summary: Show database editions available for the currently active subscription.
long-summary: Includes available service objectives and storage limits. In order to reduce verbosity, settings to intentionally reduce storage limits are hidden by default.
examples:
  - name: Show all database editions in a location.
    text: az sql db list-editions -l westus -o table
  - name: Show all available database service objectives for Standard edition.
    text: az sql db list-editions -l westus --edition Standard -o table
  - name: Show available max database sizes for P1 service objective
    text: az sql db list-editions -l westus --service-objective P1 --show-details max-size
"""

helps['sql db op'] = """
type: group
short-summary: Manage operations on a database.
"""

helps['sql db op cancel'] = """
type: command
examples:
  - name: Cancel an operation.
    text: az sql db op cancel -g mygroup -s myserver -d mydb -n d2896mydb-2ba8-4c84-bac1-387c430cce40
"""

helps['sql db rename'] = """
type: command
short-summary: Rename a database.
"""

helps['sql db replica'] = """
type: group
short-summary: Manage replication between databases.
"""

helps['sql db replica create'] = """
type: command
short-summary: Create a database as a readable secondary replica of an existing database.
long-summary: A full list of performance level options can be seen by executing `az sql db list-editions -a -o table -l LOCATION`. The secondary database must have the same edition as the primary database.
examples:
  - name: Create a database with performance level S0 as a secondary replica of an existing Standard database.
    text: az sql db replica create -g mygroup -s myserver -n originalDb --partner-server newDb --service-objective S0
  - name: Create a database with GeneralPurpose edition, Gen4 hardware, and 1 vcore as a secondary replica of an existing GeneralPurpose database
    text: az sql db replica create -g mygroup -s myserver -n originalDb --partner-server newDb -f Gen4 -c 1
"""

helps['sql db replica delete-link'] = """
type: command
short-summary: Permanently stop data replication between two database replicas.
"""

helps['sql db replica list-links'] = """
type: command
short-summary: List the replicas of a database and their replication status.
"""

helps['sql db replica set-primary'] = """
type: command
short-summary: Set the primary replica database by failing over from the current primary replica database.
"""

helps['sql db restore'] = """
type: command
short-summary: Create a new database by restoring from a backup.
"""

helps['sql db show'] = """
type: command
short-summary: Get the details for a database.
"""

helps['sql db show-connection-string'] = """
type: command
short-summary: Generates a connection string to a database.
examples:
  - name: Generate connection string for ado.net
    text: az sql db show-connection-string -s myserver -n mydb -c ado.net
"""

helps['sql db tde'] = """
type: group
short-summary: Manage a database's transparent data encryption.
"""

helps['sql db tde set'] = """
type: command
short-summary: Sets a database's transparent data encryption configuration.
"""

helps['sql db threat-policy'] = """
type: group
short-summary: Manage a database's threat detection policies.
"""

helps['sql db threat-policy update'] = """
type: command
short-summary: Update a database's threat detection policy.
long-summary: If the policy is being enabled, storage_account or both storage_endpoint and storage_account_access_key must be specified.
examples:
  - name: Enable by storage account name.
    text: |
        az sql db threat-policy update -g mygroup -s myserver -n mydb \\
            --state Enabled --storage-account mystorage
  - name: Enable by storage endpoint and key.
    text: |
        az sql db threat-policy update -g mygroup -s myserver -n mydb \\
            --state Enabled --storage-endpoint https://mystorage.blob.core.windows.net \\
            --storage-key MYKEY==
  - name: Disable a subset of alert types.
    text: |
        az sql db threat-policy update -g mygroup -s myserver -n mydb \\
            --disabled-alerts Sql_Injection_Vulnerability Access_Anomaly
  - name: Configure email recipients for a policy.
    text: |
        az sql db threat-policy update -g mygroup -s myserver -n mydb \\
            --email-addresses me@examlee.com you@example.com \\
            --email-account-admins Enabled
  - name: Disable a threat policy.
    text: az sql db threat-policy update -g mygroup -s myserver -n mydb --state Disabled
"""

helps['sql db update'] = """
type: command
short-summary: Update a database.
examples:
  - name: Update a database to Standard edition, S0 performance level (10 DTU) by specifying DTU capacity. Note that GeneralPurpose allows a wider range of max size than Standard edition.
    text: az sql db update -g mygroup -s myserver -n mydb --edition Standard --capacity 10 --max-size 250GB
  - name: Update a database to Standard edition, S1 performance level (20 DTU) by specifying performance level name. Note that GeneralPurpose allows a wider range of max size than Standard edition.
    text: az sql db update -g mygroup -s myserver -n mydb --edition Standard --service-objective S1 --max-size 250GB
  - name: Update a database to GeneralPurpose edition, 4 vcores with Gen5 hardware
    text: az sql db update -g mygroup -s myserver -n mydb --edition GeneralPurpose --capacity 4 --family Gen5
  - name: Update database with increased max size
    text: az sql db update -g mygroup -s myserver -n mydb --max-size 500GB
  - name: Update database with zone redundancy enabled
    text: az sql db update -g mygroup -s myserver -n mydb -z
  - name: Update database with zone redundancy explicitly disabled
    text: az sql db update -g mygroup -s myserver -n mydb -z false

"""

helps['sql dw'] = """
type: group
short-summary: Manage data warehouses.
"""

helps['sql dw create'] = """
type: command
short-summary: Create a data warehouse.
"""

helps['sql dw delete'] = """
type: command
short-summary: Delete a data warehouse.
"""

helps['sql dw list'] = """
type: command
short-summary: List data warehouses for a server.
"""

helps['sql dw show'] = """
type: command
short-summary: Get the details for a data warehouse.
"""

helps['sql dw update'] = """
type: command
short-summary: Update a data warehouse.
"""

helps['sql elastic-pool'] = """
type: group
short-summary: Manage elastic pools.
"""

helps['sql elastic-pool create'] = """
type: command
short-summary: Create an elastic pool.
examples:
  - name: Create elastic pool with zone redundancy enabled
    text: az sql elastic-pool create -g mygroup -s myserver -n mypool -z
  - name: Create elastic pool with zone redundancy explicitly disabled
    text: az sql elastic-pool create -g mygroup -s myserver -n mypool -z false
  - name: Create a Standard 100 DTU elastic pool.
    text: az sql elastic-pool create -g mygroup -s myserver -n mydb -e Standard -c 100
  - name: Create an elastic pool with GeneralPurpose edition, Gen4 hardware and 1 vcore.
    text: az sql elastic-pool create -g mygroup -s myserver -n mydb -e GeneralPurpose -f Gen4 -c 1
"""

helps['sql elastic-pool list-editions'] = """
type: command
short-summary: List elastic pool editions available for the active subscription.
long-summary: Also includes available pool DTU settings, storage limits, and per database settings. In order to reduce verbosity, additional storage limits and per database settings are hidden by default.
examples:
  - name: Show all elastic pool editions and pool DTU limits in the West US region.
    text: az sql elastic-pool list-editions -l westus -o table
  - name: Show all pool DTU limits for Standard edition in the West US region.
    text: az sql elastic-pool list-editions -l westus --edition Standard -o table
  - name: Show available max sizes for elastic pools with at least 100 DTUs in the West US region.
    text: az sql elastic-pool list-editions -l westus --dtu 100 --show-details max-size -o table
  - name: Show available per database settings for Standard 100 DTU elastic pools in the West US region.
    text: az sql elastic-pool list-editions -l westus --edition Standard --dtu 100 -o table --show-details db-min-dtu db-max-dtu db-max-size
"""

helps['sql elastic-pool op'] = """
type: group
short-summary: Manage operations on an elastic pool.
"""

helps['sql elastic-pool op cancel'] = """
type: command
examples:
  - name: Cancel an operation.
    text: az sql elastic-pool op cancel -g mygroup -s myserver --elastic-pool myelasticpool -n d2896mydb-2ba8-4c84-bac1-387c430cce40
"""

helps['sql elastic-pool update'] = """
type: command
short-summary: Update an elastic pool.
examples:
  - name: Update elastic pool with zone redundancy enabled
    text: az sql elastic-pool update -g mygroup -s myserver -n mypool -z
  - name: Update elastic pool with zone redundancy explicitly disabled
    text: az sql elastic-pool update -g mygroup -s myserver -n mypool -z false
"""

helps['sql failover-group'] = """
type: group
short-summary: Manage SQL Failover Groups.
"""

helps['sql failover-group create'] = """
type: command
short-summary: Creates a failover group.
"""

helps['sql failover-group set-primary'] = """
type: command
short-summary: Set the primary of the failover group by failing over all databases from the current primary server.
"""

helps['sql failover-group update'] = """
type: command
short-summary: Updates the failover group.
"""

helps['sql mi'] = """
type: group
short-summary: Manage SQL managed instances.
"""

helps['sql mi create'] = """
type: command
short-summary: Create a managed instance.
examples:
  - name: Create a managed instance with specified parameters and with identity
    text: az sql mi create -g mygroup -n myinstance -l mylocation -i -u myusername -p mypassword --license-type LicenseIncluded --subnet /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/{VNETName}/subnets/{SubnetName} --capacity 8 --storage 32GB --edition GeneralPurpose --family Gen4
  - name: Create a managed instance with minimal set of parameters
    text: az sql mi create -g mygroup -n myinstance -l mylocation -i -u myusername -p mypassword --subnet /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/{VNETName}/subnets/{SubnetName}
"""

helps['sql mi delete'] = """
type: command
short-summary: Delete a managed instance.
examples:
  - name: Delete a managed instance
    text: az sql mi delete -g mygroup -n myinstance --yes
"""

helps['sql mi key'] = """
type: group
short-summary: Manage a SQL Instance's keys.
"""

helps['sql mi key create'] = """
type: command
short-summary: Creates a SQL Instance key.
"""

helps['sql mi key delete'] = """
type: command
short-summary: Deletes a SQL Instance key.
"""

helps['sql mi key show'] = """
type: command
short-summary: Shows a SQL Instance key.
"""

helps['sql mi list'] = """
type: command
short-summary: List available managed instances.
examples:
  - name: List all managed instances in the current subscription.
    text: az sql mi list
  - name: List all managed instances in a resource group.
    text: az sql mi list -g mygroup
"""

helps['sql mi show'] = """
type: command
short-summary: Get the details for a managed instance.
examples:
  - name: Get the details for a managed instance
    text: az sql mi show -g mygroup -n myinstance
"""

helps['sql mi tde-key'] = """
type: group
short-summary: Manage a SQL Instance's encryption protector.
"""

helps['sql mi tde-key set'] = """
type: command
short-summary: Sets the SQL Instance's encryption protector.
"""

helps['sql mi update'] = """
type: command
short-summary: Update a managed instance.
examples:
  - name: Updates a mi with specified parameters and with identity
    text: az sql mi update -g mygroup -n myinstance -i -p mypassword --license-type mylicensetype --capacity vcorecapacity --storage storagesize
"""

helps['sql midb'] = """
type: group
short-summary: Manage SQL managed instance databases.
"""

helps['sql midb create'] = """
type: command
short-summary: Create a managed database.
examples:
  - name: Create a managed database with specified collation
    text: az sql midb create -g mygroup --mi myinstance -n mymanageddb --collation Latin1_General_100_CS_AS_SC
"""

helps['sql midb delete'] = """
type: command
short-summary: Delete a managed database.
examples:
  - name: Delete a managed database
    text: az sql midb delete -g mygroup --mi myinstance -n mymanageddb --yes
"""

helps['sql midb list'] = """
type: command
short-summary: List maanged databases on a managed instance.
examples:
  - name: List managed databases on a managed instance
    text: az sql midb list -g mygroup --mi myinstance
"""

helps['sql midb restore'] = """
type: command
short-summary: Restore a managed database.
examples:
  - name: Restore a managed database using Point in time restore
    text: az sql midb restore -g mygroup --mi myinstance -n mymanageddb --dest-name targetmidb --time "2018-05-20T05:34:22"
"""

helps['sql midb show'] = """
type: command
short-summary: Get the details for a managed database.
examples:
  - name: Get the details for a managed database
    text: az sql midb show -g mygroup --mi myinstance -n mymanageddb
"""

helps['sql server'] = """
type: group
short-summary: Manage SQL servers.
"""

helps['sql server ad-admin'] = """
type: group
short-summary: Manage a server's Active Directory administrator.
"""

helps['sql server ad-admin create'] = """
type: command
short-summary: Create a new server Active Directory administrator.
"""

helps['sql server ad-admin update'] = """
type: command
short-summary: Update an existing server Active Directory administrator.
"""

helps['sql server conn-policy'] = """
type: group
short-summary: Manage a server's connection policy.
"""

helps['sql server conn-policy show'] = """
type: command
short-summary: Gets a server's secure connection policy.
"""

helps['sql server conn-policy update'] = """
type: command
short-summary: Updates a server's secure connection policy.
"""

helps['sql server create'] = """
type: command
short-summary: Create a server.
examples:
  - name: Create a server.
    text: az sql server create -l westus -g mygroup -n myserver -u myadminuser -p myadminpassword
"""

helps['sql server dns-alias'] = """
type: group
short-summary: Manage a server's DNS aliases.
"""

helps['sql server dns-alias set'] = """
type: command
short-summary: Sets a server to which DNS alias should point
"""

helps['sql server firewall-rule'] = """
type: group
short-summary: Manage a server's firewall rules.
"""

helps['sql server firewall-rule create'] = """
type: command
short-summary: Create a firewall rule.
examples:
  - name: Create a firewall rule
    text: az sql server firewall-rule create -g mygroup -s myserver -n myrule --start-ip-address 1.2.3.4 --end-ip-address 5.6.7.8
  - name: Create a firewall rule that allows access from Azure services
    text: az sql server firewall-rule create -g mygroup -s myserver -n myrule --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0
"""

helps['sql server firewall-rule list'] = """
type: command
short-summary: List a server's firewall rules.
examples:
  - name: List a server's firewall rules
    text: az sql server firewall-rule list -g mygroup -s myserver
"""

helps['sql server firewall-rule show'] = """
type: command
short-summary: Shows the details for a firewall rule.
examples:
  - name: Show a firewall rule
    text: az sql server firewall-rule show -g mygroup -s myserver -n myrule
"""

helps['sql server firewall-rule update'] = """
type: command
short-summary: Update a firewall rule.
examples:
  - name: Update a firewall rule
    text: az sql server firewall-rule update -g mygroup -s myserver -n myrule --start-ip-address 9.8.7.6 --end-ip-address 5.4.3.2
"""

helps['sql server key'] = """
type: group
short-summary: Manage a server's keys.
"""

helps['sql server key create'] = """
type: command
short-summary: Creates a server key.
"""

helps['sql server key delete'] = """
type: command
short-summary: Deletes a server key.
"""

helps['sql server key show'] = """
type: command
short-summary: Shows a server key.
"""

helps['sql server list'] = """
type: command
short-summary: List available servers.
examples:
  - name: List all servers in the current subscription.
    text: az sql server list
  - name: List all servers in a resource group.
    text: az sql server list -g mygroup
"""

helps['sql server tde-key'] = """
type: group
short-summary: Manage a server's encryption protector.
"""

helps['sql server tde-key set'] = """
type: command
short-summary: Sets the server's encryption protector.
"""

helps['sql server update'] = """
type: command
short-summary: Update a server.
"""

helps['sql server vnet-rule'] = """
type: group
short-summary: Manage a server's virtual network rules.
"""

helps['sql server vnet-rule create'] = """
type: command
short-summary: Create a virtual network rule to allows access to an Azure SQL server.

examples:
  - name: Create a vnet rule by providing the subnet id.
    text: |
        az sql server vnet-rule create --server MyAzureSqlServer --name MyVNetRule \\
          -g MyResourceGroup --subnet /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Network/virtualNetworks/{VNETName}/subnets/{SubnetName}
  - name: Create a vnet rule by providing the vnet and subnet name. The subnet id is created by taking the resource group name and subscription id of the SQL server.
    text: |
        az sql server vnet-rule create --server MyAzureSqlServer --name MyVNetRule \\
            -g MyResourceGroup --subnet subnetName --vnet-name vnetName
"""

helps['sql server vnet-rule update'] = """
type: command
short-summary: Update a virtual network rule.
"""

helps['sql server wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the SQL server is met.
"""

helps['sql virtual-cluster'] = """
type: group
short-summary: Manage SQL virtual clusters.
"""

helps['sql virtual-cluster delete'] = """
type: command
short-summary: Delete a virtual cluster.
examples:
  - name: Delete a virtual cluster
    text: az sql virtual-cluster delete -g mygroup -n mycluster
"""

helps['sql virtual-cluster list'] = """
type: command
short-summary: List available virtual clusters.
examples:
  - name: List all virtual clusters in the current subscription.
    text: az sql virtual-cluster list
  - name: List all virtual clusters in a resource group.
    text: az sql virtual-cluster list -g mygroup
"""

helps['sql virtual-cluster show'] = """
type: command
short-summary: Get the details for a virtual cluster.
examples:
  - name: Get the details for a virtual cluster
    text: az sql virtual-cluster show -g mygroup -n mycluster
"""

helps['sql vm'] = """
type: group
short-summary: Manage SQL virtual machines.
"""

helps['sql vm add-to-group'] = """
type: command
short-summary: Adds SQL virtual machine to a SQL virtual machine group.
examples:
  - name: Add SQL virtual machine to a group.
    text: >
        az sql vm add-to-group -n sqlvm -g myresourcegroup --sqlvm-group sqlvmgroup --bootstrap-acc-pwd {bootstrappassword} --operator-acc-pwd {operatorpassword} --service-acc-pwd {servicepassword}
"""

helps['sql vm create'] = """
type: command
short-summary: Creates a SQL virtual machine.
parameters:
  - name: --name -n
    short-summary: Name of the SQL virtual machine. The name of the new SQL virtual machine must be equal to the underlying virtual machine created from SQL marketplace image.
examples:
  - name: Create a SQL virtual machine with AHUB billing tag.
    text: >
        az sql vm create -n sqlvm -g myresourcegroup -l eastus --license-type AHUB
  - name: Create a SQL virtual machine with specific sku type and license type.
    text: >
        az sql vm create -n sqlvm -g myresourcegroup -l eastus --image-sku Enterprise --license-type AHUB
  - name: Create a SQL virtual machine with NoAgent type, only valid for EOS SQL 2008 and SQL 2008 R2.
    text: >
        az sql vm create -n sqlvm -g myresourcegroup -l eastus --license-type AHUB --sql-mgmt-type NoAgent --image-sku Enterprise --image-offer SQL2008-WS2008R2
  - name: Enable R services in SQL2016 onwards.
    text: >
        az sql vm create -n sqlvm -g myresourcegroup -l eastus --license-type PAYG --sql-mgmt-type Full --enable-r-services true
  - name: Create SQL virtual machine and configure auto backup settings.
    text: >
        az sql vm create -n sqlvm -g myresourcegroup -l eastus --license-type PAYG --sql-mgmt-type Full --backup-schedule-type manual --full-backup-frequency Weekly --full-backup-start-hour 2 --full-backup-duration 2 --sa-key {storageKey} --storage-account 'https://storageacc.blob.core.windows.net/' --retention-period 30 --log-backup-frequency 60
  - name: Create SQL virtual machine and configure auto patching settings.
    text: >
        az sql vm create -n sqlvm -g myresourcegroup -l eastus --license-type PAYG --sql-mgmt-type Full --day-of-week sunday --maintenance-window-duration 60 --maintenance-window-start-hour 2
  - name: Create SQL virtual machine and configure SQL connectivity settings.
    text: >
        az sql vm create -n sqlvm -g myresourcegroup -l eastus --license-type PAYG --sql-mgmt-type Full --connectivity-type private --port 1433 --sql-auth-update-username {newlogin} --sql-auth-update-pwd {sqlpassword}
"""

helps['sql vm group'] = """
type: group
short-summary: Manage SQL virtual machine groups.
"""

helps['sql vm group ag-listener'] = """
type: group
short-summary: Manage SQL availability group listeners.
"""

helps['sql vm group ag-listener create'] = """
type: command
short-summary: Creates an availability group listener.
examples:
  - name: Create an availability group listener. Note the SQL virtual machines are in the same resource group as the SQL virtual machine group.
    text: >
        az sql vm group ag-listener create -n aglistenertest -g myresourcegroup --ag-name agname --group-name sqlvmgroup --ip-address 10.0.0.11 --load-balancer '/subscriptions/{yoursubscription}/resourceGroups/{yourrg}/providers/Microsoft.Network/loadBalancers/{lbname}' --probe-port 59999 --subnet '/subscriptions/{yoursubscription}/resourceGroups/{yourrg}/providers/Microsoft.Network/virtualNetworks/{vnname}/subnets/{subnetname}' --sqlvms sqlvm1 sqlvm2
  - name: Create an availability group listener. Note all resources are in the same resource group.
    text: >
        az sql vm group ag-listener create -n aglistenertest -g myresourcegroup --ag-name agname --group-name sqlvmgroup --ip-address 10.0.0.11 --load-balancer {lbname} --probe-port 59999 --subnet {subnetname} --vnet-name {vnname} --sqlvms sqlvm1 sqlvm2
"""

helps['sql vm group ag-listener update'] = """
type: command
short-summary: Updates an availability group listener.
examples:
  - name: Replace the SQL virtual machines that were in the availability group.
    text: >
        az sql vm group ag-listener update -n aglistenertest -g myresourcegroup --sqlvms sqlvm3 sqlvm4 --group-name mygroup
"""

helps['sql vm group create'] = """
type: command
short-summary: Creates a SQL virtual machine group.
examples:
  - name: Create a SQL virtual machine group for SQL2016-WS2016 Enterprise virtual machines.
    text: >
        az sql vm group create -n sqlvmgroup -l eastus -g myresourcegroup --image-offer SQL2016-WS2016 --image-sku Enterprise --domain-fqdn Domain.com --operator-acc testop --service-acc testservice --sa-key {PublicKey} --storage-account 'https://storacc.blob.core.windows.net/'
"""

helps['sql vm group update'] = """
type: command
short-summary: Updates a SQL virtual machine group if there are not SQL virtual machines attached to the group.
examples:
  - name: Update an empty SQL virtual machine group operator account.
    text: >
        az sql vm group update -n sqlvmgroup -g myresourcegroup --operator-acc testop
  - name: Update an empty SQL virtual machine group storage account and key.
    text: >
        az sql vm group update -n sqlvmgroup -g myresourcegroup --sa-key {PublicKey} --storage-account 'https://newstoracc.blob.core.windows.net/'
"""

helps['sql vm remove-from-group'] = """
type: command
short-summary: Remove SQL virtual machine from its current SQL virtual machine group.
examples:
  - name: Remove SQL virtual machine from a group.
    text: >
        az sql vm remove-from-group -n sqlvm -g myresourcegroup
"""

helps['sql vm update'] = """
type: command
short-summary: Updates the properties of a SQL virtual machine.
examples:
  - name: Add or update a tag.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --set tags.tagName=tagValue
  - name: Remove a tag.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --remove tags.tagName
  - name: Update a SQL virtual machine with specific sku type.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --image-sku Enterprise
  - name: Update a SQL virtual machine manageability from LightWeight to Full.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --sql-mgmt-type Full --yes
  - name: Update SQL virtual machine auto backup settings.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --backup-schedule-type manual --full-backup-frequency Weekly --full-backup-start-hour 2 --full-backup-duration 2 --sa-key {storageKey} --storage-account 'https://storageacc.blob.core.windows.net/' --retention-period 30 --log-backup-frequency 60
  - name: Disable SQL virtual machine auto backup settings.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --enable-auto-backup false
  - name: Update SQL virtual machine auto patching settings.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --day-of-week sunday --maintenance-window-duration 60 --maintenance-window-start-hour 2
  - name: Disable SQL virtual machine auto patching settings.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --enable-auto-patching false
  - name: Update a SQL virtual machine billing tag to AHUB.
    text: >
        az sql vm update -n sqlvm -g myresourcegroup --license-type AHUB
"""

helps['storage'] = """
type: group
short-summary: Manage Azure Cloud Storage resources.
"""

helps['storage account'] = """
type: group
short-summary: Manage storage accounts.
"""

helps['storage account create'] = """
type: command
short-summary: Create a storage account.
long-summary: >
    The SKU of the storage account defaults to 'Standard_RAGRS'.
examples:
  - name: Create a storage account 'MyStorageAccount' in resource group 'MyResourceGroup' in the West US region with locally redundant storage.
    text: az storage account create -n MyStorageAccount -g MyResourceGroup -l westus --sku Standard_LRS
    unsupported-profiles: 2017-03-09-profile
  - name: Create a storage account 'MyStorageAccount' in resource group 'MyResourceGroup' in the West US region with locally redundant storage.
    text: az storage account create -n MyStorageAccount -g MyResourceGroup -l westus --account-type Standard_LRS
    supported-profiles: 2017-03-09-profile
"""

helps['storage account delete'] = """
type: command
short-summary: Delete a storage account.
examples:
  - name: Delete a storage account using a resource ID.
    text: az storage account delete --ids /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Storage/storageAccounts/{StorageAccount}
  - name: Delete a storage account using an account name and resource group.
    text: az storage account delete -n MyStorageAccount -g MyResourceGroup
"""

helps['storage account generate-sas'] = """
type: command
parameters:
  - name: --services
    short-summary: 'The storage services the SAS is applicable for. Allowed values: (b)lob (f)ile (q)ueue (t)able. Can be combined.'
  - name: --resource-types
    short-summary: 'The resource types the SAS is applicable for. Allowed values: (s)ervice (c)ontainer (o)bject. Can be combined.'
  - name: --expiry
    short-summary: Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes invalid.
  - name: --start
    short-summary: Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes valid. Defaults to the time of the request.
  - name: --account-name
    short-summary: 'Storage account name. Must be used in conjunction with either storage account key or a SAS token. Environment Variable: AZURE_STORAGE_ACCOUNT'
examples:
  - name: Generate a sas token for the account that is valid for queue and table services on Linux.
    text: |
        end=`date -u -d "30 minutes" '+%Y-%m-%dT%H:%MZ'`
        az storage account generate-sas --permissions cdlruwap --account-name MyStorageAccount --services qt --resource-types sco --expiry $end -o tsv
  - name: Generate a sas token for the account that is valid for queue and table services on MacOS.
    text: |
        end=`date -v+30M '+%Y-%m-%dT%H:%MZ'`
        az storage account generate-sas --permissions cdlruwap --account-name MyStorageAccount --services qt --resource-types sco --expiry $end -o tsv
  - name: Generates a shared access signature for the account (autogenerated)
    text: az storage account generate-sas --account-key 00000000 --account-name MyStorageAccount --expiry 2020-01-01 --https-only --permissions acuw --resource-types co --services bfqt
    crafted: true
"""

helps['storage account keys'] = """
type: group
short-summary: Manage storage account keys.
"""

helps['storage account keys list'] = """
type: command
short-summary: List the primary and secondary keys for a storage account.
examples:
  - name: List the primary and secondary keys for a storage account.
    text: az storage account keys list -g MyResourceGroup -n MyStorageAccount
"""

helps['storage account list'] = """
type: command
short-summary: List storage accounts.
examples:
  - name: List all storage accounts in a subscription.
    text: az storage account list
  - name: List all storage accounts in a resource group.
    text: az storage account list -g MyResourceGroup
"""

helps['storage account management-policy'] = """
type: group
short-summary: Manage storage account management policies.
"""

helps['storage account management-policy create'] = """
type: command
short-summary: Creates the data policy rules associated with the specified storage account.
"""

helps['storage account management-policy update'] = """
type: command
short-summary: Updates the data policy rules associated with the specified storage account.
"""

helps['storage account network-rule'] = """
type: group
short-summary: Manage network rules.
"""

helps['storage account network-rule add'] = """
type: command
short-summary: Add a network rule.
long-summary: >
    Rules can be created for an IPv4 address, address range (CIDR format), or a virtual network subnet.
examples:
  - name: Create a rule to allow a specific address-range.
    text: az storage account network-rule add -g myRg --account-name mystorageaccount --ip-address 23.45.1.0/24
  - name: Create a rule to allow access for a subnet.
    text: az storage account network-rule add -g myRg --account-name mystorageaccount --vnet myvnet --subnet mysubnet
"""

helps['storage account network-rule list'] = """
type: command
short-summary: List network rules.
examples:
  - name: List network rules. (autogenerated)
    text: az storage account network-rule list --account-name MyAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['storage account network-rule remove'] = """
type: command
short-summary: Remove a network rule.
examples:
  - name: Remove a network rule. (autogenerated)
    text: az storage account network-rule remove --account-name MyAccount --resource-group MyResourceGroup --subnet mysubnet
    crafted: true
  - name: Remove a network rule. (autogenerated)
    text: az storage account network-rule remove --account-name MyAccount --ip-address 23.45.1.0/24 --resource-group MyResourceGroup
    crafted: true
"""

helps['storage account revoke-delegation-keys'] = """
type: command
short-summary: Revoke all user delegation keys for a storage account.
examples:
  - name: Revoke all user delegation keys for a storage account by resource ID.
    text: az storage account revoke-delegation-keys --ids /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Storage/storageAccounts/{StorageAccount}
  - name: Revoke all user delegation keys for a storage account 'MyStorageAccount' in resource group 'MyResourceGroup' in the West US region with locally redundant storage.
    text: az storage account revoke-delegation-keys -n MyStorageAccount -g MyResourceGroup
"""

helps['storage account show'] = """
type: command
short-summary: Show storage account properties.
examples:
  - name: Show properties for a storage account by resource ID.
    text: az storage account show --ids /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Storage/storageAccounts/{StorageAccount}
  - name: Show properties for a storage account using an account name and resource group.
    text: az storage account show -g MyResourceGroup -n MyStorageAccount
"""

helps['storage account show-connection-string'] = """
type: command
short-summary: Get the connection string for a storage account.
examples:
  - name: Get a connection string for a storage account.
    text: az storage account show-connection-string -g MyResourceGroup -n MyStorageAccount
  - name: Get the connection string for a storage account. (autogenerated)
    text: az storage account show-connection-string --name MyStorageAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['storage account show-usage'] = """
type: command
short-summary: Show the current count and limit of the storage accounts under the subscription.
examples:
  - name: Show the current count and limit of the storage accounts under the subscription. (autogenerated)
    text: az storage account show-usage --location westus2
    crafted: true
"""

helps['storage account update'] = """
type: command
short-summary: Update the properties of a storage account.
examples:
  - name: Update the properties of a storage account. (autogenerated)
    text: az storage account update --default-action Allow --name MyStorageAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['storage blob'] = """
type: group
short-summary: Manage object storage for unstructured data (blobs).
"""

helps['storage blob copy'] = """
type: group
short-summary: Manage blob copy operations. Use `az storage blob show` to check the status of the blobs.
"""

helps['storage blob copy start'] = """
type: command
short-summary: Copies a blob asynchronously. Use `az storage blob show` to check the status of the blobs.
examples:
  - name: Copies a blob asynchronously. Use `az storage blob show` to check the status of the blobs. (autogenerated)
    text: az storage blob copy start --account-key 00000000 --account-name MyAccount --destination-blob MyDestinationBlob --destination-container MyDestinationContainer --source-uri https://storage.blob.core.windows.net/photos
    crafted: true
"""

helps['storage blob copy start-batch'] = """
type: command
short-summary: Copy multiple blobs or files to a blob container. Use `az storage blob show` to check the status of the blobs.
parameters:
  - name: --destination-container -c
    type: string
    short-summary: The blob container where the selected source files or blobs will be copied to.
  - name: --pattern
    type: string
    short-summary: The pattern used for globbing files or blobs in the source. The supported patterns are '*', '?', '[seq', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: List the files or blobs to be uploaded. No actual data transfer will occur.
  - name: --source-account-name
    type: string
    short-summary: The source storage account from which the files or blobs are copied to the destination. If omitted, the source account is used.
  - name: --source-account-key
    type: string
    short-summary: The account key for the source storage account.
  - name: --source-container
    type: string
    short-summary: The source container from which blobs are copied.
  - name: --source-share
    type: string
    short-summary: The source share from which files are copied.
  - name: --source-uri
    type: string
    short-summary: A URI specifying a file share or blob container from which the files or blobs are copied.
    long-summary: If the source is in another account, the source must either be public or be authenticated by using a shared access signature.
  - name: --source-sas
    type: string
    short-summary: The shared access signature for the source storage account.
examples:
  - name: Copy multiple blobs or files to a blob container. Use `az storage blob show` to check the status of the blobs. (autogenerated)
    text: az storage blob copy start-batch --account-key 00000000 --account-name MyAccount --destination-container MyDestinationContainer --source-account-key MySourceKey --source-account-name MySourceAccount --source-container MySourceContainer
    crafted: true
"""

helps['storage blob delete'] = """
type: command
short-summary: Mark a blob or snapshot for deletion.
long-summary: >
    The blob is marked for later deletion during garbage collection.  In order to delete a blob, all of its snapshots must also be deleted.
    Both can be removed at the same time.
examples:
  - name: Delete a blob.
    text: az storage blob delete -c MyContainer -n MyBlob
"""

helps['storage blob delete-batch'] = """
type: command
short-summary: Delete blobs from a blob container recursively.
parameters:
  - name: --source -s
    type: string
    short-summary: The blob container from where the files will be deleted.
    long-summary: The source can be the container URL or the container name. When the source is the container URL, the storage account name will be parsed from the URL.
  - name: --pattern
    type: string
    short-summary: The pattern used for globbing files or blobs in the source. The supported patterns are '*', '?', '[seq]', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: Show the summary of the operations to be taken instead of actually deleting the file(s).
    long-summary: If this is specified, it will ignore all the Precondition Arguments that include --if-modified-since and --if-unmodified-since. So the file(s) will be deleted with the command without --dryrun may be different from the result list with --dryrun flag on.
  - name: --if-match
    type: string
    short-summary: An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
  - name: --if-none-match
    type: string
    short-summary: An ETag value, or the wildcard character (*).
    long-summary: Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
examples:
  - name: Delete all blobs ending with ".py" in a container that have not been modified for 10 days.
    text: |
        date=`date -d "10 days ago" '+%Y-%m-%dT%H:%MZ'`
        az storage blob delete-batch -s MyContainer --account-name MyStorageAccount --pattern *.py --if-unmodified-since $date
"""

helps['storage blob download-batch'] = """
type: command
short-summary: Download blobs from a blob container recursively.
parameters:
  - name: --source -s
    type: string
    short-summary: The blob container from where the files will be downloaded.
    long-summary: The source can be the container URL or the container name. When the source is the container URL, the storage account name will be parsed from the URL.
  - name: --destination -d
    type: string
    short-summary: The existing destination folder for this download operation.
  - name: --pattern
    type: string
    short-summary: The pattern used for globbing files or blobs in the source. The supported patterns are '*', '?', '[seq]', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: Show the summary of the operations to be taken instead of actually downloading the file(s).
examples:
  - name: Download all blobs that end with .py
    text: az storage blob download-batch -d . --pattern *.py -s MyContainer --account-name MyStorageAccount
"""

helps['storage blob exists'] = """
type: command
short-summary: Check for the existence of a blob in a container.
parameters:
  - name: --name -n
    short-summary: The blob name.
examples:
  - name: Check for the existence of a blob in a container. (autogenerated)
    text: az storage blob exists --account-key 00000000 --account-name MyAccount --container-name MyContainer --name MyBlob
    crafted: true
"""

helps['storage blob generate-sas'] = """
type: command
short-summary: Generates a shared access signature for the blob.
examples:
  - name: Generate a sas token for a blob with read-only permissions.
    text: |
        end=`date -u -d "30 minutes" '+%Y-%m-%dT%H:%MZ'`
        az storage blob generate-sas --account-name MyStorageAccount -c MyContainer -n MyBlob --permissions r --expiry $end --https-only
  - name: Generates a shared access signature for the blob. (autogenerated)
    text: az storage blob generate-sas --account-key 00000000 --account-name MyStorageAccount --container-name MyContainer --expiry 2018-01-01T00:00:00Z --name MyBlob --permissions r
    crafted: true
"""

helps['storage blob incremental-copy'] = """
type: group
short-summary: Manage blob incremental copy operations.
"""

helps['storage blob incremental-copy start'] = """
type: command
short-summary: Copies an incremental copy of a blob asynchronously.
long-summary: This operation returns a copy operation properties object, including a copy ID you can use to check or abort the copy operation. The Blob service copies blobs on a best-effort basis. The source blob for an incremental copy operation must be a page blob. Call get_blob_properties on the destination blob to check the status of the copy operation. The final blob will be committed when the copy completes.
examples:
  - name: Upload all files that end with .py unless blob exists and has been modified since given date.
    text: az storage blob incremental-copy start --source-container MySourceContainer --source-blob MyBlob --source-account-name MySourceAccount --source-account-key MySourceKey --source-snapshot MySnapshot --destination-container MyDestinationContainer --destination-blob MyDestinationBlob
"""

helps['storage blob lease'] = """
type: group
short-summary: Manage storage blob leases.
"""

helps['storage blob list'] = """
type: command
short-summary: List blobs in a given container.
parameters:
  - name: --include
    short-summary: 'Specifies additional datasets to include: (c)opy-info, (m)etadata, (s)napshots, (d)eleted-soft. Can be combined.'
examples:
  - name: List all storage blobs in a container whose names start with 'foo'; will match names such as 'foo', 'foobar', and 'foo/bar'
    text: az storage blob list -c MyContainer --prefix foo
"""

helps['storage blob metadata'] = """
type: group
short-summary: Manage blob metadata.
"""

helps['storage blob service-properties'] = """
type: group
short-summary: Manage storage blob service properties.
"""

helps['storage blob service-properties delete-policy'] = """
type: group
short-summary: Manage storage blob delete-policy service properties.
"""

helps['storage blob service-properties delete-policy show'] = """
type: command
short-summary: Show the storage blob delete-policy.
examples:
  - name: Show the storage blob delete-policy. (autogenerated)
    text: az storage blob service-properties delete-policy show --account-name MyAccount
    crafted: true
"""

helps['storage blob service-properties delete-policy update'] = """
type: command
short-summary: Update the storage blob delete-policy.
examples:
  - name: Update the storage blob delete-policy. (autogenerated)
    text: az storage blob service-properties delete-policy update --account-name MyAccount --days-retained 7 --enable true
    crafted: true
"""

helps['storage blob service-properties update'] = """
type: command
short-summary: Update storage blob service properties.
examples:
  - name: Update storage blob service properties. (autogenerated)
    text: az storage blob service-properties update --404-document error.html --account-name MyAccount --index-document index.html --static-website true
    crafted: true
"""

helps['storage blob set-tier'] = """
type: command
short-summary: Set the block or page tiers on the blob.
parameters:
  - name: --type -t
    short-summary: The blob type
  - name: --tier
    short-summary: The tier value to set the blob to.
  - name: --timeout
    short-summary: The timeout parameter is expressed in seconds. This method may make multiple calls to the Azure service and the timeout will apply to each call individually.
long-summary: >
    For block blob this command only supports block blob on standard storage accounts.
    For page blob, this command only supports for page blobs on premium accounts.
examples:
  - name: Set the block or page tiers on the blob. (autogenerated)
    text: az storage blob set-tier --account-key 00000000 --account-name MyAccount --container-name MyContainer --name MyBlob --tier P10
    crafted: true
"""

helps['storage blob show'] = """
type: command
short-summary: Get the details of a blob.
examples:
  - name: Show all properties of a blob.
    text: az storage blob show -c MyContainer -n MyBlob
  - name: Get the details of a blob (autogenerated)
    text: az storage blob show --account-name MyAccount --container-name MyContainer --name MyBlob
    crafted: true
"""

helps['storage blob sync'] = """
type: command
short-summary: Sync blobs recursively to a storage blob container.
long-summary: Sync command depends on Azcopy, which only works for 64-bit Operating System now. We will support 32-bit Operating System soon.
examples:
  - name: Sync a single blob to a container.
    text: az storage blob sync -c MyContainer --account-name MyStorageAccount -s "path/to/file" -d NewBlob
  - name: Sync a directory to a container.
    text: az storage blob sync -c MyContainer --account-name MyStorageAccount -s "path/to/directory"
"""

helps['storage blob upload'] = """
type: command
short-summary: Upload a file to a storage blob.
long-summary: Creates a new blob from a file path, or updates the content of an existing blob with automatic chunking and progress notifications.
parameters:
  - name: --type -t
    short-summary: Defaults to 'page' for *.vhd files, or 'block' otherwise.
  - name: --maxsize-condition
    short-summary: The max length in bytes permitted for an append blob.
  - name: --validate-content
    short-summary: Specifies that an MD5 hash shall be calculated for each chunk of the blob and verified by the service when the chunk has arrived.
  - name: --tier
    short-summary: A page blob tier value to set the blob to. The tier correlates to the size of the blob and number of allowed IOPS. This is only applicable to page blobs on premium storage accounts.
examples:
  - name: Upload to a blob.
    text: az storage blob upload -f /path/to/file -c MyContainer -n MyBlob
"""

helps['storage blob upload-batch'] = """
type: command
short-summary: Upload files from a local directory to a blob container.
parameters:
  - name: --source -s
    type: string
    short-summary: The directory where the files to be uploaded are located.
  - name: --destination -d
    type: string
    short-summary: The blob container where the files will be uploaded.
    long-summary: The destination can be the container URL or the container name. When the destination is the container URL, the storage account name will be parsed from the URL.
  - name: --pattern
    type: string
    short-summary: The pattern used for globbing files or blobs in the source. The supported patterns are '*', '?', '[seq]', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: Show the summary of the operations to be taken instead of actually uploading the file(s).
  - name: --if-match
    type: string
    short-summary: An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
  - name: --if-none-match
    type: string
    short-summary: An ETag value, or the wildcard character (*).
    long-summary: Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
  - name: --validate-content
    short-summary: Specifies that an MD5 hash shall be calculated for each chunk of the blob and verified by the service when the chunk has arrived.
  - name: --type -t
    short-summary: Defaults to 'page' for *.vhd files, or 'block' otherwise. The setting will override blob types for every file.
  - name: --maxsize-condition
    short-summary: The max length in bytes permitted for an append blob.
  - name: --lease-id
    short-summary: The active lease id for the blob
examples:
  - name: Upload all files that end with .py unless blob exists and has been modified since given date.
    text: az storage blob upload-batch -d MyContainer --account-name MyStorageAccount -s directory_path --pattern *.py --if-unmodified-since 2018-08-27T20:51Z
"""

helps['storage blob url'] = """
type: command
short-summary: Create the url to access a blob.
examples:
  - name: Create the url to access a blob (autogenerated)
    text: az storage blob url --connection-string $connectionString --container-name container1 --name blob1
    crafted: true
  - name: Create the url to access a blob (autogenerated)
    text: az storage blob url --account-name storageacct --container-name container1 --name blob1
    crafted: true
"""

helps['storage container'] = """
type: group
short-summary: Manage blob storage containers.
"""

helps['storage container create'] = """
type: command
short-summary: Create a container in a storage account.
long-summary: >
    By default, container data is private ("off") to the account owner. Use "blob" to allow public read access for blobs.
    Use "container" to allow public read and list access to the entire container.
    You can configure the --public-access using `az storage container set-permission -n CONTAINER_NAME --public-access blob/container/off`.
examples:
  - name: Create a storage container in a storage account.
    text: az storage container create -n MyStorageContainer
  - name: Create a storage container in a storage account and return an error if the container already exists.
    text: az storage container create -n MyStorageContainer --fail-on-exist
  - name: Create a storage container in a storage account and allow public read access for blobs.
    text: az storage container create -n MyStorageContainer --public-access blob
"""

helps['storage container delete'] = """
type: command
short-summary: Marks the specified container for deletion.
long-summary: >
    The container and any blobs contained within it are later deleted during garbage collection.
examples:
  - name: Marks the specified container for deletion. (autogenerated)
    text: az storage container delete --account-key 00000000 --account-name MyAccount --name MyContainer
    crafted: true
"""

helps['storage container exists'] = """
type: command
short-summary: Check for the existence of a storage container.
examples:
  - name: Check for the existence of a storage container. (autogenerated)
    text: az storage container exists --account-name MyAccount --name MyContainer
    crafted: true
"""

helps['storage container generate-sas'] = """
type: command
short-summary: Generate a SAS token for a storage container.
examples:
  - name: Generate a sas token for blob container and use it to upload a blob.
    text: |
        end=`date -u -d "30 minutes" '+%Y-%m-%dT%H:%MZ'`
        sas=`az storage container generate-sas -n MyContainer --account-name MyStorageAccount --https-only --permissions dlrw --expiry $end -o tsv`
        az storage blob upload -n MyBlob -c MyContainer --account-name MyStorageAccount -f file.txt --sas-token $sas
  - name: Generates a shared access signature for the container (autogenerated)
    text: az storage container generate-sas --account-key 00000000 --account-name MyStorageAccount --expiry 2020-01-01 --name MyContainer --permissions dlrw
    crafted: true
"""

helps['storage container immutability-policy'] = """
type: group
short-summary: Manage container immutability policies.
"""

helps['storage container lease'] = """
type: group
short-summary: Manage blob storage container leases.
"""

helps['storage container legal-hold'] = """
type: group
short-summary: Manage container legal holds.
"""

helps['storage container legal-hold show'] = """
type: command
short-summary: Get the legal hold properties of a container.
examples:
  - name: Get the legal hold properties of a container. (autogenerated)
    text: az storage container legal-hold show --account-name MyAccount --container-name MyContainer
    crafted: true
"""

helps['storage container list'] = """
type: command
short-summary: List containers in a storage account.
"""

helps['storage container metadata'] = """
type: group
short-summary: Manage container metadata.
"""

helps['storage container policy'] = """
type: group
short-summary: Manage container stored access policies.
"""

helps['storage copy'] = """
type: command
short-summary: Copy files or directories to or from Azure storage.
long-summary: Copy command depends on Azcopy, which only works for 64-bit Operating System now. We will support 32-bit Operating System soon.
examples:
  - name: Upload a single file to Azure Blob using url.
    text: az storage copy -s /path/to/file.txt -d https://[account].blob.core.windows.net/[container]/[path/to/blob]
  - name: Upload a single file to Azure Blob using account name and container name.
    text: az storage copy --source-local-path /path/to/file.txt --destination-account-name mystorageaccount --destination-container mycontainer
  - name: Upload a single file to Azure Blob with MD5 hash of the file content and save it as the blob's Content-MD5 property.
    text: az storage copy -s /path/to/file.txt -d https://[account].blob.core.windows.net/[container]/[path/to/blob] --put-md5
  - name: Upload an entire directory to Azure Blob using url.
    text: az storage copy -s /path/to/dir -d https://[account].blob.core.windows.net/[container]/[path/to/directory] --recursive
  - name: Upload an entire directory to Azure Blob using account name and container name.
    text: az storage copy --source-local-path /path/to/dir --destination-account-name mystorageaccount --destination-container mycontainer --recursive
  - name: Upload a set of files to Azure Blob using wildcards with url.
    text: az storage copy -s /path/*foo/*bar/*.pdf -d https://[account].blob.core.windows.net/[container]/[path/to/directory]
  - name: Upload a set of files to Azure Blob using wildcards with account name and container name.
    text: az storage copy --source-local-path /path/*foo/*bar/*.pdf --destination-account-name mystorageaccount --destination-container mycontainer
  - name: Upload files and directories to Azure Blob using wildcards with url.
    text: az storage copy -s /path/*foo/*bar* -d https://[account].blob.core.windows.net/[container]/[path/to/directory] --recursive
  - name: Upload files and directories to Azure Blob using wildcards with account name and container name.
    text: az storage copy --source-local-path /path/*foo/*bar* --destination-account-name mystorageaccount --destination-container mycontainer --recursive
  - name: Download a single file from Azure Blob using url, and you can also specify your storage account and container information as above.
    text: az storage copy -s https://[account].blob.core.windows.net/[container]/[path/to/blob] -d /path/to/file.txt
  - name: Download an entire directory from Azure Blob, and you can also specify your storage account and container information as above.
    text: az storage copy -s https://[account].blob.core.windows.net/[container]/[path/to/directory] -d /path/to/dir --recursive
  - name: Download a set of files from Azure Blob using wildcards, and you can also specify your storage account and container information as above.
    text: az storage copy -s https://[account].blob.core.windows.net/[container]/foo* -d /path/to/dir --recursive
  - name: Copy a single blob to another blob, and you can also specify the storage account and container information of source and destination as above.
    text: az storage copy -s https://[srcaccount].blob.core.windows.net/[container]/[path/to/blob] -d https://[destaccount].blob.core.windows.net/[container]/[path/to/blob]
  - name: Copy an entire account data from blob account to another blob account, and you can also specify the storage account and container information of source and destination as above.
    text: az storage copy -s https://[srcaccount].blob.core.windows.net -d https://[destaccount].blob.core.windows.net --recursive
  - name: Copy a single object from S3 with access key to blob, and you can also specify your storage account and container information as above.
    text: az storage copy -s https://s3.amazonaws.com/[bucket]/[object] -d https://[destaccount].blob.core.windows.net/[container]/[path/to/blob]
  - name: Copy an entire directory from S3 with access key to blob virtual directory, and you can also specify your storage account and container information as above.
    text: az storage copy -s https://s3.amazonaws.com/[bucket]/[folder] -d https://[destaccount].blob.core.windows.net/[container]/[path/to/directory] --recursive
  - name: Copy all buckets in S3 service with access key to blob account, and you can also specify your storage account information as above.
    text: az storage copy -s https://s3.amazonaws.com/ -d https://[destaccount].blob.core.windows.net --recursive
  - name: Copy all buckets in a S3 region with access key to blob account, and you can also specify your storage account information as above.
    text: az storage copy -s https://s3-[region].amazonaws.com/ -d https://[destaccount].blob.core.windows.net --recursive
  - name: Upload a single file to Azure File Share using url.
    text: az storage copy -s /path/to/file.txt -d https://[account].file.core.windows.net/[share]/[path/to/file]
  - name: Upload a single file to Azure File Share using account name and share name.
    text: az storage copy --source-local-path /path/to/file.txt --destination-account-name mystorageaccount --destination-share myshare
  - name: Upload an entire directory to Azure File Share using url.
    text: az storage copy -s /path/to/dir -d https://[account].file.core.windows.net/[share]/[path/to/directory] --recursive
  - name: Upload an entire directory to Azure File Share using account name and container name.
    text: az storage copy --source-local-path /path/to/dir --destination-account-name mystorageaccount --destination-share myshare --recursive
  - name: Upload a set of files to Azure File Share using wildcards with account name and share name.
    text: az storage copy --source-local-path /path/*foo/*bar/*.pdf --destination-account-name mystorageaccount --destination-share myshare
  - name: Upload files and directories to Azure File Share using wildcards with url.
    text: az storage copy -s /path/*foo/*bar* -d https://[account].file.core.windows.net/[share]/[path/to/directory] --recursive
  - name: Upload files and directories to Azure File Share using wildcards with account name and share name.
    text: az storage copy --source-local-path /path/*foo/*bar* --destination-account-name mystorageaccount --destination-share myshare --recursive
  - name: Download a single file from Azure File Share using url, and you can also specify your storage account and share information as above.
    text: az storage copy -s https://[account].file.core.windows.net/[share]/[path/to/file] -d /path/to/file.txt
  - name: Download an entire directory from Azure File Share, and you can also specify your storage account and share information as above.
    text: az storage copy -s https://[account].file.core.windows.net/[share]/[path/to/directory] -d /path/to/dir --recursive
  - name: Download a set of files from Azure File Share using wildcards, and you can also specify your storage account and share information as above.
    text: az storage copy -s https://[account].file.core.windows.net/[share]/foo* -d /path/to/dir --recursive
"""

helps['storage cors'] = """
type: group
short-summary: Manage storage service Cross-Origin Resource Sharing (CORS).
"""

helps['storage cors add'] = """
type: command
short-summary: Add a CORS rule to a storage account.
parameters:
  - name: --services
    short-summary: >
        The storage service(s) to add rules to. Allowed options are: (b)lob, (f)ile,
        (q)ueue, (t)able. Can be combined.
  - name: --max-age
    short-summary: The maximum number of seconds the client/browser should cache a preflight response.
  - name: --origins
    short-summary: Space-separated list of origin domains that will be allowed via CORS, or '*' to allow all domains.
  - name: --methods
    short-summary: Space-separated list of HTTP methods allowed to be executed by the origin.
  - name: --allowed-headers
    short-summary: Space-separated list of response headers allowed to be part of the cross-origin request.
  - name: --exposed-headers
    short-summary: Space-separated list of response headers to expose to CORS clients.
"""

helps['storage cors clear'] = """
type: command
short-summary: Remove all CORS rules from a storage account.
parameters:
  - name: --services
    short-summary: >
        The storage service(s) to remove rules from. Allowed options are: (b)lob, (f)ile,
        (q)ueue, (t)able. Can be combined.
examples:
  - name: Remove all CORS rules from a storage account. (autogenerated)
    text: az storage cors clear --account-name MyAccount --services bfqt
    crafted: true
"""

helps['storage cors list'] = """
type: command
short-summary: List all CORS rules for a storage account.
parameters:
  - name: --services
    short-summary: >
        The storage service(s) to list rules for. Allowed options are: (b)lob, (f)ile,
        (q)ueue, (t)able. Can be combined.
"""

helps['storage directory'] = """
type: group
short-summary: Manage file storage directories.
"""

helps['storage directory exists'] = """
type: command
short-summary: Check for the existence of a storage directory.
examples:
  - name: Check for the existence of a storage directory. (autogenerated)
    text: az storage directory exists --account-key 00000000 --account-name MyAccount --name MyDirectory --share-name MyShare
    crafted: true
"""

helps['storage directory list'] = """
type: command
short-summary: List directories in a share.
examples:
  - name: List directories in a share. (autogenerated)
    text: az storage directory list --share-name MyShare
    crafted: true
"""

helps['storage directory metadata'] = """
type: group
short-summary: Manage file storage directory metadata.
"""

helps['storage entity'] = """
type: group
short-summary: Manage table storage entities.
"""

helps['storage entity insert'] = """
type: command
short-summary: Insert an entity into a table.
parameters:
  - name: --table-name -t
    type: string
    short-summary: The name of the table to insert the entity into.
  - name: --entity -e
    type: list
    short-summary: Space-separated list of key=value pairs. Must contain a PartitionKey and a RowKey.
    long-summary: The PartitionKey and RowKey must be unique within the table, and may be up to 64Kb in size. If using an integer value as a key, convert it to a fixed-width string which can be canonically sorted. For example, convert the integer value 1 to the string value "0000001" to ensure proper sorting.
  - name: --if-exists
    type: string
    short-summary: Behavior when an entity already exists for the specified PartitionKey and RowKey.
  - name: --timeout
    short-summary: The server timeout, expressed in seconds.
examples:
  - name: Insert an entity into a table. (autogenerated)
    text: az storage entity insert --entity PartitionKey=AAA RowKey=BBB Content=ASDF2 --table-name MyTable
    crafted: true
"""

helps['storage entity query'] = """
type: command
short-summary: List entities which satisfy a query.
parameters:
  - name: --marker
    type: list
    short-summary: Space-separated list of key=value pairs. Must contain a nextpartitionkey and a nextrowkey.
    long-summary: This value can be retrieved from the next_marker field of a previous generator object if max_results was specified and that generator has finished enumerating results. If specified, this generator will begin returning results from the point where the previous generator stopped.
examples:
  - name: List entities which satisfy a query. (autogenerated)
    text: az storage entity query --table-name MyTable
    crafted: true
"""

helps['storage file'] = """
type: group
short-summary: Manage file shares that use the SMB 3.0 protocol.
"""

helps['storage file copy'] = """
type: group
short-summary: Manage file copy operations.
"""

helps['storage file copy start-batch'] = """
type: command
short-summary: Copy multiple files or blobs to a file share.
parameters:
  - name: --destination-share
    type: string
    short-summary: The file share where the source data is copied to.
  - name: --destination-path
    type: string
    short-summary: The directory where the source data is copied to. If omitted, data is copied to the root directory.
  - name: --pattern
    type: string
    short-summary: The pattern used for globbing files and blobs. The supported patterns are '*', '?', '[seq', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: List the files and blobs to be copied. No actual data transfer will occur.
  - name: --source-account-name
    type: string
    short-summary: The source storage account to copy the data from. If omitted, the destination account is used.
  - name: --source-account-key
    type: string
    short-summary: The account key for the source storage account. If omitted, the active login is used to determine the account key.
  - name: --source-container
    type: string
    short-summary: The source container blobs are copied from.
  - name: --source-share
    type: string
    short-summary: The source share files are copied from.
  - name: --source-uri
    type: string
    short-summary: A URI that specifies a the source file share or blob container.
    long-summary: If the source is in another account, the source must either be public or authenticated via a shared access signature.
  - name: --source-sas
    type: string
    short-summary: The shared access signature for the source storage account.
"""

helps['storage file delete-batch'] = """
type: command
short-summary: Delete files from an Azure Storage File Share.
parameters:
  - name: --source -s
    type: string
    short-summary: The source of the file delete operation. The source can be the file share URL or the share name.
  - name: --pattern
    type: string
    short-summary: The pattern used for file globbing. The supported patterns are '*', '?', '[seq]', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: List the files and blobs to be deleted. No actual data deletion will occur.
examples:
  - name: Delete files from an Azure Storage File Share. (autogenerated)
    text: az storage file delete-batch --account-key 00000000 --account-name MyAccount --source /path/to/file
    crafted: true
"""

helps['storage file download-batch'] = """
type: command
short-summary: Download files from an Azure Storage File Share to a local directory in a batch operation.
parameters:
  - name: --source -s
    type: string
    short-summary: The source of the file download operation. The source can be the file share URL or the share name.
  - name: --destination -d
    type: string
    short-summary: The local directory where the files are downloaded to. This directory must already exist.
  - name: --pattern
    type: string
    short-summary: The pattern used for file globbing. The supported patterns are '*', '?', '[seq]', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: List the files and blobs to be downloaded. No actual data transfer will occur.
  - name: --max-connections
    type: integer
    short-summary: The maximum number of parallel connections to use. Default value is 1.
  - name: --snapshot
    type: string
    short-summary: A string that represents the snapshot version, if applicable.
  - name: --validate-content
    type: bool
    short-summary: If set, calculates an MD5 hash for each range of the file for validation.
    long-summary: >
        The storage service checks the hash of the content that has arrived is identical to the hash that was sent.
        This is mostly valuable for detecting bitflips during transfer if using HTTP instead of HTTPS. This hash is not stored.
examples:
  - name: Download files from an Azure Storage File Share to a local directory in a batch operation. (autogenerated)
    text: az storage file download-batch --account-name MyAccount --destination . --source /path/to/file
    crafted: true
"""

helps['storage file exists'] = """
type: command
short-summary: Check for the existence of a file.
examples:
  - name: Check for the existence of a file. (autogenerated)
    text: az storage file exists --account-key 00000000 --account-name MyAccount --path path/file.txt --share-name MyShare
    crafted: true
"""

helps['storage file generate-sas'] = """
type: command
examples:
  - name: Generate a sas token for a file.
    text: |
        end=`date -u -d "30 minutes" '+%Y-%m-%dT%H:%MZ'`
        az storage file generate-sas -p path/file.txt -s MyShare --account-name MyStorageAccount --permissions rcdw --https-only --expiry $end
"""

helps['storage file list'] = """
type: command
short-summary: List files and directories in a share.
parameters:
  - name: --exclude-dir
    type: bool
    short-summary: List only files in the given share.
examples:
  - name: List files and directories in a share. (autogenerated)
    text: az storage file list --share-name MyShare
    crafted: true
"""

helps['storage file metadata'] = """
type: group
short-summary: Manage file metadata.
"""

helps['storage file upload'] = """
type: command
short-summary: Upload a file to a share that uses the SMB 3.0 protocol.
long-summary: Creates or updates an Azure file from a source path with automatic chunking and progress notifications.
examples:
  - name: Upload to a local file to a share.
    text: az storage file upload -s MyShare --source /path/to/file
  - name: Upload a file to a share that uses the SMB 3.0 protocol. (autogenerated)
    text: az storage file upload --account-key 00000000 --account-name MyStorageAccount --path path/file.txt --share-name MyShare --source /path/to/file
    crafted: true
"""

helps['storage file upload-batch'] = """
type: command
short-summary: Upload files from a local directory to an Azure Storage File Share in a batch operation.
parameters:
  - name: --source -s
    type: string
    short-summary: The directory to upload files from.
  - name: --destination -d
    type: string
    short-summary: The destination of the upload operation.
    long-summary: The destination can be the file share URL or the share name. When the destination is the share URL, the storage account name is parsed from the URL.
  - name: --destination-path
    type: string
    short-summary: The directory where the source data is copied to. If omitted, data is copied to the root directory.
  - name: --pattern
    type: string
    short-summary: The pattern used for file globbing. The supported patterns are '*', '?', '[seq', and '[!seq]'.
  - name: --dryrun
    type: bool
    short-summary: List the files and blobs to be uploaded. No actual data transfer will occur.
  - name: --max-connections
    type: integer
    short-summary: The maximum number of parallel connections to use. Default value is 1.
  - name: --validate-content
    type: bool
    short-summary: If set, calculates an MD5 hash for each range of the file for validation.
    long-summary: >
        The storage service checks the hash of the content that has arrived is identical to the hash that was sent.
        This is mostly valuable for detecting bitflips during transfer if using HTTP instead of HTTPS. This hash is not stored.
examples:
  - name: Upload files from a local directory to an Azure Storage File Share in a batch operation. (autogenerated)
    text: az storage file upload-batch --account-key 00000000 --account-name MyAccount --destination . --source /path/to/file
    crafted: true
"""

helps['storage file url'] = """
type: command
short-summary: Create the url to access a file.
examples:
  - name: Create the url to access a file. (autogenerated)
    text: az storage file url --account-name MyAccount --path path/file.txt --share-name MyShare
    crafted: true
"""

helps['storage logging'] = """
type: group
short-summary: Manage storage service logging information.
"""

helps['storage logging show'] = """
type: command
short-summary: Show logging settings for a storage account.
parameters:
  - name: --services
    short-summary: 'The storage services from which to retrieve logging info: (b)lob (q)ueue (t)able. Can be combined.'
"""

helps['storage logging update'] = """
type: command
short-summary: Update logging settings for a storage account.
parameters:
  - name: --services
    short-summary: 'The storage service(s) for which to update logging info: (b)lob (q)ueue (t)able. Can be combined.'
  - name: --log
    short-summary: 'The operations for which to enable logging: (r)ead (w)rite (d)elete. Can be combined.'
  - name: --retention
    short-summary: Number of days for which to retain logs. 0 to disable.
  - name: --version
    short-summary: Version of the logging schema.
"""

helps['storage message'] = """
type: group
short-summary: Manage queue storage messages.
"""

helps['storage metrics'] = """
type: group
short-summary: Manage storage service metrics.
"""

helps['storage metrics show'] = """
type: command
short-summary: Show metrics settings for a storage account.
parameters:
  - name: --services
    short-summary: 'The storage services from which to retrieve metrics info: (b)lob (q)ueue (t)able. Can be combined.'
  - name: --interval
    short-summary: Filter the set of metrics to retrieve by time interval
examples:
  - name: Show metrics settings for a storage account. (autogenerated)
    text: az storage metrics show --account-key 00000000 --account-name MyAccount
    crafted: true
"""

helps['storage metrics update'] = """
type: command
short-summary: Update metrics settings for a storage account.
parameters:
  - name: --services
    short-summary: 'The storage services from which to retrieve metrics info: (b)lob (q)ueue (t)able. Can be combined.'
  - name: --hour
    short-summary: Update the hourly metrics
  - name: --minute
    short-summary: Update the by-minute metrics
  - name: --api
    short-summary: Specify whether to include API in metrics. Applies to both hour and minute metrics if both are specified. Must be specified if hour or minute metrics are enabled and being updated.
  - name: --retention
    short-summary: Number of days for which to retain metrics. 0 to disable. Applies to both hour and minute metrics if both are specified.
examples:
  - name: Update metrics settings for a storage account. (autogenerated)
    text: az storage metrics update --account-name MyAccount --api true --hour true --minute true --retention 10 --services bfqt
    crafted: true
"""

helps['storage queue'] = """
type: group
short-summary: Manage storage queues.
"""

helps['storage queue list'] = """
type: command
short-summary: List queues in a storage account.
"""

helps['storage queue metadata'] = """
type: group
short-summary: Manage the metadata for a storage queue.
"""

helps['storage queue policy'] = """
type: group
short-summary: Manage shared access policies for a storage queue.
"""

helps['storage remove'] = """
type: command
short-summary: Delete blobs or files from Azure Storage.
long-summary: To delete blobs, both the source must either be public or be authenticated by using a shared access signature. Remove command depends on Azcopy, which only works for 64-bit Operating System now. We will support 32-bit Operating System soon.
examples:
  - name: Remove a single blob.
    text: az storage remove -c MyContainer -n MyBlob
  - name: Remove an entire virtual directory.
    text: az storage remove -c MyContainer -n path/to/directory --recursive
  - name: Remove only the top blobs inside a virtual directory but not its sub-directories.
    text: az storage remove -c MyContainer -n path/to/directory
  - name: Remove a subset of blobs in a virtual directory (For example, only jpg and pdf files, or if the blob name is "exactName").
    text: az storage remove -c MyContainer -n path/to/directory --recursive --include "*.jpg;*.pdf;exactName"
  - name: Remove an entire virtual directory but exclude certain blobs from the scope (For example, every blob that starts with foo or ends with bar).
    text: az storage remove -c MyContainer -n path/to/directory --recursive --include "foo*;*bar"
  - name: Remove a single file.
    text: az storage remove -s MyShare -p MyFile
  - name: Remove an entire directory.
    text: az storage remove -s MyShare -p path/to/directory --recursive
"""

helps['storage share'] = """
type: group
short-summary: Manage file shares.
"""

helps['storage share create'] = """
type: command
short-summary: Creates a new share under the specified account.
examples:
  - name: Creates a new share under the specified account. (autogenerated)
    text: az storage share create --name MyFileShare
    crafted: true
"""

helps['storage share exists'] = """
type: command
short-summary: Check for the existence of a file share.
examples:
  - name: Check for the existence of a file share. (autogenerated)
    text: az storage share exists --account-key 00000000 --account-name MyAccount --name MyFileShare
    crafted: true
"""

helps['storage share generate-sas'] = """
type: command
examples:
  - name: Generate a sas token for a fileshare and use it to upload a file.
    text: |
        end=`date -u -d "30 minutes" '+%Y-%m-%dT%H:%MZ'`
        sas=`az storage share generate-sas -n MyShare --account-name MyStorageAccount --https-only --permissions dlrw --expiry $end -o tsv`
        az storage file upload -s MyShare --account-name MyStorageAccount --source file.txt  --sas-token $sas
"""

helps['storage share list'] = """
type: command
short-summary: List the file shares in a storage account.
"""

helps['storage share metadata'] = """
type: group
short-summary: Manage the metadata of a file share.
"""

helps['storage share policy'] = """
type: group
short-summary: Manage shared access policies of a storage file share.
"""

helps['storage share url'] = """
type: command
short-summary: Create a URI to access a file share.
examples:
  - name: Create a URI to access a file share. (autogenerated)
    text: az storage share url --account-key 00000000 --account-name MyAccount --name MyFileShare
    crafted: true
"""

helps['storage table'] = """
type: group
short-summary: Manage NoSQL key-value storage.
"""

helps['storage table list'] = """
type: command
short-summary: List tables in a storage account.
"""

helps['storage table policy'] = """
type: group
short-summary: Manage shared access policies of a storage table.
"""

helps['tag'] = """
type: group
short-summary: Manage resource tags.
"""

helps['vm'] = """
type: group
short-summary: Manage Linux or Windows virtual machines.
"""

helps['vm availability-set'] = """
type: group
short-summary: Group resources into availability sets.
long-summary: >
    To provide redundancy to an application, it is recommended to group two or more virtual machines in an availability set.
    This configuration ensures that during either a planned or unplanned maintenance event, at least one virtual machine
    will be available.
"""

helps['vm availability-set convert'] = """
type: command
short-summary: Convert an Azure Availability Set to contain VMs with managed disks.
examples:
  - name: Convert an availabiity set to use managed disks by name.
    text: az vm availability-set convert -g MyResourceGroup -n MyAvSet
  - name: Convert an availability set to use managed disks by ID.
    text: >
        az vm availability-set convert --ids $(az vm availability-set list -g MyResourceGroup --query "[].id" -o tsv)
"""

helps['vm availability-set create'] = """
type: command
short-summary: Create an Azure Availability Set.
long-summary: 'For more information, see https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-manage-availability.'
examples:
  - name: Create an availability set.
    text: az vm availability-set create -n MyAvSet -g MyResourceGroup --platform-fault-domain-count 2 --platform-update-domain-count 2
"""

helps['vm availability-set delete'] = """
type: command
short-summary: Delete an availability set.
examples:
  - name: Delete an availability set.
    text: az vm availability-set delete -n MyAvSet -g MyResourceGroup
"""

helps['vm availability-set list'] = """
type: command
short-summary: List availability sets.
examples:
  - name: List availability sets.
    text: az vm availability-set list -g MyResourceGroup
"""

helps['vm availability-set list-sizes'] = """
type: command
short-summary: List VM sizes for an availability set.
examples:
  - name: List VM sizes for an availability set.
    text: az vm availability-set list-sizes -n MyAvSet -g MyResourceGroup
"""

helps['vm availability-set show'] = """
type: command
short-summary: Get information for an availability set.
examples:
  - name: Get information about an availability set.
    text: az vm availability-set show -n MyAvSet -g MyResourceGroup
"""

helps['vm availability-set update'] = """
type: command
short-summary: Update an Azure Availability Set.
examples:
  - name: Update an availability set.
    text: az vm availability-set update -n MyAvSet -g MyResourceGroup
  - name: Update an availability set tag.
    text: az vm availability-set update -n MyAvSet -g MyResourceGroup --set tags.foo=value
  - name: Remove an availability set tag.
    text: az vm availability-set update -n MyAvSet -g MyResourceGroup --remove tags.foo
"""

helps['vm boot-diagnostics'] = """
type: group
short-summary: Troubleshoot the startup of an Azure Virtual Machine.
long-summary: Use this feature to troubleshoot boot failures for custom or platform images.
"""

helps['vm boot-diagnostics disable'] = """
type: command
short-summary: Disable the boot diagnostics on a VM.
examples:
  - name: Disable boot diagnostics on all VMs in a resource group.
    text: >
        az vm boot-diagnostics disable --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

  - name: Disable the boot diagnostics on a VM
    text: |-
        az vm boot-diagnostics disable --ids $(az vm list --resource-group MyResourceGroup --query "[].id" -o tsv) --name MyVirtualMachine --resource-group MyResourceGroup
    crafted: true
"""

helps['vm boot-diagnostics enable'] = """
type: command
short-summary: Enable the boot diagnostics on a VM.
parameters:
  - name: --storage
    short-summary: Name or URI of a storage account (e.g. https://your_storage_account_name.blob.core.windows.net/)
examples:
  - name: Enable boot diagnostics on all VMs in a resource group.
    text: >
        az vm boot-diagnostics enable --storage https://mystor.blob.core.windows.net/ --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

  - name: Enable the boot diagnostics on a VM. (autogenerated)
    text: az vm boot-diagnostics enable --name MyVirtualMachine --resource-group MyResourceGroup --storage https://mystor.blob.core.windows.net/
    crafted: true
"""

helps['vm boot-diagnostics get-boot-log'] = """
type: command
short-summary: Get the boot diagnostics log from a VM.
examples:
  - name: Get diagnostics logs for all VMs in a resource group.
    text: >
        az vm boot-diagnostics get-boot-log --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

  - name: Get the boot diagnostics log from a VM. (autogenerated)
    text: az vm boot-diagnostics get-boot-log --name MyVirtualMachine --resource-group MyResourceGroup
    crafted: true
"""

helps['vm capture'] = """
type: command
short-summary: Capture information for a stopped VM.
long-summary: 'For an end-to-end tutorial, see https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-capture-image'
parameters:
  - name: --vhd-name-prefix
    type: string
    short-summary: The VHD name prefix specify for the VM disks.
  - name: --storage-container
    short-summary: The storage account container name in which to save the disks.
  - name: --overwrite
    short-summary: Overwrite the existing disk file.
examples:
  - name: Deallocate, generalize, and capture a stopped virtual machine.
    text: |
        az vm deallocate -g MyResourceGroup -n MyVm
        az vm generalize -g MyResourceGroup -n MyVm
        az vm capture -g MyResourceGroup -n MyVm --vhd-name-prefix MyPrefix
  - name: Deallocate, generalize, and capture multiple stopped virtual machines.
    text: |
        vms_ids=$(az vm list -g MyResourceGroup --query "[].id" -o tsv)
        az vm deallocate --ids {vms_ids}
        az vm generalize --ids {vms_ids}
        az vm capture --ids {vms_ids} --vhd-name-prefix MyPrefix

"""

helps['vm convert'] = """
type: command
short-summary: Convert a VM with unmanaged disks to use managed disks.
examples:
  - name: Convert a VM with unmanaged disks to use managed disks.
    text: az vm convert -g MyResourceGroup -n MyVm
  - name: Convert all VMs with unmanaged disks in a resource group to use managed disks.
    text: >
        az vm convert --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm create'] = """
type: command
short-summary: Create an Azure Virtual Machine.
long-summary: 'For an end-to-end tutorial, see https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-quick-create-cli.'
parameters:
  - name: --image
    type: string
    short-summary: >
        The name of the operating system image as a URN alias, URN, custom image name or ID, or VHD blob URI.
        This parameter is required unless using `--attach-os-disk.` Valid URN format: "Publisher:Offer:Sku:Version".
    populator-commands:
      - az vm image list
      - az vm image show
  - name: --ssh-key-values
    short-summary: Space-separated list of SSH public keys or public key file paths.
  - name: --computer-name
    short-summary: The host OS name of the virtual machine. Defaults to the name of the VM.
examples:
  - name: Create a default Ubuntu VM with automatic SSH authentication.
    text: >
        az vm create -n MyVm -g MyResourceGroup --image UbuntuLTS
  - name: Create a default RedHat VM with automatic SSH authentication using an image URN.
    text: >
        az vm create -n MyVm -g MyResourceGroup --image RedHat:RHEL:7-RAW:7.4.2018010506
  - name: Create a default Windows Server VM with a private IP address.
    text: >
        az vm create -n MyVm -g MyResourceGroup --public-ip-address "" --image Win2012R2Datacenter
  - name: Create a VM from a custom managed image.
    text: >
        az vm create -g MyResourceGroup -n MyVm --image MyImage
  - name: Create a VM by attaching to a managed operating system disk.
    text: >
        az vm create -g MyResourceGroup -n MyVm --attach-os-disk MyOsDisk --os-type linux
  - name: 'Create an Ubuntu Linux VM using a cloud-init script for configuration. See: https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init.'
    text: >
        az vm create -g MyResourceGroup -n MyVm --image debian --custom-data MyCloudInitScript.yml
  - name: Create a Debian VM with SSH key authentication and a public DNS entry, located on an existing virtual network and availability set.
    text: |
        az vm create -n MyVm -g MyResourceGroup --image debian --vnet-name MyVnet --subnet subnet1 \\
            --availability-set MyAvailabilitySet --public-ip-address-dns-name MyUniqueDnsName \\
            --ssh-key-value @key-file
  - name: Create a simple Ubuntu Linux VM with a public IP address, DNS entry, two data disks (10GB and 20GB), and then generate ssh key pairs.
    text: |
        az vm create -n MyVm -g MyResourceGroup --public-ip-address-dns-name MyUniqueDnsName \\
            --image ubuntults --data-disk-sizes-gb 10 20 --size Standard_DS2_v2 \\
            --generate-ssh-keys
  - name: Create a Debian VM using Key Vault secrets.
    text: >
        az keyvault certificate create --vault-name vaultname -n cert1 \\
          -p "$(az keyvault certificate get-default-policy)"

        secrets=$(az keyvault secret list-versions --vault-name vaultname \\
          -n cert1 --query "[?attributes.enabled].id" -o tsv)

        vm_secrets=$(az vm secret format -s "$secrets")


        az vm create -g group-name -n vm-name --admin-username deploy  \\
          --image debian --secrets "$vm_secrets"
  - name: Create a CentOS VM with a system assigned identity. The VM will have a 'Contributor' role with access to a storage account.
    text: >
        az vm create -n MyVm -g rg1 --image centos --assign-identity --scope /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/MyResourceGroup/myRG/providers/Microsoft.Storage/storageAccounts/storage1
  - name: Create a debian VM with a user assigned identity.
    text: >
        az vm create -n MyVm -g rg1 --image debian --assign-identity  /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
  - name: Create a debian VM with both system and user assigned identity.
    text: >
        az vm create -n MyVm -g rg1 --image debian --assign-identity  [system] /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
  - name: Create a VM in an availability zone in the current resource group's region
    supported-profiles: latest
    text: >
        az vm create -n MyVm -g MyResourceGroup --image Centos --zone 1
"""

helps['vm deallocate'] = """
type: command
short-summary: Deallocate a VM.
long-summary: 'For an end-to-end tutorial, see https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-capture-image'
examples:
  - name: Deallocate, generalize, and capture a stopped virtual machine.
    text: |
        az vm deallocate -g MyResourceGroup -n MyVm
        az vm generalize -g MyResourceGroup -n MyVm
        az vm capture -g MyResourceGroup -n MyVm --vhd-name-prefix MyPrefix
  - name: Deallocate, generalize, and capture multiple stopped virtual machines.
    text: |
        vms_ids=$(az vm list -g MyResourceGroup --query "[].id" -o tsv)
        az vm deallocate --ids {vms_ids}
        az vm generalize --ids {vms_ids}
        az vm capture --ids {vms_ids} --vhd-name-prefix MyPrefix

  - name: Deallocate a VM. (autogenerated)
    text: az vm deallocate --name MyVm --no-wait --resource-group MyResourceGroup
    crafted: true
"""

helps['vm delete'] = """
type: command
short-summary: Delete a VM.
examples:
  - name: Delete a VM without a prompt for confirmation.
    text: >
        az vm delete -g MyResourceGroup -n MyVm --yes
  - name: Delete all VMs in a resource group.
    text: >
        az vm delete --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm diagnostics'] = """
type: group
short-summary: Configure the Azure Virtual Machine diagnostics extension.
"""

helps['vm diagnostics get-default-config'] = """
type: command
short-summary: Get the default configuration settings for a VM.
examples:
  - name: Get the default diagnostics for a Linux VM and override the storage account name and the VM resource ID.
    text: |
        az vm diagnostics get-default-config \\
            | sed "s#__DIAGNOSTIC_STORAGE_ACCOUNT__#MyStorageAccount#g" \\
            | sed "s#__VM_OR_VMSS_RESOURCE_ID__#MyVmResourceId#g"
  - name: Get the default diagnostics for a Windows VM.
    text: >
        az vm diagnostics get-default-config --is-windows-os
"""

helps['vm diagnostics set'] = """
type: command
short-summary: Configure the Azure VM diagnostics extension.
examples:
  - name: Set up default diagnostics on a Linux VM for Azure Portal VM metrics graphs and syslog collection.
    text: |
        # Set the following 3 parameters first.
        my_resource_group={Resource group name containing your Linux VM and the storage account}
        my_linux_vm={Your Azure Linux VM name}
        my_diagnostic_storage_account={Your Azure storage account for storing VM diagnostic data}

        my_vm_resource_id=$(az vm show -g $my_resource_group -n $my_linux_vm --query "id" -o tsv)

        default_config=$(az vm diagnostics get-default-config \\
            | sed "s#__DIAGNOSTIC_STORAGE_ACCOUNT__#$my_diagnostic_storage_account#g" \\
            | sed "s#__VM_OR_VMSS_RESOURCE_ID__#$my_vm_resource_id#g")

        storage_sastoken=$(az storage account generate-sas \\
            --account-name $my_diagnostic_storage_account --expiry 2037-12-31T23:59:00Z \\
            --permissions wlacu --resource-types co --services bt -o tsv)

        protected_settings="{'storageAccountName': '$my_diagnostic_storage_account', \\
            'storageAccountSasToken': '$storage_sastoken'}"

        az vm diagnostics set --settings "$default_config" \\
            --protected-settings "$protected_settings" \\
            --resource-group $my_resource_group --vm-name $my_linux_vm

  - name: Set up default diagnostics on a Windows VM.
    text: |
        # Set the following 3 parameters first.
        my_resource_group={Resource group name containing your Windows VM and the storage account}
        my_windows_vm={Your Azure Windows VM name}
        my_diagnostic_storage_account={Your Azure storage account for storing VM diagnostic data}

        my_vm_resource_id=$(az vm show -g $my_resource_group -n $my_windows_vm --query "id" -o tsv)

        default_config=$(az vm diagnostics get-default-config  --is-windows-os \\
            | sed "s#__DIAGNOSTIC_STORAGE_ACCOUNT__#$my_diagnostic_storage_account#g" \\
            | sed "s#__VM_OR_VMSS_RESOURCE_ID__#$my_vm_resource_id#g")

        # Please use the same options, the WAD diagnostic extension has strict
        # expectations of the sas token's format. Set the expiry as desired.
        storage_sastoken=$(az storage account generate-sas \\
            --account-name $my_diagnostic_storage_account --expiry 2037-12-31T23:59:00Z \\
            --permissions acuw --resource-types co --services bt --https-only --output tsv)

        protected_settings="{'storageAccountName': '$my_diagnostic_storage_account', \\
            'storageAccountSasToken': '$storage_sastoken'}"

        az vm diagnostics set --settings "$default_config" \\
            --protected-settings "$protected_settings" \\
            --resource-group $my_resource_group --vm-name $my_windows_vm

        # # Alternatively, if the WAD extension has issues parsing the sas token,
        # # one can use a storage account key instead.
        storage_account_key=$(az storage account keys list --account-name {my_storage_account} \\
          --query [0].value -o tsv)
        protected_settings="{'storageAccountName': '$my_diagnostic_storage_account', \\
          'storageAccountKey': '$storage_account_key'}"
"""

helps['vm disk'] = """
type: group
short-summary: Manage the managed data disks attached to a VM.
long-summary: >4

    Azure Virtual Machines use disks as a place to store an operating system, applications, and data.
    All Azure virtual machines have at least two disks: An operating system disk, and a temporary disk.
    The operating system disk is created from an image, and both the operating system disk and the image are actually virtual hard disks (VHDs)
    stored in an Azure storage account. Virtual machines also can have one or more data disks, that are also stored as VHDs.


    Azure Managed and Unmanaged Data Disks have a maximum size of 4095 GB (with the exception of larger disks in preview). Azure Unmanaged Disks also have a maximum capacity of 4095 GB.


    For more information, see:

    - Azure Disks - https://docs.microsoft.com/azure/virtual-machines/linux/about-disks-and-vhds and https://docs.microsoft.com/azure/virtual-machines/windows/about-disks-and-vhds.

    - Larger Managed Disks in Public Preview - https://azure.microsoft.com/blog/introducing-the-public-preview-of-larger-managed-disks-sizes/

    - Ultra SSD Managed Disks in Public Preview - https://docs.microsoft.com/azure/virtual-machines/windows/disks-ultra-ssd


"""

helps['vm disk attach'] = """
type: command
short-summary: Attach a managed persistent disk to a VM.
long-summary: This allows for the preservation of data, even if the VM is reprovisioned due to maintenance or resizing.
examples:
  - name: Attach a new default sized (1023 GB) managed data disk to a VM.
    text: az vm disk attach -g MyResourceGroup --vm-name MyVm --name disk_name --new
  - name: Attach a managed persistent disk to a VM. (autogenerated)
    text: az vm disk attach --disk $diskId --new --resource-group MyResourceGroup --size-gb 128 --sku Standard_LRS --vm-name MyVm
    crafted: true
"""

helps['vm disk detach'] = """
type: command
short-summary: Detach a managed disk from a VM.
examples:
  - name: Detach a data disk from a VM.
    text: >
        az vm disk detach -g MyResourceGroup --vm-name MyVm --name disk_name
"""

helps['vm encryption'] = """
type: group
short-summary: "Manage encryption of VM disks."
long-summary: |
    For more information, see:
    https://docs.microsoft.com/azure/security/azure-security-disk-encryption-overview"
"""

helps['vm encryption disable'] = """
type: command
short-summary: Disable disk encryption on the OS disk and/or data disks. Decrypt mounted disks.
long-summary: |
    For Linux VMs, disabling encryption is only permitted on data volumes.
    For Windows VMS, disabling encryption is permitted on both OS and data volumes.
examples:
  - name: Disable disk encryption on the OS disk and/or data disks. (autogenerated)
    text: az vm encryption disable --name MyVirtualMachine --resource-group MyResourceGroup --volume-type DATA
    crafted: true
"""

helps['vm encryption enable'] = """
type: command
short-summary: "Enable disk encryption on the OS disk and/or data disks. Encrypt mounted disks."
long-summary: |
    Note that Azure Active Directory / service principal arguments are unnecessary for vm encryption. The older version of Azure Disk Encryption required AAD arguments.
    For more information, see:
    https://docs.microsoft.com/azure/security/azure-security-disk-encryption-overview
parameters:
  - name: --aad-client-id
    short-summary: Client ID of an AAD app with permissions to write secrets to the key vault.
  - name: --aad-client-secret
    short-summary: Client secret of the AAD app with permissions to write secrets to the key vault.
  - name: --aad-client-cert-thumbprint
    short-summary: Thumbprint of the AAD app certificate with permissions to write secrets to the key vault.
examples:
  - name: encrypt a VM using a key vault in the same resource group
    text: >
        az vm encryption enable -g MyResourceGroup -n MyVm --disk-encryption-keyvault MyVault
  - name: Enable disk encryption on the OS disk and/or data disks. Encrypt mounted disks. (autogenerated)
    text: az vm encryption enable --disk-encryption-keyvault MyVault --name MyVm --resource-group MyResourceGroup --volume-type DATA
    crafted: true
"""

helps['vm encryption show'] = """
type: command
short-summary: Show encryption status.
examples:
  - name: Show encryption status. (autogenerated)
    text: az vm encryption show --name MyVirtualMachine --resource-group MyResourceGroup
    crafted: true
"""

helps['vm extension'] = """
type: group
short-summary: Manage extensions on VMs.
long-summary: >
    Extensions are small applications that provide post-deployment configuration and automation tasks on Azure virtual machines.
    For example, if a virtual machine requires software installation, anti-virus protection, or Docker configuration, a VM extension
    can be used to complete these tasks. Extensions can be bundled with a new virtual machine deployment or run against any existing system.
"""

helps['vm extension delete'] = """
type: command
short-summary: Remove an extension attached to a VM.
examples:
  - name: Use a VM name and extension to delete an extension from a VM.
    text: az vm extension delete -g MyResourceGroup --vm-name MyVm -n extension_name
  - name: Delete extensions with IDs containing the string "MyExtension" from a VM.
    text: >
        az vm extension delete --ids \\
            $(az resource list --query "[?contains(name, 'MyExtension')].id" -o tsv)
"""

helps['vm extension image'] = """
type: group
short-summary: Find the available VM extensions for a subscription and region.
"""

helps['vm extension image list'] = """
type: command
short-summary: List the information on available extensions.
examples:
  - name: List the unique publishers for extensions.
    text: az vm extension image list --query "[].publisher" -o tsv | sort -u
  - name: Find extensions with "Docker" in the name.
    text: az vm extension image list --query "[].name" -o tsv | sort -u | grep Docker
  - name: List extension names where the publisher name starts with "Microsoft.Azure.App".
    text: |
        az vm extension image list --query \\
            "[?starts_with(publisher, 'Microsoft.Azure.App')].publisher" \\
            -o tsv | sort -u | xargs -I{} az vm extension image list-names --publisher {} -l westus
"""

helps['vm extension image list-names'] = """
type: command
short-summary: List the names of available extensions.
examples:
  - name: Find Docker extensions by publisher and location.
    text: >
        az vm extension image list-names --publisher Microsoft.Azure.Extensions \\
            -l westus --query "[?starts_with(name, 'Docker')]"
  - name: Find CustomScript extensions by publisher and location.
    text: >
        az vm extension image list-names --publisher Microsoft.Azure.Extensions \\
            -l westus --query "[?starts_with(name, 'Custom')]"
"""

helps['vm extension image list-versions'] = """
type: command
short-summary: List the versions for available extensions.
examples:
  - name: Find the available versions for the Docker extension.
    text: >
        az vm extension image list-versions --publisher Microsoft.Azure.Extensions \\
            -l westus -n DockerExtension -otable
"""

helps['vm extension image show'] = """
type: command
short-summary: Display information for an extension.
examples:
  - name: Show the CustomScript extension version 2.0.2.
    text: >
        az vm extension image show -l westus -n CustomScript \\
          --publisher Microsoft.Azure.Extensions --version 2.0.2
  - name: Show the latest version of the Docker extension.
    text: >
        publisher=Microsoft.Azure.Extensions

        extension=DockerExtension

        location=westus


        latest=$(az vm extension image list-versions \\
          --publisher {publisher} -l {location} -n {extension} \\
          --query "[].name" -o tsv | sort | tail -n 1)

        az vm extension image show -l {location} \\
          --publisher {publisher} -n {extension} --version {latest}
"""

helps['vm extension list'] = """
type: command
short-summary: List the extensions attached to a VM.
examples:
  - name: List attached extensions to a named VM.
    text: az vm extension list -g MyResourceGroup --vm-name MyVm
"""

helps['vm extension set'] = """
type: command
short-summary: Set extensions for a VM.
long-summary: Get extension details from `az vm extension image list`.
examples:
  - name: Add a user account to a Linux VM.
    text: |
        az vm extension set -n VMAccessForLinux --publisher Microsoft.OSTCExtensions --version 1.4 \\
            --vm-name MyVm --resource-group MyResourceGroup \\
            --protected-settings '{"username":"user1", "ssh_key":"ssh_rsa ..."}'
parameters:
  - name: --name -n
    populator-commands:
      - az vm extension image list
"""

helps['vm extension show'] = """
type: command
short-summary: Display information about extensions attached to a VM.
examples:
  - name: Use VM name and extension name to show the extensions attached to a VM.
    text: az vm extension show -g MyResourceGroup --vm-name MyVm -n extension_name
"""

helps['vm extension wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a virtual machine extension is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a virtual machine extension is met. (autogenerated)
    text: az vm extension wait --created --name MyExtension --resource-group MyResourceGroup --vm-name MyVm
    crafted: true
  - name: Place the CLI in a waiting state until a condition of a virtual machine extension is met. (autogenerated)
    text: az vm extension wait --exists --name MyExtension --resource-group MyResourceGroup --vm-name MyVm
    crafted: true
"""

helps['vm generalize'] = """
type: command
short-summary: Mark a VM as generalized, allowing it to be imaged for multiple deployments.
long-summary: 'For an end-to-end tutorial, see https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-capture-image'
examples:
  - name: Deallocate, generalize, and capture a stopped virtual machine.
    text: |
        az vm deallocate -g MyResourceGroup -n MyVm
        az vm generalize -g MyResourceGroup -n MyVm
        az vm capture -g MyResourceGroup -n MyVm --vhd-name-prefix MyPrefix
  - name: Deallocate, generalize, and capture multiple stopped virtual machines.
    text: |
        vms_ids=$(az vm list -g MyResourceGroup --query "[].id" -o tsv)
        az vm deallocate --ids {vms_ids}
        az vm generalize --ids {vms_ids}
        az vm capture --ids {vms_ids} --vhd-name-prefix MyPrefix

"""

helps['vm get-instance-view'] = """
type: command
short-summary: Get instance information about a VM.
examples:
  - name: Use a resource group and name to get instance view information of a VM.
    text: az vm get-instance-view -g MyResourceGroup -n MyVm
  - name: Get instance views for all VMs in a resource group.
    text: >
        az vm get-instance-view --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm host'] = """
type: group
short-summary: Manage Dedicated Hosts for Virtual Machines
"""

helps['vm host create'] = """
type: command
short-summary: Create a dedicated host.
examples:
  - name: Create a dedicated host. Ensure it auto replaces on failure
    text: |-
        az vm host create --host-group my-host-group --name my-host --platform-fault-domain 2 \\
            --auto-replace --resource-group my-resource-group --sku DSv3-Type1
  - name: Create a dedicated host in the 'east asia' region. Don't auto replace on failure.
    text: |-
        az vm host create --host-group my-host-group --name my-host --platform-fault-domain 0 \\
            --auto-replace false --resource-group my-resource-group --sku ESv3-Type1 --location eastasia
"""

helps['vm host get-instance-view'] = """
type: command
short-summary: Get instance information about a dedicated host.
examples:
  - name: Get instance view information of a dedicated host.
    text: az vm host get-instance-view --host-group my-host-group --name my-host -g my-rg

  - name: Get instance views for all dedicated hosts in a host group.
    text: >
        az vm host get-instance-view --ids $(az vm host list -g my-rg --host-group my-host-group --query "[].id" -o tsv)
"""

helps['vm host group'] = """
type: group
short-summary: Manage Dedicated Host Groups
"""

helps['vm host group create'] = """
type: command
short-summary: Create a dedicated host group.
"""

helps['vm host group list'] = """
type: command
short-summary: List dedicated host groups.
long-summary: Lists dedicated host groups by subscription. If resource group is specified, lists dedicated host groups by resource group.
"""

helps['vm host group show'] = """
type: command
short-summary: Get the details of a dedicated host group.
"""

helps['vm host group update'] = """
type: command
short-summary: Update a dedicated host group.
"""

helps['vm host list'] = """
type: command
short-summary: List dedicated hosts.
"""

helps['vm host show'] = """
type: command
short-summary: Get the details of a dedicated host.
"""

helps['vm host update'] = """
type: command
short-summary: Update a dedicated host.
examples:
  - name: Update the 'autoReplaceOnFailure' field of a dedicated host.
    text: |-
        az vm host update --host-group my-host-group --name my-host \\
            --resource-group my-resource-group --set autoReplaceOnFailure=True
"""

helps['vm identity'] = """
type: group
short-summary: manage service identities of a VM
"""

helps['vm identity assign'] = """
type: command
short-summary: Enable managed service identity on a VM.
long-summary: This is required to authenticate and interact with other Azure services using bearer tokens.
examples:
  - name: Enable the system assigned identity on a VM with the 'Reader' role.
    text: az vm identity assign -g MyResourceGroup -n MyVm --role Reader --scope /subscriptions/db5eb68e-73e2-4fa8-b18a-0123456789999/resourceGroups/MyResourceGroup
  - name: Enable the system assigned identity and a user assigned identity on a VM.
    text: az vm identity assign -g MyResourceGroup -n MyVm --role Reader --identities [system] myAssignedId
"""

helps['vm identity remove'] = """
type: command
short-summary: Remove managed service identities from a VM.
examples:
  - name: Remove the system assigned identity
    text: az vm identity remove -g MyResourceGroup -n MyVm
  - name: Remove a user assigned identity
    text: az vm identity remove -g MyResourceGroup -n MyVm --identities readerId
  - name: Remove 2 identities which are in the same resource group with the VM
    text: az vm identity remove -g MyResourceGroup -n MyVm --identities readerId writerId
  - name: Remove the system assigned identity and a user identity
    text: az vm identity remove -g MyResourceGroup -n MyVm --identities [system] readerId
"""

helps['vm identity show'] = """
type: command
short-summary: display VM's managed identity info.
examples:
  - name: display VM's managed identity info. (autogenerated)
    text: az vm identity show --name MyVirtualMachine --resource-group MyResourceGroup
    crafted: true
"""

helps['vm image'] = """
type: group
short-summary: Information on available virtual machine images.
"""

helps['vm image accept-terms'] = """
type: command
short-summary: Accept Azure Marketplace term so that the image can be used to create VMs
examples:
  - name: Accept Azure Marketplace term so that the image can be used to create VMs. (autogenerated)
    text: az vm image accept-terms --urn publisher:offer:sku:version
    crafted: true
"""

helps['vm image list'] = """
type: command
short-summary: List the VM/VMSS images available in the Azure Marketplace.
parameters:
  - name: --all
    short-summary: Retrieve image list from live Azure service rather using an offline image list
  - name: --offer -f
    short-summary: Image offer name, partial name is accepted
  - name: --publisher -p
    short-summary: Image publisher name, partial name is accepted
  - name: --sku -s
    short-summary: Image sku name, partial name is accepted
examples:
  - name: List all available images.
    text: az vm image list --all
  - name: List all offline cached CentOS images.
    text: az vm image list -f CentOS
  - name: List all CentOS images.
    text: az vm image list -f CentOS --all
"""

helps['vm image list-offers'] = """
type: command
short-summary: List the VM image offers available in the Azure Marketplace.
parameters:
  - name: --publisher -p
    populator-commands:
      - az vm list-publishers
examples:
  - name: List all offers from Microsoft in the West US region.
    text: az vm image list-offers -l westus -p MicrosoftWindowsServer
  - name: List all offers from OpenLocic in the West US region.
    text: az vm image list-offers -l westus -p OpenLogic
"""

helps['vm image list-publishers'] = """
type: command
short-summary: List the VM image publishers available in the Azure Marketplace.
examples:
  - name: List all publishers in the West US region.
    text: az vm image list-publishers -l westus
  - name: List all publishers with names starting with "Open" in westus.
    text: az vm image list-publishers -l westus --query "[?starts_with(name, 'Open')]"
"""

helps['vm image list-skus'] = """
type: command
short-summary: List the VM image SKUs available in the Azure Marketplace.
parameters:
  - name: --publisher -p
    populator-commands:
      - az vm image list-publishers
examples:
  - name: List all skus available for CentOS published by OpenLogic in the West US region.
    text: az vm image list-skus -l westus -f CentOS -p OpenLogic
"""

helps['vm image show'] = """
type: command
short-summary: Get the details for a VM image available in the Azure Marketplace.
examples:
  - name: Show information for the latest available CentOS image from OpenLogic.
    text: >
        latest=$(az vm image list -p OpenLogic -s 7.3 --all --query \\
            "[?offer=='CentOS'].version" -o tsv | sort -u | tail -n 1)
        az vm image show -l westus -f CentOS -p OpenLogic --sku 7.3 --version {latest}
  - name: Get the details for a VM image available in the Azure Marketplace. (autogenerated)
    text: az vm image show --location westus --urn publisher:offer:sku:version
    crafted: true
"""

helps['vm list'] = """
type: command
short-summary: List details of Virtual Machines.
long-summary: 'For more information on querying information about Virtual Machines, see https://docs.microsoft.com/cli/azure/query-az-cli2'
examples:
  - name: List all VMs.
    text: az vm list
  - name: List all VMs by resource group.
    text: az vm list -g MyResourceGroup
  - name: List all VMs by resource group with details.
    text: az vm list -g MyResourceGroup -d
"""

helps['vm list-ip-addresses'] = """
type: command
short-summary: List IP addresses associated with a VM.
examples:
  - name: Get the IP addresses for a VM.
    text: az vm list-ip-addresses -g MyResourceGroup -n MyVm
  - name: Get IP addresses for all VMs in a resource group.
    text: >
        az vm list-ip-addresses --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm list-sizes'] = """
type: command
short-summary: List available sizes for VMs.
examples:
  - name: List the available VM sizes in the West US region.
    text: az vm list-sizes -l westus
"""

helps['vm list-skus'] = """
type: command
short-summary: Get details for compute-related resource SKUs.
long-summary: This command incorporates subscription level restriction, offering the most accurate information.
examples:
  - name: List all SKUs in the West US region.
    text: az vm list-skus -l westus
  - name: List all available vm sizes in the East US2 region which support availability zone.
    text: az vm list-skus -l eastus2 --zone
  - name: List all available vm sizes in the East US2 region which support availability zone with name like "standard_ds1...".
    text: az vm list-skus -l eastus2 --zone --size standard_ds1
  - name: List availability set related sku information in The West US region.
    text: az vm list-skus -l westus --resource-type availabilitySets
"""

helps['vm list-usage'] = """
type: command
short-summary: List available usage resources for VMs.
examples:
  - name: Get the compute resource usage for the West US region.
    text: az vm list-usage -l westus
"""

helps['vm list-vm-resize-options'] = """
type: command
short-summary: List available resizing options for VMs.
examples:
  - name: List all available VM sizes for resizing.
    text: az vm list-vm-resize-options -g MyResourceGroup -n MyVm
  - name: List available sizes for all VMs in a resource group.
    text: >
        az vm list-vm-resize-options --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm nic'] = """
type: group
short-summary: Manage network interfaces. See also `az network nic`.
long-summary: >
    A network interface (NIC) is the interconnection between a VM and the underlying software
    network. For more information, see https://docs.microsoft.com/azure/virtual-network/virtual-network-network-interface-overview.
"""

helps['vm nic add'] = """
type: command
short-summary: Add existing NICs to a VM.
examples:
  - name: Add two NICs to a VM.
    text: az vm nic add -g MyResourceGroup --vm-name MyVm --nics nic_name1 nic_name2
"""

helps['vm nic list'] = """
type: command
short-summary: List the NICs available on a VM.
examples:
  - name: List all of the NICs on a VM.
    text: az vm nic list -g MyResourceGroup --vm-name MyVm
"""

helps['vm nic remove'] = """
type: command
short-summary: Remove NICs from a VM.
examples:
  - name: Remove two NICs from a VM.
    text: az vm nic remove -g MyResourceGroup --vm-name MyVm --nics nic_name1 nic_name2
"""

helps['vm nic set'] = """
type: command
short-summary: Configure settings of a NIC attached to a VM.
examples:
  - name: Set a NIC on a VM to be the primary interface.
    text: az vm nic set -g MyResourceGroup --vm-name MyVm --nic nic_name1 nic_name2 --primary-nic nic_name2
  - name: Configure settings of a NIC attached to a VM. (autogenerated)
    text: az vm nic set --nics nic_name1 nic_name2 --primary-nic nic_name2 --resource-group MyResourceGroup --vm-name MyVm
    crafted: true
"""

helps['vm nic show'] = """
type: command
short-summary: Display information for a NIC attached to a VM.
examples:
  - name: Show details of a NIC on a VM.
    text: az vm nic show -g MyResourceGroup --vm-name MyVm --nic nic_name1
"""

helps['vm open-port'] = """
type: command
short-summary: Opens a VM to inbound traffic on specified ports.
long-summary: >
    Adds a security rule to the network security group (NSG) that is attached to the VM's
    network interface (NIC) or subnet. The existing NSG will be used or a new one will be
    created. The rule name is 'open-port-{port}' and will overwrite an existing rule with
    this name. For multi-NIC VMs, or for more fine-grained control, use the appropriate
    network commands directly (nsg rule create, etc).
examples:
  - name: Open all ports on a VM to inbound traffic.
    text: az vm open-port -g MyResourceGroup -n MyVm --port '*'
  - name: Open a range of ports on a VM to inbound traffic with the highest priority.
    text: az vm open-port -g MyResourceGroup -n MyVm --port 80-100 --priority 100
  - name: Open all ports for all VMs in a resource group.
    text: >
        az vm open-port --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv) --port '*'

"""

helps['vm redeploy'] = """
type: command
short-summary: Redeploy an existing VM.
examples:
  - name: Redeploy a VM.
    text: az vm redeploy -g MyResourceGroup -n MyVm
  - name: Redeploy all VMs in a resource group.
    text: >
        az vm redeploy --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm resize'] = """
type: command
short-summary: Update a VM's size.
parameters:
  - name: --size
    type: string
    short-summary: The VM size.
    populator-commands:
      - az vm list-vm-resize-options
examples:
  - name: Resize a VM.
    text: az vm resize -g MyResourceGroup -n MyVm --size Standard_DS3_v2
  - name: Resize all VMs in a resource group.
    text: >
        az vm resize --size Standard_DS3_v2 --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm restart'] = """
type: command
short-summary: Restart VMs.
examples:
  - name: Restart a VM.
    text: az vm restart -g MyResourceGroup -n MyVm
  - name: Restart all VMs in a resource group.
    text: >
        az vm restart --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm run-command'] = """
type: group
short-summary: Manage run commands on a Virtual Machine.
long-summary: 'For more information, see https://docs.microsoft.com/azure/virtual-machines/windows/run-command or https://docs.microsoft.com/azure/virtual-machines/linux/run-command.'
"""

helps['vm run-command invoke'] = """
type: command
short-summary: Execute a specific run command on a vm.
long-summary: >
    `az vm run-command show` returns helpful information on each run-command.
    Discover Run command-id's via `az vmss run-command list`
parameters:
  - name: --command-id
    type: string
    short-summary: The command id
    populator-commands:
      - az vm run-command list
examples:
  - name: Install nginx on a linux VM.
    text: az vm run-command invoke -g MyResourceGroup -n MyVm --command-id RunShellScript --scripts "sudo apt-get update && sudo apt-get install -y nginx"
  - name: Run shell command on a linux VM with parameters.
    text: az vm run-command invoke -g MyResourceGroup -n MyVm --command-id RunShellScript --scripts 'echo $1 $2' --parameters hello world
  - name: Run powershell script on a windows VM with parameters. Script supplied inline. Be wary of single-quoting in CMD.exe.
    text: |-
        az vm run-command invoke  --command-id RunPowerShellScript --name win-vm -g my-resource-group  \\
            --scripts 'param([string]$arg1,[string]$arg2)' \\
            'Write-Host This is a sample script with parameters $arg1 and $arg2' \\
            --parameters 'arg1=somefoo' 'arg2=somebar'
  - name: Run powershell script on a windows VM with parameters. Script supplied from file.
    text: |-
        # script.ps1
        #   param(
        #       [string]$arg1,
        #       [string]$arg2
        #   )
        #   Write-Host This is a sample script with parameters $arg1 and $arg2

        az vm run-command invoke  --command-id RunPowerShellScript --name win-vm -g my-resource-group \\
            --scripts @script.ps1 --parameters "arg1=somefoo" "arg2=somebar"
"""

helps['vm run-command show'] = """
type: command
parameters:
  - name: --command-id
    type: string
    short-summary: The command id
    populator-commands:
      - az vm run-command list
examples:
  - name: vm run-command show (autogenerated)
    text: az vm run-command show --command-id RunShellScript --location westus2
    crafted: true
"""

helps['vm secret'] = """
type: group
short-summary: Manage VM secrets.
"""

helps['vm secret add'] = """
type: command
short-summary: Add a secret to a VM.
examples:
  - name: Add a secret to a VM. (autogenerated)
    text: az vm secret add --certificate {certificate} --keyvault {keyvault} --name MyVirtualMachine --resource-group MyResourceGroup
    crafted: true
"""

helps['vm secret format'] = """
type: command
short-summary: Transform secrets into a form that can be used by VMs and VMSSes.
parameters:
  - name: --secrets -s
    long-summary: >
        The command will attempt to resolve the vault ID for each secret. If it is unable to do so,
        specify the vault ID to use for *all* secrets using: --keyvault NAME --resource-group NAME | --keyvault ID.
examples:
  - name: Create a self-signed certificate with the default policy, and add it to a virtual machine.
    text: >
        az keyvault certificate create --vault-name vaultname -n cert1 \\
          -p "$(az keyvault certificate get-default-policy)"

        secrets=$(az keyvault secret list-versions --vault-name vaultname \\
          -n cert1 --query "[?attributes.enabled].id" -o tsv)

        vm_secrets=$(az vm secret format -s "$secrets")

        az vm create -g group-name -n vm-name --admin-username deploy  \\
          --image debian --secrets "$vm_secrets"
"""

helps['vm secret list'] = """
type: command
short-summary: List secrets on a VM.
examples:
  - name: List secrets on a VM. (autogenerated)
    text: az vm secret list --name MyVirtualMachine --resource-group MyResourceGroup
    crafted: true
"""

helps['vm secret remove'] = """
type: command
short-summary: Remove a secret from a VM.
"""

helps['vm show'] = """
type: command
short-summary: Get the details of a VM.
examples:
  - name: Show information about a VM.
    text: az vm show -g MyResourceGroup -n MyVm -d
  - name: Get the details for all VMs in a resource group.
    text: >
        az vm show -d --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm start'] = """
type: command
short-summary: Start a stopped VM.
examples:
  - name: Start a stopped VM.
    text: az vm start -g MyResourceGroup -n MyVm
  - name: Start all VMs in a resource group.
    text: >
        az vm start --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

  - name: Start a stopped VM. (autogenerated)
    text: az vm start --name MyVm --no-wait --resource-group MyResourceGroup
    crafted: true
"""

helps['vm stop'] = """
type: command
short-summary: Power off (stop) a running VM.
long-summary: The VM will continue to be billed. To avoid this, you can deallocate the VM through "az vm deallocate"
examples:
  - name: Power off (stop) a running VM.
    text: az vm stop --resource-group MyResourceGroup --name MyVm
  - name: Power off a running VM without shutting down.
    text: az vm stop --resource-group MyResourceGroup --name MyVm --skip-shutdown
  - name: Power off VMs in a resource group.
    text: >
        az vm stop --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm unmanaged-disk'] = """
type: group
short-summary: Manage the unmanaged data disks attached to a VM.
long-summary: >4

    Azure Virtual Machines use disks as a place to store an operating system, applications, and data.
    All Azure virtual machines have at least two disks: An operating system disk, and a temporary disk.
    The operating system disk is created from an image, and both the operating system disk and the image are actually virtual hard disks (VHDs)
    stored in an Azure storage account. Virtual machines also can have one or more data disks, that are also stored as VHDs.


    Azure Managed and Unmanaged Data Disks have a maximum size of 4095 GB (with the exception of larger disks in preview). Azure Unmanaged Disks also have a maximum capacity of 4095 GB.


    For more information, see:

    - Azure Disks - https://docs.microsoft.com/azure/virtual-machines/linux/about-disks-and-vhds and https://docs.microsoft.com/azure/virtual-machines/windows/about-disks-and-vhds.

    - Larger Managed Disks in Public Preview - https://azure.microsoft.com/blog/introducing-the-public-preview-of-larger-managed-disks-sizes/

    - Ultra SSD Managed Disks in Public Preview - https://docs.microsoft.com/azure/virtual-machines/windows/disks-ultra-ssd


"""

helps['vm unmanaged-disk attach'] = """
type: command
short-summary: Attach an unmanaged persistent disk to a VM.
long-summary: This allows for the preservation of data, even if the VM is reprovisioned due to maintenance or resizing.
examples:
  - name: Attach a new default sized (1023 GB) unmanaged data disk to a VM.
    text: az vm unmanaged-disk attach -g MyResourceGroup --vm-name MyVm --new
  - name: Attach an existing data disk to a VM as unmanaged.
    text: >
        az vm unmanaged-disk attach -g MyResourceGroup --vm-name MyVm \\
            --vhd-uri https://mystorage.blob.core.windows.net/vhds/d1.vhd
  - name: Attach an unmanaged persistent disk to a VM. (autogenerated)
    text: az vm unmanaged-disk attach --name MyDataDisk --new --resource-group MyResourceGroup --size-gb 50 --vm-name MyVm
    crafted: true
"""

helps['vm unmanaged-disk detach'] = """
type: command
short-summary: Detach an unmanaged disk from a VM.
examples:
  - name: Detach a data disk from a VM.
    text: >
        az vm unmanaged-disk detach -g MyResourceGroup --vm-name MyVm -n disk_name
"""

helps['vm unmanaged-disk list'] = """
type: command
short-summary: List unmanaged disks of a VM.
examples:
  - name: List the unmanaged disks attached to a VM.
    text: az vm unmanaged-disk list -g MyResourceGroup --vm-name MyVm
  - name: List unmanaged disks with names containing the string "data_disk".
    text: >
        az vm unmanaged-disk list -g MyResourceGroup --vm-name MyVm \\
            --query "[?contains(name, 'data_disk')]" --output table
"""

helps['vm update'] = """
type: command
short-summary: Update the properties of a VM.
long-summary: Update VM objects and properties using paths that correspond to 'az vm show'.
examples:
  - name: Add or update a tag.
    text: az vm update -n name -g group --set tags.tagName=tagValue
  - name: Remove a tag.
    text: az vm update -n name -g group --remove tags.tagName
  - name: Set the primary NIC of a VM.
    text: az vm update -n name -g group --set networkProfile.networkInterfaces[1].primary=false networkProfile.networkInterfaces[0].primary=true
  - name: Add a new non-primary NIC to a VM.
    text: az vm update -n name -g group --add networkProfile.networkInterfaces primary=false id={NIC_ID}
  - name: Remove the fourth NIC from a VM.
    text: az vm update -n name -g group --remove networkProfile.networkInterfaces 3
"""

helps['vm user'] = """
type: group
short-summary: Manage user accounts for a VM.
"""

helps['vm user delete'] = """
type: command
short-summary: Delete a user account from a VM.
examples:
  - name: Delete a user account.
    text: az vm user delete -u username -n MyVm -g MyResourceGroup
  - name: Delete a user on all VMs in a resource group.
    text: >
        az vm user delete -u username --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm user reset-ssh'] = """
type: command
short-summary: Reset the SSH configuration on a VM.
long-summary: >
    The extension will restart the SSH service, open the SSH port on your VM, and reset the SSH configuration to default values. The user account (name, password, and SSH keys) are not changed.
examples:
  - name: Reset the SSH configuration.
    text: az vm user reset-ssh -n MyVm -g MyResourceGroup
  - name: Reset the SSH server on all VMs in a resource group.
    text: >
        az vm user reset-ssh --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm user update'] = """
type: command
short-summary: Update a user account.
parameters:
  - name: --ssh-key-value
    short-summary: SSH public key file value or public key file path
examples:
  - name: Update a Windows user account.
    text: az vm user update -u username -p password -n MyVm -g MyResourceGroup
  - name: Update a Linux user account.
    text: az vm user update -u username --ssh-key-value "$({ ~/.ssh/id_rsa.pub)" -n MyVm -g MyResourceGroup
  - name: Update a user on all VMs in a resource group.
    text: >
        az vm user update -u username --ssh-key-value "$({ ~/.ssh/id_rsa.pub)" --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vm wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the VM is met.
examples:
  - name: Wait until a VM is created.
    text: az vm wait -g MyResourceGroup -n MyVm --created
  - name: Wait until all VMs in a resource group are deleted.
    text: >
        az vm wait --deleted --ids $(az vm list -g MyResourceGroup --query "[].id" -o tsv)

"""

helps['vmss'] = """
type: group
short-summary: Manage groupings of virtual machines in an Azure Virtual Machine Scale Set (VMSS).
"""

helps['vmss create'] = """
type: command
short-summary: Create an Azure Virtual Machine Scale Set.
long-summary: 'For an end-to-end tutorial, see https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-linux-create-cli.'
parameters:
  - name: --image
    type: string
    short-summary: >
        The name of the operating system image as a URN alias, URN, custom image name or ID, or VHD blob URI.
        Valid URN format: "Publisher:Offer:Sku:Version".
    populator-commands:
      - az vm image list
      - az vm image show
  - name: --ssh-key-values
    short-summary: Space-separated list of SSH public keys or public key file paths.
examples:
  - name: Create a Windows VM scale set with 5 instances, a load balancer, a public IP address, and a 2GB data disk.
    text: >
        az vmss create -n MyVmss -g MyResourceGroup --instance-count 5 --image Win2016Datacenter --data-disk-sizes-gb 2
  - name: Create a Linux VM scale set with an auto-generated ssh key pair, a public IP address, a DNS entry, an existing load balancer, and an existing virtual network.
    text: |
        az vmss create -n MyVmss -g MyResourceGroup --public-ip-address-dns-name my-globally-dns-name \\
            --load-balancer MyLoadBalancer --vnet-name MyVnet --subnet MySubnet --image UbuntuLTS \\
            --generate-ssh-keys
  - name: Create a Linux VM scale set from a custom image using the default existing public SSH key.
    text: >
        az vmss create -n MyVmss -g MyResourceGroup --image MyImage
  - name: Create a Linux VM scale set with a load balancer and custom DNS servers. Each VM has a public-ip address and a custom domain name.
    text: >
        az vmss create -n MyVmss -g MyResourceGroup --image centos \\
            --public-ip-per-vm --vm-domain-name myvmss --dns-servers 10.0.0.6 10.0.0.5
  - name: 'Create a Linux VM scale set using a cloud-init script for configuration. See: https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init'
    text: >
        az vmss create -g MyResourceGroup -n MyVmss --image debian --custom-data MyCloudInitScript.yml
  - name: Create a Debian VM scaleset using Key Vault secrets.
    text: >
        az keyvault certificate create --vault-name vaultname -n cert1 \\
          -p "$(az keyvault certificate get-default-policy)"

        secrets=$(az keyvault secret list-versions --vault-name vaultname \\
          -n cert1 --query "[?attributes.enabled].id" -o tsv)

        vm_secrets=$(az vm secret format -s "$secrets")


        az vmss create -g group-name -n vm-name --admin-username deploy  \\
          --image debian --secrets "$vm_secrets"
  - name: Create a VM scaleset with system assigned identity. The VM will have a 'Contributor' Role with access to a storage account.
    text: >
        az vmss create -n MyVmss -g MyResourceGroup --image centos --assign-identity --scope /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/MyResourceGroup/myRG/providers/Microsoft.Storage/storageAccounts/storage1
  - name: Create a debian VM scaleset with a user assigned identity.
    text: >
        az vmss create -n MyVmss -g rg1 --image debian --assign-identity  /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
  - name: Create a debian VM scaleset with both system and user assigned identity.
    text: >
        az vmss create -n MyVmss -g rg1 --image debian --assign-identity  [system] /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
  - name: Create a single zone VM scaleset in the current resource group's region
    supported-profiles: latest
    text: >
        az vmss create -n MyVmss -g MyResourceGroup --image Centos --zones 1
"""

helps['vmss deallocate'] = """
type: command
short-summary: Deallocate VMs within a VMSS.
examples:
  - name: Deallocate VMs within a VMSS. (autogenerated)
    text: az vmss deallocate --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss delete-instances'] = """
type: command
short-summary: Delete VMs within a VMSS.
examples:
  - name: Delete VMs within a VMSS. (autogenerated)
    text: az vmss delete-instances --instance-ids 0 --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss diagnostics'] = """
type: group
short-summary: Configure the Azure Virtual Machine Scale Set diagnostics extension.
"""

helps['vmss diagnostics get-default-config'] = """
type: command
short-summary: Show the default config file which defines data to be collected.
"""

helps['vmss diagnostics set'] = """
type: command
short-summary: Enable diagnostics on a VMSS.
examples:
  - name: Enable diagnostics on a VMSS. (autogenerated)
    text: |-
        az vmss diagnostics set --protected-settings {protected-settings} --resource-group MyResourceGroup --settings '{"commandToExecute": "echo testing"}' --vmss-name MyVmss
    crafted: true
"""

helps['vmss disk'] = """
type: group
short-summary: Manage data disks of a VMSS.
"""

helps['vmss disk attach'] = """
type: command
short-summary: Attach managed data disks to a scale set or its instances.
examples:
  - name: Attach managed data disks to a scale set or its instances. (autogenerated)
    text: az vmss disk attach --disk {disk} --instance-id 0 --resource-group MyResourceGroup
    crafted: true
  - name: Attach managed data disks of a given size to a scale set or its instances. (autogenerated)
    text: az vmss disk attach --name MyVmss --resource-group MyResourceGroup --size-gb 50
    crafted: true
"""

helps['vmss disk detach'] = """
type: command
short-summary: Detach managed data disks from a scale set or its instances.
examples:
  - name: Detach managed data disks from a scale set or its instances. (autogenerated)
    text: az vmss disk detach --instance-id 0 --lun {lun} --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss encryption'] = """
type: group
short-summary: "Manage encryption of VMSS."
long-summary: "For more information, see: https://docs.microsoft.com/azure/security/azure-security-disk-encryption-overview"
"""

helps['vmss encryption disable'] = """
type: command
short-summary: Disable the encryption on a VMSS with managed disks.
examples:
  - name: disable encryption a VMSS
    text: >
        az vmss encryption disable -g MyResourceGroup -n MyVm
"""

helps['vmss encryption enable'] = """
type: command
short-summary: "Encrypt a VMSS with managed disks."
long-summary: "For more information, see: For more information, see: https://docs.microsoft.com/azure/security/azure-security-disk-encryption-overview"
examples:
  - name: encrypt a VM scale set using a key vault in the same resource group
    text: >
        az vmss encryption enable -g MyResourceGroup -n MyVmss --disk-encryption-keyvault MyVault
  - name: Encrypt a VMSS with managed disks. (autogenerated)
    text: az vmss encryption enable --disk-encryption-keyvault MyVault --name MyVmss --resource-group MyResourceGroup --volume-type DATA
    crafted: true
"""

helps['vmss encryption show'] = """
type: command
short-summary: Show encryption status.
examples:
  - name: Show encryption status. (autogenerated)
    text: az vmss encryption show --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss extension'] = """
type: group
short-summary: Manage extensions on a VM scale set.
"""

helps['vmss extension delete'] = """
type: command
short-summary: Delete an extension from a VMSS.
examples:
  - name: Delete an extension from a VMSS. (autogenerated)
    text: az vmss extension delete --name MyExtension --resource-group MyResourceGroup --vmss-name MyVmss
    crafted: true
"""

helps['vmss extension image'] = """
type: group
short-summary: Find the available VM extensions for a subscription and region.
"""

helps['vmss extension image list'] = """
type: command
short-summary: List the information on available extensions.
examples:
  - name: List the unique publishers for extensions.
    text: az vmss extension image list --query "[].publisher" -o tsv | sort -u
  - name: Find extensions with "Docker" in the name.
    text: az vmss extension image list --query "[].name" -o tsv | sort -u | grep Docker
  - name: List extension names where the publisher name starts with "Microsoft.Azure.App".
    text: |
        az vmss extension image list --query \\
            "[?starts_with(publisher, 'Microsoft.Azure.App')].publisher" \\
            -o tsv | sort -u | xargs -I{} az vmss extension image list-names --publisher {} -l westus
"""

helps['vmss extension list'] = """
type: command
short-summary: List extensions associated with a VMSS.
examples:
  - name: List extensions associated with a VMSS. (autogenerated)
    text: az vmss extension list --resource-group MyResourceGroup --vmss-name MyVmss
    crafted: true
"""

helps['vmss extension set'] = """
type: command
short-summary: Add an extension to a VMSS or update an existing extension.
long-summary: Get extension details from `az vmss extension image list`.
parameters:
  - name: --name -n
    populator-commands:
      - az vm extension image list
examples:
  - name: >
        Set an extension which depends on two previously set extensions. That is, When a VMSS instance is created or reimaged, the customScript extension will be provisioned only after all extensions that it depends on have been provisioned. The extension need not depend on the other extensions for pre-requisite configurations.
    text: >
        az vmss extension set --vmss-name my-vmss --name customScript --resource-group my-group \\
            --version 2.0 --publisher Microsoft.Azure.Extensions \\
            --provision-after-extensions NetworkWatcherAgentLinux VMAccessForLinux  \\
            --settings '{"commandToExecute": "echo testing"}'
"""

helps['vmss extension show'] = """
type: command
short-summary: Show details on a VMSS extension.
examples:
  - name: Show details on a VMSS extension. (autogenerated)
    text: az vmss extension show --name MyExtension --resource-group MyResourceGroup --vmss-name MyVmss
    crafted: true
"""

helps['vmss get-instance-view'] = """
type: command
short-summary: View an instance of a VMSS.
parameters:
  - name: --instance-id
    short-summary: A VM instance ID or "*" to list instance view for all VMs in a scale set.

examples:
  - name: View an instance of a VMSS. (autogenerated)
    text: az vmss get-instance-view --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss identity'] = """
type: group
short-summary: manage service identities of a VM scaleset.
"""

helps['vmss identity assign'] = """
type: command
short-summary: Enable managed service identity on a VMSS.
long-summary: This is required to authenticate and interact with other Azure services using bearer tokens.
examples:
  - name: Enable system assigned identity on a VMSS with the 'Owner' role.
    text: az vmss identity assign -g MyResourceGroup -n MyVmss --role Owner --scope /subscriptions/db5eb68e-73e2-4fa8-b18a-0123456789999/resourceGroups/MyResourceGroup
"""

helps['vmss identity remove'] = """
type: command
short-summary: Remove user assigned identities from a VM scaleset.
examples:
  - name: Remove system assigned identity
    text: az vmss identity remove -g MyResourceGroup -n MyVmss
  - name: Remove 2 identities which are in the same resource group with the VM scaleset
    text: az vmss identity remove -g MyResourceGroup -n MyVmss --identities readerId writerId
  - name: Remove system assigned identity and a user identity
    text: az vmss identity remove -g MyResourceGroup -n MyVmss --identities [system] readerId
"""

helps['vmss identity show'] = """
type: command
short-summary: display VM scaleset's managed identity info.
examples:
  - name: display VM scaleset's managed identity info. (autogenerated)
    text: az vmss identity show --name MyVirtualMachine --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss list'] = """
type: command
short-summary: List VMSS.
"""

helps['vmss list-instance-connection-info'] = """
type: command
short-summary: Get the IP address and port number used to connect to individual VM instances within a set.
examples:
  - name: Get the IP address and port number used to connect to individual VM instances within a set. (autogenerated)
    text: az vmss list-instance-connection-info --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss list-instance-public-ips'] = """
type: command
short-summary: List public IP addresses of VM instances within a set.
examples:
  - name: List public IP addresses of VM instances within a set. (autogenerated)
    text: az vmss list-instance-public-ips --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss nic'] = """
type: group
short-summary: Manage network interfaces of a VMSS.
"""

helps['vmss reimage'] = """
type: command
short-summary: Reimage VMs within a VMSS.
parameters:
  - name: --instance-id
    short-summary: VM instance ID. If missing, reimage all instances.
examples:
  - name: Reimage VMs within a VMSS. (autogenerated)
    text: az vmss reimage --instance-id 1 --name MyScaleSet --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['vmss restart'] = """
type: command
short-summary: Restart VMs within a VMSS.
examples:
  - name: Restart VMs within a VMSS. (autogenerated)
    text: az vmss restart --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss rolling-upgrade'] = """
type: group
short-summary: Manage rolling upgrades.
"""

helps['vmss run-command'] = """
type: group
short-summary: Manage run commands on a Virtual Machine Scale Set.
long-summary: 'For more information, see https://docs.microsoft.com/azure/virtual-machines/windows/run-command or https://docs.microsoft.com/azure/virtual-machines/linux/run-command.'
"""

helps['vmss run-command invoke'] = """
type: command
short-summary: Execute a specific run command on a Virtual Machine Scale Set instance.
long-summary: >
    `az vmss run-command show` returns helpful information on each run-command.
    Discover Run command-id's via `az vmss run-command list`
parameters:
  - name: --command-id
    type: string
    short-summary: The command id
    populator-commands:
      - az vmss run-command list
  - name: --instance-id
    short-summary: Scale set VM instance id.
examples:
  - name: Install nginx on a VMSS instance.
    text: az vmss run-command invoke -g MyResourceGroup -n MyVMSS --command-id RunShellScript \\ --instance-id 0 --scripts "sudo apt-get update && sudo apt-get install -y nginx"
  - name: Invoke a run-command with parameters on a VMSS instance.
    text: az vmss run-command invoke -g MyResourceGroup -n MyVMSS --command-id RunShellScript \\ --instance-id 4 --scripts 'echo $1 $2' --parameters hello world
  - name: 'Invoke command on all VMSS instances using the VMSS instance resource IDs. Note: "@-" expands to stdin.'
    text: |-
        az vmss list-instances -n MyVMSS -g my-rg --query "[].id" --output tsv | \\
        az vmss run-command invoke --scripts 'echo $1 $2' --parameters hello world  \\
            --command-id RunShellScript --ids @-
  - name: Run powershell script on a windows VMSS instance with parameters. Script supplied inline. Be wary of single-quoting in CMD.exe.
    text: |-
        az vmss run-command invoke  --command-id RunPowerShellScript --name win-vm -g my-resource-group \\
            --scripts 'param([string]$arg1,[string]$arg2)' \\
            'Write-Host This is a sample script with parameters $arg1 and $arg2' \\
            --parameters 'arg1=somefoo' 'arg2=somebar' --instance-id 2
  - name: Run powershell script on a windows VMSS instance with parameters. Script supplied from file.
    text: |-
        # script.ps1
        #   param(
        #       [string]$arg1,
        #       [string]$arg2
        #   )
        #   Write-Host This is a sample script with parameters $arg1 and $arg2

        az vmss run-command invoke  --command-id RunPowerShellScript --name win-vm -g my-resource-group \\
            --scripts @script.ps1 --parameters "arg1=somefoo" "arg2=somebar" --instance-id 5
"""

helps['vmss run-command show'] = """
type: command
parameters:
  - name: --command-id
    type: string
    short-summary: The command id
    populator-commands:
      - az vmss run-command list
examples:
  - name: vmss run-command show (autogenerated)
    text: az vmss run-command show --command-id RunShellScript --location westus2
    crafted: true
"""

helps['vmss scale'] = """
type: command
short-summary: Change the number of VMs within a VMSS.
parameters:
  - name: --new-capacity
    short-summary: Number of VMs in the VMSS.
examples:
  - name: Change the number of VMs within a VMSS. (autogenerated)
    text: az vmss scale --name MyScaleSet --new-capacity 6 --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss show'] = """
type: command
short-summary: Get details on VMs within a VMSS.
parameters:
  - name: --instance-id
    short-summary: VM instance ID. If missing, show the VMSS.
examples:
  - name: Get details on VMs within a VMSS. (autogenerated)
    text: az vmss show --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss start'] = """
type: command
short-summary: Start VMs within a VMSS.
examples:
  - name: Start VMs within a VMSS. (autogenerated)
    text: az vmss start --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss stop'] = """
type: command
short-summary: Power off (stop) VMs within a VMSS.
long-summary: The VMs will continue to be billed. To avoid this, you can deallocate VM instances within a VMSS through "az vmss deallocate"
examples:
  - name: Power off (stop) VMs within a VMSS. (autogenerated)
    text: az vmss stop --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
  - name: Power off VMs within a VMSS without shutting down.
    text: az vmss stop --name MyScaleSet --resource-group MyResourceGroup --skip-shutdown
"""

helps['vmss update'] = """
type: command
short-summary: Update a VMSS.
examples:
  - name: Update a VMSS. (autogenerated)
    text: az vmss update --name MyScaleSet --resource-group MyResourceGroup --set virtualMachineProfile.storageProfile.imageReference.version=16.04.201801090
    crafted: true
  - name: Update a VMSS' license type for Azure Hybrid Benefit.
    text: az vmss update --name MyScaleSet --resource-group MyResourceGroup --license-type windows_server
  - name: Update a VM instance's protection policies.
    text: az vmss update --name MyScaleSet --resource-group MyResourceGroup --instance-id 4             --protect-from-scale-set-actions False --protect-from-scale-in
  - name: Update a VM instance's protection policies.
    text: az vmss update --name MyScaleSet --resource-group MyResourceGroup --instance-id 4             --set protectionPolicy.protectFromScaleIn=True protectionPolicy.protectFromScaleSetActions=False

"""

helps['vmss update-instances'] = """
type: command
short-summary: Upgrade VMs within a VMSS.
examples:
  - name: Upgrade VMs within a VMSS. (autogenerated)
    text: az vmss update-instances --instance-ids 1 --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
"""

helps['vmss wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a scale set is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a scale set is met. (autogenerated)
    text: az vmss wait --created --name MyScaleSet --resource-group MyResourceGroup
    crafted: true
  - name: Place the CLI in a waiting state until the VMSS has been updated.
    text: az vmss wait --updated --name MyScaleSet --resource-group MyResourceGroup
  - name: Place the CLI in a waiting state until the VMSS instance has been updated.
    text: az vmss wait --updated --instance-id 1 --name MyScaleSet --resource-group MyResourceGroup
"""

helps['webapp'] = """
type: group
short-summary: Manage web apps.
"""

helps['webapp auth'] = """
type: group
short-summary: Manage webapp authentication and authorization
"""

helps['webapp auth show'] = """
type: command
short-summary: Show the authentification settings for the webapp.
examples:
  - name: Show the authentification settings for the webapp. (autogenerated)
    text: az webapp auth show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth update'] = """
type: command
short-summary: Update the authentication settings for the webapp.
examples:
  - name: Enable AAD by enabling authentication and setting AAD-associated parameters. Default provider is set to AAD. Must have created a AAD service principal beforehand.
    text: >
        az webapp auth update  -g myResourceGroup -n myUniqueApp --enabled true \\
          --action LoginWithAzureActiveDirectory \\
          --aad-allowed-token-audiences https://webapp_name.azurewebsites.net/.auth/login/aad/callback \\
          --aad-client-id ecbacb08-df8b-450d-82b3-3fced03f2b27 --aad-client-secret very_secret_password \\
          --aad-token-issuer-url https://sts.windows.net/54826b22-38d6-4fb2-bad9-b7983a3e9c5a/
  - name: Allow Facebook authentication by setting FB-associated parameters and turning on public-profile and email scopes; allow anonymous users
    text: >
        az webapp auth update -g myResourceGroup -n myUniqueApp --action AllowAnonymous \\
          --facebook-app-id my_fb_id --facebook-app-secret my_fb_secret \\
          --facebook-oauth-scopes public_profile email
"""

helps['webapp browse'] = """
type: command
short-summary: Open a web app in a browser.
examples:
  - name: Open a web app in a browser. (autogenerated)
    text: az webapp browse --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config'] = """
type: group
short-summary: Configure a web app.
"""

helps['webapp config appsettings'] = """
type: group
short-summary: Configure web app settings. Updating or removing application settings will cause an app recycle.
"""

helps['webapp config appsettings delete'] = """
type: command
short-summary: Delete web app settings.
examples:
  - name: Delete web app settings. (autogenerated)
    text: az webapp config appsettings delete --name MyWebApp --resource-group MyResourceGroup --setting-names {setting-names}
    crafted: true
"""

helps['webapp config appsettings list'] = """
type: command
short-summary: Get the details of a web app's settings.
examples:
  - name: Get the details of a web app's settings. (autogenerated)
    text: az webapp config appsettings list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config appsettings set'] = """
type: command
short-summary: Set a web app's settings.
examples:
  - name: Set the default NodeJS version to 6.9.1 for a web app.
    text: >
        az webapp config appsettings set -g MyResourceGroup -n MyUniqueApp --settings WEBSITE_NODE_DEFAULT_VERSION=6.9.1
  - name: Set using both key-value pair and a json file with more settings.
    text: >
        az webapp config appsettings set -g MyResourceGroup -n MyUniqueApp --settings mySetting=value @moreSettings.json
parameters:
  - name: --settings
    short-summary: Space-separated appsettings in KEY=VALUE format. Use @{file} to load from a file.
  - name: --slot-settings
    short-summary: Space-separated slot appsettings in KEY=VALUE format. Use @{file} to load from a file.
"""

helps['webapp config backup'] = """
type: group
short-summary: Manage backups for web apps.
"""

helps['webapp config backup create'] = """
type: command
short-summary: Create a backup of a web app.
examples:
  - name: Create a backup of a web app. (autogenerated)
    text: az webapp config backup create --container-url {container-url} --resource-group MyResourceGroup --webapp-name MyWebapp
    crafted: true
"""

helps['webapp config backup list'] = """
type: command
short-summary: List backups of a web app.
examples:
  - name: List backups of a web app. (autogenerated)
    text: az webapp config backup list --resource-group MyResourceGroup --webapp-name MyWebapp
    crafted: true
"""

helps['webapp config backup restore'] = """
type: command
short-summary: Restore a web app from a backup.
"""

helps['webapp config backup show'] = """
type: command
short-summary: Show the backup schedule for a web app.
"""

helps['webapp config backup update'] = """
type: command
short-summary: Configure a new backup schedule for a web app.
"""

helps['webapp config connection-string'] = """
type: group
short-summary: Manage a web app's connection strings.
"""

helps['webapp config connection-string delete'] = """
type: command
short-summary: Delete a web app's connection strings.
examples:
  - name: Delete a web app's connection strings. (autogenerated)
    text: az webapp config connection-string delete --name MyWebApp --resource-group MyResourceGroup --setting-names {setting-names}
    crafted: true
"""

helps['webapp config connection-string list'] = """
type: command
short-summary: Get a web app's connection strings.
examples:
  - name: Get a web app's connection strings. (autogenerated)
    text: az webapp config connection-string list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config connection-string set'] = """
type: command
short-summary: Update a web app's connection strings.
examples:
  - name: Add a mysql connection string.
    text: >
        az webapp config connection-string set -g MyResourceGroup -n MyUniqueApp -t mysql \\
            --settings mysql1='Server=myServer;Database=myDB;Uid=myUser;Pwd=myPwd;'
"""

helps['webapp config container'] = """
type: group
short-summary: Manage web app container settings.
"""

helps['webapp config container delete'] = """
type: command
short-summary: Delete a web app container's settings.
"""

helps['webapp config container set'] = """
type: command
short-summary: Set a web app container's settings.
examples:
  - name: Set a web app container's settings. (autogenerated)
    text: az webapp config container set --docker-custom-image-name MyDockerCustomImage --docker-registry-server-password StrongPassword --docker-registry-server-url https://{azure-container-registry-name}.azurecr.io --docker-registry-server-user DockerUserId --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config container show'] = """
type: command
short-summary: Get details of a web app container's settings.
examples:
  - name: Get details of a web app container's settings. (autogenerated)
    text: az webapp config container show --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config hostname'] = """
type: group
short-summary: Configure hostnames for a web app.
"""

helps['webapp config hostname add'] = """
type: command
short-summary: Bind a hostname to a web app.
examples:
  - name: Bind a hostname to a web app. (autogenerated)
    text: az webapp config hostname add --hostname $fqdn --resource-group MyResourceGroup --webapp-name MyWebapp
    crafted: true
"""

helps['webapp config hostname delete'] = """
type: command
short-summary: Unbind a hostname from a web app.
"""

helps['webapp config hostname get-external-ip'] = """
type: command
short-summary: Get the external-facing IP address for a web app.
examples:
  - name: Get the external-facing IP address for a web app. (autogenerated)
    text: az webapp config hostname get-external-ip --resource-group MyResourceGroup --webapp-name MyWebapp
    crafted: true
"""

helps['webapp config hostname list'] = """
type: command
short-summary: List all hostname bindings for a web app.
examples:
  - name: List all hostname bindings for a web app. (autogenerated)
    text: az webapp config hostname list --resource-group MyResourceGroup --webapp-name MyWebapp
    crafted: true
"""

helps['webapp config set'] = """
type: command
short-summary: Set a web app's configuration.
examples:
  - name: turn on "alwaysOn"
    text: >
        az webapp config set -g MyResourceGroup -n MyUniqueApp --always-on true
  - name: turn on "alwaysOn" through a json with content '{"alwaysOn", true}'
    text: >
        az webapp config set -g MyResourceGroup -n MyUniqueApp --generic-configurations "{"alwaysOn": true}"

"""

helps['webapp config show'] = """
type: command
short-summary: Get the details of a web app's configuration.
examples:
  - name: Get the details of a web app's configuration. (autogenerated)
    text: az webapp config show --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config snapshot'] = """
type: group
short-summary: Manage web app snapshots.
"""

helps['webapp config snapshot list'] = """
type: command
short-summary: List the restorable snapshots for a web app.
examples:
  - name: List the restorable snapshots for a web app. (autogenerated)
    text: az webapp config snapshot list --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config snapshot restore'] = """
type: command
short-summary: Restore a web app snapshot.
examples:
  - name: Restore web app files from a snapshot. Overwrites the web app's current files and settings.
    text: >
        az webapp config snapshot restore -g MyResourceGroup -n MySite --time 2018-12-11T23:34:16.8388367
  - name: Restore a snapshot of web app SourceApp to web app TargetApp. Use --restore-content-only to not restore app settings. Overwrites TargetApp's files.
    text: >
        az webapp config snapshot restore -g TargetResourceGroup -n TargetApp --source-name SourceApp --source-resource-group OriginalResourceGroup --time 2018-12-11T23:34:16.8388367 --restore-content-only
"""

helps['webapp config ssl'] = """
type: group
short-summary: Configure SSL certificates for web apps.
"""

helps['webapp config ssl bind'] = """
type: command
short-summary: Bind an SSL certificate to a web app.
examples:
  - name: Bind an SSL certificate to a web app. (autogenerated)
    text: az webapp config ssl bind --certificate-thumbprint {certificate-thumbprint} --name MyWebapp --resource-group MyResourceGroup --ssl-type SNI
    crafted: true
"""

helps['webapp config ssl delete'] = """
type: command
short-summary: Delete an SSL certificate from a web app.
examples:
  - name: Delete an SSL certificate from a web app. (autogenerated)
    text: az webapp config ssl delete --certificate-thumbprint {certificate-thumbprint} --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config ssl list'] = """
type: command
short-summary: List SSL certificates for a web app.
examples:
  - name: List SSL certificates for a web app. (autogenerated)
    text: az webapp config ssl list --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config ssl unbind'] = """
type: command
short-summary: Unbind an SSL certificate from a web app.
"""

helps['webapp config ssl upload'] = """
type: command
short-summary: Upload an SSL certificate to a web app.
examples:
  - name: Upload an SSL certificate to a web app. (autogenerated)
    text: az webapp config ssl upload --certificate-file {certificate-file} --certificate-password {certificate-password} --name MyWebapp     --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config storage-account'] = """
type: group
short-summary: Manage a web app's Azure storage account configurations. (Linux Web Apps and Windows Containers Web Apps Only)
"""

helps['webapp config storage-account add'] = """
type: command
short-summary: Add an Azure storage account configuration to a web app. (Linux Web Apps and Windows Containers Web Apps Only)
examples:
  - name: Add a connection to the Azure Files file share called MyShare in the storage account named MyStorageAccount.
    text: >
        az webapp config storage-account add -g MyResourceGroup -n MyUniqueApp \\
          --custom-id CustomId \\
          --storage-type AzureFiles \\
          --account-name MyStorageAccount \\
          --share-name MyShare \\
          --access-key MyAccessKey \\
          --mount-path /path/to/mount
"""

helps['webapp config storage-account delete'] = """
type: command
short-summary: Delete a web app's Azure storage account configuration. (Linux Web Apps and Windows Containers Web Apps Only)
examples:
  - name: Delete a web app's Azure storage account configuration. (Linux Web Apps and Windows Containers Web Apps Only) (autogenerated)
    text: az webapp config storage-account delete --custom-id CustomId --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config storage-account list'] = """
type: command
short-summary: Get a web app's Azure storage account configurations. (Linux Web Apps and Windows Containers Web Apps Only)
examples:
  - name: Get a web app's Azure storage account configurations. (Linux Web Apps and Windows Containers Web Apps Only) (autogenerated)
    text: az webapp config storage-account list --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config storage-account update'] = """
type: command
short-summary: Update an existing Azure storage account configuration on a web app. (Linux Web Apps and Windows Containers Web Apps Only)
examples:
  - name: Update the mount path for a connection to the Azure Files file share with the ID MyId.
    text: >
        az webapp config storage-account update -g MyResourceGroup -n MyUniqueApp \\
          --custom-id CustomId \\
          --mount-path /path/to/new/mount
  - name: Update an existing Azure storage account configuration on a web app. (Linux Web Apps and Windows Containers Web Apps Only) (autogenerated)
    text: az webapp config storage-account update --access-key MyAccessKey --account-name MyAccount --custom-id CustomId --mount-path /path/to/new/mount --name MyUniqueApp --resource-group MyResourceGroup --share-name MyShare --storage-type AzureFiles
    crafted: true
"""

helps['webapp cors'] = """
type: group
short-summary: Manage Cross-Origin Resource Sharing (CORS)
"""

helps['webapp cors add'] = """
type: command
short-summary: Add allowed origins
examples:
  - name: add a new allowed origin
    text: >
        az webapp cors add -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
"""

helps['webapp cors remove'] = """
type: command
short-summary: Remove allowed origins
examples:
  - name: remove an allowed origin
    text: >
        az webapp cors remove -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
  - name: remove all allowed origins
    text: >
        az webapp cors remove -g {myRG} -n {myAppName} --allowed-origins
"""

helps['webapp cors show'] = """
type: command
short-summary: show allowed origins
examples:
  - name: show allowed origins (autogenerated)
    text: az webapp cors show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp create'] = """
type: command
short-summary: Create a web app.
long-summary: The web app's name must be able to produce a unique FQDN as AppName.azurewebsites.net.
examples:
  - name: Create a web app with the default configuration.
    text: >
        az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName
  - name: Create a web app with a NodeJS 6.2 runtime and deployed from a local git repository.
    text: >
        az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName --runtime "node|6.2" --deployment-local-git
"""

helps['webapp create-remote-connection'] = """
type: command
short-summary: Creates a remote connection using a tcp tunnel to your web app
"""

helps['webapp delete'] = """
type: command
short-summary: Delete a web app.
examples:
  - name: Delete a web app. (autogenerated)
    text: az webapp delete --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deleted'] = """
type: group
short-summary: Manage deleted web apps.
"""

helps['webapp deleted list'] = """
type: command
short-summary: List web apps that have been deleted.
"""

helps['webapp deleted restore'] = """
type: command
short-summary: Restore a deleted web app.
long-summary: Restores the files and settings of a deleted web app to the specified web app.
examples:
  - name: Restore a deleted app to the Staging slot of MySite.
    text: >
        az webapp deleted restore -g MyResourceGroup -n MySite -s Staging --deleted-id /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Web/locations/location/deletedSites/1234
  - name: Restore a deleted app to the app MySite. Do not restore the deleted app's settings.
    text: >
        az webapp deleted restore -g MyResourceGroup -n MySite --deleted-id /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Web/locations/location/deletedSites/1234 --restore-content-only
"""

helps['webapp deployment'] = """
type: group
short-summary: Manage web app deployments.
"""

helps['webapp deployment container'] = """
type: group
short-summary: Manage container-based continuous deployment.
"""

helps['webapp deployment container config'] = """
type: command
short-summary: Configure continuous deployment via containers.
examples:
  - name: Configure continuous deployment via containers. (autogenerated)
    text: az webapp deployment container config --enable-cd true --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment container show-cd-url'] = """
type: command
short-summary: Get the URL which can be used to configure webhooks for continuous deployment.
examples:
  - name: Get the URL which can be used to configure webhooks for continuous deployment (autogenerated)
    text: az webapp deployment container show-cd-url --name MyWebApp --resource-group MyResourceGroup --slot staging
    crafted: true
"""

helps['webapp deployment list-publishing-credentials'] = """
type: command
short-summary: Get the details for available web app publishing credentials
examples:
  - name: Get the details for available web app publishing credentials (autogenerated)
    text: az webapp deployment list-publishing-credentials --name MyWebapp --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['webapp deployment list-publishing-profiles'] = """
type: command
short-summary: Get the details for available web app deployment profiles.
examples:
  - name: Get the details for available web app deployment profiles. (autogenerated)
    text: az webapp deployment list-publishing-profiles --name MyWebapp --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['webapp deployment slot'] = """
type: group
short-summary: Manage web app deployment slots.
"""

helps['webapp deployment slot auto-swap'] = """
type: command
short-summary: Configure deployment slot auto swap.
"""

helps['webapp deployment slot create'] = """
type: command
short-summary: Create a deployment slot.
examples:
  - name: Create a deployment slot. (autogenerated)
    text: az webapp deployment slot create --name MyWebapp --resource-group MyResourceGroup --slot staging
    crafted: true
"""

helps['webapp deployment slot delete'] = """
type: command
short-summary: Delete a deployment slot.
examples:
  - name: Delete a deployment slot. (autogenerated)
    text: az webapp deployment slot delete --name MyWebapp --resource-group MyResourceGroup --slot staging
    crafted: true
"""

helps['webapp deployment slot list'] = """
type: command
short-summary: List all deployment slots.
examples:
  - name: List all deployment slots. (autogenerated)
    text: az webapp deployment slot list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment slot swap'] = """
type: command
short-summary: Change deployment slots for a web app.
examples:
  - name: Swap a staging slot into production for the MyUniqueApp web app.
    text: >
        az webapp deployment slot swap  -g MyResourceGroup -n MyUniqueApp --slot staging \\
            --target-slot production
"""

helps['webapp deployment source'] = """
type: group
short-summary: Manage web app deployment via source control.
"""

helps['webapp deployment source config'] = """
type: command
short-summary: Manage deployment from git or Mercurial repositories.
examples:
  - name: Manage deployment from git or Mercurial repositories. (autogenerated)
    text: az webapp deployment source config --branch master --manual-integration --name MyWebApp --repo-url https://github.com/Azure-Samples/function-image-upload-resize --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment source config-local-git'] = """
type: command
short-summary: Get a URL for a git repository endpoint to clone and push to for web app deployment.
examples:
  - name: Get an endpoint and add it as a git remote.
    text: >
        az webapp deployment source config-local-git \\
            -g MyResourceGroup -n MyUniqueApp

        git remote add azure \\
            https://{deploy_user_name}@MyUniqueApp.scm.azurewebsites.net/MyUniqueApp.git
"""

helps['webapp deployment source config-zip'] = """
type: command
short-summary: Perform deployment using the kudu zip push deployment for a web app.
long-summary: >
    By default Kudu assumes that zip deployments do not require any build-related actions like
    npm install or dotnet publish. This can be overridden by including a .deployment file in your
    zip file with the following content '[config] SCM_DO_BUILD_DURING_DEPLOYMENT = true',
    to enable Kudu detection logic and build script generation process.
    See https://github.com/projectkudu/kudu/wiki/Configurable-settings#enabledisable-build-actions-preview.
    Alternately the setting can be enabled using the az webapp config appsettings set command.
examples:
  - name: Perform deployment by using zip file content.
    text: >
        az webapp deployment source config-zip \\
            -g {myRG} -n {myAppName} \\
            --src {zipFilePathLocation}
"""

helps['webapp deployment source delete'] = """
type: command
short-summary: Delete a source control deployment configuration.
examples:
  - name: Delete a source control deployment configuration. (autogenerated)
    text: az webapp deployment source delete --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment source show'] = """
type: command
short-summary: Get the details of a source control deployment configuration.
examples:
  - name: Get the details of a source control deployment configuration. (autogenerated)
    text: az webapp deployment source show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment source sync'] = """
type: command
short-summary: Synchronize from the repository. Only needed under manual integration mode.
examples:
  - name: Synchronize from the repository. Only needed under manual integration mode. (autogenerated)
    text: az webapp deployment source sync --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment user'] = """
type: group
short-summary: Manage user credentials for deployment.
"""

helps['webapp deployment user set'] = """
type: command
short-summary: Update deployment credentials.
long-summary: All function and web apps in the subscription will be impacted since they share the same deployment credentials.
examples:
  - name: Set FTP and git deployment credentials for all apps.
    text: >
        az webapp deployment user set --user-name MyUserName
"""

helps['webapp hybrid-connection'] = """
type: group
short-summary: methods that list, add and remove hybrid-connections from webapps
"""

helps['webapp hybrid-connection add'] = """
type: command
short-summary: add a hybrid-connection to a webapp
examples:
  - name: add a hybrid-connection to a webapp
    text: az webapp hybrid-connection add -g MyResourceGroup -n MyWebapp --namespace [HybridConnectionNamespace] --hybrid-connection [HybridConnectionName] -s [slot]
"""

helps['webapp hybrid-connection list'] = """
type: command
short-summary: list the hybrid-connections on a webapp
examples:
  - name: list the hybrid-connections on a webapp
    text: az webapp hybrid-connection list -g MyResourceGroup -n MyWebapp -s [slot]
"""

helps['webapp hybrid-connection remove'] = """
type: command
short-summary: remove a hybrid-connection from a webapp
examples:
  - name: remove a hybrid-connection from a webapp
    text: az webapp hybrid-connection remove  -g MyResourceGroup -n MyWebapp --namespace [HybridConnectionNamespace] --hybrid-connection [HybridConnectionName] -s [slot]
"""

helps['webapp identity'] = """
type: group
short-summary: manage web app's managed service identity
"""

helps['webapp identity assign'] = """
type: command
short-summary: assign or disable managed service identity to the web app
examples:
  - name: assign local identity and assign a reader role to the current resource group.
    text: >
        az webapp identity assign -g MyResourceGroup -n MyUniqueApp --role reader --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/MyResourceGroup
  - name: enable identity for the web app.
    text: >
        az webapp identity assign -g MyResourceGroup -n MyUniqueApp
"""

helps['webapp identity remove'] = """
type: command
short-summary: Disable web app's managed service identity
"""

helps['webapp identity show'] = """
type: command
short-summary: display web app's managed service identity
examples:
  - name: display webapp's managed service identity (autogenerated)
    text: az webapp identity show --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp list'] = """
type: command
short-summary: List web apps.
examples:
  - name: List default host name and state for all web apps.
    text: >
        az webapp list --query "[].{hostName: defaultHostName, state: state}"
  - name: List all running web apps.
    text: >
        az webapp list --query "[?state=='Running']"
"""

helps['webapp list-runtimes'] = """
type: command
short-summary: List available built-in stacks which can be used for web apps.
"""

helps['webapp log'] = """
type: group
short-summary: Manage web app logs.
"""

helps['webapp log config'] = """
type: command
short-summary: Configure logging for a web app.
examples:
  - name: Configure logging for a web app. (autogenerated)
    text: az webapp log config --name MyWebapp --resource-group MyResourceGroup --web-server-logging off
    crafted: true
"""

helps['webapp log download'] = """
type: command
short-summary: Download a web app's log history as a zip file.
long-summary: This command may not work with web apps running on Linux.
examples:
  - name: Download a web app's log history as a zip file. (autogenerated)
    text: az webapp log download --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp log show'] = """
type: command
short-summary: Get the details of a web app's logging configuration.
examples:
  - name: Get the details of a web app's logging configuration. (autogenerated)
    text: az webapp log show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp log tail'] = """
type: command
short-summary: Start live log tracing for a web app.
long-summary: This command may not work with web apps running on Linux.
"""

helps['webapp restart'] = """
type: command
short-summary: Restart a web app.
examples:
  - name: Restart a web app. (autogenerated)
    text: az webapp restart --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp show'] = """
type: command
short-summary: Get the details of a web app.
examples:
  - name: Get the details of a web app. (autogenerated)
    text: az webapp show --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp ssh'] = """
type: command
short-summary: SSH command establishes a ssh session to the web container and developer would get a shell terminal remotely.
examples:
  - name: ssh into a web app
    text: >
        az webapp ssh -n MyUniqueAppName -g MyResourceGroup
"""

helps['webapp start'] = """
type: command
short-summary: Start a web app.
examples:
  - name: Start a web app. (autogenerated)
    text: az webapp start --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp stop'] = """
type: command
short-summary: Stop a web app.
examples:
  - name: Stop a web app. (autogenerated)
    text: az webapp stop --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp traffic-routing'] = """
type: group
short-summary: Manage traffic routing for web apps.
"""

helps['webapp traffic-routing clear'] = """
type: command
short-summary: Clear the routing rules and send all traffic to production.
"""

helps['webapp traffic-routing set'] = """
type: command
short-summary: Configure routing traffic to deployment slots.
examples:
  - name: Configure routing traffic to deployment slots. (autogenerated)
    text: az webapp traffic-routing set --distribution staging=50 --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp traffic-routing show'] = """
type: command
short-summary: Display the current distribution of traffic across slots.
examples:
  - name: Display the current distribution of traffic across slots. (autogenerated)
    text: az webapp traffic-routing show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp up'] = """
type: command
short-summary: >
    Create a webapp and deploy code from a local workspace to the app. The command is required to run from the folder
    where the code is present. Current support includes Node, Python, .NET Core and ASP.NET, staticHtml. Node,
    Python apps are created as Linux apps. .Net Core, ASP.NET and static HTML apps are created as Windows apps. If command
    is run from an empty folder, an empty windows web app is created.
examples:
  - name: View the details of the app that will be created, without actually running the operation
    text: >
        az webapp up -n MyUniqueAppName --dryrun
  - name: Create a web app with the default configuration, by running the command from the folder where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName
  - name: Create a web app in a specific region, by running the command from the folder where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName -l locationName
  - name: Deploy new code to an app that was originally created using the same command
    text: >
        az webapp up -n MyUniqueAppName -l locationName
  - name: Create a web app and enable log streaming after the deployment operation is complete. This will enable the default configuration required to enable log streaming.
    text: >
        az webapp up -n MyUniqueAppName --logs
"""

helps['webapp update'] = """
type: command
short-summary: Update a web app.
examples:
  - name: Update the tags of a web app.
    text: >
        az webapp update -g MyResourceGroup -n MyAppName --set tags.tagName=tagValue
"""

helps['webapp vnet-integration'] = """
type: group
short-summary: methods that list, add, and remove virtual network integrations from a webapp
"""

helps['webapp vnet-integration add'] = """
type: command
short-summary: add a regional virtual network integration to a webapp
examples:
  - name: add a regional virtual network integration to a webapp
    text: az webapp vnet-integration add -g MyResourceGroup -n MyWebapp --vnet MyVnetName --subnet MySubnetName -s [slot]
"""

helps['webapp vnet-integration list'] = """
type: command
short-summary: list the virtual network integrations on a webapp
examples:
  - name: list the virtual network integrations on a webapp
    text: az webapp vnet-integration list -g MyResourceGroup -n MyWebapp -s [slot]
"""

helps['webapp vnet-integration remove'] = """
type: command
short-summary: remove a regional virtual network integration from webapp
examples:
  - name: remove a regional virtual network integration from webapp
    text: az webapp vnet-integration remove -g MyResourceGroup -n MyWebapp -s [slot]
"""

helps['webapp webjob'] = """
type: group
short-summary: Allows management operations for webjobs on a web app.
"""

helps['webapp webjob continuous'] = """
type: group
short-summary: Allows management operations of continuous webjobs on a web app.
"""

helps['webapp webjob continuous list'] = """
type: command
short-summary: List all continuous webjobs on a selected web app.
examples:
  - name: List all continuous webjobs on a selected webapp. (autogenerated)
    text: az webapp webjob continuous list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp webjob continuous remove'] = """
type: command
short-summary: Delete a specific continuous webjob.
examples:
  - name: Delete a specific continuous webjob. (autogenerated)
    text: az webapp webjob continuous remove --name MyWebApp --resource-group MyResourceGroup --webjob-name MyWebjob
    crafted: true
"""

helps['webapp webjob continuous start'] = """
type: command
short-summary: Start a specific continuous webjob on a selected web app.
examples:
  - name: Start a specific continuous webjob on a selected web app. (autogenerated)
    text: az webapp webjob continuous start --name MyWebApp --resource-group MyResourceGroup --webjob-name MyWebjob
    crafted: true
"""

helps['webapp webjob continuous stop'] = """
type: command
short-summary: Stop a specific continuous webjob.
examples:
  - name: Stop a specific continuous webjob. (autogenerated)
    text: az webapp webjob continuous stop --name MyWebApp --resource-group MyResourceGroup --webjob-name MyWebjob
    crafted: true
"""

helps['webapp webjob triggered'] = """
type: group
short-summary: Allows management operations of triggered webjobs on a web app.
"""

helps['webapp webjob triggered list'] = """
type: command
short-summary: List all triggered webjobs hosted on a web app.
examples:
  - name: List all triggered webjobs hosted on a web app. (autogenerated)
    text: az webapp webjob triggered list --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp webjob triggered log'] = """
type: command
short-summary: Get history of a specific triggered webjob hosted on a web app.
examples:
  - name: Get history of a specific triggered webjob hosted on a web app. (autogenerated)
    text: az webapp webjob triggered log --name MyWebApp --resource-group MyResourceGroup --webjob-name MyWebjob
    crafted: true
"""

helps['webapp webjob triggered remove'] = """
type: command
short-summary: Delete a specific triggered webjob hosted on a web app.
examples:
  - name: Delete a specific triggered webjob hosted on a web app. (autogenerated)
    text: az webapp webjob triggered remove --name MyWebApp --resource-group MyResourceGroup --webjob-name MyWebjob
    crafted: true
"""

helps['webapp webjob triggered run'] = """
type: command
short-summary: Run a specific triggered webjob hosted on a web app.
"""
