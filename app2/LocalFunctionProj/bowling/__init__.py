import logging
import json
import azure.functions as func


def computeValue(element: str) -> int:
    if element == "X":
        elementValue = 10
    elif element == "/":
        elementValue = 10
    elif element == "-":
        elementValue = 0
    else:
        elementValue = int(element)

    return elementValue


def computeScore(scorecard: str) -> int:
    """computes a bowling score from a scorecard


    scorecard - a complete games scorecard
    """

    value = 0
    for location in range(0, len(scorecard)):
        element = scorecard[location]
        elementValue = computeValue(element)
        if location < 9:
            if element == "X":
                elementValue += computeValue(scorecard[location + 1])
                elementValue += computeValue(scorecard[location + 2])
            elif element == "/":
                elementValue -= computeValue(scorecard[location - 1])
                elementValue += computeValue(scorecard[location + 1])
            else:
                pass
        else:
            pass
        value += elementValue
    return value


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    scorecard = req.params.get("scorecard")
    if not scorecard:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            scorecard = req_body.get("scorecard")

    if scorecard:
        mimeType = "application/json"
        scoreValue = computeScore(scorecard)
        score = json.dumps({"score": scoreValue})
        return func.HttpResponse(body=score, mimetype=mimeType)
    else:
        return func.HttpResponse(status_code=204)
