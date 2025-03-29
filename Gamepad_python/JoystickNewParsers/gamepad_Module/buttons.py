from inputs import get_gamepad

def idk():
    while True:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            
idk()

