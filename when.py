import pandas as pd
import requests
import requests_cache
import os
from datetime import datetime

requests_cache.install_cache('strava', expire_after=10800)  # cache for 3 hours

access_token = os.environ['STRAVA_ACCESS_TOKEN']
api_base = 'https://www.strava.com/api/v3'
request_params = {'access_token': '{0}'.format(access_token)}


def get_athlete_id(access_token):
    response = requests.get('{0}/athlete'.format(api_base), params=request_params)
    return response.json()['id']


def get_most_recent_activity(athlete_id):
    response = requests.get('{0}/activities'.format(api_base), params=request_params)
    return pd.to_datetime(response.json()[0]['start_date_local'])


athlete_id = get_athlete_id(access_token)
most_recent_activity_time = get_most_recent_activity(athlete_id)

timedelta = datetime.now() - most_recent_activity_time

print("Last run was {0} days, {1} hours, {2} seconds ago".format(timedelta.components.days, timedelta.components.hours, timedelta.components.seconds))
