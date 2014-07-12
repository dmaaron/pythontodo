from django.shortcuts import render
from todolist.models import Task
from twilio.rest import TwilioRestClient
from django.conf import settings

# Create your views here.
def tasks(request):
    template_name='tasks.html'
    tasks=Task.objects.all()
    context={'tasks':tasks}
    if request.method == 'POST':
        task_description = request.POST.get('task')
        Task.objects.create(description=task_description)
        with open('{}/todolist/digits.txt'.format(settings.BASE_DIR), 'r') as phone_number_file:
            phone_number = phone_number_file.readlines()[0]
        account_SID='AC29a92553fae2bfdf83a2ec5e09bfec87'
        auth_token='a437cf3cf441bd04cfbb31ef858f03bf'
        client=TwilioRestClient(account_SID,auth_token)
        client.messages.create(body="Congrats, you added the following task: {}".format(task_description),
            to=phone_number,
            from_="+16467627640" )       
    return render(request, template_name, context)
