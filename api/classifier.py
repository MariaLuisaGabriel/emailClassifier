from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

def handler(request: BaseHTTPRequestHandler):
    emailcontent = request.get("query", {}).get("email","vazio")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": emailcontent
    }