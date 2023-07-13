function myFunction() {
  let task_id = document.getElementById("myButton").value;
  BX24.callMethod("tasks.task.get", {'taskId': task_id, 'fields': ["DEADLINE"]}, function (res){
    let deadline = dayjs(res.answer.result.task['deadline']).add(1, 'hour').format('DD.MM.YYYY HH:mm');
    BX24.callMethod("tasks.task.update", {'taskId': task_id, 'fields': {"DEADLINE": deadline.toString()}});
  })
}
