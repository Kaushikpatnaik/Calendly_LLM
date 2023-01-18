"""
Mock interface to Google Calendar bcs permissions make iterations slower
"""
from typing import Sequence, Optional
from datetime import datetime, timedelta
from collections import defaultdict

now = datetime.now()
current_date = datetime.now().date()
tomorrow = current_date + timedelta(days=1)
next_week = current_date + timedelta(weeks=1)
two_weeks = current_date + timedelta(weeks=2)
next_friday = now + timedelta((4 - now.weekday()) % 7)
test_meet_link = "https://meet.google.com/abc-def-ghi"
test_meet_link2 = "https://meet.google.com/pqr-stu-vwx"

# rescheduling and editing means the model needs access to current meetings via an API
# the prompt will be need to be updated based on the information retrieved in order to complete the plan
# all_info_prior_meetings is the returned meeting information from the API
all_info_prior_meetings = [
    {
        "event_id": "1",
        "summary": "weekly design sync",
        "location": ["Main Conference Room", test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (tomorrow + timedelta(days=3) + timedelta(hours=9)).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": (
                tomorrow
                + timedelta(days=3)
                + timedelta(hours=9)
                + timedelta(minutes=60)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": [
            "kaushik@gmail.com",
            "kabir@gmail.com",
            "ron@gmail.com",
            "patrick@gmail.com",
        ],
        "reminders": {
            "useDefault": True,
        },
    },
    {
        "event_id": "2",
        "summary": "weekly design sync",
        "location": ["Main Conference Room", test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (next_week + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": (
                next_week + timedelta(hours=9) + timedelta(minutes=60)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": [
            "kaushik@gmail.com",
            "kabir@gmail.com",
            "ron@gmail.com",
            "patrick@gmail.com",
        ],
        "reminders": {
            "useDefault": True,
        },
    },
    {
        "event_id": "3",
        "summary": "sprint meeting",
        "location": [test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (tomorrow + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": (
                tomorrow + timedelta(hours=9) + timedelta(minutes=30)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": [
            "kaushik@gmail.com",
            "asiya@gmail.com",
            "ram@gmail.com",
            "arvind@gmail.com",
            "alex@gmail.com",
        ],
        "reminders": {
            "useDefault": True,
        },
    },
    {
        "event_id": "4",
        "summary": "discuss eng roadmap",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (
                current_date + timedelta(days=2) + timedelta(hours=10)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": (
                current_date
                + timedelta(days=2)
                + timedelta(hours=10)
                + timedelta(minutes=60)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": [
            "kaushik@gmail.com",
            "asiya@gmail.com",
            "ram@gmail.com",
            "arvind@gmail.com",
            "alex@gmail.com",
        ],
        "reminders": {
            "useDefault": True,
        },
    },
    {
        "event_id": "5",
        "summary": "project proposal review",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (next_friday + timedelta(hours=16)).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": (
                next_friday + timedelta(hours=16) + timedelta(minutes=30)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": ["kaushik@gmail.com", "roh@gmail.com"],
        "reminders": {
            "useDefault": True,
        },
    },
    {
        "event_id": "6",
        "summary": "product meeting",
        "location": ["Secondary conference room", test_meet_link],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (two_weeks + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": (
                two_weeks + timedelta(days=2) + timedelta(minutes=30)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": [
            "kaushik@gmail.com",
            "roh@gmail.com",
            "arvind@gmail.com",
            "alex@gmail.com",
        ],
        "reminders": {
            "useDefault": True,
        },
    },
    {
        "event_id": "7",
        "summary": "lunch with rochit",
        "location": ["Zareen's Palo Alto"],
        "description": "This is a new meeting",
        "start": {
            "dateTime": (tomorrow + timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": (
                two_weeks + timedelta(hours=12) + timedelta(minutes=60)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": ["kaushik@gmail.com", "rochit@gmail.com"],
        "reminders": {
            "useDefault": True,
        },
    },
]


def name_to_emails(list_of_names: Sequence[str]):
    return [name + "@gmail.com" for name in list_of_names]


def get_events():
    return all_info_prior_meetings


def create_event(
    meeting_agenda: str,
    date: datetime.date,
    time: timedelta,
    duration: timedelta,
    invitees: Sequence[str],
):
    # Set the meeting details
    starttime = date + time
    endtime = date + time + duration
    len_events = len(get_events())
    event = {
        "event_id": str(len_events),
        "summary": meeting_agenda,
        "location": "Online",
        "description": "This is a new meeting",
        "start": {
            "dateTime": starttime.strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": endtime.strftime("%Y-%m-%d %H:%M:%S"),
            "timeZone": "America/New_York",
        },
        "attendees": [{"email": email} for email in invitees],
        "reminders": {
            "useDefault": True,
        },
    }
    all_info_prior_meetings.append(event)

    return


def edit_event(
    event_id: str,
    meeting_agenda: Optional[str] = None,
    date: Optional[datetime.date] = None,
    time: Optional[timedelta] = None,
    duration: Optional[timedelta] = None,
    invitees: Optional[Sequence[str]] = None,
    cancel=False,
):
    for idx, event_info in enumerate(all_info_prior_meetings):
        if event_info["event_id"] == event_id:
            if cancel:
                return all_info_prior_meetings.pop(idx)
            starttime = datetime.strptime(
                event_info["start"]["dateTime"], "%Y-%m-%d %H:%M:%S"
            )
            endtime = datetime.strptime(
                event_info["end"]["dateTime"], "%Y-%m-%d %H:%M:%S"
            )
            event_duration = endtime - starttime
            event_date = starttime.date()
            event_time = starttime - datetime.combine(event_date, datetime.min.time())
            if meeting_agenda:
                event_info["summary"] = meeting_agenda
            if date:
                event_info["start"]["dateTime"] = (date + event_time).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                event_info["end"]["dateTime"] = (
                    date + event_time + event_duration
                ).strftime("%Y-%m-%d %H:%M:%S")
            if time:
                event_info["start"]["dateTime"] = (event_date + time).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                event_info["end"]["dateTime"] = (
                    event_date + time + event_duration
                ).strftime("%Y-%m-%d %H:%M:%S")
            if duration:
                event_info["end"]["dateTime"] = (
                    event_date + event_time + duration
                ).strftime("%Y-%m-%d %H:%M:%S")
            if invitees:
                event_info["attendees"] += invitees
            return event_info


def _availability_invitee():
    # utility to convert event DB to availibility for invitees
    attendee_event_times = defaultdict(list)
    for event in all_info_prior_meetings:
        event_attendees = event["attendees"]
        event_start_time = datetime.strptime(
            event["start"]["dateTime"], "%Y-%m-%d %H:%M:%S"
        )
        event_end_time = datetime.strptime(
            event["end"]["dateTime"], "%Y-%m-%d %H:%M:%S"
        )
        for event_attendee in event_attendees:
            attendee_event_times[event_attendee].append(
                [event_start_time, event_end_time]
            )

    return attendee_event_times


attendee_event_times = _availability_invitee()


def _get_available_times(event_times: list, duration: timedelta):
    """
    Gets the list of available times for a given list of event times.

    Args:
        event_times (list): A list of start and end times for events.
        duration (timedelta): The duration of the meeting.

    Returns:
        A set of datetime objects representing the available times.
    """

    # group events by date
    events_by_date = defaultdict(list)
    for event in event_times:
        date = event[0].date()
        events_by_date[date].append(event)

    # find available times per date
    available_times = []
    for date, events in events_by_date.items():
        start_time = datetime.combine(
            date, datetime.strptime("09:00:00", "%H:%M:%S").time()
        )
        end_time = datetime.combine(
            date, datetime.strptime("17:00:00", "%H:%M:%S").time()
        )
        for event in events:
            event_start_time = event[0]
            event_end_time = event[1]
            if event_start_time > start_time:
                if event_end_time - start_time >= duration:
                    available_times.append([start_time, event_start_time])
            start_time = event_end_time
        if start_time < end_time:
            if end_time - start_time >= duration:
                available_times.append([start_time, end_time])

    return available_times


def _find_intersection_times(events_a, events_b):
    intersection = []
    for event_a in events_a:
        for event_b in events_b:
            start_a = event_a[0]
            end_a = event_a[1]
            start_b = event_b[0]
            end_b = event_b[1]
            if start_a < end_b and start_b < end_a:
                intersection.append(
                    [
                        max(start_a, start_b).strftime("%Y-%m-%d %H:%M:%S"),
                        min(end_a, end_b).strftime("%Y-%m-%d %H:%M:%S"),
                    ]
                )
    return intersection


def find_time(invitees: Sequence[str], duration: timedelta, meeting_agenda: str):
    """
    Finds a time when all invitees are available for a meeting of the given duration.

    Args:
        invitees (Sequence[str]): A list of invitees
        duration (timedelta): The duration of the meeting
        meeting_agenda (str): The agenda of the meeting

    Returns:
        datetime: A datetime object representing the time when all invitees are available
    """

    # Get the list of available times for each invitee
    available_times = defaultdict(list)
    for invitee in invitees:
        available_times[invitee] = _get_available_times(
            attendee_event_times[invitee], duration
        )

    # Find the intersection of all available times
    first_invitee_avail = available_times[invitees[0]]
    for invitee in invitees[1:]:
        first_invitee_avail = _find_intersection_times(
            first_invitee_avail, available_times[invitee]
        )

    # Find the earliest time in the intersection
    earliest_time = min(first_invitee_avail)

    return earliest_time
