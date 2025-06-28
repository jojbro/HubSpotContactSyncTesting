# HubSpot Contact Sync Test

This is a project I made to explore the HubSpot API, and learn the ropes of APIs in general. 

This Python script uses the HubSpot API to:
- Retrieve contacts from one HubSpot portal (GET)
- Post them to another HubSpot portal (POST)

## Requirements

- Python 3.x
- `requests` library with `pip install requests`
- `python-dotenv` (if using `.env` for API tokens) `pip install requests`

## Limitations
- Limit of 10 contacts for GET request

## Setup

### Create a new .env file

access_token_source = "your-source-token"
access_token_destination = "your-destination-token"

### Add .env to .gitignore

Add `*.env` to your `.gitignore` file.