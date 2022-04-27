import logging
import json
import pandas as pd
from io import StringIO
import azure.functions as func
from spreadsheet_to_json import convert_to_json

def main(req: func.HttpRequest) -> func.HttpResponse:
    file = req.get_body()
    if file:
        _json = convert_to_json(file)
        return func.HttpResponse(json.dumps(_json), mimetype='application/json',status_code=200)
    else:
        return func.HttpResponse(
             "Please supply a file to read in bytes format",
             status_code=404
        )
