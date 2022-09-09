from modules import py_lottery as lottery

lottery = lottery.Lottery()

entries = [24, 14, 63, 'b']

my_ticket = lottery.ticket(entries)
results = lottery.check(my_ticket)


print(f"Your ticket:\n {my_ticket}\n"
      f"Lucky sequence:\n - {lottery.lucky_entry}\n"
      f"Result:\n - {results}")
