signup_schema = {
    "type": "object",
    "properties": {
        "firstname": {type: "string"},
        "lastname": {type: "string"},
        "email": {type: "string"},
        "password": {type: "string"},
        "username": {type: "string"},
        "phoneNumber": {type: "string"},
        "registered": {type: "string"}
    },
    "required": ["firstname", "lastname", "email", "password", "username", "phoneNumber"]
}

login_schema = {
    "type": "object",
    "properties": {
            "email": {type: "string"},
        "password": {type: "string"}
    },
    "required": ["email", "password"]
}
meetup_schema = {
    "type": "object",
    "properties": {
        "location": {type: "string"},
        "topic": {type: "string"},
        "happeningOn": {type: "string"},
        "tags": {type: "string"},
    },
    "required": ["location", "topic", "happeningOn"]
}

question_schema = {
    "type": "object",
    "properties": {
        "title": {type: "string"},
        "body": {type: "string"},
        "upvotes": {type: "string"},
        "downvotes": {type: "string"},
    },
    "required": ["title", "body", "upvotes", "downvotes"]
}
rsvp_schema = {
    "type": "object",
    "properties": {
        "meetup": {type: "integer"},
        "response": {type: "string"},
    },
    "required": ["response"]
}
