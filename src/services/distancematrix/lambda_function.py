from google_distance_matrix import GoogleDistanceMatrix


def lambda_handler(event, context):
    print(event)
    response = GoogleDistanceMatrix().get_distance_matrix(
        event['input_origins'], event['input_destinations'])
    return {
        'statusCode': 200,
        'body': response
    }
