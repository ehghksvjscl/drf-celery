from django.http import HttpResponse

from works.tasks import task_process_work

def process_work(request):
    task_process_work.delay()
    return HttpResponse('done')
