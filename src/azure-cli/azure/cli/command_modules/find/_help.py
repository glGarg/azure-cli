# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['find'] = """
b'type: command\nshort-summary: I\'m an AI robot, my advice is based on our Azure documentation as well as the usage patterns of Azure CLI and Azure ARM users. Using me improves Azure products and documentation.\nexamples:\n  - name: Give me any Azure CLI group and I\xe2\x80\x99ll show the most popular commands within the group.\n    text: |\n        az find "az storage"\n  - name: Give me any Azure CLI command and I\xe2\x80\x99ll show the most popular parameters and subcommands.\n    text: |\n        az find "az monitor activity-log list"\n  - name: You can also enter a search term, and I\'ll try to help find the best commands.\n    text: |\n        az find "arm template"\n'"""
