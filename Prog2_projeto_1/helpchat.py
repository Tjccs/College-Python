import sys
import filesReading

class Operators:

    def __init__(self, name, language, field, end_time, minutes_done):
        self.name = name
        self.language = language
        self.field = field
        self.end_time = end_time
        self.minutes_done = minutes_done


class Help_Requests:

    def __init__(self, user, language, domain, subscrition, time):
        self.user = user
        self.language = language
        self.domain = domain
        self.subscrition = subscrition
        self.time = time


def update():
    filesReading.FileReader(sys.argv[1])
    filesReading.FileReader(sys.argv[2])


if __name__ == "__main__":

    update()