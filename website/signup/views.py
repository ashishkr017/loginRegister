from django.shortcuts import render
import mysql.connector as sql
fn=""
ln=""
s=""
em=""
pwd=""
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if(request.method=="POST"):
        m=sql.connect(host="localhost",user="root",passwd="Ashiucristo@1",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First":
                fn=value
            if key=="Last":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        try:
            c="insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
            cursor.execute(c)
            m.commit()
            t=tuple(cursor.fetchall())
        except:
            return render(request,"userexist.html")
        if(t==()):
            return render(request,'welcome.html')
        else:
            return render(request,"error.html")
    #return render(request,'update.html')
    return render(request,'signup_page.html')
