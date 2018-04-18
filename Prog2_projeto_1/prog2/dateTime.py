
import copy

class dateTime:

    def __init__(self, hour = 0, minutes = 0):
        self.hour = int(hour)
        self.minutes = minutes

    def get_hours(self):
        """Get the number of hours from a HH:MM time representation.

        Requires: hm str with a time represented as HH:MM.
        Ensures: int with the number of hours.
        """

        return self.hour

    def get_minutes(self):
        """Get the number of minutes from a HH:MM time representation.

        Requires: hm str with a time represented as HH:MM
        Ensures: int with the number of minutes.
        """
        return self.minutes

    def time_str(self, hour, minutes):
        """ This Function tells the hour and minutes with ":"
        Requires: h and m str and h and m > 0 and m < 24
        Ensures: Returns in int the hours plus ":" plus minutes
        """
        hours = str(hour)
        minute = str(minutes)

        if int(hour) < 10:
            hours = '0' + hours

        if minutes < 10:
            minute = "0" + minute

        return hours + ":" + minute

    def add_minutes(self,incr = 5):
        """Increment the given time by the given amount of minutes.

        Requires:
        - h_m str with a time represented as HH:MM;
        - incr int with the number of minutes.
        Ensures: str with a time represented as HH:MM, the result of incrementing hm by incr minutes.
        """
        
        h = self.get_hours()
        minute = self.minutes
        
        add = int(minute) + int(incr)

        if add >= 60:
            add -= 60
            hour = int(h) + 1

        return self.time_str(self.hour, add)
