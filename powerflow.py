import pandapower as pp
import pandas as pd
from pandapower.networks.power_system_test_cases import case14


net = case14() # Load the IEEE 14-bus test case
pp.runpp(net)  # Run power flow analysis

# label buses with slack bus, PV bus, and PQ buses
bus_types = pd.Series("PQ", index=net.bus.index, name="type") # makes one label per bus, all set to PQ
generators = net.gen[net.gen.in_service] # list of generators that are in service
bus_types.loc[generators.bus] = "PV" # set the bus type to PV for buses with generators

external_grid_buses = net.ext_grid[net.ext_grid.in_service].bus # list of buses with external grid connections
bus_types.loc[external_grid_buses] = "Slack" # set the bus type to Slack for buses with external grid connections

table = pd.concat([bus_types, net.res_bus], axis=1) # combine bus types and power flow results into a single table
table.index.name = "Bus" # set the index name to "Bus"
print(table) # print the table to the console
print(bus_types.value_counts()) # print the count of each bus type

print(table.round(3).to_markdown()) # print the table in markdown format, rounded to 3 decimal places