import postgresql
from django.http import HttpResponse
from django.shortcuts import render

def first(request):
#    return HttpResponse('This is first page')
    return render(request,'first.html')

def second(request):
    date_from = request.GET['dfrom']
    date_to = request.GET['dto']
    fyear = date_from[0:4]
    fmonth = date_from[5:7]
    fday = date_from[8:10]
    fhour = date_from[11:13]
    fminute = date_from[14:16]
    fsec = '0'+'0'

    dyear = date_to[0:4]
    dmonth = date_to[5:7]
    dday = date_to[8:10]
    dhour = date_to[11:13]
    dminute = date_to[14:16]
    dsec = '0'+'0'

    final_date_from = fyear+'-'+fmonth+'-'+fday+' '+fhour+':'+fminute+':'+fsec
    final_date_to = dyear+'-'+dmonth+'-'+dday+' '+dhour+':'+dminute+':'+dsec
    print(f"Время {final_date_from}")
    print(f"Время {final_date_to}")
    pgdb = postgresql.open('pq://centrum:DY5YfYkrF7@10.0.89.12:5432/centrum')
    print('connect to centrum db')
    sql = "select source_camera_event_id from its_passage_event \
     where passage_date between '" + final_date_from + "' and '" + final_date_to + "' \
     and hcm_id in (select id from its_hcm h where h.road_id in (1,2,3,4,5,6,7,8));"
    pgrs = pgdb.query(sql)
    print(pgrs)
    print("#TOTALY events ", len(pgrs))

    pgdb.close()
    return render(request,'second.html',{'datefrom':final_date_from,'dateto':final_date_to,'events':len(pgrs)})

