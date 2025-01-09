from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = "stock.move"

    product_customer_code = fields.Char(compute="_compute_product_customer_code", )

    @api.depends("product_id")
    def _compute_product_customer_code(self):
        for line in self:
            if line.product_id:
                supplierinfo = line.product_id._select_customerinfo(
                    partner=line.picking_id.sale_id.partner_id
                )
                code = supplierinfo.product_code
            else:
                code = ""
            line.product_customer_code = code

# class StockMoveLine(models.Model):
#     _inherit = "stock.move.line"
#
#     def _get_aggregated_product_quantities(self, **kwargs):
#         res = super()._get_aggregated_product_quantities()
#         print("===========res==========",res)
#         return res