import logging
import json
import hashlib
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('data')
    if not data:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            data = req_body.get('data')

    customerKey="asdf1234"

    if data:
        token = hashlib.sha256()
        token.update(bytes(data,'UTF-8'))
        token.update(bytes(customerKey,'UTF-8'))
        mimeType = "application/json"
        tokenizedData =json.dumps({
            "token" : token.hexdigest()
            })

        return func.HttpResponse(body=tokenizedData, mimetype=mimeType)
    else:
        return func.HttpResponse(status_code=204)
