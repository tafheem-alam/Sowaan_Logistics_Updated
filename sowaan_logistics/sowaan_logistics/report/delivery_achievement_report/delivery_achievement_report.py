import frappe

def execute(filters=None):
    filters = filters or {}

    # Filter values from the report parameters
    values = {
        "status": "Completed",  # default filter as per your JSON
        "from_date": filters.get("from_date"),
        "to_date": filters.get("to_date"),
        "vehicle": filters.get("vehicle"),
        "driver": filters.get("driver")
    }

    # Convert empty filters to None
    for key in values:
        if not values[key]:
            values[key] = None

    # Define columns
    columns = [
        {"fieldname": "Delivery Trip", "label": "Delivery Trip", "fieldtype": "Link", "options": "Delivery Trip", "width": 120},
        {"fieldname": "Delivery Note", "label": "Delivery Note", "fieldtype": "Link", "options": "Delivery Note", "width": 120},
        {"fieldname": "Driver Name", "label": "Driver Name", "fieldtype": "Data", "width": 120},
        {"fieldname": "Customer", "label": "Customer", "fieldtype": "Data", "width": 120},
        {"fieldname": "Status", "label": "Status", "fieldtype": "Data", "width": 120},
        {"fieldname": "Vehicle", "label": "Vehicle", "fieldtype": "Link", "options": "Vehicle", "width": 120},
        {"fieldname": "Driver", "label": "Driver", "fieldtype": "Link", "options": "Driver", "width": 120},
        {"fieldname": "Departure Time", "label": "Departure Time", "fieldtype": "Datetime", "width": 120},
        {"fieldname": "Distance", "label": "Distance", "fieldtype": "Float", "width": 120},
    ]

    # SQL Query to fetch data
    results = frappe.db.sql("""
        SELECT
            dt.name AS 'Delivery Trip',
            ds.delivery_note AS 'Delivery Note',
            dt.driver_name AS 'Driver Name',
            ds.customer AS 'Customer',
            dt.status AS 'Status',
            dt.vehicle AS 'Vehicle',
            dt.driver AS 'Driver',
            dt.departure_time AS 'Departure Time',
            ds.distance AS 'Distance'
        FROM
            `tabDelivery Trip` dt
        LEFT JOIN
            `tabDelivery Stop` ds ON ds.parent = dt.name AND ds.parenttype = 'Delivery Trip'
        WHERE
            dt.status = %(status)s
            AND (%(from_date)s IS NULL OR dt.departure_time >= %(from_date)s)
            AND (%(to_date)s IS NULL OR dt.departure_time <= %(to_date)s)
            AND (%(vehicle)s IS NULL OR dt.vehicle = %(vehicle)s)
            AND (%(driver)s IS NULL OR dt.driver = %(driver)s)
        ORDER BY dt.modified DESC
        LIMIT 20
    """, values, as_dict=True)

    return columns, results
