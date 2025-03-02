import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Carregar os dados
df = pd.read_csv("/home/anaraujo/Desktop/datascience_course/4_data_visualization/avaliacao/rain/rain_aus/weatherAUS.csv")



# Criar um geolocalizador
geolocator = Nominatim(user_agent="geoapi", timeout=10)

# Função para buscar coordenadas com tratamento de erro e delay
def get_coordinates(city):
    try:
        print(f"Buscando coordenadas para: {city}...")  
        location = geolocator.geocode(f"{city}, Australia", timeout=10)  
        if location:
            print(f"Coordenadas encontradas: {location.latitude}, {location.longitude}")
            return pd.Series([location.latitude, location.longitude])
        else:
            print(f"⚠️ Coordenadas não encontradas para {city}")
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Erro ao buscar {city}: {e}")
    return pd.Series([None, None])


# Criar DataFrame de locais únicos
locations = df['Location'].unique()
city_coords = pd.DataFrame(locations, columns=["Location"])
city_coords["Latitude"] = None  # Inicializa com valores nulos
city_coords["Longitude"] = None



# Preencher coordenadas que ainda não foram buscadas
missing_coords = city_coords[city_coords["Latitude"].isna() | city_coords["Longitude"].isna()]
if not missing_coords.empty:
    missing_coords[["Latitude", "Longitude"]] = missing_coords["Location"].apply(get_coordinates)
    time.sleep(1)  # Delay para evitar bloqueio da API

    # Atualizar cache
    city_coords.update(missing_coords)
    city_coords.to_csv("city_coordinates.csv", index=False)  # Salvar coordenadas para futuras execuções

# Mesclar coordenadas com o DataFrame original
df = df.merge(city_coords, on="Location", how="left")

# Salvar DataFrame atualizado
df.to_csv('weather_update.csv', index=False)

print(df.head())  # Visualizar os primeiros dados

