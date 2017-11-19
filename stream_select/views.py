import matplotlib
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import matplotlib.pyplot as plt
import numpy as np
from django.core.urlresolvers import reverse

op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11, op12, op13, op14, op15, op16, op17 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
streams = ['mechanical', 'civil', 'electrical', 'electronics', 'computer', 'software']
val = [int(0)] * 6

def HomeView(request):
    template = 'stream_select/home.html'
    context = {}
    
    return render(request, template, context)

def QuestionView(request):
    global op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11, op12, op13, op14, op15, op16, op17
    context = {}
    template = 'stream_select/ques.html'
    if request.method == "POST":
        if request.POST.get('opt1') != None:
            op1 = request.POST.get('opt1')
        if request.POST.get('opt2') != None:
            op2 = request.POST.get('opt2')
        if request.POST.get('opt3') != None:
            op3 = request.POST.get('opt3')
        if request.POST.get('opt4') != None:
            op4 = request.POST.get('opt4')
        if request.POST.get('opt5') != None:
            op5 = request.POST.get('opt5')
        if request.POST.get('opt6') != None:
            op6 = request.POST.get('opt6')
        if request.POST.get('opt7') != None:
            op7 = request.POST.get('opt7')
        if request.POST.get('opt8') != None:
            op8 = request.POST.get('opt8')
        if request.POST.get('opt9') != None:
            op9 = request.POST.get('opt9')
        if request.POST.get('opt10') != None:
            op10 = request.POST.get('opt10')
        if request.POST.get('opt11') != None:
            op11 = request.POST.get('opt11')
        if request.POST.get('opt12') != None:
            op12 = request.POST.get('opt12')
        if request.POST.get('opt13') != None:
            op13 = request.POST.get('opt13')
        if request.POST.get('opt14') != None:
            op14 = request.POST.get('opt14')
        if request.POST.get('opt15') != None:
            op15 = request.POST.get('opt15')
        if request.POST.get('opt16') != None:
            op16 = request.POST.get('opt16')
        if request.POST.get('opt17') != None:
            op17 = request.POST.get('opt17')
        print(op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11, op12, op13, op14, op15, op16, op17)
        return redirect(reverse('stream_select:result'))

    return render(request, template, context)

def calc(request):
    global op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11, op12, op13, op14, op15, op16, op17, streams, val

    val[5] = (int(op1)*20) + (int(op2)*50) + (int(op3)*30)
    val[4] = (int(op3)*30) + (int(op4)*20) + (int(op5)*30) + (int(op7)*20)
    val[3] = (int(op6)*40) + (int(op7)*40) + (int(op8)*20)
    val[2] = (int(op8)*20) + (int(op9)*40) + (int(op10)*40)
    val[0] = (int(op11)*20) + (int(op12)*30) + (int(op13)*20) + (int(op17)*30)
    val[1] = (int(op14)*20) + (int(op15)*40) + (int(op16)*40)

    template = 'stream_select/result.html'
    context = {'mechanical': val[0], 'civil': val[1],
               'electrical': val[2], 'electronics': val[3],
               'computer' : val[4], 'software':val[5]
               }
    print(context)
    y_bos = np.arange(len(streams))
    plt.bar(y_bos, val, align='center', alpha = 0.5)
    plt.xticks(y_bos, streams)
    plt.ylabel('Usage')
    plt.title('Result')

    plt.savefig('stream_select/static/stream_select/graph.png')
    return render(request, template, context)

