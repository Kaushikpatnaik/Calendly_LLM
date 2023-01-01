'''
Mock interface to Google Calendar bcs permissions make iterations slower
'''
from datetime import datetime, timedelta

now = datetime.now()
current_date = datetime.now().date()
tomorrow = current_date + timedelta(days=1)
next_week = current_date + timedelta(weeks=1)
two_weeks = current_date + timedelta(weeks=2)
next_friday = now + timedelta( (4-now.weekday()) % 7 )
test_meet_link = "https://meet.google.com/abc-def-ghi"
test_meet_link2 = "https://meet.google.com/pqr-stu-vwx"

# rescheduling and editing means the model needs access to current meetings via an API
# the prompt will be need to be updated based on the information retrieved in order to complete the plan
# all_info_prior_meetings is the returned meeting information from the API
all_info_prior_meetings = [
    {
        "summary": "Weekly design sync",
        "location": ["Main Conference Room", test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (tomorrow + timedelta(days=3) + timedelta(hours=9)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (tomorrow + timedelta(days=3) + timedelta(hours=9) + timedelta(mins=60)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "kabir@gmail.com", "ron@gmail.com", "patrick@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
    },
    {
        "summary": "Weekly design sync",
        "location": ["Main Conference Room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (next_week + timedelta(hours=9)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (next_week + timedelta(hours=9) + timedelta(mins=60)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "kabir@gmail.com", "ron@gmail.com", "patrick@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
    },
    {
        "summary": "Spring meeting",
        "location": [test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (tomorrow + timedelta(hours=9)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (tomorrow + timedelta(hours=9) + timedelta(mins=30)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "asiya@gmail.com", "ram@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
    },
    {
        "summary": "Discuss Eng roadmap",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (current_date + timedelta(days=2) + timedelta(hours=10)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (current_date + timedelta(days=2) + timedelta(hours=10) + timedelta(mins=60)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "asiya@gmail.com", "ram@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
     {
        "summary": "Project proposal review",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (next_friday + timedelta(hours=16)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (next_friday + timedelta(hours=16) + timedelta(mins=30)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "roh@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
     {
        "summary": "Product meeting",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (two_weeks + timedelta(days=2)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (two_weeks + timedelta(days=2) + timedelta(mins=30)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "roh@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
     {
        "summary": "Lunch with Rochit",
        "location": ["Zareen's Palo Alto"],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (tomorrow + timedelta(hours=12)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (two_weeks + timedelta(hours=12) + timedelta(mins=60)).strfttime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "rochit@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
]

def name_to_emails(list_of_names):
    return [name+"@gmail.com" for name in list_of_names]

def get_events():
    return all_info_prior_meetings

def create_event(meeting_agenda, date, time, duration, invitees):
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

    return event

def edit_event(event_id, meeting_agenda, date, time, duration, invitees):
    # Set the meeting details
    event = {
        'summary': meeting_agenda,
        'location': 'Online',
        'description': 'This is an edited meeting',
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

    return 