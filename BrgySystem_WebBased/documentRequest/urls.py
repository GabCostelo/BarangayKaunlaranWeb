from django.urls import path

from . import views

app_name = 'documentRequest'

urlpatterns = [
    path('request_document/',views.docRequestView,name='docReqview'),
    path('document_request/',views.docRequestList,name='docReqList'),
    path('pdf/<int:pk>',views.generatePdf.as_view(),name='generatePdf'),
    path('pdfclearance/<int:pk>',views.generatePdfClearance.as_view(),name='generatePdfClearance'),
    path('pdfresidency/<int:pk>',views.generatePdfResidency.as_view(),name='generatePdfResidency'),
    path('update/<int:pk>',views.updateReq,name='updateReq'),
    path('sentUpdate/<int:pk>',views.sendUpdate,name='sendUpdate'),

]
