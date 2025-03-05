import requests

from . import auth

__BASE_URL = 'https://open.api.nexon.com'
__BASE_HEADERS = {
    'x-nxopen-api-key': auth.__API_KEY
}

def request(url, method, headers=None, params=None):
    url = __BASE_URL + url
    headers = (
        dict(headers, **__BASE_HEADERS)
        if headers is not None
        else dict(**__BASE_HEADERS)
    )
    params = params if params is not None else {}
    if 'date' in params and params['date'] is None:
        del params['date']

    if method.upper() == 'GET':
        res = requests.get(url, headers=headers, params=params)
    elif method.upper() == 'POST':
        res = requests.post(url, headers=headers, params=params)
    else:
        return {
            'success': False,
            'error_code': 400,
            'error': {
                'name': "Method Error",
                'message': "Invalid Request Method",
            },
        }

    if res.status_code == 200:
        return {
            'success': True,
            'data': res.json(),
        }
    else:
        return {
            'success': False,
            'error_code': res.status_code,
            'error': res.json()['error'],
        }
