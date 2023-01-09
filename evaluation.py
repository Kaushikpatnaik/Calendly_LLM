from datetime import datetime, timedelta

# need zero follow-up
# different ways of stating meeting details, including multiple people
all_info_create_test_cases = [
    "Book a meeting with Sirish next tuesday at 3pm. Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long",
    "Schedule 30 minutes with ramesh tomorrow at 4:30pm to chat about hiring plans",
    "Setup a follow-up with patrick a week from today for 30mins at 2pm. Need to discuss project updates",
    "Want to meet asiya to discuss eng roadmap. Can you schedule a 1hr meeting thursday at 11am",
    "Need to give updates on product progress to Paul. I will need a few days to work on this, so schedule 1hr two weeks from today at 10am",
    "Setup a early dinner with Roh, Mihir and Sirish tomorrow at 6pm",
    "Block deep work time 9am-12pm tomorrow to focus on coding for GPT-3 agent",
    "Create a meeting for phone interview with Ram, next Wednesday at 3pm",
    "Meeting to discuss Eng roadmap, with Ravi, Asiya, Paul and Roh this Friday at 11am",
    "Book some time with Roh and Mihir to discuss eng pipeline, next Monday at 3pm"
]

all_info_create_test_answers = []

# rescheduling and editing
all_info_edit_test_cases = [
    "Reschedule tomorrow's sprint meeting to start at 11am",
    "Cancel the design sync this week",
    "Add Roh to the meeting on eng roadmap",
    "I can't attend next week's design sync",
    "Need to pickup my parents this friday afternoon. Can't make meetings post 3pm",
    "Edit the product meeting agenda two weeks from now to focus on user feedback",
    "Update lunch plans with Rochit to 1.5 hrs",
    "Extend project proposal review by 30mins",
    "Update the design sync meeting two weeks from now. Asiya and Mihir will be presenting updates on UI",
    "Move the eng roadmap meeting to next week"
]

all_info_edit_test_answers = []

all_info_find_test_cases = [
    "Find some time to discuss Engg. roadmap next week. Invite Raci, Roh, Mihir to the meeting. Meeting should be 1 hr long",
    "Can you find 30 mins for a quick review of product plans for 2023. Invite Asiya, Paul, Mihir and Ravi.",
    "Setup some time with Patrick, Ramesh, Roh for engineering interview next week. Interview will last for 2 hrs",
    "Need to sync with Ramesh, Ravi, Patrick on some project updates for 30mins in two weeks. Can you find some time?",
    "Setup a meeting to discuss candidate feedback for 15 mins with Patrick, Ramesh and Roh this week",
    "Book a meeting with Sirish next week. Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long",
    "Need to give updates on product progress to Paul. I will need a few days to work on this, so schedule 1hr two weeks from today",
    "Want to meet asiya to discuss eng roadmap. Can you schedule a 1hr meeting this week",
    "Schedule a 30min sprint review this week with Ravi, Sirish and Roh",
    "Grabbin lunch with Paul in two weeks. Find a time"
]

# follow up
follow_up_test_cases = [
    ["Book a meeting with Sirish.", "next tuesday at 3pm.", "Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long"],
    ["Schedule 30 minutes with ramesh tomorrow.", "4:30pm to chat about hiring plans"],
    ["Setup a follow-up with patrick.", "a week from today for 30mins at 2pm.", "Need to discuss project updates"],
    ["Want to meet asiya to discuss eng roadmap.", "Can you schedule a 1hr meeting thursday at 11am"],
    ["Reschedule tomorrow's sprint meeting.", "start at 11am"],
    ["Add Roh to the meeting.", "on eng roadmap"],
    ["Find some time to discuss Engg. roadmap next week.", "Invite Ravi, Roh, Mihir to the meeting. Meeting should be 1 hr long"],
    ["Can you find 30 mins for a quick review of product plans for 2023.", "Invite Asiya, Paul, Mihir and Ravi."],
    ["Setup some time with Patrick, Ramesh, Roh.", "For engineering interview next week.", "Interview will last for 2 hrs"],
    ["Need to sync with Ramesh, Ravi, Patrick.", "Project updates for 30mins in two weeks. Can you find some time?"],
]
