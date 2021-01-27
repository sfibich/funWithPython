import logging
import json
import hashlib
import azure.functions as func

def romanize(data) {
    return ('V')
    }

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('integer')
    if not data:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            data = req_body.get('integer')


    if data:
        romanNumeral = romanize(data)
        tokenizedData = json.dumps({
            "Roman Numeral" : romanNumeral
            })

        return func.HttpResponse(body=tokenizedData, mimetype=mimeType)
    else:
        return func.HttpResponse(status_code=204)
