def detect_agent(user_request: str):

    request = user_request.lower()

    if any(word in request for word in [
        "quiz",
        "mcq",
        "question",
        "true false",
    ]):
        return "quiz"

    elif any(word in request for word in [
        "flashcard",
        "flash card",
    ]):
        return "flashcard"

    elif any(word in request for word in [
        "plan",
        "schedule",
        "timetable",
    ]):
        return "planner"

    elif any(word in request for word in [
        "pdf",
        "document",
        "notes",
    ]):
        return "resource"

    return "study"