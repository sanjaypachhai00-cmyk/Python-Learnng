# from django.shortcuts import render
# def home(request):
#     context={
#         'name':'Messi',
#         'age': 23,
#         'course':'Computer Engineering',
#         'year':2024,
#         'parent_name':'sundar_pachhai',
#   }
#     return render(request,'home.html',context)


# from django.shortcuts import render
# def home(request):
#     context={
#         'name':'sanjay',
#         'age':15
#     }  
#     return render(request,'home.html',context)

from django.shortcuts import render

def home(request):
    subjects=[
        'AI',
        'SE',
        'DSAP',
        'PS',
        'EM',
        'ES'

    ]
    context={
    'subjects':subjects
}
    return render(request,'home.html',context)