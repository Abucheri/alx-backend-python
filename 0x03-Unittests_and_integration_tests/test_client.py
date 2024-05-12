#!/usr/bin/env python3
"""Test suite for client module."""

import unittest
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos")
    ])
    @patch('client.get_json')
    def test_public_repos_url(self, org_name, expected_url, mock_get_json):
        """Test GithubOrgClient._public_repos_url method."""

        # Mock get_json to return the expected URL
        mock_get_json.return_value = {"repos_url": expected_url}

        # Create an instance of GithubOrgClient with the org_name
        test_client = GithubOrgClient(org_name)

        # Get the public repos URL using the property method
        public_repos_url = test_client._public_repos_url

        # Assert that the return value matches the expected URL
        self.assertEqual(public_repos_url, expected_url)

        # Assert that get_json was called exactly once
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos method."""

        # Mock the public_repos_url property
        mock_url = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = mock_url

        # Mock get_json to return a payload of your choice
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        # Create an instance of GithubOrgClient
        test_client = GithubOrgClient("google")

        # Call the method under test
        repos = test_client.public_repos()

        # Assert that the return value matches the expected
        # list of repositories
        self.assertEqual(repos, ["repo1", "repo2"])

        # Assert that get_json was called exactly once
        mock_get_json.assert_called_once()
