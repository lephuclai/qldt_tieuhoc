from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from qldt_app.models import hocSinh, diem, lop

def giaovien_home(request):
    return render(request,"giaovien_templates/home.html") 
    
def themHocSinh(request):
    return render(request,"giaovien_templates/themHocSinh.html")

def luuHocSinh(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        hovaten=request.POST.get("hovaten")
        ngaysinh=request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        tenlop=request.POST.get("tenlop")
        tenbo=request.POST.get("tenbo")
        sdtbo=request.POST.get("sdtbo")
        emailbo=request.POST.get("emailbo")
        tenme=request.POST.get("tenme")
        sdtme=request.POST.get("sdtme")
        emailme=request.POST.get("emailme")
        
        try:
            hocsinhmoi=hocSinh.objects.create(
                hovaten=hovaten,
                ngaysinh=ngaysinh,
                gioitinh=gioitinh,
                diachi=diachi,
                tenbo=tenbo,
                sdtbo=sdtbo,
                emailbo=emailbo,
                tenme=tenme,
                sdtme=sdtme,
                emailme=emailme,
            )
            
            lop_obj=lop.objects.get(tenlop=tenlop)
            hocsinhmoi.malop=lop_obj
            hocsinhmoi.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/themHocSinh")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/themHocSinh")    

def quanlyHocSinh(request):
    hocsinh=hocSinh.objects.all()
    return render(request, 'giaovien_templates/quanlyHocSinh.html', {'hocsinh':hocsinh})  

def chinhsuaHocSinh(request, mahs):
    hocsinh=hocSinh.objects.get(mahs=mahs)
    return render(request, 'giaovien_templates/chinhsuaHocSinh.html', {'hocsinh':hocsinh, 'mahs':mahs})
    
def luuchinhsuaHocSinh(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mahs=request.POST.get("mahs")
        hovaten=request.POST.get("hovaten")
        # ngaysinh=request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        tenbo=request.POST.get("tenbo")
        sdtbo=request.POST.get("sdtbo")
        emailbo=request.POST.get("emailbo")
        tenme=request.POST.get("tenme")
        sdtme=request.POST.get("sdtme")
        emailme=request.POST.get("emailme")

        try:
            hocsinh=hocSinh.objects.get(mahs=mahs)
            hocsinh.hovaten=hovaten
            hocsinh.gioitinh=gioitinh
            hocsinh.diachi=diachi
            hocsinh.tenbo=tenbo
            hocsinh.sdtbo=sdtbo
            hocsinh.emailbo=emailbo
            hocsinh.tenme=tenme
            hocsinh.sdtme=sdtme
            hocsinh.emailme=emailme
            hocsinh.save()

            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect("/chinhsuaHocSinh/" + str(hocsinh.mahs))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect("/chinhsuaHocSinh/" + str(hocsinh.mahs))
        
def xoaHocSinh(request, mahs):
    hocsinh=hocSinh.objects.get(mahs=mahs)
    return render(request, 'giaovien_templates/xoaHocSinh.html', {'hocsinh':hocsinh, 'mahs':mahs})
        
def luuXoaHocSinh(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mahs=request.POST.get('mahs')
        try:
            hocsinh=hocSinh.objects.get(mahs=mahs)
            hocsinh.delete()
            return HttpResponseRedirect("/quanlyHocSinh")
        except:
            return HttpResponseRedirect("/quanlyHocSinh")     