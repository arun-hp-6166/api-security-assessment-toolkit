import requests


def parse_openapi_spec(spec_url):
    result = {
        "spec_url": spec_url,
        "status": "completed",
        "endpoints": [],
        "error": None
    }

    try:
        response = requests.get(spec_url, timeout=10)

        if response.status_code != 200:
            result["status"] = "failed"
            result["error"] = f"Unable to fetch OpenAPI spec. Status code: {response.status_code}"
            return result

        spec = response.json()
        paths = spec.get("paths", {})

        for path, methods in paths.items():
            for method in methods.keys():
                result["endpoints"].append({
                    "method": method.upper(),
                    "path": path
                })

    except Exception as error:
        result["status"] = "failed"
        result["error"] = str(error)

    return result
