import base64
from odoo import models, fields, api
import io
import xlsxwriter

class GeneralLedgerWizard(models.TransientModel):
    _name = 'general.ledger.wizard'
    _description = 'General Ledger Report Wizard'

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    journal_id = fields.Many2one('account.journal', string='Journal')
    analytic_account_id = fields.Many2many('account.analytic.account', string='Analytic')
    

    def _get_general_ledger_data(self):
        domain = []
        
        if self.date_from:
            domain.append(('date', '>=', self.date_from))
        if self.date_to:
            domain.append(('date', '<=', self.date_to))
        if self.journal_id:
            domain.append(('journal_id', '=', self.journal_id.id))
        
        if self.analytic_account_id:
            domain.append(('analytic_line_ids.account_id', '=', self.analytic_account_id.id))
            
        return self.env['account.move.line'].search(domain)

    def generate_report(self):
        data = self._get_general_ledger_data()

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Analytic General Ledger Report')

        # Write date range filter
        date_range_format = workbook.add_format({'bold': True, 'align': 'left'})
        date_range_label = "Date Range Filter: from: {} to: {}".format(
            self.date_from.strftime('%Y-%m-%d') if self.date_from else "N/A",
            self.date_to.strftime('%Y-%m-%d') if self.date_to else "N/A"
        )
        worksheet.write(0, 0, date_range_label, date_range_format)

        # Skip a row for better visual separation
        row = 1

        # Write header row
        header_format = workbook.add_format({'bold': True, 'align': 'center'})
        header_row = ['Date', 'Journal', 'Account', 'Analytic', 'Debit', 'Credit']
        for col, label in enumerate(header_row):
            worksheet.write(row, col, label, header_format)

        # Write data rows
        row = 2
        for entry in data:
                worksheet.write(row, 0, entry.date.strftime('%Y-%m-%d'))
                
                # Write the journal name or a blank cell if no journal
                journal_name = entry.journal_id.name if entry.journal_id else ""
                worksheet.write(row, 1, journal_name)
                
                # Write the account name or a blank cell if no account
                account_name = entry.account_id.display_name if entry.account_id else ""
        
                # Check if the account is a receivable or payable account
                account_type = False
                if entry.partner_id:
                    partner = entry.partner_id
                    if partner.property_account_receivable_id.id == entry.account_id.id:
                        account_type = 'receivable'
                    elif partner.property_account_payable_id.id == entry.account_id.id:
                        account_type = 'payable'
                
                if account_type:
                    worksheet.write(row, 2, account_name)
                else:
                    worksheet.write(row, 2, "")  # Empty cell for non-receivable/payable accounts
                

                if entry.analytic_line_ids:
                    # Assuming you want to write the first analytic line's account_id as a string
                    analytic_account = entry.analytic_line_ids[0].account_id.display_name
                    worksheet.write(row, 3, analytic_account)
                else:
                    worksheet.write(row, 3, "")  # Empty cell if no analytic line
                    
                # Write the debit amount or a blank cell if no debit
                worksheet.write(row, 4, entry.debit if entry.debit is not None else 0)
                
                # Write the credit amount or a blank cell if no credit
                worksheet.write(row, 5, entry.credit if entry.credit is not None else 0)
                
                row += 1

 
        workbook.close()
        output.seek(0)

        # Encode the XLSX data as base64
        base64_data = base64.b64encode(output.read())

        # Create an attachment and associate it with the wizard
        attachment = self.env['ir.attachment'].create({
            'name': 'Analytic General_Ledger_Report.xlsx',
            'type': 'binary',
            'datas': base64_data,
            'res_model': self._name,
            'res_id': self.id,
        })

        # Return an action to display the attachment
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'self',
        }
