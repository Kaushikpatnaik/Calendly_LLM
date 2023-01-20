from datetime import datetime, timedelta

# need zero follow-up
# different ways of stating meeting details, including multiple people
all_info_create_test_cases = [
    "Book a meeting with Sirish next tuesday at 3pm. Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long.",
    "Schedule 30 minutes with ramesh tomorrow at 4:30pm to chat about hiring plans.",
    "Setup a follow-up with patrick a week from today for 30mins at 2pm. Need to discuss project updates.",
    "Want to meet asiya to discuss eng roadmap. Can you schedule a 1hr meeting thursday at 11am.",
    "Need to give updates on product progress to Paul. I will need a few days to work on this, so schedule 1hr two weeks from today at 10am.",
    "Setup an early 1.5 hr dinner with Roh, Mihir and Sirish tomorrow at 6pm to catch up.",
    "Block deep work time 9am-12pm tomorrow to focus on coding for GPT-3 agent.",
    "Create a 30min meeting for phone interview with Ram, next Wednesday at 3pm.",
    "1hr Meeting to discuss Eng roadmap, with Ravi, Asiya, Paul and Roh this Friday at 11am.",
    "Book some time, 45 mins, with Roh and Mihir to discuss eng pipeline, next Monday at 3pm.",
]

now = datetime.now()
current_date = datetime.now().date().strftime("%Y-%m-%d")
tomorrow = (current_date + timedelta(days=1)).strftime("%Y-%m-%d")
next_week = (current_date + timedelta(weeks=1)).strftime("%Y-%m-%d")
two_weeks = (current_date + timedelta(weeks=2)).strftime("%Y-%m-%d")

def get_next_weekday(day_of_week):
    today = (datetime.now() + timedelta(weeks=1)).date()
    days_until_weekday = day_of_week - today.weekday()
    next_weekday = today + timedelta(days_until_weekday)
    return next_weekday.strftime("%Y-%m-%d")

def get_weekday(day_of_week):
    today = datetime.now().date()
    days_until_weekday = day_of_week - today.weekday()
    if days_until_weekday <= 0: # Target day has passed
        days_until_weekday += 7
    next_weekday = today + timedelta(days_until_weekday)
    return next_weekday.strftime("%Y-%m-%d")


all_info_create_test_answers = [
    {
        "event_id": "7",
        "summary": "Discuss 2023 plans",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": get_next_weekday(1) + " 15:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": get_next_weekday(1) + " 16:00:00", "timeZone": "America/New_York"},
        "attendees": [{"email": "sirish@gmail.com"}],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "8",
        "summary": "Chat with Ramesh about hiring plans",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": tomorrow + " 16:30:00", "timeZone": "America/New_York"},
        "end": {"dateTime": tomorrow + " 17:00:00", "timeZone": "America/New_York"},
        "attendees": [{"email": "ramesh@gmail.com"}],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "9",
        "summary": "Follow-up with Patrick",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": next_week + " 14:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": next_week + " 14:30:00", "timeZone": "America/New_York"},
        "attendees": [{"email": "patrick@gmail.com"}],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "10",
        "summary": "Discuss Eng Roadmap",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": get_weekday(3) + " 11:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": get_weekday(3) + " 12:00:00", "timeZone": "America/New_York"},
        "attendees": [{"email": "asiya@gmail.com"}],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "11",
        "summary": "Product progress update",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": two_weeks + " 10:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": two_weeks + " 11:00:00", "timeZone": "America/New_York"},
        "attendees": [{"email": "paul@gmail.com"}],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "12",
        "summary": "Dinner with Roh, Mihir and Sirish",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": tomorrow + " 18:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": tomorrow + " 19:30:00", "timeZone": "America/New_York"},
        "attendees": [
            {"email": "roh@gmail.com"},
            {"email": "mihir@gmail.com"},
            {"email": "sirish@gmail.com"},
        ],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "13",
        "summary": "Deep work time for GPT-3 agent",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": tomorrow + " 09:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": tomorrow + " 12:00:00", "timeZone": "America/New_York"},
        "attendees": [],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "14",
        "summary": "Phone interview with Ram",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": get_next_weekday(2) + " 15:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": get_next_weekday(2) + " 15:30:00", "timeZone": "America/New_York"},
        "attendees": [{"email": "ram@gmail.com"}],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "15",
        "summary": "Discuss Eng roadmap",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": get_weekday(4) + " 11:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": get_weekday(4) + " 12:00:00", "timeZone": "America/New_York"},
        "attendees": [
            {"email": "ravi@gmail.com"},
            {"email": "asiya@gmail.com"},
            {"email": "paul@gmail.com"},
            {"email": "roh@gmail.com"},
        ],
        "reminders": {"useDefault": True},
    },
    {
        "event_id": "16",
        "summary": "Discuss eng pipeline",
        "location": "Online",
        "description": "This is a new meeting",
        "start": {"dateTime": get_next_weekday(0) + " 15:00:00", "timeZone": "America/New_York"},
        "end": {"dateTime": get_next_weekday(0) + " 15:45:00", "timeZone": "America/New_York"},
        "attendees": [{"email": "roh@gmail.com"}, {"email": "mihir@gmail.com"}],
        "reminders": {"useDefault": True},
    },
]

# rescheduling and editing
all_info_edit_test_cases = [
    "Reschedule tomorrow's sprint meeting to start at 11am.",
    "Cancel the design sync this week.",
    "Add Roh to the meeting on eng roadmap.",
    "I can't attend next week's design sync.",
    "Need to pickup my parents this friday afternoon. Can't make meetings post 3pm.",
    "Edit the product meeting agenda two weeks from now to focus on user feedback.",
    "Update lunch plans with Rochit to 1.5 hrs.",
    "Extend project proposal review by 30mins.",
    "Update the design sync meeting two weeks from now. Asiya and Mihir will be presenting updates on UI.",
    "Move the eng roadmap meeting to next week.",
]

all_info_edit_test_answers = []

all_info_find_test_cases = [
    "Find some time to discuss Engg. roadmap next week. Invite Raci, Roh, Mihir to the meeting. Meeting should be 1 hr long",
    "Can you find 30 mins for a quick review of product plans for 2023. Invite Asiya, Paul, Mihir and Ravi.",
    "Setup some time with Patrick, Ramesh, Roh for engineering interview next week. Interview will last for 2 hrs",
    "Need to sync with Ramesh, Ravi, Patrick on some project updates for 30mins in two weeks. Can you find some time?",
    "Setup a meeting to discuss candidate feedback for 15 mins with Patrick, Ramesh and Roh this week",
    "Book a meeting with Sirish next week. Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long",
    "Need to give updates on product progress to Paul. I will need a few days to work on this, so find 1hr after two weeks",
    "Want to meet asiya to discuss eng roadmap. Can you schedule a 1hr meeting this week",
    "Schedule a 30min sprint review this week with Ravi, Sirish and Roh",
    "Grabbin lunch with Paul in two weeks. Find a time",
]

# follow up
follow_up_test_cases = [
    [
        "Book a meeting with Sirish.",
        "next tuesday at 3pm.",
        "Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long.",
    ],
    ["Schedule 30 minutes with ramesh tomorrow.", "4:30pm to chat about hiring plans."],
    [
        "Setup a follow-up with patrick.",
        "a week from today for 30mins at 2pm.",
        "Need to discuss project updates.",
    ],
    [
        "Want to meet asiya to discuss eng roadmap.",
        "Can you schedule a 1hr meeting thursday at 11am.",
    ],
    ["Reschedule tomorrow's sprint meeting.", "start at 11am."],
    ["Add Roh to the meeting.", "on eng roadmap."],
    [
        "Find some time to discuss Engg. roadmap next week.",
        "Invite Ravi, Roh, Mihir to the meeting. Meeting should be 1 hr long.",
    ],
    [
        "Can you find 30 mins for a quick review of product plans for 2023.",
        "Invite Asiya, Paul, Mihir and Ravi.",
    ],
    [
        "Setup some time with Patrick, Ramesh, Roh.",
        "For engineering interview next week.",
        "Interview will last for 2 hrs.",
    ],
    [
        "Need to sync with Ramesh, Ravi, Patrick.",
        "Project updates for 30mins in two weeks. Can you find some time?",
    ],
]
