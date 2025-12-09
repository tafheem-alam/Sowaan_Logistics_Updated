import frappe

def execute(filters=None):
    filters = filters or {}

    # Filter values from the report parameters
    values = {
        "from": filters.get("from"),
        "to": filters.get("to"),
        "company": filters.get("company"),
        "vehicle": filters.get("vehicle"),
    }

    # Convert empty strings to None so optional filters work
    for key in values:
        if not values[key]:
            values[key] = None

    # Define report columns
    columns = [
        {"fieldname": "Vehicle", "label": "Vehicle", "fieldtype": "Link", "options": "Vehicle"},
        {"fieldname": "Vehicle Description", "label": "Vehicle Description", "fieldtype": "Data"},
        {"fieldname": "Driver", "label": "Driver", "fieldtype": "Link", "options": "Driver"},
        {"fieldname": "Driver Name", "label": "Driver Name", "fieldtype": "Data"},
        {"fieldname": "From", "label": "From", "fieldtype": "Link", "options": "Address"},
        {"fieldname": "To", "label": "To", "fieldtype": "Link", "options": "Address"},
        {"fieldname": "Time In", "label": "Time In", "fieldtype": "Datetime"},
        {"fieldname": "Time Out", "label": "Time Out", "fieldtype": "Datetime"},
        {"fieldname": "Trip Number", "label": "Trip Number", "fieldtype": "Data"},
        {"fieldname": "Start KM", "label": "Start KM", "fieldtype": "Float"},
        {"fieldname": "End KM", "label": "End KM", "fieldtype": "Float"},
        {"fieldname": "Distance Covered", "label": "Distance Covered", "fieldtype": "Float"},
        {"fieldname": "Fuel Type", "label": "Fuel Type", "fieldtype": "Data"},
        {"fieldname": "Fuel Subtype", "label": "Fuel Subtype", "fieldtype": "Float"},
        {"fieldname": "Average Rate Per KM", "label": "Average Rate Per KM", "fieldtype": "Float"},
        {"fieldname": "Fuel Consumption Qty", "label": "Fuel Consumption Qty", "fieldtype": "Float"},
        {"fieldname": "Fuel Rate Per Litre", "label": "Fuel Rate Per Litre", "fieldtype": "Float"},
        {"fieldname": "Fuel Consumption Amount", "label": "Fuel Consumption Amount", "fieldtype": "Float"},
    ]

    # SQL Query to fetch data
    results = frappe.db.sql("""
        SELECT 
            lt.vehicle AS 'Vehicle',
            lt.vehicle_description as 'Vehicle Description',
            lt.driver AS 'Driver',
            lt.driver_name as 'Driver Name',
            lt.from AS 'From',
            lt.to AS 'To',
            lt.time_in AS 'Time In',
            lt.time_out AS 'Time Out',
            lt.trip_number AS 'Trip Number',
            FORMAT(lt.start_km, 2) AS 'Start KM',
            FORMAT(lt.end_km, 2) AS 'End KM',
            FORMAT(lt.distance_covered, 2) AS 'Distance Covered',
            lt.fuel_type AS 'Fuel Type',
            FORMAT(lt.fuel_subtype, 2) AS 'Fuel Subtype',
            FORMAT(lt.float_value, 2) AS 'Average Rate Per KM',
            FORMAT(lt.fuel_consumption, 2) AS 'Fuel Consumption Qty',
            FORMAT(lt.fuel_rate_per_litre, 2) AS 'Fuel Rate Per Litre',
            FORMAT(lt.fuel_consumption_amount, 2) AS 'Fuel Consumption Amount'
        FROM 
            `tabLogistics Table` lt
        INNER JOIN 
            `tabLogistic Car` lb ON lb.name = lt.parent
        WHERE 
            lb.docstatus = 1
            AND (%(from)s IS NULL OR %(to)s IS NULL OR lb.date BETWEEN %(from)s AND %(to)s)
            AND (%(company)s IS NULL OR lb.company = %(company)s)
            AND (%(vehicle)s IS NULL OR lt.vehicle = %(vehicle)s)
        ORDER BY lb.date DESC
    """, values, as_dict=True)

    return columns, results
