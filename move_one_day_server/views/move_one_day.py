import json
import datetime as dt
import dateutil.parser as pr

from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from integration_utils.bitrix24.models import BitrixUserToken

TASK_ID = 0


@main_auth(on_start=True, set_cookie=True)
def button_view(request):
    global TASK_ID
    TASK_ID = int(json.loads(request.POST['PLACEMENT_OPTIONS'])['taskId'])
    local_task_id = TASK_ID
    return render(request, 'button.html', locals())


@main_auth(on_cookies=True)
def move_one_day(request):
    id_user = request.bitrix_user.bitrix_id
    but = request.bitrix_user_token
    tasks_user_id = but.call_api_method("tasks.task.get", {"taskId": TASK_ID,
                                                           "select":
                                                               ["CREATED_BY"]})
    id_user_created_task = tasks_user_id['result']['task']['createdBy']
    if int(id_user) == int(id_user_created_task):
        date_info = but.call_api_method("tasks.task.get", {"taskId": TASK_ID,
                                                           "select":
                                                               ["DEADLINE"]})
        date_without_parse = date_info['result']['task']['deadline']
        date_parse = pr.parse(date_without_parse)
        true_date = date_parse + dt.timedelta(days=1)
        new_format = true_date.strftime('%d.%m.%Y %H:%M:%S')
        but.call_api_method("tasks.task.update", {"taskId": TASK_ID, "fields":
            {"DEADLINE": str(new_format)}
                                                  })
        return render(request, 'button.html', locals())

    return render(request, 'button.html')


@main_auth(on_cookies=True)
def move_one_hour(request):
    but = request.bitrix_user_token
    date_info = but.call_api_method("tasks.task.get", {"taskId": TASK_ID,
                                                       "select": ["DEADLINE"]})
    date_without_parse = date_info['result']['task']['deadline']
    date_parse = pr.parse(date_without_parse)
    true_date = date_parse + dt.timedelta(hours=1)
    new_format = true_date.strftime('%d.%m.%Y %H:%M:%S')
    but.call_api_method("tasks.task.update", {"taskId": TASK_ID, "fields": {
        "DEADLINE": str(new_format)
    }})
    return render(request, 'button.html', locals())


@main_auth(on_cookies=True)
def move_one_week(request):
    but = request.bitrix_user_token
    date_info = but.call_api_method("tasks.task.get", {"taskId": TASK_ID,
                                                       "select": ["DEADLINE"]})
    date_without_parse = date_info['result']['task']['deadline']
    date_parse = pr.parse(date_without_parse)
    true_date = date_parse + dt.timedelta(weeks=1)
    new_format = true_date.strftime('%d.%m.%Y %H:%M:%S')
    but.call_api_method("tasks.task.update", {"taskId": TASK_ID, "fields": {
        "DEADLINE": str(new_format)
    }})
    return render(request, 'button.html', locals())
