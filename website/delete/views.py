from django.shortcuts import render
import mysql.connector as sql

em=""

pwd=""
# Create your views here.
def deleteaction(request):
    global em,newpwd
    if(request.method=="POST"):
        m=sql.connect(host="localhost",user="root",passwd="Ashiucristo@1",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            
            if key=="email":
                em=value
            if key=="password":
                pwd=value
           
        c="Delete from users  where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        m.commit()
        t=tuple(cursor.fetchall())
        if(t==()):
            return render(request,'deletesucessfull.html')
        else:
            return render(request,"error.html")
    #return render(request,'update.html')
    #return render(request,'signup_page.html')
    return render(request,'delete.html')