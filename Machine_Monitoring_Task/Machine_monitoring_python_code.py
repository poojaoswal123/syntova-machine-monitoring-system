
import math

# Power limits of machines
power_limits = {
    101: 18.0,
    102: 25.0,
    103: 12.0
}

# Power readings
readings = [
    {"machine_id": 101, "timestamp": "09:00", "power_kw": 16.5},
    {"machine_id": 101, "timestamp": "09:15", "power_kw": 19.1},
    {"machine_id": 101, "timestamp": "09:30", "power_kw": 17.0},
    {"machine_id": 102, "timestamp": "09:00", "power_kw": 22.5},
    {"machine_id": 102, "timestamp": "09:15", "power_kw": 22.5},
    {"machine_id": 103, "timestamp": "09:00", "power_kw": 11.5},
    {"machine_id": 103, "timestamp": "09:15", "power_kw": 12.7}
]


# Function to analyze power
def analyze_power(readings, power_limits):

    summary = {}

    # Analyze each reading
    for reading in readings:

        machine_id = reading.get("machine_id")
        power = reading.get("power_kw")

        # Check whether machine id exists
        if machine_id not in power_limits:
            print("Unknown machine:", machine_id)
            continue

        # Check whether power is valid
        if (not isinstance(power, (int, float))
                or isinstance(power, bool)
                or not math.isfinite(power)
                or power < 0):
            print("Invalid power reading:", power)
            continue

        limit = power_limits[machine_id]

        # Check power status
        if power > limit:
            status = "HIGH"
        else:
            status = "NORMAL"

        # Calculate energy for 15 minutes
        energy = power * 0.25               # Energy = Power * Time   ( 15 min = 0.25 hr) 

        print("Machine ID:", machine_id)
        print("Time:", reading.get("timestamp"))
        print("Power:", power, "kW")
        print("Status:", status)
        print("Energy:", round(energy, 2), "kWh")

        # Summary for each machine
        if machine_id not in summary:
            summary[machine_id] = {
                "total_energy": 0,
                "total_power": 0,
                "peak_power": 0,
                "high_count": 0,
                "count": 0
            }

        # Calculate summary values
        summary[machine_id]["total_energy"] += energy
        summary[machine_id]["total_power"] += power
        summary[machine_id]["peak_power"] = max(summary[machine_id]["peak_power"], power)
        summary[machine_id]["count"] += 1       # count - Total number of valid readings

        if status == "HIGH":
            summary[machine_id]["high_count"] += 1   # high_count- Number of readings where power exceeded the limit


    # Final summary
    print("\nFINAL SUMMARY")

    for machine_id, data in sorted(summary.items()):

        average_power = data["total_power"] / data["count"]

        print("\nMachine ID:", machine_id)
        print("Total Energy:", round(data["total_energy"], 2), "kWh")
        print("Average Power:", round(average_power, 2), "kW")
        print("Peak Power:", round(data["peak_power"], 2), "kW")
        print("HIGH Count:", data["high_count"])


# Call the function
analyze_power(readings, power_limits)



# Test Case 1: Unknown machine ID
print("\nTEST CASE 1: Unknown Machine")
test_readings = [
    {"machine_id": 999, "timestamp": "10:00", "power_kw": 15.0}
]
analyze_power(test_readings, power_limits)


# Test Case 2: Zero power
print("\nTEST CASE 2: Zero Power")
test_readings = [
    {"machine_id": 101, "timestamp": "10:00", "power_kw": 0}
]
analyze_power(test_readings, power_limits)