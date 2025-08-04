import random

SYMBOLS = ['🍒', '🍋', '🔔', '💎']

def spin_reels():
    """Return a list of three random symbols."""
    return [random.choice(SYMBOLS) for _ in range(3)]

def calculate_payout(result):
    """Return payout based on matching symbols."""
    if len(set(result)) == 1:
        return 100  # three of a kind
    elif len(set(result)) == 2:
        return 20   # two of a kind
    return 0        # no match