import pandapower as pp
from pandapower.networks.power_system_test_cases import case14


net = case14() # Load the IEEE 14-bus test case
pp.runpp(net)  # Run power flow analysis

print(net.res_bus)  # Print bus results
print(net.res_line)  # Print line results
print(net.res_load)  # Print load results
print(net.res_gen)  # Print generator results
print(net.res_ext_grid)  # Print external grid results