import nltk

def evaluate(query):
    tokens = nltk.word_tokenize(query)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    print(entities)
    if 'add' in query:
        action = 'add'
    elif 'edit' in query:
        action = 'edit'
    elif 'exit' in query:
        action = 'exit'

    event = {
              'summary': 'Google I/O 2015',
              'location': '800 Howard St., San Francisco, CA 94103',
              'description': 'A chance to hear more about Google\'s developer products.',
              'start': {
                'dateTime': '2015-05-28T09:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
              },
              'end': {
                'dateTime': '2015-05-28T17:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
              },
              'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
              ],
              'attendees': [
                {'email': 'lpage@example.com'},
                {'email': 'sbrin@example.com'},
              ],
              'reminders': {
                'useDefault': False,
                'overrides': [
                  {'method': 'email', 'minutes': 24 * 60},
                  {'method': 'popup', 'minutes': 10},
                ],
              },
            }
    return(action, event, "7pm")
