// Copyright (c) 2025, Sowaan and contributors
// For license information, please see license.txt

frappe.query_reports["Logistics Buses Report"] = {
	"filters": [
{
   "fieldname": "from",
   "fieldtype": "Date",
   "label": "From ",
   "mandatory": 0,
   "wildcard_filter": 0
  },
  {
   "default": "Today",
   "fieldname": "to",
   "fieldtype": "Date",
   "label": "To",
   "mandatory": 0,
   "wildcard_filter": 0
  },
  {
   "default": "SASCO Industries",
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
  }
	]
};
