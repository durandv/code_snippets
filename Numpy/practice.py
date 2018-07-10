import numpy as np
store = np.array(["Z", "Z", "Y", "Y", "X"])
cost  = np.array([8, 0, 5, 0, 3])
select_cost = cost[store == "Y"]
print(select_cost)