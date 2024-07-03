from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    channel_name = fields.Char(string='Channel name')

