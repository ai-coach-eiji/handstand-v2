from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title':'姿勢判定アプリ'}
    return render(request, 'pose_estimation/index.html', context)