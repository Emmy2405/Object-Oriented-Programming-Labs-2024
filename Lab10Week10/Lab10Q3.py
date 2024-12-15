class Meeting:
    total_meetings = 0  # Class variable to track total meetings created

    def __init__(self, attendees=0):
        """
        Initialize a new Meeting instance.
        :param attendees: Initial number of attendees in the meeting (default is 0).
        """
        self.attendees = attendees
        Meeting.total_meetings += 1
        print(f"Welcome to Meeting #{Meeting.total_meetings}!")
        print(f"Current number of attendees: {self.attendees}")

    def join_meeting(self, number=1):
        """
        Increase the number of attendees in the meeting.
        :param number: Number of people joining the meeting (default is 1).
        """
        self.attendees += number
        print(f"{number} attendee(s) joined. Current number of attendees: {self.attendees}")

    def leave_meeting(self, number=1):
        """
        Decrease the number of attendees in the meeting.
        :param number: Number of people leaving the meeting (default is 1).
        """
        if number > self.attendees:
            print("Cannot remove more attendees than currently in the meeting.")
        else:
            self.attendees -= number
            print(f"{number} attendee(s) left. Current number of attendees: {self.attendees}")


# Main Program
if __name__ == "__main__":
    # Create the first meeting
    meeting1 = Meeting(5)
    meeting1.join_meeting(3)
    meeting1.leave_meeting(2)

    # Create a second meeting
    meeting2 = Meeting()
    meeting2.join_meeting(10)
    meeting2.leave_meeting(5)
