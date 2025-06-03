setting = input().split();
package_count = int(setting[0]);
truck_count = int(setting[1]);
packages = [];
for i in range(package_count):
    packages.append(int(input()));

def allocation():
    max_p = sum(packages);
    left = 0;
    right = max_p;
    while left < right:
        mid = (left + right) // 2;
        load = calculate_load(mid);
        if load >= package_count:
            right = mid;
        else:
            left = mid + 1;
    return right;

def calculate_load(p):
    i = 0;
    j = 0;
    current_truck_p = p;
    while i < package_count and j < truck_count:
        if packages[i] <= current_truck_p:
            current_truck_p -= packages[i];
            i += 1;
        else:
            j += 1;
            current_truck_p = p;
    return i;

print(allocation());
