# Is the claw machine due a win?

The code behind episode 02 of **The Maths Of It** on YouTube.

Everyone knows the gambler's fallacy: a coin has no memory, so a losing streak doesn't make a win "due". That's true for a machine with fixed odds. But many claw machines can be set to pay out a target number of prizes, and a machine like that *does* have a memory.

## The two machines

- **Fixed odds:** every go has the same chance, here 1 in 10. Past goes change nothing.
- **Payout regulator** (the "compensator" in the operator manuals): every 10 plays the machine adds 1 to a counter. While the counter is above 0 the claw grips strongly. Every win takes 1 off. On average it still pays 1 prize per 10 plays, but *when* it pays depends on what happened before.

The grip chances are assumptions for illustration, not measured from a real machine: a player wins **50%** of goes on a strong grip and **2%** on a weak one. Change them with `--strong` and `--weak`.

## Results (2 million simulated goes each)

Chance that the **next** go wins, after a run of losses:

| Losses in a row | Payout regulator | Fixed odds |
|---:|---:|---:|
| 0 (just after a win) | 2.1% | 10.0% |
| 3 | 2.4% | 9.9% |
| 6 | 5.4% | 10.2% |
| 8 | 17.6% | 10.1% |
| 9 | **39.0%** | 9.9% |
| 12 | 25.4% | 10.1% |

Average goes until you win on the regulator machine, if you walk up after:

| Losses in a row | Goes to a win |
|---:|---:|
| 0 | 10.00 |
| 5 | 5.86 |
| 9 | 3.18 |

With fixed odds of 1 in 10, the chance of at least one win within k goes is 1 − 0.9^k, so you need **7** goes for an even chance, **22** for 90% and **29** for 95%.

## Run it

```
pip install -r requirements.txt
python is_the_claw_due.py                          # the tables above
python is_the_claw_due.py --strong 0.3 --every 15  # try your own settings
```

Each run is a random simulation, so the last decimal can move slightly with a different `--seed`.

## UK rules (as of November 2026)

- A crane grab is a Category D gaming machine: £1 maximum stake, £50 maximum prize, non-money prizes only.
- Most Category D machines must display their return to player, but crane grabs and penny falls are exempt.
- A crane that uses a compensator to set its payout must be marked as a gaming machine of "skill and chance combined".
- A government consultation from 15 October 2025 proposed raising the crane prize limit to £75. The responses are still being analysed.

## Sources

- ICE Grab n Win 60 service manual (Betson): https://www.betson.com/wp-content/uploads/wpallimport/files/service-manuals/grab-n-win-60-merchandiser-crane-ice-service-manual.pdf
- MetaFilter, quoting LAI, ICE and Coastal operator manuals: https://metafilter.com/152746/Claw-machines-are-often-less-games-of-skill-as-chance
- Gambling Commission, Category D gaming machines: https://www.gamblingcommission.gov.uk/licensees-and-businesses/guide/page/d-gaming-machines
- Gambling Commission, non-complex Category D crane grabs: https://www.gamblingcommission.gov.uk/licensees-and-businesses/guide/non-complex-cat-d-gaming-machines-crane-grabs
- GOV.UK, consultation on Category D gaming machines (October 2025): https://www.gov.uk/government/consultations/consultation-on-category-d-gaming-machines-and-licensing-for-bingo-premises/category-d-gaming-machines

## Limits

The 50% and 2% grip chances are made up to show the shape of the effect. No public source gives the settings UK arcades actually use, and real machines vary. The point is the shape: on a regulator machine, a run of losses makes the next win more likely.

This is about how the machines work, not a way to make money: on average every machine still takes more than it pays out.

MIT licence.
