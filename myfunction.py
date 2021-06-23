try:

    import json
    import sys
    import requests
    print("All imports ok ...")
except Exception as e:
    print("Error Imports : {} ".format(e))


def lambda_handler(event, context):

    print("Hello AWS!")
    print("event = {}".format(event))
    return {
        'statusCode': 200,
    }