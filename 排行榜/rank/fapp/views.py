from rest_framework.response import Response
from rest_framework import views
import json,redis
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rank import settings

pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                            db=settings.REDIS_DATA_DB,decode_responses=True)


# Create your views here.



class Rank(views.APIView):

    def get(self, request):
        user = request.GET.get('user')
        start = request.GET.get('start',None)
        end = request.GET.get('end',None)
        if start == None:
            start = 0
        else:
            start = int(start)-1
        if end ==None:
            end = -1
        else:
            end = int(end)-1
        r = redis.Redis(connection_pool=pool)
        rank_list = r.zrange('rank', start, end, withscores=True,desc=True)
        rank_list_2 = []
        for i in rank_list:
            element = {}
            element['user_name'] = i[0]
            element['user_rank'] = start+1
            start+=1
            element['user_score'] = i[1]
            rank_list_2.append(element)
        user_rank = r.zrevrank('rank',user)+1
        user_score = r.zscore('rank',user)
        user_info = {'user_name':user,'user_rank':user_rank,'user_score':user_score}
        return JsonResponse({'status': True, 'info':rank_list_2,'current_user':user_info})
    def post(self,request):
        json_result = request.POST.dict()
        score = float(json_result['score'])
        if score<1 or score>10000000:
            return_json = {'status': False, 'msg': '上传失败'}
            return HttpResponse(json.dumps(return_json), content_type='application/json')
        r = redis.Redis(connection_pool=pool)
        res = r.zadd('rank',json_result['name'],score)
        if res == True:
            return_json = {'status': True, 'msg': '上传成功'}
        else:
            return_json = {'status': False, 'msg': '上传失败'}
        return HttpResponse(json.dumps(return_json), content_type='application/json')
