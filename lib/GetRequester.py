""" All work should be completed in lib/GetRequester.py. Use the previous code-along on getting data from APIs as a reference when building out your class.

Start by creating a GetRequester class. This class should be able to initialize with a string URL.

The GetRequester class should have a get_response_body method that sends a GET request to the URL passed in on initialization. This method should return the body of the response.

The GetRequester class should have a load_json method that should use get_response_body to send a request, then return a Python list or dictionary made up of data converted from the response of that request.

The tests in this lab will use your code to send a request for some JSON data, located at https://learn-co-curriculum.github.io/json-site-example/endpoints/people.jsonLinks to an external site.. Read the test error messages for additional as you work for additional information. Don't forget to import the necessary Python modules and classes!

This is a test-driven lab. Run pipenv install to create your virtual environment and pipenv shell to enter the virtual environment. Then run pytest -x to run your tests. Use these instructions and pytest's error messages to complete your work in the lib/ folder.

Once all of your tests are passing, commit and push your work using git to submit. """
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

