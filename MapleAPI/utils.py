from datetime import date, datetime, timedelta
from . import character

def datestring(y=None, m=1, d=1):
    if y is None:
        y = date.today().year
        m = date.today().month
        d = date.today().day

    dt = datetime(y, m, d) - timedelta(days=1)
    return dt.strftime("%Y-%m-%d")

def search_stat(stat, query, exact=False):
    return list(
        filter(
            lambda x: x['stat_name'] == query if exact else query in x['stat_name'],
            stat['final_stat']
        )
    )

def power(name):
    stat = character.stat(name)
    po = search_stat(stat['data'], '전투력')[0]
    return int(po['stat_value'])
