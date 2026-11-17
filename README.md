# Mini Interconnection Study
A Python/pandapower study of how a new generator affects a transmission grid.

> Work in progress. In Phase 1 (Learn Power Flow Basics)

## Key Results
- IEEE 14-bus base case converges
- Total system losses: 13.39 MW (272.39 MW generated, 259.0 MW load)

## Phase 1: Learn Power Flow Basics

I classified every bus as PQ by default, then set buses with in-service generators to PV and the external grid bus to Slack.

### IEEE 14-bus results
#### Buses
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

#### Lines
|    |   loading_percent |
|---:|------------------:|
|  0 |             1.508 |
|  1 |             0.721 |
|  2 |             0.709 |
|  3 |             0.543 |
|  4 |             0.403 |
|  5 |             0.24  |
|  6 |             0.627 |
|  7 |             0.077 |
|  8 |             0.077 |
|  9 |             0.181 |
| 10 |             0.064 |
| 11 |             0.097 |
| 12 |             0.04  |
| 13 |             0.017 |
| 14 |             0.057 |

## What I Learned

###### Slack Buses
A slack bus is a bus used to balance the active power and reactive power in a system. 

###### PV Buses
A PV bus is a bus where the real power and the voltage magnitude are specified.

###### PQ Bus
A PQ bus is a bus where the real power and reactive power are specified. 

###### Loading Percent
Measures how close a line is to its maximum load