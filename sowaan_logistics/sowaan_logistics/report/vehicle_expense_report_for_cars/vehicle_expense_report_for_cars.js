// Copyright (c) 2025, Sowaan and contributors
// For license information, please see license.txt

frappe.query_reports["Vehicle Expense Report for Cars"] = {
	"filters": [
{
   "fieldname": "from",
   "fieldtype": "Date",
   "label": "From",
   "mandatory": 1,
   "wildcard_filter": 0
  },
  {
   "fieldname": "to",
   "fieldtype": "Date",
   "label": "To",
   "mandatory": 1,
   "wildcard_filter": 0
  },
  {
   "fieldname": "company",
   "fieldtype": "Link",
   "label": "Company",
   "mandatory": 0,
   "options": "Company",
   "wildcard_filter": 0
  },
  {
   "fieldname": "vehicle",
   "fieldtype": "Link",
   "label": "Vehicle",
   "mandatory": 0,
   "options": "Vehicle",
   "wildcard_filter": 0
  },
  {
   "fieldname": "driver",
   "fieldtype": "Link",
   "label": "Driver",
   "mandatory": 0,
   "options": "Driver",
   "wildcard_filter": 0
  }
	]
};
