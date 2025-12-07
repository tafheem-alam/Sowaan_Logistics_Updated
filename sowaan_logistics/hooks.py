app_name = "sowaan_logistics"
app_title = "Sowaan Logistics"
app_publisher = "Sowaan"
app_description = "Logistic App for different types of logistics like bus, car"
app_email = "info@sowaan.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sowaan_logistics",
# 		"logo": "/assets/sowaan_logistics/logo.png",
# 		"title": "Sowaan Logistics",
# 		"route": "/sowaan_logistics",
# 		"has_permission": "sowaan_logistics.api.permission.has_app_permission"
# 	}
# ]

fixtures = [
    {"doctype": "Custom Field"},
    {"doctype": "Client Script"},
    {"doctype": "Server Script"},
    {"doctype": "Property Setter"},
    {"doctype": "Report Reference Doctype"},
    # Export Reports for these doctypes
    {
    "doctype": "Report",
    "filters": [
        #["is_standard", "=", "No"],        # get only custom or modified reports
        ["name", "in", [
            "Vehicle Expenses for Delivery Trip",
            "Delivery Achievement Report",
            "Delivery Note Trends",
            "Delivery Trip Report",
            "Delivered Items To Be Billed",
            "Logistics Buses Report",
            "Logistics Car Report",            
            "Vehicle Expense Report for Buses",
            "Vehicle",
            "Vehicle Report",
            "Vehicle Log Report",
            "Vehicle Expenses",
            "Driver",
            "Gate Pass",
            "Logistics Buses",
            "Logistic Car",
            "Logistics Table",
            "Delivery Stops on Gate Pass",
            "Delivery Trip",
            "Delivery Note",
            "Vehicle Expense Report for Cars",
            "Vehicle Expense Report for Buses",
            ""
        ]]
        ]
    },   

    # Workspace and its items/shortcuts
    {
        "doctype": "Workspace",
        "filters": [
            ["module", "=", "Sowaan Logistics"]
        ]
    },
    {
        "dt": "Workspace Link",
        "filters": [
            ["module", "=", "Sowaan Logistics"]
        ]
    }
    

    # Export all Workspace shortcuts/layouts if needed (optional)
    # "Workspace"

]




# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sowaan_logistics/css/sowaan_logistics.css"
# app_include_js = "/assets/sowaan_logistics/js/sowaan_logistics.js"

# include js, css files in header of web template
# web_include_css = "/assets/sowaan_logistics/css/sowaan_logistics.css"
# web_include_js = "/assets/sowaan_logistics/js/sowaan_logistics.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sowaan_logistics/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sowaan_logistics/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sowaan_logistics.utils.jinja_methods",
# 	"filters": "sowaan_logistics.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sowaan_logistics.install.before_install"
# after_install = "sowaan_logistics.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sowaan_logistics.uninstall.before_uninstall"
# after_uninstall = "sowaan_logistics.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sowaan_logistics.utils.before_app_install"
# after_app_install = "sowaan_logistics.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sowaan_logistics.utils.before_app_uninstall"
# after_app_uninstall = "sowaan_logistics.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sowaan_logistics.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sowaan_logistics.tasks.all"
# 	],
# 	"daily": [
# 		"sowaan_logistics.tasks.daily"
# 	],
# 	"hourly": [
# 		"sowaan_logistics.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sowaan_logistics.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sowaan_logistics.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sowaan_logistics.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sowaan_logistics.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sowaan_logistics.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sowaan_logistics.utils.before_request"]
# after_request = ["sowaan_logistics.utils.after_request"]

# Job Events
# ----------
# before_job = ["sowaan_logistics.utils.before_job"]
# after_job = ["sowaan_logistics.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sowaan_logistics.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

