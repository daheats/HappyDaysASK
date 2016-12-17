from __future__ import print_function
import random

quotes = [
    "You have brains in your head you have feet in your shoes you can steer yourself in any direction you choose... Doctor Seuss", 
    "Doing what you like is freedom. Liking what you do is happiness... Frank Tyger", 
    "Be happy with what you have. Be excited about what you want... Alan Cohen", 
    "Don't worry about a thing, 'cause every little thing gonna be alright... Bob Marley",
    "Life is a journey, and if you fall in love with the journey, you will be in love forever... Peter Hagerty", 
    "You're off to great places! Today is your day! Your mountain is waiting so get on your way... Doctor Seuss", 
    "If you can dream it. You can do it... Walt Disney",
    "Once you choose hope, anything's possible... Christopher Reeve",
    "Do one thing every day that scares you... Eleanor Roosevelt",
    "Failure is another stepping stone to greatness...Oprah Winfrey",
    "You miss 100 percent of the shots you don't take... Wayne Gretzky",
    "The way I see it, if you want the rainbow, you gotta put up with the rain...Dolly Parton",
    "Everything you can imagine is real...Pablo Picasso",
    "Be yourself. Everyone else is already taken...Oscar Wilde",
    "The mind is everything. What you think you become...Buddha",
    "Believe you can and you're halfway there...Theodore Roosevelt",
    "Tension is who you think you should be, relaxation is who you are",
    "Be the reason someone smiles today",
    "Just keep swimming... Dory Finding Nemo",
    "All our dreams can come true if we have the courage to pursue them... Walt Disney",
    "Be the change you wish to see",
    "Today you are you that is truer than true there is no one alive who is youer than you... Doctor Seuss",
    "Inhale confidence, exhale doubt",
    "Love the life you live, live the life you love... Bob Marley",
    "Nothing is impossible, the word itself says I'm possible... Audrey Hepburn",
    "The most beautiful thing you can wear is confidence... Blake Lively",
    "It's always seems impossible, until it's done... Nelson Mandela",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment... Buddha",
    "Every moment is a fresh beginnning... TS Eliot",
    "Don't count the days, make the days count... Muhammad Ali",
    "Light tomorrow with today... Elizabeth Barrett Browning",
    "Believe you can and you're halfway there... Theodore Roosevelt",
    "The purpose of our lives is to be happy... Dalai Lama",
    "Life isn't about finding yourself, life is about creating yourself... George Bernard Shaw",
    "Don't worry be happy... Bobby McFerrin",
    "Happiness is a choice, choose happy.",
    "If you want to be happy, be... Leo Tolstoy",
    "Happiness is when what you think, what you say, and what you are are in haromny... Mahatma Gandhi",
    "Be happy for this moment, this moment if your life...Omr Khayyam",
    "Happiness depends upon ourselves... Aristotle",
    "Happiness can exist only in acceptance... George Orwell",
    "Most folks are as happy as they make up their minds to be... Abraham Lincoln",
    "The Constitution only gives people the right to pursue happiness. You have to catch it yourself... Benjamin Franklin",
    "That should be the measure of success for everyone. It's not money, it's not fame, it's not celebrity; my index of success is happiness... Lupe Fiasco"
    "Happinness is good health and a bad memory... Ingrid Bergman",
    "Happiness makes up in height for what it lacks in length...Robert Frost",
    "You are braver than you believe, stronger than you seem, and smarter than you think... Christopher Robin...Winnie the Pooh",
    "Hakuna Matata...Timon and Pumba...The Lion King",
    "Always let your conscience be your guide... Jiminy Cricket... Pinnochio",
    "To infinity and beyond... Buzz Lightyear...Toy Story",
    "Try not. Do. Or Do not. There is no try... Yoda",
    "Let it go... Elsa...Frozen",
    "You control your destiny, you don't need magic to do it...Merida...Brave",
    "To laugh at yourself is to love yourself...Mickey Mouse",
    "Venture outside your comfort zone. The rewards are worth it...Rapunzel...Tangled",
    "Don't just fly, soar...Dumbo",
    "Everyone you meet is fighting a battle you know nothing about. Be kind always...Ian Maclaren",
    "If you don't like where you are, then change it. You're not a tree...Jim Rohn",
    "A good day is a good day. A bad day is a good story. At the end of the day, it's all good... Glennon Melton",
    "If things start happening, don't worry, don't steew, just go right along and you'll start happening too... Dr. Seuss",
    "And will you succeed? Yes indeed, yes indeed! Ninety-eight and three-quarters percent guranteed...Dr. Seuss",
    "Just tell yourself duckie, you're really quite lucky... Dr. Seuss",
    "Keep your eyes on the stars, and your feet on the ground... Theodore Roosevelt",
    "Never give up, for that is just the place and time that the tide will turn...Harriet Beecher Stowe",
    "There's a way to do it better. Find it... Thomas Edison",
    "When something is important enough, you do it even if the odds are not in your favor...Elon Musk",
    "Well done is better than well said... Benjamin Franklin",
    "The most effective way to do it, is to do it ...Amelia Earhart",
    "",
    "",
    "",
    ]

def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    print("on_session_started requestId=" +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])

def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()

def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "HappyDaysIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.NoIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return handle_anotherq_request(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_help_request(intent, session)
    elif intent_name == "AnotherQuoteIntent":
        return handle_anotherq_request(intent, session)
    elif intent_name == "AMAZON.CancelIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return handle_finish_session_request(intent, session)
    else:
        return handle_finish_session_request(intent, session)
        
def get_welcome_response():
    session_attributes = {}
    random_number = random.randint(0, len(quotes))
    speech_output = "Here's a dose of happiness..." + quotes[random_number] + "... Would you like to hear another quote?"
    reprompt_text = "Would you like to hear another quote?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def handle_anotherq_request(intent, session):
        attributes = {}
        random_number = random.randint(0, len(quotes))
        speech_output = "Here's another quote!" + quotes[random_number] + "... Would you like to hear another quote?"
        reprompt_text = "Would you like to hear another quote?"
        should_end_session = False
        return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def handle_help_request(intent, session):
    attributes = {}
    speech_output = "(You can ask me for a positive quote by saying give me a quote, or, you can say exit... What can I help you with?)"
    reprompt_text = "So, how can I help you?"
    should_end_session = False
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def handle_finish_session_request(intent, session):
    attributes = {}
    reprompt_text = None
    speech_output = "Ok! Have a happy day!"
    should_end_session = True
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speechlet_response
    }