import logging
import json
import hashlib
import azure.functions as func


def romanizeEdgeCaseStringBuilder(romanizedData: str) -> str:
    # Handle 9s for any type of number
    romanizedData = (
        romanizedData.replace("IIII", "IV")
        .replace("VVVV", "VX")
        .replace("XXXX", "XL")
        .replace("LLLL", "LC")
    )
    romanizedData = romanizedData.replace("CCCC", "CD")

    # Handle odd ball cases
    romanizedData = romanizedData.replace("VIV", "IX")
    romanizedData = romanizedData.replace("LXL", "XC")
    romanizedData = romanizedData.replace("DCD", "CM")
    return romanizedData


def romanizeStringBuilder(integerData: str, divisor: int, romanCharacter: str) -> str:
    """Simplistic casting of Base 10 Integer to Base Roman (?)

    Parameters
    ----------
    integerData : str, required
        The integer data to be converted as a string
    divisor : int, required
        The Base 10 value of the romanCharacter
    romanCharacter : str, required
        The Roman Numerical (character) value to be used in the converstion
    """

    numberOfs = integerData // divisor
    romanizedData = romanCharacter * numberOfs
    logging.info(f"Number of {divisor}s:{numberOfs}")

    return romanizedData


def romanize(data: str) -> str:
    """Converts an integer string into a roman numeral string


    Parameters
    ----------
    data : str, required
        The integer as a string the method will convert to a roman roman numeral
    """

    integerData = int(data)
    romanizedData = ""

    romanizedData += romanizeStringBuilder(integerData, 1000, "M")
    integerData = integerData % 1000

    romanizedData += romanizeStringBuilder(integerData, 500, "D")
    integerData = integerData % 500

    romanizedData += romanizeStringBuilder(integerData, 100, "C")
    integerData = integerData % 100

    romanizedData += romanizeStringBuilder(integerData, 50, "L")
    integerData = integerData % 50

    romanizedData += romanizeStringBuilder(integerData, 10, "X")
    integerData = integerData % 10

    romanizedData += romanizeStringBuilder(integerData, 5, "V")
    integerData = integerData % 5

    romanizedData += romanizeStringBuilder(integerData, 1, "I")
    logging.info(romanizedData)

    romanizedData = romanizeEdgeCaseStringBuilder(romanizedData)

    return romanizedData


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    data = req.params.get("integer")
    if not data:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            data = req_body.get("integer")

    if data:
        mimeType = "application/json"

        romanNumeral = romanize(data)
        tokenizedData = json.dumps({"Roman Numeral": romanNumeral})

        return func.HttpResponse(body=tokenizedData, mimetype=mimeType)
    elif data:
        return func.HttpResponse(body="data is not an integer", status_code=400)
    else:
        return func.HttpResponse(status_code=204)
