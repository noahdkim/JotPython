import httplib2

from apiclient import discovery
import validate
import datetime
import interpret
import jot_calendar

CALENDAR_ID = 'u8jj8hlk075sv057h3uuda1hg0@group.calendar.google.com'
def add_to_calendar(event):
    print(event)

def main():
    ## Begin setup ##
    credentials = validate.get_credentials()
    http = credentials.authorize(httplib2.Http())

    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    ## Setup complete ##
    while True:
        ## Take in Request ##
        query = input("Jot> ")
        action, event, time = interpret.evaluate(query)
        if action=="add":
            jot_calendar.add(event, service, CALENDAR_ID)
        elif action=="edit":
            jot_calendar.edit(event)
        else:
            break



    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId=CALENDAR_ID, timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()
