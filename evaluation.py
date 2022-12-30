from datetime import datetime, timedelta

now = datetime.now()
current_date = datetime.now().date()
tomorrow = current_date + timedelta(days=1)
next_week = current_date + timedelta(weeks=1)
two_weeks = current_date + timedelta(weeks=2)
next_friday = now + timedelta( (4-now.weekday()) % 7 )
test_meet_link = "https://meet.google.com/abc-def-ghi"
test_meet_link2 = "https://meet.google.com/pqr-stu-vwx"

# need zero follow-up
# different ways of stating meeting details, including multiple people
all_info_create_test_cases = [
    "Book a meeting with alex next tuesday at 3pm. Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long",
    "Schedule 30 minutes with ramesh tomorrow at 4:30pm to chat about hiring plans",
    "Setup a follow-up with patrick a week from from today for 30mins at 2pm. Need to discuss project updates",
    "Want to meet asiya to discuss eng roadmap. Can you schedule a 1hr meeting thursday at 11am",
    "Need to give updates on product progress to Paul. I will need a few days to work on this, so schedule 1hr two weeks from today at 10am",
    "Setup a early dinner with Roh, Mihir and Alex tomorrow at 6pm",
    "Block deep work time 9am-12pm tomorrow to focus on coding for GPT-3 agent"
]

# rescheduling and editing
# rescheduling and editing means the model needs access to current meetings via an API
# the prompt will be need to be updated based on the information retrieved in order to complete the plan
# all_info_prior_meetings is the returned meeting information from the API
all_info_prior_meetings = [
    {
        "meeting_name": "Weekly design sync",
        "datetime": tomorrow + timedelta(days=3) + timedelta(hours=9),
        "duration": 60,
        "invitees": ["kaushik@gmail.com", "kabir@gmail.com", "ron@gmail.com", "patrick@gmail.com"],
        "location": ["Main Conference Room", test_meet_link],
    },
    {
        "meeting_name": "Weekly design sync",
        "datetime": next_week + timedelta(hours=9),
        "duration": 60,
        "invitees": ["kaushik@gmail.com", "kabir@gmail.com", "ron@gmail.com", "patrick@gmail.com"],
        "location": ["Main Conference Room", test_meet_link],
    },
    {
        "meeting_name": "Spring meeting",
        "datetime": tomorrow + timedelta(hours=9),
        "duration": 30,
        "invitees": ["kaushik@gmail.com", "asiya@gmail.com", "ram@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        "location": [test_meet_link],
    },
    {
        "meeting_name": "Discuss Eng roadmap",
        "datetime": current_date + timedelta(days=2) + timedelta(hours=10),
        "duration": 60,
        "invitees": ["kaushik@gmail.com", "asiya@gmail.com", "ram@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        "location": ["Secondary conference room", test_meet_link],
     },
     {
        "meeting_name": "Project proposal review",
        "datetime": next_friday + timedelta(hours=16),
        "duration": 30,
        "invitees": ["kaushik@gmail.com", "roh@gmail.com"],
        "location": ["Secondary conference room", test_meet_link],
     },
     {
        "meeting_name": "Product meeting",
        "datetime": two_weeks + timedelta(days=2),
        "duration": 30,
        "invitees": ["kaushik@gmail.com", "roh@gmail.com", "arvind@gmail.com", "alex@gmail.com"],
        "location": ["Secondary conference room", test_meet_link],
     },
     {
        "meeting_name": "Lunch with Rochit",
        "datetime": tomorrow + timedelta(hours=12),
        "duration": 60,
        "invitees": ["kaushik@gmail.com", "rochit@gmail.com"],
        "location": ["Zareen's Palo Alto"],
     },
]
all_info_edit_test_cases = [
    "Reschedule tomorrow's sprint meeting to start at 11am",
    "Cancel the design sync this week",
    "Add Roh to the meeting on eng roadmap",
    "I can't attend next week's design sync",
    "Need to pickup my parents this friday afternoon. respond as No to all meetings post 3pm",
    "Edit the product meeting agenda two weeks from now to focus on user feedback",
    "Update lunch plans with Rochit to 1.5 hrs",
    "Extend project proposal review by 30mins",
    "Add seconday conference room for the sprint meeting this week. Keep the meet link",
    "Update Eng roadmap link to https://meet.google.com/pqr-stu-vwx"
]

# need 1 follow up
one_info_test_cases = []

# need >1 follow up
multiple_info_test_cases = []

def get_op_exec_scores(result_dict):
    # For each parsed output run python exec and get scores
    exec_results = []
    for prompt, v in result_dict.items():
        for model_name, op in v.items():
            try:
                exec(op)
                exec_results.append([prompt, model_name, True])
            except:
                exec_results.append([prompt, model_name, False])
    return exec_results