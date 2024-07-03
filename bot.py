import requests

def handle_message(message):
    
    if message.startswith('@test_bot задача'):
        words = message.split(' ')
        
        task_name = ' '.join(words[2:])
        
        response = requests.post('http://localhost/create_task', json={
            'task_name': task_name,
            'project_id': 1,
        })
        
        if response.status_code == 200:
            print('Задача создана: ' + response.json()['task_url'])
            message.reply('Задача "' + task_name + '" создана: ' + response.json()['task_url'])
        else:
            print('Ошибка создания задачи')
            message.reply('Ошибка при создании задачи')