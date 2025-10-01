def handler(request):
    emailcontent = request.get("query", {}).get("email","vazio")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": emailcontent
    }