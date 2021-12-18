# -*- coding: utf-8 -*-
# from odoo import http


# class StudentAssignment(http.Controller):
#     @http.route('/student_assignment/student_assignment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_assignment/student_assignment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_assignment.listing', {
#             'root': '/student_assignment/student_assignment',
#             'objects': http.request.env['student_assignment.student_assignment'].search([]),
#         })

#     @http.route('/student_assignment/student_assignment/objects/<model("student_assignment.student_assignment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_assignment.object', {
#             'object': obj
#         })
