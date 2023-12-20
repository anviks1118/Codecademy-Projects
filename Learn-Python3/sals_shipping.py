"""
Practice with conditional statements and variables
"""

# Ground Shipping
weight = 41.5

if weight <= 2:
  cost_ground = weight * 1.50 + 20
  print (cost_ground)
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
  print (cost_ground)
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
  print (cost_ground)
elif weight > 10:
  cost_ground = weight * 4.75 + 20
  print (cost_ground)

# Ground shipping premium
premiumGroundShipping = 125.00
print (premiumGroundShipping)

# Drone shipping
weight = 41.5

if weight <= 2:
  cost_drone = weight * 4.50
  print (cost_drone)
elif weight <= 6:
  cost_drone = weight * 9.00
  print (cost_drone)
elif weight <= 10:
  cost_drone = weight * 12.00
  print (cost_drone)
elif weight > 10:
  cost_drone = weight * 14.25
  print (cost_drone)
