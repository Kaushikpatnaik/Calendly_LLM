api_list_option = """
    Assume access to datetime, google calendar and google meet python libraries. Import other libraries as needed.
    Use one or more of provided functions below:
    1.name_to_emails(list_of_names)
    2.create_event(meeting_agenda, date, time, invitees)
    3.get_events()
    4.edit_event(event_id, meeting_agenda, date, time, duration, invitees)
    """

api_list_none = """"""

prompt_w_api = f"""You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. {api_list_option}
Write code for completing the following request. Let's think step by step.""" + "{query}"

prompt_wo_api = """You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. Write code for completing the following request. Let's think step by step.{query}"""