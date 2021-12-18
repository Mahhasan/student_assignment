# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assignment(models.Model):
    _name = 'assignment'
    _description = 'Assignment Table'

    name = fields.Char(string="Assignment Title")
    deadline = fields.Char(string="Deadline")
    description = fields.Char(string="Description")
    assign_to = fields.Char(string="Assign To")