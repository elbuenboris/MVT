from multiprocessing import context
from django.shortcuts import render
from family.models import Members

def create_member(request):
    new_member = Members.objects.create(name = 'Rene', last_name = 'Aceves', age = 24, gender = 'male', height = '1,78m')
    context = {
        'new_member':new_member
    }
    return render(request, 'new_member.html', context=context)

def members_list(request):
    members = Members.objects.all()
    context = {
        'members':members
    }
    return render(request, 'members_list.html', context=context)