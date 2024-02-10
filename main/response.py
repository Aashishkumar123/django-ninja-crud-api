def response_200(data):
    response = {"status_code": 200, "message": "Success", "data": data}
    return response


def response_201(message):
    response = {"status_code": 201, "message": message}
    return response
