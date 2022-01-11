from django.http import HttpResponse
from django.shortcuts import render
from .models import houses,boss



def index(request):

    housesList = list(houses.objects.all())
    firstBoss = list(boss.objects.all())

    print(housesList[0].housename)
    print(firstBoss[0].name)

    context = {'housesList': housesList}
               # 'firstBoss': firstBoss}
    # get_data = Data()
    # Instances = get_data.get_instance_count()
    # Jobs = get_data.get_jobs_count()
    # Tasks = get_data.get_task_count()
    # JobList = get_data.get_jobs()
    # InstancesList = get_data.get_instances()
    # TaskList = get_data.get_tasks()
    #
    # After_Week = datetime.date.today() + relativedelta(weeks=1)
    # Now = datetime.date.today()
    #
    # context = {'segment': 'index',
    #            'Instances': Instances,
    #            'Jobs': Jobs,
    #            'Tasks': Tasks,
    #            'JobList': JobList,
    #            'InstancesList': InstancesList,
    #            'TaskList': TaskList,
    #            'After_Week': After_Week,
    #            'Now': Now}

    # html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    return HttpResponse("hello")


