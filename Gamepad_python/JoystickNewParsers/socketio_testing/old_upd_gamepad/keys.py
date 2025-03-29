from inputs import get_key

def idk():
    while True:
        events = get_key()
        for event in events:
            print(event.ev_type, event.code, event.state)
            
idk()

