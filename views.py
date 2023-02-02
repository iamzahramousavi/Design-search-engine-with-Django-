from django.shortcuts import render
from hazm import stopwords_list
from context.models import *
import json
import os
from .forms import *
import math
import re
import string

OurPunctuation = string.punctuation


def hazfAlaem(some):
    result = some.lower()
    result = re.sub(r'\d+', ' ', result)
    result = re.sub(r'[^\w\s]|\n|_', ' ', result)
    text = ' '.join([word for word in result.split() if word not in stopwords_list()])
    return text


def first(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'esna.json')

    with open(file_path, 'r') as f:
        db = json.load(f)
    for i in range(0, len(db)):
        DataScraped.objects.create(link=db[i]['url'], titleOrg=db[i]['title'], title=hazfAlaem(db[i]['title']),
                                   bodyOrg=db[i]['body'], body=hazfAlaem(db[i]['body']), pubDate=db[i]['pubDate'],
                                   category=db[i]['category'], tags=db[i]['tags'])
        print(i)
    return render(request, 'indext/update.html')


def token(request):
    li = []
    tok = Tokens.objects.all()
    for k in range(0, len(tok)):
        li.append(tok[k].name)
    contexts = DataScraped.objects.all()
    for i in range(0, len(contexts)):
        print(i)
        MyList = [contexts[i].title.split(), contexts[i].body.split()]
        for r in range(0, 2):
            my_dict = {i: MyList[r].count(i) for i in MyList[r]}
            for j in list(my_dict.keys()):
                if j not in li:
                    Tokens.objects.create(name=j,
                                          posting=str(r) + '$' + str(my_dict[j]) + '$' + str(contexts[i].id) + ',')
                    li.append(j)
                else:
                    po = Tokens.objects.filter(name__exact=j)[0].posting
                    po = po + str(r) + '$' + str(my_dict[j]) + '$' + str(contexts[i].id) + ','
                    Tokens.objects.filter(name__exact=j).update(posting=po)


    return render(request, 'indext/update.html')


def home(request):
    form = SearchForm()
    result = 0
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            query = data['search'].split()
            query_tf_idf = tfIdfMaker(query)
            finalList = cosSim(query_tf_idf)
            end = []
            for i in finalList:
                end.append(i[1])

            result = []
            for i in end:
                tm = DataScraped.objects.filter(id__exact=i)
                result += tm

            return render(request, 'indext/results.html', {'result': result, 'query': query, 'query_tf_idf': query_tf_idf})

    return render(request, 'indext/browser.html', {"form": form})


def createIdf(request):
    N = len(DataScraped.objects.all())
    for i in Tokens.objects.all():
        print(i.id)
        docList = i.posting.split(',')[:-1]
        empty = []
        for j in docList:
            empty.append(j.split('$')[-1])
        docFrq = len(set(empty))
        tmp = math.log2(N / docFrq)
        Idf.objects.create(token=i, idf=tmp)

    return render(request, 'indext/update.html')


def createTfIdf(request):
    for document in DataScraped.objects.all():
        print(document.id)
        myFirstRegionList = document.title.split()
        myFirstRegionDict = {
            i: myFirstRegionList.count(i) / len(set(myFirstRegionList)) *
               Idf.objects.filter(token=Tokens.objects.filter(name__exact=i)[0])[0].idf for i in myFirstRegionList}

        mySecondRegionList = document.body.split()
        mySecondRegionDict = {
            i: mySecondRegionList.count(i) / len(set(mySecondRegionList)) *
               Idf.objects.filter(token=Tokens.objects.filter(name__exact=i)[0])[0].idf for i in mySecondRegionList}

        tf_idf = list(myFirstRegionDict.values())
        length = 0
        for i in tf_idf:
            length += i ** 2
        lenFirst = math.sqrt(length)

        tf_idf = list(mySecondRegionDict.values())
        length = 0
        for i in tf_idf:
            length += i ** 2
        lenSecond = math.sqrt(length)

        TfIdfList.objects.create(doc=document, tfIdfFirstList=myFirstRegionDict, tfIdfSecondList=mySecondRegionDict,
                                 lengthFirst=lenFirst, lengthSecond=lenSecond)
    return render(request, 'indext/update.html')

#
# def createTfCRF(request):
#     content = DataScraped.objects.all()
#     for i in Tokens.objects.all()[:10]:
#         print(i.id)
#         docList = i.posting.split(',')[:-1]
#         empty = []
#         for j in docList:
#             empty.append(j.split('$')[-1])
#         docFrq = len(set(empty))
#         print(docFrq)
#
#
#     return render(request, 'indext/update.html')


# def createCategory(request):
#
#     for document in DataScraped.objects.all():
#         print(document.id)
#         cat = Category.objects.filter(name__exact=document.category)
#         if cat.exists():
#             li = cat[0].docList
#             cat.update(docList=li + document.id)
#         else:
#             Category.objects.create(name=document.category, docList=[document.id])
#
#     return render(request, 'indext/update.html')


def navigate(request):
    return render(request, 'indext/navigate.html')


def tfIdfMaker(query):
    tf_idf = {
        i: query.count(i) / len(set(query)) * Idf.objects.filter(token=Tokens.objects.filter(name__exact=i)[0])[
            0].idf for i in query}
    return tf_idf


def cosSim(query_tf_idf):
    length = 0
    for i in list(query_tf_idf.values()):
        length += i ** 2
    queryLength = math.sqrt(length)

    r1 = []
    r2 = []
    for tok in list(query_tf_idf.keys()):
        to = Tokens.objects.filter(name__exact=tok)[0]
        for i in to.posting.split(',')[:-1]:
            region = i.split('$')[0]

            if region == '0':
                r1.append(i.split('$')[-1])

            if region == '1':
                r2.append(i.split('$')[-1])

    tfIdfRegion1 = TfIdfList.objects.filter(doc__id__in=set(r1))
    tfIdfRegion2 = TfIdfList.objects.filter(doc__id__in=set(r2))
    # print('r1',tfIdfRegion1, tfIdfRegion2)

    final_2_region = []
    importance = 2.1
    for region in [tfIdfRegion1, tfIdfRegion2]:
        final = []
        for i in range(0, len(region)):
            qd = 0
            for queryToken in list(query_tf_idf.keys()):

                if queryToken in region[i].tfIdfSecondList.keys():
                    qd += region[i].tfIdfSecondList[queryToken] * query_tf_idf[queryToken]

            cos_sim = qd / (queryLength * region[i].lengthSecond)
            final.append([cos_sim * importance, region[i].doc.id])
        importance = 1
        final_2_region.append(final)

    region1 = final_2_region[0]
    region2 = final_2_region[1]
    for i in range(0, len(region1)):
        for j in range(0, len(region2)):
            if region1[i][1] == region2[j][1]:
                region2[j][0] += region1[i][0]
                break
            else:
                region2.append(region1[i])

    final_sort = sorted(region2, key=lambda l: l[0])
    print(final_sort)
    return reversed(final_sort)
