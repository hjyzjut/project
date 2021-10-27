import json

def json_load(request):
    data = []
    for val in request.data['data']:
        val['user'] = request.data['user']
        data.append(val)
    return data

