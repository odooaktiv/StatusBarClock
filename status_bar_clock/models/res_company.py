# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class ResCompany(models.Model):
    """Added the new field."""

    _inherit = 'res.company'

    clock_format = fields.Char(
        string="Clock Format", default="%m/%d/%Y %H:%M:%S")
