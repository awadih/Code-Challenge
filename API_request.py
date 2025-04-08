from requests.exceptions import HTTPError
import requests
import json
import pandas as pd


class Request:
    def __init__(self, city, days):
        self.city = city
        self.days = days

    def forcast(self):
        """
        returns required forcast data for days in the city:
            In hour element:
                time => time
                wind_speed => wind_kph
                cloud_coverage => cloud
                temperature => temp_c
        :return: dataframe
        """
        url = 'https://api.weatherapi.com/v1/forecast.json?key=bea853d469e0444dbe7152331220507&q={}&days={}'.format(
            self.city, self.days)
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_data = json.loads(response.text)
            # Collect required data as one hour element for the 3 days
            list_hour_elements = list()
            for i in range(3):
                list_hour_elements.extend(json_data['forecast']['forecastday'][i]['hour'])
            dataFrame = pd.DataFrame(list_hour_elements)
            df_required = dataFrame[['time', 'wind_kph', 'temp_c', 'cloud']]
            df_required = df_required.rename(columns={'time': 'Datum/Uhr', 'wind_kph': 'Windgeschwindigkeit (Km/h)',
                                                      'temp_c': 'Temperatur (Celsius)',
                                                      'cloud': 'Cloud coverage (Percent)'})
            return df_required
        except HTTPError as http_err:
            print(f'HTTPS error: {http_err}')
        except Exception as err:
            print(f'Other error: {err}')
        return pd.DataFrame({'Datum/Uhr': [], 'Windgeschwindigkeit (Km/h)': [], 'Temperatur (Celsius)': [],
                             'Cloud coverage (Percent)': []})
