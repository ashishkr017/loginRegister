from django.shortcuts import render
import mysql.connector as sql


em=""
newpwd=""
pwd=""
# Create your views here.
def updateaction(request):
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
            if key=="new password":
                newpwd=value
        c="update users set password='{}' where email='{}'".format(newpwd,em)   
        cursor.execute(c)
        m.commit()
        t=tuple(cursor.fetchall())
        if(t==()):
            return render(request,'sucessfull.html')
        else:
            return render(request,"error.html")
    return render(request,'update.html')
    

         
# def update_db_data(request):
#    # conn = MySQLdb.connect(host= "localhost", user="test_user", passwd="test_pwd",db="myproject")
#     conn=sql.connect(host="localhost",user="root",passwd="Ashiucristo@1",database='website')
#     cursor = conn.cursor()
#     try:
#         cursor.execute("UPDATE user SET user_name = 'test'")
#         print("sucess")
#         html = "<html><body>sucess</body></html>"
#         conn.commit()
#     except:
#         print("fail")
#         html = "<html><body>fail</body></html>"
#         conn.rollback()
#     conn.close()
#     return HttpResponse(html)