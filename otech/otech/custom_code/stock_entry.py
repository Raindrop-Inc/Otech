import frappe

# def on_save(doc, method):
#     for item in doc.items:
#         for task in frappe.db.get_all("Task wise Budget", filters = {"parent":item.custom_task, "item_name":item.item_code}, fields=["*"]):
#             frappe.db.set_value("Task wise Budget", task.name, "consumed_qty", item.qty)
#             frappe.db.set_value("Task wise Budget", task.name, "remaining_qty", task.estimated_qty - item.qty)
#             frappe.db.set_value("Task wise Budget", task.name, "remaining_", (100 - (task.remaining_qty / task.estimated_qty) * 100))
#             frm.refresh_field('remaining_')
#             # frappe.db.set_value("Task wise Budget", task.name, "remaining_", (100 - ((task.remaining_qty / task.estimated_qty) * 100))
#             frappe.db.commit()    

import frappe

def on_save(doc, method):
    for item in doc.items:
        tasks = frappe.db.get_all("Task wise Budget", filters={"parent": item.custom_task, "item_name": item.item_code}, fields=["*"])
        for task in tasks:
            consumed_qty = item.qty
            remaining_qty = task.estimated_qty - consumed_qty
            remaining_percentage = 100 - ((remaining_qty / task.estimated_qty) * 100)

            frappe.db.set_value("Task wise Budget", task.name, "consumed_qty", consumed_qty)
            frappe.db.set_value("Task wise Budget", task.name, "remaining_qty", remaining_qty)
            frappe.db.set_value("Task wise Budget", task.name, "remaining_", remaining_percentage)

    frappe.db.commit()
