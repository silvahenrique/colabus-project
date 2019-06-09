import json
from botocore.vendored import requests

API_OLHO_VIVO_ENDPOINT = "http://api.olhovivo.sptrans.com.br/v2.1"
TOKEN = "YOUR KEY"


def hit_api(session, resource, querystring=None, method='GET'):
    url = API_OLHO_VIVO_ENDPOINT + resource
    return session.request(method, url, params=querystring)


def api_auth(session):
    querystring = {"token": TOKEN}
    response = hit_api(
        session, resource='/Login/Autenticar', querystring=querystring,
        method='POST')
    print(response.text)


def lambda_handler(event, context):
    session = requests.Session()
    api_auth(session)

    if 'search_term' in event['search_term']:
        return {
            'statusCode': 500,
            'body': {'message': 'Can\'t continue without a search_term!'}
        }

    search_term = event['search_term']
    querystring = {"termosBusca": search_term}
    response = hit_api(
        session, resource='/Linha/Buscar', querystring=querystring)

    parsed = json.loads(response.text)

    return {
        'statusCode': 200,
        'body': parsed
    }
