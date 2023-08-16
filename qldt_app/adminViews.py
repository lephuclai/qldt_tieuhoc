from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from qldt_app.models import nguoiDung, nhanVien, giaoVien, monHoc, lop

def admin_home(request):
    return render(request,"admin_templates/home.html")

def themNhanVien(request):
    return render(request,"admin_templates/themNhanVien.html")

def luuNhanVien(request):
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
        vitri=request.POST.get("vitri")
        
        try:
            nhanvienmoi=nguoiDung.objects.create_user(hovaten=hovaten, username=username, ngaysinh=ngaysinh, gioitinh=gioitinh, diachi=diachi, cccd=cccd, email=email, password=password, sdt=sdt, ngaybatdau=ngaybatdau, user_type = 2)
            nhanvienmoi.nhanvien.vitri=vitri
            nhanvienmoi.save()
            messages.success(request,"Thêm nhân viên thành công")
            return HttpResponseRedirect("/themNhanVien")
        except:
            messages.error(request,"Thêm nhân viên không thành công")
            return HttpResponseRedirect("/themNhanVien")   
        
def quanlyNhanVien(request):
    nhanvien=nhanVien.objects.all()
    return render(request, 'admin_templates/quanlyNhanVien.html', {'nhanvien':nhanvien})  

def chinhsuaNhanVien(request, mand):
    nhanvien=nhanVien.objects.get(admin=mand)
    return render(request, 'admin_templates/chinhsuaNhanVien.html', {'nhanvien':nhanvien, 'mand':mand})
    
def luuchinhsuaNhanVien(request):
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
        vitri=request.POST.get("vitri")

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
            
            nhanvien_model=nhanVien.objects.get(admin_id=mand)
            nhanvien_model.vitri=vitri
            nhanvien_model.save()

            messages.success(request,"Chỉnh sửa nhân viên thành công")
            return HttpResponseRedirect("/chinhsuaNhanVien/" + str(nguoidung.mand))
        except:
            messages.error(request,"Chỉnh sửa nhân viên không thành công")
            return HttpResponseRedirect("/chinhsuaNhanVien/" + str(nguoidung.mand))
        
def xoaNhanVien(request, mand):
    nhanvien=nhanVien.objects.get(admin=mand)
    return render(request, 'admin_templates/xoaNhanVien.html', {'nhanvien':nhanvien, 'mand':mand})
        
def luuXoaNhanVien(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mand=request.POST.get("mand")
        try:
            nguoidung=nguoiDung.objects.get(mand=mand)
            nguoidung.delete()
            return HttpResponseRedirect("/quanlyNhanVien")
        except:
            return HttpResponseRedirect("/quanlyNhanVien")    
    

def themGiaoVien(request):
    return render(request,"admin_templates/themGiaoVien.html")

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
            messages.success(request,"Thêm giáo viên thành công")
            return HttpResponseRedirect("/themGiaoVien")
        except:
            messages.error(request,"Thêm giáo viên không thành công")
            return HttpResponseRedirect("/themGiaoVien")   
        
def quanlyGiaoVien(request):
    giaovien=giaoVien.objects.all()
    return render(request, 'admin_templates/quanlyGiaoVien.html', {'giaovien':giaovien})  

def chinhsuaGiaoVien(request, mand):
    giaovien=giaoVien.objects.get(admin=mand)
    return render(request, 'admin_templates/chinhsuaGiaoVien.html', {'giaovien':giaovien, 'mand':mand})
    
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

            messages.success(request,"Chỉnh sửa giáo viên thành công")
            return HttpResponseRedirect("/chinhsuaGiaoVien/" + str(nguoidung.mand))
        except:
            messages.error(request,"Chỉnh sửa giáo viên không thành công")
            return HttpResponseRedirect("/chinhsuaGiaoVien/" + str(nguoidung.mand))
        
def xoaGiaoVien(request, mand):
    giaovien=giaoVien.objects.get(admin=mand)
    return render(request, 'admin_templates/xoaGiaoVien.html', {'giaovien':giaovien, 'mand':mand})
        
def luuXoaGiaoVien(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mand=request.POST.get("mand")
        try:
            nguoidung=nguoiDung.objects.get(mand=mand)
            nguoidung.delete()
            return HttpResponseRedirect("/quanlyGiaoVien")
        except:
            return HttpResponseRedirect("/quanlyGiaoVien")                
        

def themMonHoc(request):
    return render(request,"admin_templates/themMonHoc.html")

def luuMonHoc(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        tenmonhoc=request.POST.get("tenmonhoc")
        sotiet=request.POST.get("sotiet")
        
        try:
            monhocmoi=monHoc.objects.create(tenmonhoc=tenmonhoc, sotiet=sotiet)
            monhocmoi.save()
            messages.success(request,"Thêm môn học thành công")
            return HttpResponseRedirect("/themMonHoc")
        except:
            messages.error(request,"Thêm môn học không thành công")
            return HttpResponseRedirect("/themMonHoc")   
        
def quanlyMonHoc(request):
    monhoc=monHoc.objects.all()
    return render(request, 'admin_templates/quanlyMonHoc.html', {'monhoc':monhoc})  

def chinhsuaMonHoc(request, mamonhoc):
    monhoc=monHoc.objects.get(mamonhoc=mamonhoc)
    return render(request, 'admin_templates/chinhsuaMonHoc.html', {'monhoc':monhoc, 'mamonhoc':mamonhoc})
    
def luuchinhsuaMonHoc(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mamonhoc=request.POST.get("mamonhoc")
        tenmonhoc=request.POST.get("tenmonhoc")
        sotiet=request.POST.get("sotiet")

        try:
            monhoc=monHoc.objects.get(mamonhoc=mamonhoc)
            monhoc.tenmonhoc=tenmonhoc
            monhoc.sotiet=sotiet
            monhoc.save()

            messages.success(request,"Chỉnh sửa môn học thành công")
            return HttpResponseRedirect("/chinhsuaMonHoc/" + str(monhoc.mamonhoc))
        except:
            messages.error(request,"Chỉnh sửa môn học không thành công")
            return HttpResponseRedirect("/chinhsuaMonHoc/" + str(monhoc.mamonhoc))
        
def xoaMonHoc(request, mamonhoc):
    monhoc=monHoc.objects.get(mamonhoc=mamonhoc)
    return render(request, 'admin_templates/xoaMonHoc.html', {'monhoc':monhoc, 'mamonhoc':mamonhoc})
        
def luuXoaMonHoc(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mamonhoc=request.POST.get("mamonhoc")
        try:
            monhoc=monHoc.objects.get(mamonhoc=mamonhoc)
            monhoc.delete()
            return HttpResponseRedirect("/quanlyMonHoc")
        except:
            return HttpResponseRedirect("/quanlyMonHoc")
        
        
def themLop(request):
    return render(request,"admin_templates/themLop.html")

def luuLop(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        tenlop=request.POST.get("tenlop")
        
        try:
            lopmoi=lop.objects.create(tenlop=tenlop)
            lopmoi.save()
            messages.success(request,"Thêm lớp thành công")
            return HttpResponseRedirect("/themLop")
        except:
            messages.error(request,"Thêm lớp không thành công")
            return HttpResponseRedirect("/themLop")   
        
def quanlyLop(request):
    v_lop=lop.objects.all()
    return render(request, 'admin_templates/quanlyLop.html', {'v_lop':v_lop})  

def chinhsuaLop(request, malop):
    v_lop=lop.objects.get(malop=malop)
    return render(request, 'admin_templates/chinhsuaLop.html', {'v_lop':v_lop, 'malop':malop})
    
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

            messages.success(request,"Chỉnh sửa lớp thành công")
            return HttpResponseRedirect("/chinhsuaLop/" + str(v_lop.malop))
        except:
            messages.error(request,"Chỉnh sửa lớp không thành công")
            return HttpResponseRedirect("/chinhsuaLop/" + str(v_lop.malop))
        
def xoaLop(request, malop):
    v_lop=lop.objects.get(malop=malop)
    return render(request, 'admin_templates/xoaLop.html', {'v_lop':v_lop, 'malop':malop})
        
def luuXoaLop(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        malop=request.POST.get("malop")
        try:
            v_lop=lop.objects.get(malop=malop)
            v_lop.delete()
            return HttpResponseRedirect("/quanlyLop")
        except:
            return HttpResponseRedirect("/quanlyLop")

def timGiaoVien(request):
    return render(request,"admin_templates/timGiaoVien.html")

def ketquatimGiaoVien(request):
    tengv=request.POST.get('tengv')
    try:
        giaovien=nguoiDung.objects.get(hovaten=tengv)
        return render(request, "admin_templates/ketquatimGiaoVien.html", {'giaovien': giaovien})
    except:
        messages.error(request,"Không tìm được giáo viên")
        return render(request, "admin_templates/timGiaoVien.html")
    
def timNhanVien(request):
    return render(request,"admin_templates/timNhanVien.html")

def ketquatimNhanVien(request):
    tennv=request.POST.get('tennv')
    try:
        nhanvien=nguoiDung.objects.get(hovaten=tennv)
        return render(request, "admin_templates/ketquatimNhanVien.html", {'nhanvien': nhanvien})
    except:
        messages.error(request,"Không tìm được nhân viên")
        return render(request, "admin_templates/timNhanVien.html")
    
def timLop(request):
    return render(request,"admin_templates/timLop.html")

def ketquatimLop(request):
    tenlop=request.POST.get('tenlop')
    try:
        v_lop=lop.objects.get(tenlop=tenlop)
        return render(request, "admin_templates/ketquatimLop.html", {'v_lop': v_lop})
    except:
        messages.error(request,"Không tìm được lớp")
        return render(request, "admin_templates/timLop.html")
    
def timMonHoc(request):
    return render(request,"admin_templates/timMonHoc.html")

def ketquatimMonHoc(request):
    tenmonhoc=request.POST.get('tenmonhoc')
    try:
        monhoc=monHoc.objects.get(tenmonhoc=tenmonhoc)
        return render(request, "admin_templates/ketquatimMonHoc.html", {'monhoc': monhoc})
    except:
        messages.error(request,"Khong tìm được môn học")
        return render(request, "admin_templates/timMonHoc.html")           

        
    
    