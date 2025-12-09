import frappe

def execute(filters=None):
    filters = filters or {}

    # Optional filters can be added if needed
    values = {
        "vehicle": filters.get("vehicle"),
        "make": filters.get("make"),
        "model": filters.get("model"),
        "vehicle_group": filters.get("vehicle_group"),
        "driver": filters.get("driver"),
    }

    # Convert empty filters to None
    for key in values:
        if not values[key]:
            values[key] = None

    # Define columns
    columns = [
        {"fieldname": "name", "label": "Vehicle", "fieldtype": "Link", "options": "Vehicle", "width": 120},
        {"fieldname": "make", "label": "Make", "fieldtype": "Data", "width": 120},
        {"fieldname": "model", "label": "Model", "fieldtype": "Data", "width": 120},
        {"fieldname": "custom_vehicle_group", "label": "Vehicle Group", "fieldtype": "Data", "width": 120},
        {"fieldname": "custom_emirates_registered", "label": "Emirates Registered", "fieldtype": "Data", "width": 120},
        {"fieldname": "employee", "label": "Employee", "fieldtype": "Link", "options": "Employee", "width": 120},
        {"fieldname": "custom_driver_full_name", "label": "Driver Full Name", "fieldtype": "Data", "width": 120},
        {"fieldname": "fuel_type", "label": "Fuel Type", "fieldtype": "Data", "width": 120},
        {"fieldname": "custom_registration_expiry_date", "label": "Registration Expiry Date", "fieldtype": "Date", "width": 120},
    ]

    # SQL Query to fetch data
    results = frappe.db.sql("""
        SELECT
            name,
            make,
            model,
            custom_vehicle_group,
            custom_emirates_registered,
            employee,
            custom_driver_full_name,
            fuel_type,
            custom_registration_expiry_date
        FROM
            `tabVehicle`
        WHERE
            (%(vehicle)s IS NULL OR name = %(vehicle)s)
            AND (%(make)s IS NULL OR make = %(make)s)
            AND (%(model)s IS NULL OR model = %(model)s)
            AND (%(vehicle_group)s IS NULL OR custom_vehicle_group = %(vehicle_group)s)
            AND (%(driver)s IS NULL OR custom_driver_full_name = %(driver)s)
        ORDER BY modified DESC
        LIMIT 20
    """, values, as_dict=True)

    return columns, results
