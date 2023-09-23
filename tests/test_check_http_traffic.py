# coding: utf-8
"""."""
from datadome_module.main import check_http_traffic
import responses


@check_http_traffic
def method_to_check(**kwargs):
    """."""
    result = kwargs.get("request")
    return result


@responses.activate
def test_check_http_traffic_decorator_allow(mock_request):
    """."""
    responses.add(
        method=responses.POST,
        url="http://localhost:8000/check_incomming_http_traffic",
        json={"status": "Granted"},
        status=201,
    )
    result = method_to_check(request=mock_request)
    assert result.allow_traffic is True


@responses.activate
def test_check_http_traffic_decorator_denied(mock_request):
    """."""
    responses.add(
        method=responses.POST,
        url="http://localhost:8000/check_incomming_http_traffic",
        json={"status": "Denied"},
        status=403,
    )
    result = method_to_check(request=mock_request)
    assert result.allow_traffic is False
