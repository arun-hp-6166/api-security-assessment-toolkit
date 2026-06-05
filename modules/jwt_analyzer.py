import jwt


def analyze_jwt(token):
    result = {
        "status": "completed",
        "algorithm": None,
        "findings": []
    }

    if not token:
        result["status"] = "skipped"
        result["findings"].append("No JWT token supplied")
        return result

    try:
        header = jwt.get_unverified_header(token)

        result["algorithm"] = header.get("alg")

        if header.get("alg") == "none":
            result["findings"].append(
                "JWT uses 'none' algorithm (high risk)"
            )

        decoded = jwt.decode(
            token,
            options={"verify_signature": False}
        )

        result["payload"] = decoded

    except Exception as error:
        result["status"] = "failed"
        result["error"] = str(error)

    return result
