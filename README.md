# API Security Assessment Toolkit

A Python-based API security assessment framework designed to assist security professionals, penetration testers, and developers in identifying common API security weaknesses.

## Features

* Security Header Analysis
* JWT Token Inspection
* Rate Limiting Assessment
* Markdown Report Generation
* Configurable Target Definitions
* Offline Testing Support

## Current Modules

### Security Headers Check

Identifies missing security-related HTTP headers:

* Content-Security-Policy
* Strict-Transport-Security
* X-Content-Type-Options
* X-Frame-Options
* Referrer-Policy
* Permissions-Policy

### JWT Analysis

Performs basic JWT inspection:

* Header extraction
* Algorithm identification
* Detection of insecure algorithms
* Payload decoding (without signature verification)

### Rate Limiting Assessment

Tests API endpoints for rate limiting controls by:

* Sending multiple requests
* Recording response codes
* Detecting HTTP 429 responses

### Reporting

Generates a structured Markdown report containing findings from all executed modules.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<username>/api-security-assessment-toolkit.git

cd api-security-assessment-toolkit
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Configure the target inside `config.yaml`:

```yaml
target:
  base_url: "http://127.0.0.1:80"
  jwt_token: ""
```

Run the assessment:

```bash
python main.py
```

View the generated report:

```bash
cat reports/sample_report.md
```

---

## Example Findings

### Security Headers

* Missing Content-Security-Policy
* Missing Strict-Transport-Security
* Missing X-Frame-Options

### Rate Limiting

* 10 requests sent
* No HTTP 429 responses observed
* Potential absence of rate limiting controls

---

## Roadmap

Planned enhancements:

* OpenAPI / Swagger Parsing
* BOLA Detection Module
* Authentication Testing
* HTML Reporting
* CVSS-Based Risk Scoring
* Docker Support
* GitHub Actions CI/CD
* OWASP API Top 10 Mapping

---

## Disclaimer

This tool is intended for authorized security testing and educational purposes only. Users are responsible for ensuring they have permission to assess target systems.
