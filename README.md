# Mini Interconnection Study
A Python/pandapower study of how a new generator affects a transmission grid.

> **Status:** Phase 1 of 5 (Power Flow Basics), in progress

## Key Results (so far)
- IEEE 14-bus base case converges with Newton-Raphson power flow
- Total system losses: 13.39 MW (272.39 MW generated, 259.0 MW load)
- Bus voltages range from 1.010 to 1.090 pu; 7 buses sit above 1.05 pu

## Roadmap
- [ ] **Phase 1: Power flow basics** (IEEE 14- and 118-bus)
- [ ] **Phase 2: N-1 contingency scan** (line/transformer outages, voltage and loading limits)
- [ ] **Phase 3: Solar plant injection capability**
- [ ] **Phase 4: Short-circuit study** (fault current before/after the plant)
- [ ] **Phase 5: Texas A&M synthetic grid + polish**

---

## Learning Log

### Phase 1: Power Flow Basics
**Goal:** Run a power flow on a standard test case and understand every column of the results.

**What I did**
- Loaded IEEE 14-bus in pandapower and ran `pp.runpp(net)`
- Classified buses: PQ by default, PV where an in-service generator sits, Slack at the external grid

**Results: IEEE 14-bus**

|   Bus | type   |   vm_pu |   va_degree |     p_mw |   q_mvar |
|------:|:-------|--------:|------------:|---------:|---------:|
|     0 | Slack  |   1.06  |       0     | -232.393 |   16.549 |
|     1 | PV     |   1.045 |      -4.983 |  -18.3   |  -30.857 |
|     2 | PV     |   1.01  |     -12.725 |   94.2   |   -6.075 |
|     3 | PQ     |   1.018 |     -10.313 |   47.8   |   -3.9   |
|     4 | PQ     |   1.02  |      -8.774 |    7.6   |    1.6   |
|     5 | PV     |   1.07  |     -14.221 |   11.2   |   -5.231 |
|     6 | PQ     |   1.062 |     -13.36  |    0     |    0     |
|     7 | PV     |   1.09  |     -13.36  |    0     |  -17.623 |
|     8 | PQ     |   1.056 |     -14.939 |   29.5   |   -4.585 |
|     9 | PQ     |   1.051 |     -15.097 |    9     |    5.8   |
|    10 | PQ     |   1.057 |     -14.791 |    3.5   |    1.8   |
|    11 | PQ     |   1.055 |     -15.076 |    6.1   |    1.6   |
|    12 | PQ     |   1.05  |     -15.156 |   13.5   |    5.8   |
|    13 | PQ     |   1.036 |     -16.034 |   14.9   |    5     |

Line loading peaked at 1.5%. That's not realistic: case14's lines likely have placeholder
thermal ratings (check `net.line.max_i_ka`), so I'll use case118 for loading checks.

**What I learned**
| Bus type | Specified | Solved for | Role |
|---|---|---|---|
| Slack | \|V\|, angle | P, Q | Balances the system and covers losses; angle reference |
| PV | P, \|V\| | Q, angle | Generator holding its voltage setpoint |
| PQ | P, Q | \|V\|, angle | Load bus |

- **Sign convention:** pandapower reports bus power from the load's point of view, so negative `p_mw` means the bus is generating (e.g. the slack bus at -232 MW).
- **Loading percent:** line current as a percentage of its thermal current rating.
- **Newton-Raphson:** _(in progress, by 11/19)_

**Open questions**
- Why are several case14 voltages above 1.05 pu, and would a real utility accept that?

### Phase 2: N-1 Contingency Scan
_Planned: starts 11/30_

---

## How to Run
_(coming in Phase 5)_

## Repo Layout
_(coming in Phase 5)_