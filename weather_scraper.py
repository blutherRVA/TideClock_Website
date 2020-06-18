import requests
import keys2

lat_ex = '37.5'
lon_ex = '-76.3'



def weath(lat, long):
    # This is the URL that your login form points to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + '&appid=' + keys2.apiKey

    # Dictionary to create login payload

    payload = {
        'username': keys2.apiUserName,
        'pass': keys2.apiPassWord
    }

    with requests.Session() as session:
        post = session.post(post_login_url, data=payload)
        r = session.get(request_url)
        precip = r.json()["weather"]

        for item in precip:
            return item["description"]
            # print(item["description"])


def wind(lat, long):
    # This is the URL that your login form poits to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + '&appid=' + keys2.apiKey

    # Dictionary to create login payload


    payload = {
        'username': keys2.apiUserName,
        'pass': keys2.apiPassWord
    }

    with requests.Session() as session:
        post = session.post(post_login_url, data=payload)
        r = session.get(request_url)
        wind = r.json()["wind"]
        wind_current = wind["speed"]
        return wind_current

def wind_dir(lat, long):
    # This is the URL that your login form poits to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + '&appid=' + keys2.apiKey

    # Dictionary to create login payload
    # OpenWeatherMap API Key  'keys.key'

    payload = {
        'username': keys2.apiUserName,
        'pass': keys2.apiPassWord
    }

    with requests.Session() as session:
        post = session.post(post_login_url, data=payload)
        r = session.get(request_url)
        wind = r.json()["wind"]
        wind_current = wind["deg"]
        if 0 <= wind_current < 90:
            return 'NE'
        elif 90 <= wind_current < 180:
            return 'SE'
        elif 180 <= wind_current < 270:
            return 'SW'
        elif 270 <= wind_current < 360:
            return 'NW'
        else:
            return 'No Wind Data'


if __name__ == "__main__":
    print(weath(lat_ex, lon_ex))
    print(wind(lat_ex, lon_ex))
    print(wind_dir(lat_ex, lon_ex))