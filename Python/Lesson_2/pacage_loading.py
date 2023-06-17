current_package_weight = 0
package_count = 0
packages_sent = 0
total_weight_sent = 0
unused_capacity = 0
max_unused_capacity = 0
max_unused_package = 0
max_items = int(input("Enter the maximum number of items to be shipped: "))

while package_count < max_items:
        item_weight = input(f"Enter the weight of item {package_count + 1} (0 to exit): ")

        if not item_weight.isdigit():
            print("Invalid input. Please enter a valid weight.")
            continue

        item_weight = int(item_weight)

        if item_weight == 0:
            break

        if item_weight < 1 or item_weight > 10:
            print("Invalid weight. Please enter a weight between 1 and 10.")
            continue

        if current_package_weight + item_weight > 20:
            print(f"Package {package_count + 1} sent")
            packages_sent += 1
            total_weight_sent += current_package_weight
            unused_capacity += 20 - current_package_weight

            if 20 - current_package_weight > max_unused_capacity:
                max_unused_capacity = 20 - current_package_weight
                max_unused_package = package_count + 1

            current_package_weight = 0

        current_package_weight += item_weight
        package_count += 1

if current_package_weight > 0:
        packages_sent += 1
        total_weight_sent += current_package_weight
        unused_capacity += 20 - current_package_weight

        if 20 - current_package_weight > max_unused_capacity:
            max_unused_capacity = 20 - current_package_weight
            max_unused_package = package_count + 1

print("All packages sent!")
print(f"Number of packages sent: {packages_sent}")
print(f"Total weight of packages sent: {total_weight_sent} kg")
print(f"Total 'unused' capacity: {unused_capacity} kg")
print(f"Package number with the most 'unused' capacity: Package {max_unused_package}")
print(f"Amount of 'unused' capacity in that package: {max_unused_capacity} kg")