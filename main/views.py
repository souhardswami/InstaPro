from django.shortcuts import render

from django.http import request,HttpResponse

from .models import Photos,Users,Like,Comment



# Create your views here.

from django.db import connection

def home(request):



    

    sql='''                \
            select comment_text,user_id \
            from main_comment \
            cross join main_users \
        '''


    # sql='''
    #     create view main_entity as
    # select id, name from main_users   \

    
   
    # sql='''select name from sqlite_master \
    #     where type='view' \
    #     '''
    
    

    with connection.cursor() as cursor:
        
        cursor.execute(sql)
    
        
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        



    # iam='bob'

    # users=Users.objects.raw('SELECT  FROM main_users')

    # print(users.name)

    # sql='''
    #     SELECT *
    #     FROM main_users
    #     -- where username='bob123'
        
    #     limit 2
    #     '''

    # p=Users.objects.raw(sql)
    # for i in p:
    #     print(i.username)    
    #     print(i.name)    


    # for i in users:
    #     print(i.image_id)
    
    photos=Photos.objects.filter(users__id=1)
    

    
    
    for photo in photos:
        like_count=Like.objects.filter(photo_id=photo.id)
        # print(like_count.query)

        
        photo.count=len(like_count)

        comment=Comment.objects.filter(photo_id=photo.id)
        # print(comment.query)

        

        
           
        ll=[]
        for i in comment:
            d={
                "text":'',
                "user":""

            }
            d['text']=i.comment_text
            d['user']=i.user_id
            ll.append(d)
         

        photo.comments=ll


        

    # print(photos)



    # like=Like.objects.get(id=1)
    # print(like.photo_id)






    
    context={

        

        "cont":photos

        }


    


    return render(request,'main.html',context)