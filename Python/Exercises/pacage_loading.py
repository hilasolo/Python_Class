max_items = int(input("Enter the maximum number of items to be shipped: ")) 
packages_sent = 0
total_weight_sent = 0
unused_capacity = 0
max_unused_capacity = 0
max_unused_capacity_package = 0

for package_number in range(1, max_items + 1):
  item_weight = int(input(f"Enter the weight of item {package_number}: "))
        
  if item_weight == 0:
            break
        
  if item_weight < 1 or item_weight > 10:
      print("Invalid weight entered. Weight should be between 1 and 10.")
      continue
        
  if total_weight_sent + item_weight > 20:
            packages_sent += 1
            unused_capacity += 20 - total_weight_sent
            
            if 20 - total_weight_sent > max_unused_capacity:
                max_unused_capacity = 20 - total_weight_sent
                max_unused_capacity_package = packages_sent
            
            total_weight_sent = item_weight
  else:
            total_weight_sent += item_weight
    
unused_capacity += (max_items - packages_sent) * 20

print("Number of packages sent:", packages_sent)
print("Total weight of packages sent:", total_weight_sent)
print("Total unused capacity:", unused_capacity)
print("Package number with the most unused capacity:", max_unused_capacity_package)
print("Unused capacity in that package:", max_unused_capacity)