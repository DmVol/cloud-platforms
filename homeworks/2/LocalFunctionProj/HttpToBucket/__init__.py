import logging

import azure.functions as func


def main(req: func.HttpRequest, outputblob: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    result = req.get_json()
    result['param'] = name

    outputblob.set(str(result))

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. version(1)")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response. version(1)",
             status_code=200
        )
