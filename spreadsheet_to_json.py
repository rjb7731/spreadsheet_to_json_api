import pandas as pd
from io import BytesIO
import json

def convert_to_json(file_bytes):
    try:
        df=pd.read_excel(BytesIO(file_bytes))
    except:
        df=pd.read_csv(BytesIO(file_bytes))
    json_collection = []
    for x in range(len(df)):
        row = df.iloc[x].to_json()
        _json =json.loads(row)
        json_collection.append(_json)
    return json_collection