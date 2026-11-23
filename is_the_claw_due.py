"""
Is the claw machine due a win?
The code behind episode 02 of The Maths Of It.

Two ways a claw machine can decide when you win:

  1. Fixed odds: every go has the same chance (here 1 in 10). The machine
     has no memory, so a losing streak tells you nothing.
  2. A payout regulator (the "compensator" many real cranes use): the
     machine counts plays. Every 10 plays it adds 1 to a counter P. While
     P is above 0 the claw grips strongly; every win takes 1 off P.
     So the machine pays out about 1 prize per 10 plays on average,
     and how long since the last win DOES change your chances.

The grip chances (50% on a strong grip, 2% on a weak one) are assumptions
for illustration, not figures from a real machine. Change them with
--strong and --weak, or change the payout rate with --every.

Run:  python is_the_claw_due.py
      python is_the_claw_due.py --strong 0.3 --every 15
"""
import argparse
import math
import numpy as np


def regulator(n_plays, every=10, strong=0.5, weak=0.02, rng=None):
    """Simulate a payout regulator. Returns a True/False array: did each play win?"""
    rng = rng or np.random.default_rng()
    P, count = 0, every
    wins = np.zeros(n_plays, bool)
    r = rng.random(n_plays)
    for i in range(n_plays):
        count -= 1
        if count == 0:                 # every `every` plays, one more prize is owed
            P += 1
            count = every
        if r[i] < (strong if P > 0 else weak):
            wins[i] = True
            P -= 1                     # paying out a prize takes one off the counter
    return wins


def fixed_odds(n_plays, p=0.1, rng=None):
    """Every play has the same chance p, no memory."""
    rng = rng or np.random.default_rng()
    return rng.random(n_plays) < p


def losses_before(wins):
    """For each play: how many losses in a row came just before it."""
    out = np.empty(len(wins), int)
    k = 0
    for i, w in enumerate(wins):
        out[i] = k
        k = 0 if w else k + 1
    return out


def chance_next_go(wins, max_streak=15):
    """Chance the next play wins, after k losses in a row (k = 0 means right after a win)."""
    since = losses_before(wins)
    return [wins[since == k].mean() for k in range(max_streak + 1)]


def goes_to_a_win(wins, start_after):
    """Average number of plays, including the winning one, for someone who walks up
    when the machine has just had `start_after` losses in a row."""
    since = losses_before(wins)
    starts = np.where(since == start_after)[0]
    win_at = np.where(wins)[0]
    nxt = np.searchsorted(win_at, starts)
    ok = nxt < len(win_at)
    return float((win_at[nxt[ok]] - starts[ok] + 1).mean())


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--plays', type=int, default=2_000_000, help='number of plays to simulate')
    ap.add_argument('--every', type=int, default=10, help='regulator: one prize owed per this many plays')
    ap.add_argument('--strong', type=float, default=0.5, help='chance of a win on a strong grip')
    ap.add_argument('--weak', type=float, default=0.02, help='chance of a win on a weak grip')
    ap.add_argument('--seed', type=int, default=7)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    p = 1 / a.every

    reg = regulator(a.plays, a.every, a.strong, a.weak, rng)
    fix = fixed_odds(a.plays, p, rng)
    print(f'{a.plays:,} plays simulated each way')
    print(f'Plays per win:  regulator {a.plays / reg.sum():.2f}   fixed odds {a.plays / fix.sum():.2f}\n')

    print('Chance the NEXT go wins, after k losses in a row')
    print(f"{'k':>3}  {'regulator':>9}  {'fixed':>6}")
    for k, (r_, f_) in enumerate(zip(chance_next_go(reg), chance_next_go(fix))):
        print(f'{k:>3}  {r_ * 100:>8.1f}%  {f_ * 100:>5.1f}%')

    print('\nAverage goes until you win, if you walk up after k losses in a row (regulator)')
    for k in (0, 5, 9):
        print(f'  after {k:>2} losses: {goes_to_a_win(reg, k):.2f} goes')

    print(f'\nFixed odds of 1 in {a.every}: goes needed to have a decent chance of winning')
    for q in (0.5, 0.9, 0.95):
        n = math.ceil(math.log(1 - q) / math.log(1 - p))
        print(f'  {q:.0%} chance of at least one win: {n} goes (so £{n} at £1 a go)')
