from flask import Flask, request, jsonify, render_template

def receber_dados(request):
    emailcontent = request.get("query", {}).get("email")
    return {
        "statusCode": 200,
        "body": jsonify({
        "mensagem": f"{emailcontent}"
    })
}