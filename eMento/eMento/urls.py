"""eMento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import providers
from . import consumers
from . import adminView 
from . import staffView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('providerLogin/',providers.ProviderLogin),
    path('account/',providers.Account),
    path('feedback/',providers.Feedback),
    path('Application',providers.Application),
    path('jobapplication',providers.JobApplication),
 
 #consumer

    path('consumerregister/',consumers.ConsumerRegister),
    path('consumerLogin/', consumers.ConsumerLogin),
    path('account/',consumers.EnrolledCourses),
    path('feedback/',consumers.Feedback),
    path('Application',consumers.Mentor),
    path('jobapplication',consumers.Message),
    path('assesment/',consumers.Assesment),

 #admin
    path('/viewadmindetails',adminView.ViewAdminDetails),
    path('/addbranch',adminView.AddBranch),
    path('/displaybranches',adminView.displayBranches),
    path('/addstaff',adminView.AddStaff),
    path('/displaystaffMembers',adminView.displayBranches),
    path('/editstaffmembersdetails',adminView.EditStaffMemberDetails),
    path('/uploadresources',adminView.UploadResources),
    path('/viewreport',adminView.ViewReport),
    path('/feedbackadmin',adminView.feedback),
    path('/messageadmin',adminView.Message),

 #staff
    
    path('/stafflogin',staffView.StaffLogin),
    path('/staffdetails',staffView.ViewStaffDetails),
    path('/addconsumers',staffView.AddConsumers),
    path('/displayconsumers',staffView.displayConsumers),
    path('/editconsumerdetails',staffView.EditConsumerDetails),
    path('/staffuploadresources',staffView.UploadResources),
    path('/viewreportstaff',staffView.ViewReport),
    path('/stafffeedback',staffView.feedback),
    path('/staffmessage',staffView.Message),
    path('/assesmentrecord',staffView.AssesmentRecord),

]


