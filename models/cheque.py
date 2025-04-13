from odoo import models, fields, api

class Cheque(models.Model):
    _name = 'cheque.management'
    _description = 'Customer Cheque'

    name = fields.Char(string='Cheque Number', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    amount = fields.Float(string='Amount', required=True)
    issue_date = fields.Date(string='Issue Date', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    state = fields.Selection([
        ('received', 'Received'),
        ('endorsed', 'Endorsed to Supplier'),
        ('deposited', 'Deposited in Bank'),
        ('returned', 'Returned'),
    ], string='Status', default='received')
    note = fields.Text(string='Notes')

    def action_endorse_to_supplier(self):
        self.state = 'endorsed'

    def action_deposit_to_bank(self):
        self.state = 'deposited'

    def action_returned(self):
        self.state = 'returned'
