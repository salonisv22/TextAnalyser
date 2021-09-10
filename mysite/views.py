from django.http import HttpResponse
from django.shortcuts import render


def analyser(request):
    data = request.POST.get('text','default')
    remove_punc = request.POST.get('removePunc','off')
    remove_extra_space = request.POST.get('removeExtraSpace','off')
    covert_to_upper = request.POST.get('convertToUpper','off')
    result=""
    method=""
    punctuations='''!"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~'''
    if remove_punc=='on':
        method += 'remove punctuations '
        for char in data:
            if char not in punctuations:
                result+=char
        data = result

    if remove_extra_space=='on':
        method+= "remove spaces "
        i=0
        for i in range(len(data)-1):
            if not (data[i]==' ' and data[i]==data[i+1]):
                result+=data[i]
        if i+1<len(data):
            result+=data[i+1]
        data = result

    if covert_to_upper=='on':
        method+="convert to upper"
        result = result.upper()
        data = result

    params = {'method':method,'result':result}
    return render(request,'analysed.html',params)


def getPage1(request):
    params = {'name':'harry','place':'mars'}
    return render(request,'page1.html',params)
