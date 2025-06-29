# HubSpot Contact Sync Test

This is a project I made to explore the HubSpot API, and learn the ropes of APIs in general. 

This Python script uses the HubSpot API to:
- Retrieve contacts from one HubSpot portal: Source (GET)
- Post them to another HubSpot portal: Destination (POST)

## Requirements

- Python 3.x
- `requests` library with `pip install requests`
- `python-dotenv` (if using `.env` for API tokens) `pip install python-dotenv`
- HubSpot private app access token for x2 portals (source and destination). [HubSpot Docs Private Apps Overview](https://developers.hubspot.com/docs/guides/apps/private-apps/overview)

## Limitations
- Limit of 10 contacts for the GET request

## Setup

### Create a new .env file
Replace with your access tokens.

- access_token_source = "your-source-token"
- access_token_destination = "your-destination-token"

### Add .env to .gitignore

Add `*.env` to your `.gitignore` file.
