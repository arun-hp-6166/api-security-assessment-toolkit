import os


def write_list(file, items):
    if not items:
        file.write("- None\n")
        return

    for item in items:
        file.write(f"- {item}\n")


def generate_report(results):
    os.makedirs("reports", exist_ok=True)

    with open("reports/sample_report.md", "w") as file:
        file.write("# API Security Assessment Report\n\n")

        if "security_headers" in results:
            data = results["security_headers"]

            file.write("## Security Headers Check\n\n")
            file.write(f"Target URL: `{data['url']}`\n\n")
            file.write(f"Status: `{data['status']}`\n\n")

            file.write("### Present Headers\n")
            write_list(file, data.get("present_headers", []))

            file.write("\n### Missing Headers\n")
            write_list(file, data.get("missing_headers", []))

            file.write("\n")

        if "jwt_analysis" in results:
            data = results["jwt_analysis"]

            file.write("## JWT Analysis\n\n")
            file.write(f"Status: `{data['status']}`\n\n")
            file.write(f"Algorithm: `{data.get('algorithm')}`\n\n")

            file.write("### Findings\n")
            write_list(file, data.get("findings", []))

            file.write("\n")

        if "openapi_parser" in results:
            data = results["openapi_parser"]

            file.write("## OpenAPI / Swagger Endpoint Inventory\n\n")
            file.write(f"Spec URL: `{data.get('spec_url')}`\n\n")
            file.write(f"Status: `{data.get('status')}`\n\n")
            file.write(f"Error: `{data.get('error')}`\n\n")

            file.write("### Discovered Endpoints\n")
            endpoints = data.get("endpoints", [])

            file.write(f"Total Endpoints Discovered: `{len(endpoints)}`\n\n")
            
            if not endpoints:
                file.write("- None\n")
            else:
                for endpoint in endpoints:
                    file.write(
                        f"- `{endpoint['method']}` `{endpoint['path']}`\n"
                    )

            file.write("\n")

        if "rate_limit" in results:
            data = results["rate_limit"]

            file.write("## Rate Limit Test\n\n")
            file.write(f"Target URL: `{data.get('url')}`\n\n")
            file.write(f"Status: `{data['status']}`\n\n")
            file.write(f"Error: `{data.get('error')}`\n\n")
            file.write(f"Total Requests Sent: `{data['total_requests']}`\n\n")
            file.write(
                f"Rate Limiting Detected: `{data.get('rate_limiting_detected')}`\n\n"
            )

            file.write("### Response Status Codes\n")
            write_list(file, data.get("responses", []))
