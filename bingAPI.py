import json 
import os
from pprint import pprint
import requests

'''
This sample uses the Bing Visual Search API with a local, query image and returns several web links
and data of the exact image and/or similar images.
'''
def func(url):
    # Add your Bing Search V7 subscriptionKey and endpoint to your environment variables.
    endpoint = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'

    subscription_key = '6cfe249ba58f46a9b04dbe7f180d592e'

    image_path = 'https://images.pexels.com/photos/8764560/pexels-photo-8764560.jpeg' # for example: my_image.jpg

    # Construct the request
    query = "Describe this image\n"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    # file = {'image' : ('MY-IMAGE', open(image_path, 'rb'))} # MY-IMAGE is the name of the image file (no extention)
    params = {
    'q': query,
    'count': 10,  # Number of results per request (adjust as needed)
    'offset': 0,  # Number of results to skip (if paginating)
    'mkt': 'en-US'  # Market code (adjust as needed)
}
    data = {'imageInfo': {'url': url}}
    response = requests.post(endpoint, headers=headers, params=params, json=data)
    return response.json()
    # Call the API
    # try:
    #     response = requests.post(endpoint, headers=headers, files=file)
    #     response.raise_for_status()

    #     print("\nHeaders:\n")
    #     print(response.headers)

    #     print("\nJSON Response:\n")
    #     pprint(response.json())
    # except Exception as ex:
    #     raise ex

