import frappe

def on_save(doc, method):
    for item in doc.items:
        for task in frappe.db.get_all("Task wise Budget", filters = {"parent":item.custom_task, "item_name":item.item_code}, fields=["*"]):
            frappe.db.set_value("Task wise Budget", task.name, "consumed_qty", item.qty)
            frappe.db.set_value("Task wise Budget", task.name, "remaining_qty", task.estimated_qty - item.qty)
            frappe.db.set_value("Task wise Budget", task.name, "remaining_", ((task.remaining_qty / task.estimated_qty) * 100))
            # frappe.db.set_value("Task wise Budget", task.name, "remaining_", (100 - ((task.estimated_qty - item.qty) / task.estimated_qty) * 100))
            frappe.db.commit()                                                                                             
