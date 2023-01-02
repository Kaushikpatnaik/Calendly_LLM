api_list_option = """
    Assume access to datetime, typing python libraries.
    Use one or more of provided functions below:
    1.name_to_emails(list_of_names: Sequence[str])
    2.create_event(meeting_agenda: str, date: datetime.date, time: datetime.timedelta, duration: datetime.timedelta, invitees: Sequence[str])
    3.get_events()
    4.edit_event(event_id: str, meeting_agenda: str, date: datetime.date, time: datetime.timedelta, duration: datetime.timedelta, invitees: Sequence[str])
    
    import the functions from provided_api.py file.
    """

api_list_none = """"""

prompt_w_api = f"""You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. {api_list_option}
Write code for completing the following request. Let's think step by step.""" + "{query}"

prompt_wo_api = """You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. Write code for completing the following request. Let's think step by step.{query}"""