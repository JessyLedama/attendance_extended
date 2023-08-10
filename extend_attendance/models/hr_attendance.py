# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HRAttendance(models.TransientModel):
    _inherit = 'hr.attendance'

    employee_number = fields.Char(related='hr.employee.x_employee_number', string='Employee Number', store=True)
