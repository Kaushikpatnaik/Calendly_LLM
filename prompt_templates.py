api_list_option = """
    Assume access to datetime, typing python libraries.
    Use one or more of provided functions below:
    1.name_to_emails(list_of_names: Sequence[str])
    2.create_event(meeting_agenda: str, date: datetime.date, time: datetime.timedelta, duration: datetime.timedelta, invitees: Sequence[str])
    3.get_events()
    4.edit_event(event_id: str, meeting_agenda: str, date: datetime.date, time: datetime.timedelta, duration: datetime.timedelta, invitees: Sequence[str])
    5.get_event(id: str)

    import the functions from provided_api.py file.
    """

api_list_none = """"""

prompt_w_api = f"""You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. {api_list_option}
Write code for completing the following request. Let's think step by step.""" + "{query}"

prompt_wo_api = """You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. Write code for completing the following request. Let's think step by step.{query}"""

prompt_w_few_shot_examples = f"""You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. {api_list_option}

Write code for completing the following request. Let's think step by step.
Use the following examples for reasoning steps.

Meeting with Ashish at Blue bottle coffee in San Mateo coming Saturday at 10:30am. Can you setup a meeting? 1hr meeting is fine.

from provided_api import *
# we need to convert the names of the invitees to emails
list_of_names = ["Ashish"]
invitee_emails = name_to_emails(list_of_names)

# get date for meeting
from datetime import datetime, timedelta

today = datetime.date()
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

""" + "{query}"