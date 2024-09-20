from mitmproxy import http
import urllib.parse

# List of common XSS patterns
XSS_PATTERNS = [
    "<script>",
    "</script>",
    "javascript:",
    "onerror=",
    "onload=",
    "onmouseover=",
    "onfocus=",
    "onchange=",
    "onclick=",
    "onmousedown=",
    "onmouseup=",
    "onkeydown=",
    "onkeyup=",
    "onkeypress=",
    "prompt("
    "image"
]

def check_for_xss(data: str) -> bool:
    decoded_data = urllib.parse.unquote(data).lower()
    return any(pattern in decoded_data for pattern in XSS_PATTERNS)

def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    headers = flow.request.headers
    body = flow.request.get_text()

    # Check for XSS patterns in URL
    if check_for_xss(url):
        print(f"[XSS] Potential XSS vulnerability detected in URL: {url}")

    # Check for XSS patterns in headers
    for header, value in headers.items():
        if check_for_xss(value):
            print(f"[XSS] Potential XSS vulnerability detected in header: {header}={value}")

    # Check for XSS patterns in request body
    if check_for_xss(body):
        print(f"[XSS] Potential XSS vulnerability detected in body: {body}")

def response(flow: http.HTTPFlow) -> None:
    # Check for XSS patterns in response content
    body = flow.response.get_text()
    if check_for_xss(body):
        print(f"[XSS] Potential XSS vulnerability detected in response body: {body}")
