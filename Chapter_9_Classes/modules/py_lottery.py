from random import choice

LUCKY_TICKET = [16, 24, 32, 46, 53, 36, 63,
                2, 7, 71, 'd', 'h', 'k', 'o',
                'y'
                ]


class Lottery:
    """A class to represent a lottery game."""

    def __init__(self, sequence_size=4):
        """Generates the default lucky ticket."""
        self.lucky_sequence = {}
        self.seq_size = sequence_size
        for seq in list(range(0, self.sequence_size)):
            self.lucky_sequence[seq] = choice(LUCKY_TICKET)

    def generate(self, sequence_size):
        """Generates the lucky ticket with given sequence amount."""
        self.seq_size = sequence_size
        for seq in list(range(0, self.seq_size)):
            self.lucky_sequence[seq] = choice(LUCKY_TICKET)

    def check(self, **ticket):
        """Returns the results of given ticket."""
        results = {}
        for seq, lucky_value in ticket.items():
            seq = int(seq)
            results[seq] = self.lucky_sequence.get(seq) == lucky_value

        return results

    def ticket(self, *ticket):
        if ticket:
            for seq in range(0, self.seq_size):
