from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from qldt_app.models import nguoiDung, giaoVien, monHoc, lop

def nhanvien_home(request):
    return render(request,"nhanvien_templates/home.html") 

def themGiaoVien(request):
    return render(request,"nhanvien_templates/themGiaoVien.html")

def luuGiaoVien(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        hovaten=request.POST.get("hovaten")
        username=request.POST.get('username')
        ngaysinh=request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        cccd=request.POST.get("cccd")
        email=request.POST.get("email")
        password=request.POST.get("password")
        sdt=request.POST.get("sdt")
        ngaybatdau=request.POST.get("ngaybatdau")
        tenmonhoc=request.POST.get("tenmonhoc")
        tenlop=request.POST.get("tenlop")
        
        try:
            giaovienmoi=nguoiDung.objects.create_user(hovaten=hovaten, username=username, ngaysinh=ngaysinh, gioitinh=gioitinh, diachi=diachi, cccd=cccd, email=email, password=password, sdt=sdt, ngaybatdau=ngaybatdau, user_type = 3)
            monhoc_obj=monHoc.objects.get(tenmonhoc=tenmonhoc)
            giaovienmoi.giaovien.mamonhoc=monhoc_obj
            lop_obj=lop.objects.get(tenlop=tenlop)
            giaovienmoi.giaovien.malop=lop_obj
            giaovienmoi.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/NVthemGiaoVien")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/NVthemGiaoVien")   
        
def quanlyGiaoVien(request):
    giaovien=giaoVien.objects.all()
    return render(request, 'nhanvien_templates/quanlyGiaoVien.html', {'giaovien':giaovien})  

def chinhsuaGiaoVien(request, mand):
    giaovien=giaoVien.objects.get(admin=mand)
    return render(request, 'nhanvien_templates/chinhsuaGiaoVien.html', {'giaovien':giaovien, 'mand':mand})
    
def luuchinhsuaGiaoVien(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mand=request.POST.get("mand")
        hovaten=request.POST.get('hovaten')
        username=request.POST.get('username')
        # ngaysinh=request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        cccd=request.POST.get("cccd")
        email=request.POST.get("email")
        password=request.POST.get("password")
        sdt=request.POST.get("sdt")
        # ngaybatdau=request.POST.get("ngaybatdau")
        tenlop=request.POST.get("tenlop")
        tenmonhoc=request.POST.get("tenmonhoc")

        try:
            nguoidung=nguoiDung.objects.get(mand=mand)
            nguoidung.hovaten=hovaten
            nguoidung.username=username
            # nguoidung.ngaysinh=ngaysinh
            nguoidung.gioitinh=gioitinh
            nguoidung.diachi=diachi
            nguoidung.cccd=cccd
            nguoidung.email=email
            nguoidung.password=password
            nguoidung.sdt=sdt
            # nguoidung.ngaybatdau=ngaybatdau
            nguoidung.save()
            
            monhoc_obj=monHoc.objects.get(tenmonhoc=tenmonhoc)
            lop_obj=lop.objects.get(tenlop=tenlop)
            giaovien_model=giaoVien.objects.get(admin_id=mand)
            giaovien_model.mamonhoc=monhoc_obj
            giaovien_model.malop=lop_obj
            giaovien_model.save()

            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect("/NVchinhsuaGiaoVien/" + str(nguoidung.mand))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect("/NVchinhsuaGiaoVien/" + str(nguoidung.mand))
        
def xoaGiaoVien(request, mand):
    giaovien=giaoVien.objects.get(admin=mand)
    return render(request, 'nhanvien_templates/xoaGiaoVien.html', {'giaovien':giaovien, 'mand':mand})
        
def luuXoaGiaoVien(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mand=request.POST.get("mand")
        try:
            nguoidung=nguoiDung.objects.get(mand=mand)
            nguoidung.delete()
            return HttpResponseRedirect("/NVquanlyGiaoVien")
        except:
            return HttpResponseRedirect("/NVquanlyGiaoVien")                
        
        
def themLop(request):
    return render(request,"nhanvien_templates/themLop.html")

def luuLop(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        tenlop=request.POST.get("tenlop")
        
        try:
            lopmoi=lop.objects.create(tenlop=tenlop)
            lopmoi.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/NVthemLop")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/NVthemLop")   
        
def quanlyLop(request):
    v_lop=lop.objects.all()
    return render(request, 'nhanvien_templates/quanlyLop.html', {'v_lop':v_lop})  

def chinhsuaLop(request, malop):
    v_lop=lop.objects.get(malop=malop)
    return render(request, 'nhanvien_templates/chinhsuaLop.html', {'v_lop':v_lop, 'malop':malop})
    
def luuchinhsuaLop(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        malop=request.POST.get("malop")
        tenlop=request.POST.get("tenlop")

        try:
            v_lop=lop.objects.get(malop=malop)
            v_lop.tenlop=tenlop
            v_lop.save()

            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect("/NVchinhsuaLop/" + str(v_lop.malop))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect("/NVchinhsuaLop/" + str(v_lop.malop))
        
def xoaLop(request, malop):
    v_lop=lop.objects.get(malop=malop)
    return render(request, 'nhanvien_templates/xoaLop.html', {'v_lop':v_lop, 'malop':malop})
        
def luuXoaLop(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        malop=request.POST.get("malop")
        try:
            v_lop=lop.objects.get(malop=malop)
            v_lop.delete()
            return HttpResponseRedirect("/NVquanlyLop")
        except:
            return HttpResponseRedirect("/NVquanlyLop")
