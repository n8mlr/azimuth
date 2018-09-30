from __future__ import print_function
import json


def hello(event, context):
    print("Cloudwatch log entry goes here...")
    body = {
        "message": "Nate went serverless",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
