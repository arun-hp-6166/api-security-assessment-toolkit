import requests


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def check_security_headers(base_url):
    result = {
        "url": base_url,
        "status": "completed",
        "missing_headers": [],
        "present_headers": []
    }

    try:
        response = requests.get(base_url, timeout=10)
        headers = response.headers

        for header in SECURITY_HEADERS:
            if header in headers:
                result["present_headers"].append(header)
            else:
                result["missing_headers"].append(header)

    except requests.exceptions.RequestException as error:
        result["status"] = "failed"
        result["error"] = str(error)

    return result
