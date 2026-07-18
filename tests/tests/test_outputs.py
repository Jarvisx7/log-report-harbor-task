import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_report_is_a_json_object_with_the_required_fields():
    """Success criterion 1: save /app/report.json as a JSON object with exactly the required fields."""
    assert REPORT_PATH.is_file(), "missing /app/report.json"
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests_is_correct():
    """Success criterion 2: report the exact number of requests in access.log."""
    assert load_report()["total_requests"] == 6


def test_unique_ips_is_correct():
    """Success criterion 3: report the exact number of distinct client IP addresses in access.log."""
    assert load_report()["unique_ips"] == 3


def test_top_path_is_correct():
    """Success criterion 4: report the most requested path in access.log."""
    assert load_report()["top_path"] == "/index.html"
