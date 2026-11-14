# Mini Interconnection Study


### Bus Types of the IEEE 14 Bus Case
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

###### Slack Buses
A slack bus is a bus used to balance the active power and reactive power in a system. I determined it in this case by checking if it has an external grid collection. This is because pandapower uses this as the default way to identify a slack bus.

###### PV Buses
A PV bus is a bus where the real power and the voltage magnitude are specified. Real power and voltage are specified for buses that are generators, which is how I indentified them in this case.

###### PQ Bus
A PQ bus is a bus where the real power and reactive power are specified. This is the default bus type, and those buses that were not PV or slack were idenitified as PQ in this case.