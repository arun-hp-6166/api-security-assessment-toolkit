import yaml
from modules.headers_check import check_security_headers
from modules.jwt_analyzer import analyze_jwt
from modules.rate_limit_tester import test_rate_limit
from modules.openapi_parser import parse_openapi_spec
from modules.report_generator import generate_report


def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


def main():
    config = load_config()
    base_url = config["target"]["base_url"]
    results = {}

    print("[+] Starting API Security Assessment...")

    if config["tests"]["security_headers"]:
        results["security_headers"] = check_security_headers(base_url)

    if config["tests"]["jwt_analysis"]:
        token = config["target"].get("jwt_token", "")
        results["jwt_analysis"] = analyze_jwt(token)

    if config["tests"]["rate_limit"]:
        endpoint = config["rate_limit"]["endpoint"]
        count = config["rate_limit"]["requests"]
        results["rate_limit"] = test_rate_limit(base_url + endpoint, count)

    if config["tests"]["openapi_parser"]:
        spec_url = config["openapi"]["spec_url"]
        results["openapi_parser"] = parse_openapi_spec(spec_url)

    generate_report(results)

    print("[+] Assessment completed. Report saved in reports/sample_report.md")


if __name__ == "__main__":
    main()
