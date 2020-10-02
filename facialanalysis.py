import json
import csv
import boto3
from datasecret import aws_access_key_id, aws_secret_access_key, aws_session_token
import pprint

# creating a variable with image location
photo = 'person.jpg'

# calling client method by passing arguments like service names,access key, id and token adnd make instance of it
client = boto3.client('rekognition',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, region_name='us-east-1')

# reading image and using read method the source image is converted into binary form
with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

# using detect_faces method for facial analysis and getting all requires results by passing images in bytes and passing arugment Attributes for getting all results like wearing glass ,having mustache or not,eyes are open or not etc
response = client.detect_faces(
    Image={'Bytes': source_bytes}, Attributes=['ALL'])

# If there is multiple faces image passed then multiple face detail retrieve so loop used  get details of multiple face
for k, v in response.items():
    if k == "FaceDetails":
        for people in v:
            # to remove encoding problem bytes using json dump to convert into string and json loads to python format
            people = json.dumps(people)
            people = json.loads(people)
            # print the results into console
            print('\t\t=====================PREDICTIONS========================')
            print('\t\tlooks like a face: ',
                  people['Confidence'], '%')
            print('\t\tappears to be: ',
                  people['Gender']['Value'], '-', people['Gender']['Confidence'], '%')
            print('\t\tage range: ',
                  people['AgeRange']['Low'], '-', people['AgeRange']['High'])
            print('\t\tsimiling: ',
                  people['Smile']['Value'], '-', people['Smile']['Confidence'], '%')
            print('\t\tappears to be: ',
                  people['Emotions'][0]['Type'], '-', people['Emotions'][0]['Confidence'], '%')
            print('\t\twearing glasses: ',
                  people['Sunglasses']['Value']
                  )
            print('\t\twearing sunglasses: ',
                  people['Sunglasses']['Value'], '-', people['Sunglasses']['Confidence'], '%'
                  )
            print('\t\teyes are open: ',
                  people['EyesOpen']['Value'], '-', people['EyesOpen']['Confidence'], "%"
                  )
            print('\t\tmouth is open: ',
                  people['MouthOpen']['Value'], '-', people['MouthOpen']['Confidence'], '%'
                  )
            print('\t\tdoes not have a mustache: ',
                  people['Mustache']['Value'], '-', people['Mustache']['Confidence'], '%'
                  )
            print('\t\tdoes not have a beard: ',
                  people['Beard']['Value'], '-', people['Beard']['Confidence'], '%'
                  )
            print('\t\t========================================================')
