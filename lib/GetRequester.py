import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url #initializing the class with the url being a string
    def get_response_body(self):
        response = requests.get(self.url) #sending a GET request to the server

        if response.status_code == 200:
            return response.content # if request was successful and returns a raw data coz we said response.content
        else:
            print(f'Error: Failed to get response from {self.url}. Status code: {response.status_code}')
            return None # checks if the status code is correct and if its correct it returns the text els it says error
        


    def load_json(self): #getting the response body from the server and converts it to python list or directory
        response_body = self.get_response_body() # takes the get_responce_body function. like it youses the get_responce_body method
        try:
            data = json.loads(response_body)# uses json.loads to convert the response ito readable form 
            return data # returns the converted 
        except json.JSONDecodeError:
            print('Error: Invalid JSON')
            return None
        
        
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()

