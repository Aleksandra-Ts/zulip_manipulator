from odoo import http
from odoo.http import request

class ZulipController(http.Controller):

    @http.route('/create_task', type='json', auth="public", methods=['POST'])
    def create_task(self, **kwargs):
        
        task_name = kwargs.get('task_name')
        project_id = kwargs.get('project_id')
        
        task = request.env['project.task'].create({
            'name': task_name,
            'project_id': project_id,
        })
        response = {
            'task_id': task.id,
            'task_url': request.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/web#id=' + str(task.id) + '&view_type=form&model=project.task',
        }
        return response
