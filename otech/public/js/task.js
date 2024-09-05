frappe.ui.form.on('Task', {
	refresh(frm) {
		// your code here
	}
})

frappe.ui.form.on('Task Budget', {
    
// 	refresh(frm) {
// 		// your code here
		
// 	}
    estimated_qty: function(frm, cdt, cdn) {
        console.log('Estimated Qty changed');
        calculate_amount_task_budget(cdt, cdn);
    },
    rate: function(frm, cdt, cdn) {
        console.log('Rate changed');
        calculate_amount_task_budget(cdt, cdn);
    },
    completed: function(frm, cdt, cdn) {
        calculate_amount_task_budget(cdt, cdn);
    }

});

frappe.ui.form.on('Task wise Budget', {
// 	refresh(frm) {
// 		// your code here
// 		frm.refresh_field('custom_task_wise_budget');
// 	},
    
    estimated_qty: function(frm, cdt, cdn) {
        console.log('Estimated Qty changed');
        calculate_amount(cdt, cdn);
    },
    rate: function(frm, cdt, cdn) {
        console.log('Rate changed');
        calculate_amount(cdt, cdn);
    },
    consumed_qty: function(frm, cdt, cdn) {
        console.log('Cunsumed Quantity changed');
        calculate_amount(cdt, cdn);
    }
    // frm.refresh_field('Task wise Budget') // Refresh the child table
});

function calculate_amount(cdt, cdn) {
    var row = locals[cdt][cdn];
    console.log('Calculating amount for row:', row);
    if (row.estimated_qty && row.rate) {
        var amount = row.estimated_qty * row.rate;
        console.log('Calculated Amount:', amount);
        frappe.model.set_value(cdt, cdn, 'amount', amount);
    }
    // else if (row.estimated_qty && row.)
    else {
        console.log('Setting Amount to 0');
        frappe.model.set_value(cdt, cdn, 'amount', 0);
    }
    // var remaining_qty = 0;
    if (row.estimated_qty && row.consumed_qty) {
        // refresh_field(“total_amount”);
        var remaining_qty = row.estimated_qty - row.consumed_qty;
        console.log('Remaining Qty:', remaining_qty);
        // cur_frm.refresh_field('remaining_qty');
        frappe.model.set_value(cdt, cdn, 'remaining_qty', remaining_qty);
        
    }
    else {
        frappe.model.set_value(cdt, cdn, 'remaining_qty', 0);
    }
    if (row.estimated_qty > 0) {
        // frm.refresh_field('remaining_'); // Refresh the child table
        var remaining_ = (100 - (remaining_qty / row.estimated_qty) * 100);
        // cur_frm.refresh_field('remaining_');
        frappe.model.set_value(cdt, cdn, 'remaining_', remaining_);
    } 
    else {
        frappe.model.set_value(cdt, cdn, 'remaining_percent', 0);
    }
    // cur_frm.refresh_field('custom_task_wise_budget'); // Refresh the child table
}

function calculate_amount_task_budget(cdt, cdn) {
    var row = locals[cdt][cdn];
    console.log('Calculating amount for row:', row);
    if (row.estimated_qty && row.rate) {
        var amount = row.estimated_qty * row.rate;
        console.log('Calculated Amount:', amount);
        frappe.model.set_value(cdt, cdn, 'amount', amount);
    }
    // else if (row.estimated_qty && row.)
    else {
        console.log('Setting Amount to 0');
        frappe.model.set_value(cdt, cdn, 'amount', 0);
    }
    // if (row.estimated_qty && row.completed) {
    //     var remaining_qty = row.estimated_qty - row.consumed_qty;
    //     frappe.model.set_value(cdt, cdn, 'remaining_qty', remaining_qty);
    // } else {
    //     frappe.model.set_value(cdt, cdn, 'remaining_qty', 0);
    // }
    if (row.estimated_qty > 0) {
        var remaining = (row.completed / row.estimated_qty) * 100;
        frappe.model.set_value(cdt, cdn, 'remaining', remaining);
    } else {
        frappe.model.set_value(cdt, cdn, 'remaining_percent', 0);
    }
}
