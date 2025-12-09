import frappe

def execute(filters=None):
    filters = filters or {}

    # Filter values from the report parameters
    values = {
        "from_date": filters.get("from_date"),
        "to_date": filters.get("to_date"),
        "project": filters.get("project"),
        "delivery_trip": filters.get("delivery_trip"),
        "delivery_note": filters.get("delivery_note"),
        "company": filters.get("company"),
    }

    # Convert empty strings to None so optional filters work
    for key in values:
        if not values[key]:
            values[key] = None

    # Define report columns
    columns = [
        {"fieldname": "Posting Date", "label": "Posting Date", "fieldtype": "Date"},
        {"fieldname": "Delivery Trip", "label": "Delivery Trip", "fieldtype": "Link", "options": "Delivery Trip"},
        {"fieldname": "Driver Name", "label": "Driver Name", "fieldtype": "Data"},
        {"fieldname": "Vehicle", "label": "Vehicle", "fieldtype": "Data"},
        {"fieldname": "Company", "label": "Company", "fieldtype": "Data"},
        {"fieldname": "Project", "label": "Project", "fieldtype": "Data"},
        {"fieldname": "#DO NO.", "label": "#DO NO.", "fieldtype": "Link", "options": "Delivery Note"},
        {"fieldname": "Area", "label": "Area", "fieldtype": "Data"},
        {"fieldname": "Distance", "label": "Distance", "fieldtype": "Data"},
        {"fieldname": "UOM", "label": "UOM", "fieldtype": "Data"},
        {"fieldname": "Fuel Type", "label": "Fuel Type", "fieldtype": "Data"},
        {"fieldname": "Fuel Subtype", "label": "Fuel Subtype", "fieldtype": "Data"},
        {"fieldname": "Fuel rate Per KM", "label": "Fuel rate Per KM", "fieldtype": "Data"},
        {"fieldname": "Fuel Consumption Qty", "label": "Fuel Consumption Qty", "fieldtype": "Data"},
        {"fieldname": "Average Fuel per KM", "label": "Average Fuel per KM", "fieldtype": "Data"},
        {"fieldname": "Fuel Consumption Amount", "label": "Fuel Consumption Amount", "fieldtype": "Data"}
    ]

    # SQL Query to fetch data
    results = frappe.db.sql("""
        SELECT 
            dt.custom_posting_date AS 'Posting Date',
            dt.name AS 'Delivery Trip',
            dt.driver_name AS 'Driver Name',
            dt.vehicle AS 'Vehicle',
            dt.company AS 'Company',
            dn.project AS 'Project',  
            ds.delivery_note AS '#DO NO.',
            ad.city AS 'Area',
            ds.distance AS 'Distance',
            ds.uom AS 'UOM',
            ds.custom_fuel_type as 'Fuel Type',
            ds.custom_fuel_value AS 'Fuel rate Per KM',
            ds.custom_total_value AS 'Fuel Consumption Qty',
            ds.custom_rate as 'Average Fuel per KM',
            ds.custom_fuel_subtype as 'Fuel Subtype',
            ds.custom_fuel_consumption as 'Fuel Consumption Amount'
        FROM 
            `tabDelivery Trip` dt
        JOIN 
            `tabDelivery Stop` ds ON ds.parent = dt.name AND ds.parenttype = 'Delivery Trip'
        JOIN 
            `tabDelivery Note` dn ON dn.name = ds.delivery_note
        JOIN 
            `tabDynamic Link` dl ON ds.customer = dl.link_name AND dl.parenttype = 'Address'
        JOIN 
            `tabAddress` ad ON ad.name = dl.parent
        WHERE 
            dt.docstatus = 1  
            AND (%(from_date)s IS NULL OR %(to_date)s IS NULL OR dt.custom_posting_date BETWEEN %(from_date)s AND %(to_date)s)
            AND (%(project)s IS NULL OR dn.project = %(project)s)
            AND (%(delivery_trip)s IS NULL OR dt.name = %(delivery_trip)s)
            AND (%(delivery_note)s IS NULL OR ds.delivery_note = %(delivery_note)s)
            AND (%(company)s IS NULL OR dt.company = %(company)s)
        ORDER BY dt.name
    """, values, as_dict=True)

    return columns, results
