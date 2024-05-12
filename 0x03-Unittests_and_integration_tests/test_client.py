#!/usr/bin/env python3
"""Test suite for client module."""

import unittest
from unittest.mock import patch
from parameterized import parameterized


GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Create an instance of GithubOrgClient
        test_client = GithubOrgClient(org_name)

        # Call the method under test
        test_return = test_client.org

        # Assert that the return value matches the expected payload
        self.assertEqual(test_return, mock_get_json.return_value)

        # Assert that get_json was called exactly once
        mock_get_json.assert_called_once()
