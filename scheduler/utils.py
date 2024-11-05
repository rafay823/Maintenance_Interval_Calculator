from models.vehicle import  MaintenanceInterval
from data.maintenance_interval_data import MAINTENANCE_INTERVALS
from typing import Dict

"""Get predefined maintenance intervals or allow custom input."""
def get_maintenance_intervals(make: str, model: str, year: str) -> MaintenanceInterval:
    key = f"{make} {model}"
    print(key)
    if key in MAINTENANCE_INTERVALS:
        if year in MAINTENANCE_INTERVALS[key]:
            return MAINTENANCE_INTERVALS[key][year]

    print(f"No predefined intervals for {key}. Let's set custom intervals.")
    intervals = {}
    for service_type in ["Oil Change", "Inspection", "Brake Fluid"]:
        while True:
            try:
                interval = int(input(f"Enter interval in km for {service_type}: "))
                if interval <= 0:
                    print("Interval must be a positive number. Please try again.")
                    continue
                intervals[service_type] = interval
                break
            except ValueError:
                print("Invalid interval. Please enter a number.")

    return MaintenanceInterval(intervals=intervals)


def calculate_next_maintenance(current_mileage: int, intervals: MaintenanceInterval) -> Dict[str, int]:
    upcoming_maintenance = {}
    for service, interval in intervals.intervals.items():
        next_due = (current_mileage // interval + 1) * interval
        remaining_km = next_due - current_mileage
        upcoming_maintenance[service] = remaining_km
    return upcoming_maintenance
