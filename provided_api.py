import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def name_to_emails(list_of_names):
    return [name+"@gmail.com" for name in list_of_names]

def create_event(meeting_agenda, date, time, duration, invitees):
    # Replace with your own credentials
    creds = Credentials.from_authorized_user_info(info=None)

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
    print(f'Event created: {event.get("htmlLink")}')
    
def get_events(calendar_id):
    # Replace with your own credentials
    creds = Credentials.from_authorized_user_info(info=None)

    # Create a service object
    service = build('calendar', 'v3', credentials=creds)

    # Set the time range for the events
    time_min = '2022-01-01T00:00:00Z'
    time_max = '2022-12-31T23:59:59Z'

    # Call the Calendar API to retrieve the events
    events_result = service.events().list(calendarId=calendar_id, timeMin=time_min, timeMax=time_max, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    # Print the events
    if not events:
        print('No events found.')
    else:
        print('Events:')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(f'{event["summary"]} on {start}')
    

def edit_event(event_id, meeting_agenda, date, time, duration, invitees):