api_list_option = """
    Assume access to datetime, typing python libraries.
    Use one or more of provided functions below:
    1.name_to_emails(list_of_names: Sequence[str])
    2.create_event(meeting_agenda: str, date: datetime.date, time: datetime.timedelta, duration: datetime.timedelta, invitees: Sequence[str])
    3.get_events()
    4.edit_event(event_id: str, meeting_agenda: Optional[str], date: Optional[datetime.date], time: Optional[datetime.timedelta], duration: Optional[datetime.timedelta], invitees: Optional[Sequence[str]], cancel=False))
    5.get_event(id: str)

    import the functions from provided_api.py file.
    """

api_list_none = """"""

prompt_w_api = """You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. {api_list_option}
Write code for completing the following request. Let's think step by step.""" + "{query}"

prompt_wo_api = """You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. Write code for completing the following request. Let's think step by step.{query}"""

prompt_w_few_shot_examples = f"""You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. {api_list_option}

Write code for completing the following request. Let's think step by step.
Use the following examples for reasoning steps.

Meeting with Ashish at Blue bottle coffee in San Mateo coming Saturday at 10:30am. Can you setup a meeting? 1hr meeting is fine.

from provided_api import *
# lowercase names and meeting agenda
list_of_names = ["Ashish"]
list_of_names = [s.lower() for s in list_of_names]

meeting_summary = "Meet with Ashish".lower()

# we need to convert the names of the invitees to emails
invitee_emails = name_to_emails(list_of_names)

# get date for meeting
from datetime import datetime, timedelta

today = datetime.now().date()
days_until_saturday = 5 - today.weekday()
if days_until_saturday <= 0: # Target day has passed
    days_until_saturday += 7
coming_saturday = today + timedelta(days_until_saturday)

# time for meeting
time = timedelta(hours=10, minutes=30)

# duration for meeting
duration = timedelta(hours=1)

# create the meeting
create_event("Meet with Ashish", coming_saturday, time, duration, invitee_emails)

# return created meeting
new_event = get_events()[-1]
print(new_event)

Having lunch at 12 for 1.5 hrs with Bill and Jack on Jan 10th at South Park Commons

from provided_api import *
# lowercase names and meeting agenda
list_of_names = ["Bill", "Jack"]
list_of_names = [s.lower() for s in list_of_names]

meeting_summary = ""Lunch with Bill and Jack"".lower()

# we need to convert the names of the invitees to emails
list_of_names = ["Bill", "Jack"]
invitee_emails = name_to_emails(list_of_names)

# get date for meeting
from datetime import datetime, timedelta
meeting_date = datetime.date(2023, 1, 10)

# time for meeting
time = timedelta(hours=12)

# duration for meeting
duration = timedelta(hours=1, minutes=30)

# create the meeting
create_event("Lunch with Bill and Jack", meeting_date, time, duration, invitee_emails)

# return created meeting
new_event = get_events()[-1]
print(new_event)

Cancel the design sync this week

from provided_api import *
# lowercase names and meeting agenda
meeting_summary = "design sync".lower()

# meeting date range
from datetime import datetime, timedelta

dt = datetime.now().date()
window_start = dt - timedelta(days=dt.weekday())
window_start = datetime.combine(window_start, datetime.min.time())
window_end = window_start + timedelta(days=6)
window_end = datetime.combine(window_end, datetime.min.time())

# get possible events based on meeting name
events = get_events()
possible_events = []
for event in events:
    if meeting_summary in event["summary"]:
        possible_events.append(event)

# identify correct event
datetime_format = "%Y-%m-%d %H:%M:%S"
if len(possible_events) == 1:
    correct_event_id = possible_events[0]["event_id"]
else:
    for event in possible_events:
        event_strt = datetime.strptime(event["start"]["dateTime"], datetime_format)
        event_end = datetime.strptime(event["end"]["dateTime"], datetime_format)
        if event_strt >= window_start and event_end <= window_end:
            correct_event_id = event["event_id"]

# edit correct event_id
edited_event = edit_event(correct_event_id, cancel=True)
print(edited_event)
"""+"{query}"

self_heal_prompt = """
Goal: edit the python program given the error string

The following is the program so far:

{program}

The error upon executing the program is:
{error}

Update the code according based on provided program and error.
Feel free to include print statements in the code to help debug issues, their output will be included and visible.
"""