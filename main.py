from models.vehicle import VehicleData
from scheduler.utils import get_maintenance_intervals, calculate_next_maintenance
from pydantic import ValidationError

def get_vehicle_data() -> VehicleData | None:
    try:
        make = input("Enter the vehicle make: ")
        model = input("Enter the vehicle model: ")
        year = input("Enter the vehicle year: ")
        current_mileage = int(input("Enter the current mileage (km): "))
        return VehicleData(make=make, model=model, year=year, current_mileage=current_mileage)
    except (ValueError, ValidationError) as e:
        print(f"Invalid input: {e}")
        return None

def display_upcoming_maintenance(upcoming_maintenance):
    print("\nUpcoming Maintenance Tasks:")
    for service, remaining_km in upcoming_maintenance.items():
        print(f"{service}: {remaining_km} km remaining")

def main():
    while True:
        print("Vehicle Maintenance Scheduler")
        vehicle_data = get_vehicle_data()
        if not vehicle_data:
            continue
        intervals = get_maintenance_intervals(vehicle_data.make, vehicle_data.model,vehicle_data.year)
        upcoming_maintenance = calculate_next_maintenance(vehicle_data.current_mileage, intervals)
        display_upcoming_maintenance(upcoming_maintenance)

        choice = input("\nWould you like to check maintenance for another vehicle? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the Vehicle Maintenance Scheduler. Goodbye!")
            break

if __name__ == "__main__":
    main()
