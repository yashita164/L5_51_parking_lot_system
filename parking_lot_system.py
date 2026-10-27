"""Manage parking slots, fees, vehicle hashes, and parking manifests."""

import hashlib
import secrets
from pathlib import Path

parking_slots = {
    "P01": {
        "plate": "KA01AB1234",
        "hours": 2,
        "rate": 20.0,
        "is_occupied": True,
    },
    "P02": {
        "plate": "TN07CD5678",
        "hours": 0,
        "rate": 20.0,
        "is_occupied": False,
    },
    "P03": {
        "plate": "MH02EF9012",
        "hours": 4,
        "rate": 30.0,
        "is_occupied": True,
    },
}

collections = {"total": 0.0}


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle in an available slot and record its charge."""
    if entry_logs is None:
        entry_logs = []

    if slot_id not in parking_slots or parking_slots[slot_id]["is_occupied"]:
        return False

    if not isinstance(hours_booked, (int, float)) or hours_booked <= 0:
        return False

    parking_slots[slot_id]["plate"] = plate_no
    parking_slots[slot_id]["hours"] = hours_booked
    parking_slots[slot_id]["is_occupied"] = True

    charge = parking_slots[slot_id]["rate"] * hours_booked
    collections["total"] += charge

    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} "
        f"for {hours_booked} hours; charge: {charge:.2f}"
    )
    return True


def release_slot(slot_id):
    """Release a parking slot, returning False for an unknown slot."""
    if slot_id not in parking_slots:
        return False

    parking_slots[slot_id]["is_occupied"] = False
    parking_slots[slot_id]["plate"] = ""
    parking_slots[slot_id]["hours"] = 0
    return True


def check_slot_availability(slot_id):
    """Return True if a known parking slot is vacant."""
    slot = parking_slots.get(slot_id)
    return slot is not None and not slot["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier=1.0):
    """Calculate a parking fee using a numeric surge multiplier."""
    if slot_id not in parking_slots:
        raise ValueError(f"Unknown parking slot: {slot_id}")

    if (
        not isinstance(surge_multiplier, (int, float))
        or isinstance(surge_multiplier, bool)
        or surge_multiplier < 0
    ):
        raise ValueError("Surge multiplier must be a non-negative number.")

    slot = parking_slots[slot_id]
    return slot["rate"] * slot["hours"] * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Return a SHA-256 digest of a vehicle license plate."""
    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def generate_ticket_pin():
    """Generate a cryptographically secure four-digit ticket PIN."""
    return str(secrets.randbelow(9000) + 1000)


def export_parking_manifest(filename="parking_manifest.txt"):
    """Export the current parking-slot data to a text manifest."""
    manifest_path = Path(filename)
    with manifest_path.open("w", encoding="utf-8") as manifest:
        for slot_id, details in parking_slots.items():
            manifest.write(
                f"{slot_id}: plate={details['plate']}, "
                f"hours={details['hours']}, rate={details['rate']}, "
                f"occupied={details['is_occupied']}\n"
            )

    print(f"Parking manifest exported to: {manifest_path}")


def get_available_summary(slots):
    """Return the number of vacant slots in the supplied mapping."""
    return sum(
        not details["is_occupied"] for details in slots.values()
    )


def main():
    """Run a demonstration of the parking lot system."""
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")

    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.50))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())

    export_parking_manifest()
    print("Vacant slots:", get_available_summary(parking_slots))
    print("Total collections:", f"{collections['total']:.2f}")


if __name__ == "__main__":
    main()
