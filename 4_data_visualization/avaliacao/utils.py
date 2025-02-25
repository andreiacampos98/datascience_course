import pandas as pd
from geopy.geocoders import Nominatim
df = pd.read_csv("/home/acer/Desktop/datascience_course/4_data_visualization/avaliacao/rain/rain_aus/weatherAUS.csv")

print(df)

print(df.info())

print(df.describe())


geolocator = Nominatim(user_agent="geoapi")

def get_coordinates(city):
    try:
        location = geolocator.geocode(city, timeout=10)
        if location:
            return pd.Series([location.latitude, location.longitude])
    except Exception as e:
        print(f"Erro ao buscar {city}: {e}")
    return pd.Series([None, None])


locations=df['Location'].unique()
city_coords = pd.DataFrame(locations, columns=["Location"])
city_coords[["Latitude", "Longitude"]] = city_coords["Location"].apply(get_coordinates)

print(city_coords)

df = df.merge(city_coords, on="Location", how="left")

print(df)
df.to_csv('weather_update.csv', index=False)
