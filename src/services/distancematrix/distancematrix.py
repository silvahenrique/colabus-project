from botocore.vendored import requests

from settings import API_KEY, GOOGLE_DISTANCE_MATRIX_ENDPOINT


class GoogleDistanceMatrix:
    @staticmethod
    def get_distance_matrix(input_origins, input_destinations):
        user_location_seperator = ','
        destinations_seperator = '|'

        input_origins = [str(value) for (key, value) in input_origins.items()]
        origins = user_location_seperator.join(input_origins)

        destinations = ''
        for input_destination in input_destinations:
            input_destination = [str(value) for (key, value) in input_destination.items()]
            destinations += user_location_seperator.join(input_destination) + destinations_seperator
        destinations = destinations[:-1]

        querystring = {
            "units": "metric",
            "origins": origins,
            "destinations": destinations,
            "key": API_KEY
        }

        response = requests.request("GET", GOOGLE_DISTANCE_MATRIX_ENDPOINT, params=querystring)
        return response.json()
