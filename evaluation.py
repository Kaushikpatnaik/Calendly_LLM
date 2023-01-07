from datetime import datetime, timedelta

# need zero follow-up
# different ways of stating meeting details, including multiple people
all_info_create_test_cases = [
    "Book a meeting with alex next tuesday at 3pm. Agenda for the meeting is to discuss 2023 plans. Meeting should be 1hr long",
    "Schedule 30 minutes with ramesh tomorrow at 4:30pm to chat about hiring plans",
    "Setup a follow-up with patrick a week from today for 30mins at 2pm. Need to discuss project updates",
    "Want to meet asiya to discuss eng roadmap. Can you schedule a 1hr meeting thursday at 11am",
    "Need to give updates on product progress to Paul. I will need a few days to work on this, so schedule 1hr two weeks from today at 10am",
    "Setup a early dinner with Roh, Mihir and Alex tomorrow at 6pm",
    "Block deep work time 9am-12pm tomorrow to focus on coding for GPT-3 agent",
]

all_info_create_test_answers = []

# rescheduling and editing
all_info_edit_test_cases = [
    "Reschedule tomorrow's sprint meeting to start at 11am",
    "Cancel the design sync this week",
    "Add Roh to the meeting on eng roadmap",
    "I can't attend next week's design sync",
    "Need to pickup my parents this friday afternoon. respond as No to all meetings post 3pm",
    "Edit the product meeting agenda two weeks from now to focus on user feedback",
    "Update lunch plans with Rochit to 1.5 hrs",
    "Extend project proposal review by 30mins",
]

all_info_edit_test_answers = []

# follow up
follow_up_test_cases = []
