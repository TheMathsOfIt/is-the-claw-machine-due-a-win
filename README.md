# Is the claw machine due a win?

Code for episode 2 of [The Maths Of It](https://www.youtube.com/@TheMathsOfIt).

**Try it in your browser:** https://themathsofit.github.io/is-the-claw-machine-due-a-win/

A fixed-odds claw has no memory. A claw with a payout counter does: it owes a prize every few plays and grips hard until it pays.

| Losses in a row | Payout counter | Fixed odds |
|---:|---:|---:|
| 0 | 2.1% | 10% |
| 5 | 3.7% | 10% |
| 9 | **39%** | 10% |

Chance the next go wins, from 2 million simulated goes. The grip chances (50% strong, 2% weak) are assumptions.

## Run it

```
pip install -r requirements.txt
python is_the_claw_due.py
python is_the_claw_due.py --every 15 --strong 0.3
```

## Sources

- [ICE Grab n Win 60 service manual](https://www.betson.com/wp-content/uploads/wpallimport/files/service-manuals/grab-n-win-60-merchandiser-crane-ice-service-manual.pdf)
- [Operator manual settings (LAI, ICE, Coastal), via MetaFilter](https://metafilter.com/152746/Claw-machines-are-often-less-games-of-skill-as-chance)
- [Gambling Commission: Category D machines](https://www.gamblingcommission.gov.uk/licensees-and-businesses/guide/page/d-gaming-machines)
- [Gambling Commission: crane grabs](https://www.gamblingcommission.gov.uk/licensees-and-businesses/guide/non-complex-cat-d-gaming-machines-crane-grabs)
- [GOV.UK: Category D consultation, October 2025](https://www.gov.uk/government/consultations/consultation-on-category-d-gaming-machines-and-licensing-for-bingo-premises/category-d-gaming-machines)

MIT licence.
