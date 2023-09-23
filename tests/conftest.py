# coding: utf-8
"""Pytest configuration file."""

import pytest
import requests_mock


@pytest.fixture(scope="function")
def mock_request():
    """."""
    mock_request = requests_mock.Mocker()
    mock_request.headers = {
        "host": "http://test",
        "client_IP": "127.0.0.1",
        "user-agent": "user-agent-test",
    }
    mock_request.client = "127.0.0.0"
    return mock_request
