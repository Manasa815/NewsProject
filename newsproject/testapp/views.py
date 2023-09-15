from django.shortcuts import render
def indexview(request):
    return render(request,'testapp/index.html')
def movies_view(request):
    head_mssg='movies information'
    sub_mssg1='sid and kaira marriage'
    sub_mssg2='ranbir and alia marriage'
    sub_mssg3='virat and anushka marriage'
    my_dict={'head_mssg':head_mssg,'sub_mssg1':sub_mssg1,'sub_mssg2':sub_mssg2,'sub_mssg3':sub_mssg3}
    return render(request,"testapp/demo.html",my_dict)
def sports_view(request):
    head_mssg='Sports information'
    sub_mssg1='IPL match'
    sub_mssg2='world cup match'
    sub_mssg3='T20 matches'
    my_dict={'head_mssg':head_mssg,'sub_mssg1':sub_mssg1,'sub_mssg2':sub_mssg2,'sub_mssg3':sub_mssg3}
    return render(request,"testapp/demo.html",my_dict)

# Create your views here.
