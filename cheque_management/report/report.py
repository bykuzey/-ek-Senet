from odoo import api, models

class ChequeReport(models.AbstractModel):
    _name = 'report.cheque_management.report_cheque_document'
    _description = 'Cheque Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['cheque.management'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'cheque.management',
            'docs': docs,
        }
