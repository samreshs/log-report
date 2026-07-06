import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "no report.json found"
    return json.loads(REPORT_PATH.read_text())


def test_total_requests():
    """Verifies instruction criterion 1: Count the total number of requests."""
    data = load_report()
    assert data["total_requests"] == 6


def test_unique_client_ips():
    """Verifies instruction criterion 2: Count the number of unique client IP addresses."""
    data = load_report()
    assert data["unique_ips"] == 3


def test_most_frequently_requested_path():
    """Verifies instruction criterion 3: Identify the most frequently requested path."""
    data = load_report()
    assert data["top_path"] == "/index.html"


def test_report_is_valid_json_at_required_path():
    """Verifies instruction criterion 4: Save the report as valid JSON to /app/report.json."""
    data = load_report()
    assert isinstance(data, dict)