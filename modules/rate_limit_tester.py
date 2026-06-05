import requests
import time


def test_rate_limit(url, request_count):
    result = {
        "url": url,
        "status": "completed",
        "total_requests": request_count,
        "responses": [],
        "rate_limiting_detected": False,
        "error": None
    }

    try:
        for _ in range(request_count):
            response = requests.get(url, timeout=10)
            result["responses"].append(response.status_code)
            time.sleep(0.2)

        if 429 in result["responses"]:
            result["rate_limiting_detected"] = True

    except requests.exceptions.RequestException as error:
        result["status"] = "failed"
        result["error"] = str(error)

    return result
