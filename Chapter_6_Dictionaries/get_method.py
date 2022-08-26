alien = {'color': 'green', 'points': 5}

# Using get() to return a determined value if the key doesn't exist.
show = alien.get('colors', 'Invalid key')

# Return of get() in case that the passed key doesn't exist.
print(show)
