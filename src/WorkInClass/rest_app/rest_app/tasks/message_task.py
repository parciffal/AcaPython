from ..celery import app
from ..tools.email_tools import my_send_email

@app.task()
def mail_task(data):
    verify_data = {}
    verify_data['subject'] = 'Activate your account'
    verify_data['message'] = 'Here is your activate code\n{}'\
                                .format(data['activate_code'])
    verify_data['to'] = [data['to']]
    my_send_email(verify_data)
