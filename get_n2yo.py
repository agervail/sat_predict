import requests
from datetime import datetime

sats = [{'name': 'NOAA_15', 'norad': '25338'},
        {'name': 'NOAA_18', 'norad': '28654'},
        {'name': 'NOAA_19', 'norad': '33591'},
        {'name': 'METEOR_M2', 'norad': '40069'}]

date_format = '%a-%d/%m %H:%M'
hour_format = '%H:%M'

with open('key.private', 'r') as f:
    key = f.readline().strip()

for s in sats:
    r = requests.get('https://www.n2yo.com/rest/v1/satellite/radiopasses/'\
                     + s['norad'] + '/44.535/5.824/0/4/40/',
                     params={'apiKey': key})
    r_j = r.json()

    print('-' * 30)
    print(r_j['info']['satname'])
    for p in r_j['passes']:
        pass_hour_start = datetime.fromtimestamp(p['startUTC'])
        pass_hour_start = pass_hour_start.strftime(date_format)
        pass_hour_max = datetime.fromtimestamp(p['maxUTC'])
        pass_hour_max = pass_hour_max.strftime(hour_format)
        pass_hour_end = datetime.fromtimestamp(p['endUTC'])
        pass_hour_end = pass_hour_end.strftime(hour_format)

        max_elev = p['maxEl']
        print(pass_hour_start, '-', pass_hour_end,
              '\tMaxElev:', max_elev, '(', pass_hour_max, ')',
              '\t', p['startAzCompass'], ' => ', p['endAzCompass'])
