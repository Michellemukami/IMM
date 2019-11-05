from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse

# Create your views here.


def index(request):
    '''
    view to redirect the user to their specific dashboard
    '''

    # current_user=request.user

    # if current_user.is_superuser==True:

    #     print(current_user.is_superuser,"yeah")
    #     return redirect(tatuAdmin_views.admin_home)

    # elif current_user.profile.is_staff==True and current_user.profile.is_customer==False:
    #     print(current_user.is_superuser,"agent")
    #     return redirect(agent_views.agent_home)

    # else :
    #     tickets=Create_ticket.get_my_tickets(request.user)
    #     return render(request,'customer/index.html',{'tickets':tickets})

    return HttpResponse('heello')
