'''
Mock interface to Google Calendar bcs permissions make iterations slower
'''
from typing import Sequence
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
        "event_id": "1",
        "summary": "Weekly design sync",
        "location": ["Main Conference Room", test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (tomorrow + timedelta(days=3) + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (tomorrow + timedelta(days=3) + timedelta(hours=9) + timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "kabir@gmail.com", "ron@gmail.com", "patrick@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
    },
    {
        "event_id": "2",
        "summary": "Weekly design sync",
        "location": ["Main Conference Room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (next_week + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (next_week + timedelta(hours=9) + timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "kabir@gmail.com", "ron@gmail.com", "patrick@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
    },
    {
        "event_id": "3",
        "summary": "Spring meeting",
        "location": [test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (tomorrow + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (tomorrow + timedelta(hours=9) + timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "asiya@gmail.com", "ram@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
    },
    {
        "event_id": "4",
        "summary": "Discuss Eng roadmap",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (current_date + timedelta(days=2) + timedelta(hours=10)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (current_date + timedelta(days=2) + timedelta(hours=10) + timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "asiya@gmail.com", "ram@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
     {
        "event_id": "5",
        "summary": "Project proposal review",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (next_friday + timedelta(hours=16)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (next_friday + timedelta(hours=16) + timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "roh@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
     {
        "event_id": "6",
        "summary": "Product meeting",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (two_weeks + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (two_weeks + timedelta(days=2) + timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "roh@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
     {
        "event_id": "7",
        "summary": "Lunch with Rochit",
        "location": ["Zareen's Palo Alto"],
        "description": "This is a new meeting",
                "start": {
            "dateTime": (tomorrow + timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': (two_weeks + timedelta(hours=12) + timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        "attendees": ["kaushik@gmail.com", "rochit@gmail.com"],
        'reminders': {
            'useDefault': True,
        },
     },
]

def name_to_emails(list_of_names: Sequence[str]):
    return [name+"@gmail.com" for name in list_of_names]

def get_events():
    return all_info_prior_meetings

def create_event(meeting_agenda: str, date: datetime.date, time: timedelta, duration: timedelta, invitees: Sequence[str]):
    # Set the meeting details
    starttime = date + time
    endtime = date + time + duration
    len_events = len(get_events())
    event = {
        'event_id': str(len_events),
        'summary': meeting_agenda,
        'location': 'Online',
        'description': 'This is a new meeting',
        'start': {
            'dateTime': starttime.strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': endtime.strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'attendees': [{'email': email} for email in invitees],
        'reminders': {
            'useDefault': True,
        },
    }
    all_info_prior_meetings.append(event)

    return

def edit_event(event_id: str, meeting_agenda: str, date: datetime.date, time: timedelta, duration: timedelta, invitees: Sequence[str]):
    # Set the meeting details
    starttime = date + time
    endtime = date + time + duration
    event = {
        'summary': meeting_agenda,
        'location': 'Online',
        'description': 'This is an edited meeting',
        'start': {
            'dateTime': starttime.strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': endtime.strftime("%Y-%m-%d %H:%M:%S"),
            'timeZone': 'America/New_York',
        },
        'attendees': [{'email': email} for email in invitees],
    }

    for event_info in all_info_prior_meetings:
        if event_info['event_id'] == event_id:
            event_info.update(event)

    return

from provided_api import name_to_emails, create_event, get_events, edit_event
import datetime

# Get tomorrow's date
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

# Create the event
create_event(meeting_agenda="Deep work time for GPT-3 agent", date=tomorrow, time=datetime.time(9, 0), duration=datetime.timedelta(hours=3), invitees=name_to_emails(["John", "Jane"]))

# Get the event
event = get_events()[0]

# Edit the event
edit_event(event_id=event.id, meeting_agenda="Deep work time for GPT-3 agent", date=tomorrow, time=datetime.time(9, 0), duration=datetime.timedelta(hours=3), invitees=name_to_emails(["John", "Jane"]))