#!/usr/bin/env python3
"""Test suite for client module."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests for GithubOrgClient.org"""

        # Create a GithubOrgClient instance
        client = GithubOrgClient(org_name)

        # Call the org method
        client.org()

        # Assert that get_json was called once with the expected URL
        expected_url = client.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)
