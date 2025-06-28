import requests
import json
from dotenv import load_dotenv # This reads the .env file and imports the libraries to use later in this file
import os

def main():
    base_url = "https://api.hubapi.com"
    
    load_dotenv()  # Load environment variables

    access_token_source = os.getenv("access_token_source")
    access_token_destination = os.getenv("access_token_destination")

     # Step 1: GET contacts from Source portal
     
     #Where the request is sent
    get_url = f"{base_url}/crm/v3/objects/contacts?limit=10"

    #info used by the script to access the API
    get_headers = {
        'Authorization': f'Bearer {access_token_source}',
        'Content-Type': 'application/json'
    }

    #The action to print text to the terminal
    print("Requesting contacts from Portal A...")
    #Explains what the type of request is (GET)
    response = requests.get(get_url, headers=get_headers)

    #Start of logic IF successful retrieval, start these steps
    if response.status_code == 200:
        print("I've got it! Contact retrieval success! Here's the list of contacts:")
        print(json.dumps(response.json(), indent=2))  # pretty-print the response.text in the JSON format in terminal


        # Step 2: POST contacts to Destination portal
        # Wheret he request is sent
        post_url = f"{base_url}/crm/v3/objects/contacts"
        # info used by the script to access the API
        post_headers = {
        'Authorization': f'Bearer {access_token_destination}',
        'Content-Type': 'application/json'
        }   

        #Define 'Contacts' that the loop will assign the results in
        contacts = response.json().get("results", [])

        # starts a loop to check contact info from the GET request
        for i, contact in enumerate(contacts, 1):
            props = contact.get("properties", {})
            firstname = props.get("firstname", "Unknown")
            lastname = props.get("lastname", "Unknown")
            email = props.get("email")
            
            if not email:
                print(f"Skipping contact #{i} (missing email)")
                continue
        
            #POSTs the contact info to the Destination portal
            post_payload = {
                "properties": {
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email
                }
            }

            #Print info in terminal about status
            print(f"Syncing contact #{i}: {firstname} {lastname} ({email})")
            post_response = requests.post(post_url, headers=post_headers, json=post_payload)
            print(f"Status: {post_response.status_code}, Response: {post_response.text}")
    
    #Other half of logic IF NOT successful, write this
    else:
        print("Failed to retrieve contacts:")
        print(f"Status: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()