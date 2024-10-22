app_name = "otech"
app_title = "Otech"
app_publisher = "Doreen and Mukesh"
app_description = "Otech customisations"
app_email = "doreenmwapekatebe8@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/otech/css/otech.css"
# app_include_js = "/assets/otech/js/otech.js"

# include js, css files in header of web template
# web_include_css = "/assets/otech/css/otech.css"
# web_include_js = "/assets/otech/js/otech.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "otech/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Task" : "public/js/task.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "otech.utils.jinja_methods",
#	"filters": "otech.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "otech.install.before_install"
# after_install = "otech.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "otech.uninstall.before_uninstall"
# after_uninstall = "otech.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "otech.utils.before_app_install"
# after_app_install = "otech.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "otech.utils.before_app_uninstall"
# after_app_uninstall = "otech.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "otech.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Stock Entry": {
		# "on_update": "otech.otech.custom_code.stock_entry.on_save",
		"on_submit": "otech.otech.custom_code.stock_entry.on_save",
		# "on_cancel": "method",
		"on_cancle": "otech.otech.custom_code.stock_entry.on_cancel",
		# "on_trash": "method"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"otech.tasks.all"
#	],
#	"daily": [
#		"otech.tasks.daily"
#	],
#	"hourly": [
#		"otech.tasks.hourly"
#	],
#	"weekly": [
#		"otech.tasks.weekly"
#	],
#	"monthly": [
#		"otech.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "otech.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "otech.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "otech.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["otech.utils.before_request"]
# after_request = ["otech.utils.after_request"]

# Job Events
# ----------
# before_job = ["otech.utils.before_job"]
# after_job = ["otech.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"otech.auth.validate"
# ]
fixtures = [     {
        "dt": "Custom Field",
        "filters": [
            [
                "module", "in", [
                    "Otech"
                ]
            ]
        ]

    },
]
