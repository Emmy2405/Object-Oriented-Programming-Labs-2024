class Attendee:
    attendees_count = 0

    def __init__(self):
        Attendee.attendees_count += 1
        print(f"Welcome to the meeting! Current attendees: {Attendee.attendees_count}")

    @staticmethod
    def leave_meeting():
        if Attendee.attendees_count > 0:
            Attendee.attendees_count -= 1
        print(f"Someone left. Current attendees: {Attendee.attendees_count}")


attendee1 = Attendee()
attendee2 = Attendee()
Attendee.leave_meeting()
