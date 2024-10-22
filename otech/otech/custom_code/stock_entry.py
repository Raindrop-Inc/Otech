# import frappe

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
    if doc.get("consumed_qty_updated"):
        return 
    for item in doc.items:
        tasks = frappe.db.get_all("Task wise Budget", filters={"parent": item.custom_task, "item_name": item.item_code}, fields=["*"])
        for task in tasks:
            current_consumed_qty = task.consumed_qty or 0
            new_consumed_qty = current_consumed_qty + item.qty
            # consumed_qty = item.qty
            remaining_qty = task.estimated_qty - new_consumed_qty
            remaining_percentage = 100 - ((remaining_qty / task.estimated_qty) * 100)

            frappe.db.set_value("Task wise Budget", task.name, "consumed_qty", new_consumed_qty)
            frappe.db.set_value("Task wise Budget", task.name, "remaining_qty", remaining_qty)
            frappe.db.set_value("Task wise Budget", task.name, "remaining_", remaining_percentage)
    doc.consumed_qty_updated = True
    doc.save()
    frappe.db.commit()

def on_cancel(doc, method):
    # if doc.get("is_canceled"):  # Assuming 'is_canceled' is a field that indicates cancellation
        for item in doc.items:
            tasks = frappe.db.get_all("Task wise Budget", filters={"parent": item.custom_task, "item_name": item.item_code}, fields=["*"])
            for task in tasks:
                current_consumed_qty = task.consumed_qty or 0
                # Reduce consumed_qty by the quantity of the canceled item
                new_consumed_qty = current_consumed_qty - item.qty
                remaining_qty = task.estimated_qty - new_consumed_qty
                remaining_percentage = 100 - ((remaining_qty / task.estimated_qty) * 100)

                frappe.db.set_value("Task wise Budget", task.name, "consumed_qty", new_consumed_qty)
                frappe.db.set_value("Task wise Budget", task.name, "remaining_qty", remaining_qty)
                frappe.db.set_value("Task wise Budget", task.name, "remaining_", remaining_percentage)
        doc.save()
        frappe.db.commit()
