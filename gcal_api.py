import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def name_to_emails(list_of_names):
    return [name+"@gmail.com" for name in list_of_names]

def _setup_oauth():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file(os.path.join(os.environ['secret_location'], 'token.json'), SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(os.environ['secret_location'], 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.path.join(os.environ['secret_location'], 'token.json'), 'w') as token:
            token.write(creds.to_json())
    
    return creds

def get_events():
    creds = _setup_oauth()

    # Create a service object
    service = build('calendar', 'v3', credentials=creds)

    # Set the time range for the events
    time_min = '2022-12-24T00:00:00Z'
    time_max = '2023-01-31T23:59:59Z'

    # Call the Calendar API to retrieve the events
    events_result = service.events().list(calendarId='primary', timeMin=time_min, timeMax=time_max, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events

def create_event(meeting_agenda, date, time, duration, invitees):
    # Replace with your own credentials
    creds = _setup_oauth()

    # Create a service object
    service = build('calendar', 'v3', credentials=creds)

    # Set the calendar ID
    calendar_id = 'primary'

    # Set the meeting details
    event = {
        'summary': meeting_agenda,
        'location': 'Online',
        'description': 'This is a new meeting',
        'start': {
            'dateTime': f'{date}T{time}:00',
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': f'{date}T{time + duration}:00',
            'timeZone': 'America/New_York',
        },
        'attendees': [{'email': email} for email in invitees],
        'reminders': {
            'useDefault': True,
        },
    }

    # Create the event
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return event

def edit_event(event_id, meeting_agenda, date, time, duration, invitees):
    # Replace with your own credentials
    creds = _setup_oauth()

    # Create a service object
    service = build('calendar', 'v3', credentials=creds)

    # Set the calendar ID
    calendar_id = 'primary'

    # Set the meeting details
    event = {
        'summary': meeting_agenda,
        'location': 'Online',
        'description': 'This is a new meeting',
        'start': {
            'dateTime': f'{date}T{time}:00',
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': f'{date}T{time + duration}:00',
            'timeZone': 'America/New_York',
        },
        'attendees': [{'email': email} for email in invitees],
    }
    
    try:
        updated_event = service.events().patch(calendarId='primary', eventId=event_id, body=event).execute()
        return updated_event
    except HttpError as error:
        print("An error occured")
