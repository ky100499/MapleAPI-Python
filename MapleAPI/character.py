from . import req
from . import utils

def ocid(name):
    res = req.request(
        '/maplestory/v1/id',
        'GET',
        params={
            'character_name': name
        }
    )

    if res['success']:
        return {
            'success': True,
            'data': res['data']['ocid'],
        }
    else:
        return res

def basicinfo(name, date=None):
    _ocid = ocid(name)
    if not _ocid['success']:
        return _ocid
    else:
        date = date if date is not None else utils.datestring()
        return req.request(
            '/maplestory/v1/character/basic',
            'GET',
            params={
                'ocid': _ocid['data'],
                'date': date,
            }
        )

def popularity(name, date=None):
    _ocid = ocid(name)
    if not _ocid['success']:
        return _ocid
    else:
        date = date if date is not None else utils.datestring()
        return req.request(
            '/maplestory/v1/character/popularity',
            'GET',
            params={
                'ocid': _ocid['data'],
                'date': date,
            }
        )

def stat(name, date=None):
    _ocid = ocid(name)
    if not _ocid['success']:
        return _ocid
    else:
        date = date if date is not None else utils.datestring()
        return req.request(
            '/maplestory/v1/character/stat',
            'GET',
            params={
                'ocid': _ocid['data'],
                'date': date,
            }
        )
