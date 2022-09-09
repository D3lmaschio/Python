from random import choice

LUCKY_TICKET = [16, 24, 32, 46, 53, 36, 63,
                2, 7, 71, 'd', 'h', 'k', 'o',
                'y'
                ]


class Lottery:
    """A class to represent a lottery game."""

    def __init__(self, entry_len=4):
        """Generates the default lucky ticket."""
        self.lucky_entry = {}
        self.entry_len = entry_len
        for entry in list(range(0, self.entry_len)):
            self.lucky_entry[entry] = choice(LUCKY_TICKET)

    def generate(self, entry_len=4):
        """Generates the lucky ticket with given length."""
        self.entry_len = entry_len
        for entry in list(range(0, self.entry_len)):
            self.lucky_entry[entry] = choice(LUCKY_TICKET)

    def check(self, ticket={}):
        """
        Returns the results of given ticket.
        - Will return None if no entries are passed.
        """
        results = {}
        if ticket:
            for entry, value in ticket.items():
                entry = int(entry)
                results[entry] = self.lucky_entry.get(entry) == value

            return results
        else:
            return False

    def ticket(self, entries=[]):
        """
        Returns a ticket with given entries.
        - If entry len doesn't match with instance len will return None.
        """
        ticket = {}
        if len(entries) == self.entry_len:
            for entry in range(0, self.entry_len):
                value = entries[entry]
                ticket[entry] = value

            return ticket
        else:
            return None
