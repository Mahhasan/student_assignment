# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'Student Table'

    name = fields.Char(string="Student Name")
    email = fields.Char(string="Email")
    department = fields.Char(string="Department")
    phone = fields.Char(string="Phone")