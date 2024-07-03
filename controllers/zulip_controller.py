import logging
import zulip
from odoo import http
from odoo.http import request
import json

_logger = logging.getLogger(__name__)

class ZulipController(http.Controller):

    @http.route('/create_task', type='json', auth="user", methods=['POST'])
    def create_task(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            task_name = data.get('data').split('\n')[-1]
            project_channel = data.get('message').get('display_recipient')

            if not task_name or not project_channel:
                raise ValueError("Invalid input data")

            project = request.env['project.project'].search([('channel_name', '=', project_channel)], limit=1)

            if project:
                task = request.env['project.task'].create({
                    'name': task_name,
                    'project_id': project.id,
                })

                response = {
                    'task_id': task.id,
                    'task_url': request.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/web#id=' + str(task.id) + '&view_type=form&model=project.task',
                }

                message_content = f"Задача [{task_name}]({response['task_url']}) создана"
                return {
                    "content": message_content
                }
            else:
                message_content = "Проект не найден"
                return {
                    "content": message_content
                }

        except ValueError as e:
            _logger.error("Error creating task: %s", str(e))
            return {
                "content": "Произошла ошибка при создании задачи. Пожалуйста, проверьте входные данные."
            }
        except Exception as e:
            _logger.error("Unexpected error: %s", str(e))
            return {
                "content": "Произошла непредвиденная ошибка при создании задачи. Пожалуйста, попробуйте еще раз позже."
            }