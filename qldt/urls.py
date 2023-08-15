from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from qldt import settings
from qldt_app import views
from qldt_app import adminViews, nhanvienViews, giaovienViews

urlpatterns = [
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name='logout'),
    path('doLogin', views.doLogin),
    path('admin_home', adminViews.admin_home, name='admin_home'),
    path('nhanvien_home', nhanvienViews.nhanvien_home, name='nhanvien_home'),
    path('giaovien_home', giaovienViews.giaovien_home, name='giaovien_home'),
    
    path('themNhanVien', adminViews.themNhanVien),
    path('luuNhanVien', adminViews.luuNhanVien),
    path('quanlyNhanVien', adminViews.quanlyNhanVien),
    path('chinhsuaNhanVien/<str:mand>', adminViews.chinhsuaNhanVien, name='chinhsuaNhanVien'),
    path('luuchinhsuaNhanVien', adminViews.luuchinhsuaNhanVien, name='luuchinhsuaNhanVien'),
    path('xoaNhanVien/<str:mand>', adminViews.xoaNhanVien, name='xoaNhanVien'),
    path('luuxoaNhanVien', adminViews.luuXoaNhanVien, name='luuxoaNhanVien'),
    path('timNhanVien', adminViews.timNhanVien, name='timNhanVien'),
    path('ketquatimNhanVien', adminViews.ketquatimNhanVien, name='ketquatimNhanVien'), 
    
    path('themGiaoVien', adminViews.themGiaoVien),
    path('luuGiaoVien', adminViews.luuGiaoVien),
    path('quanlyGiaoVien', adminViews.quanlyGiaoVien),
    path('chinhsuaGiaoVien/<str:mand>', adminViews.chinhsuaGiaoVien, name='chinhsuaGiaoVien'),
    path('luuchinhsuaGiaoVien', adminViews.luuchinhsuaGiaoVien, name='luuchinhsuaGiaoVien'),
    path('xoaGiaoVien/<str:mand>', adminViews.xoaGiaoVien, name='xoaGiaoVien'),
    path('luuxoaGiaoVien', adminViews.luuXoaGiaoVien, name='luuxoaGiaoVien'),  
    path('timGiaoVien', adminViews.timGiaoVien, name='timGiaoVien'),
    path('ketquatimGiaoVien', adminViews.ketquatimGiaoVien, name='ketquatimGiaoVien'),  
    
    path('themMonHoc', adminViews.themMonHoc),
    path('luuMonHoc', adminViews.luuMonHoc),
    path('quanlyMonHoc', adminViews.quanlyMonHoc),
    path('chinhsuaMonHoc/<str:mamonhoc>', adminViews.chinhsuaMonHoc, name='chinhsuaMonHoc'),
    path('luuchinhsuaMonHoc', adminViews.luuchinhsuaMonHoc, name='luuchinhsuaMonHoc'),
    path('xoaMonHoc/<str:mamonhoc>', adminViews.xoaMonHoc, name='xoaMonHoc'),
    path('luuxoaMonHoc', adminViews.luuXoaMonHoc, name='luuxoaMonHoc'),
    path('timMonHoc', adminViews.timMonHoc, name='timMonhoc'),
    path('ketquatimMonHoc', adminViews.ketquatimMonHoc, name='ketquatimMonHoc'),
    
    path('themLop', adminViews.themLop),
    path('luuLop', adminViews.luuLop),
    path('quanlyLop', adminViews.quanlyLop),
    path('chinhsuaLop/<str:malop>', adminViews.chinhsuaLop, name='chinhsuaLop'),
    path('luuchinhsuaLop', adminViews.luuchinhsuaLop, name='luuchinhsuaLop'),
    path('xoaLop/<str:malop>', adminViews.xoaLop, name='xoaLop'),
    path('luuxoaLop', adminViews.luuXoaLop, name='luuxoaLop'),
    path('timLop', adminViews.timLop, name='timLop'),
    path('ketquatimLop', adminViews.ketquatimLop, name='ketquatimLop'),
    
    path('NVthemGiaoVien', nhanvienViews.themGiaoVien),
    path('NVluuGiaoVien', nhanvienViews.luuGiaoVien),
    path('NVquanlyGiaoVien', nhanvienViews.quanlyGiaoVien),
    path('NVchinhsuaGiaoVien/<str:mand>', nhanvienViews.chinhsuaGiaoVien, name='NVchinhsuaGiaoVien'),
    path('NVluuchinhsuaGiaoVien', nhanvienViews.luuchinhsuaGiaoVien, name='NVluuchinhsuaGiaoVien'),
    path('NVxoaGiaoVien/<str:mand>', nhanvienViews.xoaGiaoVien, name='NVxoaGiaoVien'),
    path('NVluuxoaGiaoVien', nhanvienViews.luuXoaGiaoVien, name='NVluuxoaGiaoVien'),
    path('NVtimGiaoVien', nhanvienViews.timGiaoVien, name='NVtimGiaoVien'),
    path('NVketquatimGiaoVien', nhanvienViews.ketquatimGiaoVien, name='NVketquatimGiaoVien'),
        
    path('NVthemLop', nhanvienViews.themLop),
    path('NVluuLop', nhanvienViews.luuLop),
    path('NVquanlyLop', nhanvienViews.quanlyLop),
    path('NVchinhsuaLop/<str:malop>', nhanvienViews.chinhsuaLop, name='NVchinhsuaLop'),
    path('NVluuchinhsuaLop', nhanvienViews.luuchinhsuaLop, name='NVluuchinhsuaLop'),
    path('NVxoaLop/<str:malop>', nhanvienViews.xoaLop, name='NVxoaLop'),
    path('NVluuxoaLop', nhanvienViews.luuXoaLop, name='NVluuxoaLop'),
    path('NVtimLop', nhanvienViews.timLop, name='NVtimLop'),
    path('NVketquatimLop', nhanvienViews.ketquatimLop, name='NVketquatimLop'),
    
    path('themHocSinh', giaovienViews.themHocSinh),
    path('luuHocSinh', giaovienViews.luuHocSinh),
    path('quanlyHocSinh', giaovienViews.quanlyHocSinh),
    path('chinhsuaHocSinh/<str:mahs>', giaovienViews.chinhsuaHocSinh, name='chinhsuaHocSinh'),
    path('luuchinhsuaHocSinh', giaovienViews.luuchinhsuaHocSinh, name='luuchinhsuaHocSinh'),
    path('xoaHocSinh/<str:mahs>', giaovienViews.xoaHocSinh, name='xoaHocSinh'),
    path('luuxoaHocSinh', giaovienViews.luuXoaHocSinh, name='luuxoaHocSinh'),
    path('timHocSinh', giaovienViews.timHocSinh, name='timHocSinh'),
    path('ketquatimHocSinh', giaovienViews.ketquatimHocSinh, name='ketquatimHocSinh'),
    # path('thongkeDiemLop/<str:malop>', giaovienViews.thongkeDiemLop, name='thongkeDiemLop'),
    
    path('themDiem/<str:mahs>', giaovienViews.themDiem, name='themDiem'),
    path('luuDiem', giaovienViews.luuDiem),
    path('quanlyDiem/<str:mahs>', giaovienViews.quanlyDiem),
    path('chinhsuaDiem/<str:maxulydiem>', giaovienViews.chinhsuaDiem, name='chinhsuaDiem'),
    path('luuchinhsuaDiem', giaovienViews.luuchinhsuaDiem, name='luuchinhsuaDiem'),
    path('xoaDiem/<str:maxulydiem>', giaovienViews.xoaDiem, name='xoaDiem'),
    path('luuxoaDiem', giaovienViews.luuXoaDiem, name='luuxoaDiem'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
