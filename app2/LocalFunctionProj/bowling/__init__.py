import logging
import json
import azure.functions as func


def computeScore(scorecard: str) -> int:
    """computes a bowling score from a scorecard


    scorecard - a complete games scorecard
    """
    return 10


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("scorecard")
    if not scorecard:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            scorecard = req_body.get("scorecard")

    if name:
        scoreValue = computeScore(scorecard)
        score = json.dumps({"score": scoreValue})
        return func.HttpResponse(scoreValue)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a 'scorecard' in the query string or in the request body to get the computeScore.",
            status_code=200,
        )
