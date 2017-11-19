from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.shortcuts import render_to_response
import requests
import json
import urllib
from django.template import RequestContext
from django.template import loader
from .forms import HomeForm
from .forms import DealForm
from .forms import VillForm


url2=urllib.urlopen('http://127.0.0.1:7071/mem/?format=json')
url3=urllib.urlopen('http://127.0.0.1:7071/farm/?format=json')
url4=urllib.urlopen('http://127.0.0.1:7071/well/?format=json')
url5=urllib.urlopen('http://127.0.0.1:7071/crop/?format=json')
url6=urllib.urlopen('http://127.0.0.1:7071/Medi/?format=json')
url7=urllib.urlopen('http://127.0.0.1:7071/Mup/?format=json')
url8=urllib.urlopen('http://127.0.0.1:7071/vill/?format=json')
url9=urllib.urlopen('http://127.0.0.1:7071/Deal/?format=json')
l2=url2.read()
l3=url3.read()
l4=url4.read()
l5=url5.read()
l6=url6.read()
l7=url7.read()
l8=url8.read()
l9=url9.read()
s2=json.loads(l2)
s3=json.loads(l3)
s4=json.loads(l4)
s5=json.loads(l5)
s6=json.loads(l6)
s7=json.loads(l7)
s8=json.loads(l8)
s9=json.loads(l9)
def pie(request):     
        
        F_id=[]
        l1=[]
        l2=[]
        lat=[[]]
        lon=[[]]
        for a in s3:
                F_id.append(int(a['F_id']))
                l1.append(float(a['aLatitude']))
                l1.append(float(a['bLatitude']))
                l1.append(float(a['cLatitude']))
                l1.append(float(a['dLatitude']))
                l2.append(float(a['aLongitude']))
                l2.append(float(a['bLongitude']))
                l2.append(float(a['cLongitude']))
                l2.append(float(a['dLongitude']))
                lat.append(l1)
                lon.append(l2)
                l1=[]
                l2=[]
        lat.remove([])
        lon.remove([])
        q=5
        fid=[]
        cr2=[]
        crpa=[[]]
        for k in s5:
                if q==5:
                        fid.append(k['F_id'])
                        cr2.append(int(k['profit']))
                        q=6
                else:
                        if k['F_id'] in fid:
                                cr2.append(int(k['profit']))
                        else:
                                crpa.append(cr2)
                                fid.append(k['F_id'])
                                cr2=[]
                                cr2.append(int(k['profit']))
        crpa.append(cr2)
        crpa.remove([])

        alt=[[]]
        for i in range(len(lat)):
                pk=[]
                a1=reduce(lambda x,y:x+y,lat[i])/len(lat[i])
                pk.append(a1)
                b1=reduce(lambda x,y:x+y,lon[i])/(len(lon[i]))
                pk.append(b1)
                alt.append(pk)
        alt.remove([])
        final=[[]]
        for v in range(len(alt)):
                fin=alt[v]+crpa[v]
                final.append(fin)
        final.remove([])
                        
        return render(request,'clientapp/main/test.html',context={'data2':s2,'data3':s3,'data4':s4 ,'data5' :s5,'data6':final})

def hh(request):
	return render(request,'clientapp/main/house.html',context={'data2':s2})
	
def well(request):
	return render(request,'clientapp/main/3d.html',context={'data4':s4})
	
def index(request):
        return render(request,'clientapp/home.html')
		
		
def farm(request):
	F_id=[]
        l1=[]
        l2=[]
        lat=[[]]
        lon=[[]]
        for a in s3:
                F_id.append(int(a['F_id']))
                l1.append(float(a['aLatitude']))
                l1.append(float(a['bLatitude']))
                l1.append(float(a['cLatitude']))
                l1.append(float(a['dLatitude']))
                l2.append(float(a['aLongitude']))
                l2.append(float(a['bLongitude']))
                l2.append(float(a['cLongitude']))
                l2.append(float(a['dLongitude']))
                lat.append(l1)
                lon.append(l2)
                l1=[]
                l2=[]
        lat.remove([])
        lon.remove([])
        q=5
        fid=[]
        cr2=[]
        crpa=[[]]
        for k in s5:
                if q==5:
                        fid.append(k['F_id'])
                        cr2.append(int(k['profit']))
                        q=6
                else:
                        if k['F_id'] in fid:
                                cr2.append(int(k['profit']))
                        else:
                                crpa.append(cr2)
                                fid.append(k['F_id'])
                                cr2=[]
                                cr2.append(int(k['profit']))
        crpa.append(cr2)
        crpa.remove([])

        alt=[[]]
        for i in range(len(lat)):
                pk=[]
                a1=reduce(lambda x,y:x+y,lat[i])/len(lat[i])
                pk.append(a1)
                b1=reduce(lambda x,y:x+y,lon[i])/(len(lon[i]))
                pk.append(b1)
                alt.append(pk)
        alt.remove([])
        final=[[]]
        for v in range(len(alt)):
                fin=alt[v]+crpa[v]
                final.append(fin)
        final.remove([])
                        
        return render(request,'clientapp/main/pie.html',context={'data3':s3 ,'data6':final})
def house(request):
	return 0

def get_details(request):
	data1=[]
	data2=[]        
	F_id=[]
	l1=[]
	l2=[]
	lat=[[]]
	lon=[[]]
	fid=[]
	cr2=[]
	crpa=[[]]
	if request.method=='POST':
		form=HomeForm(request.POST)
		if form.is_valid(): 
			P=form.cleaned_data['Aadhar']
			q=form.cleaned_data['passwd']
			form=HomeForm()
			for k in s2:
				if (k['AadharNo']==P and k['passwd']==q):
					request.session.Hid=k['id']
					for d in s2:
						if d['Hid']==request.session.Hid:
							data1.append(d)
								
					for u in s3:
						if u['H_id']==request.session.Hid:
							data2.append(u)
							F_id.append(int(u['F_id']))
					for k in s5:
						if q==5:
							
							fid.append(k['F_id'])
							cr2.append(k['F_id'])
							cr2.append(int(k['profit']))
							q=6
						else:
							if k['F_id'] in fid:
								cr2.append(int(k['profit']))
							else:
								crpa.append(cr2)
								fid.append(k['F_id'])
								cr2=[]
								cr2.append(k['F_id'])
								cr2.append(int(k['profit']))
					crpa.append(cr2)
					crpa.remove([])	
					cc=[]

					#			cc.append(crpa[i])
							
					return render(request,'clientapp/detail/Details.html',context={'data2':data2,'data1':data1,'data3':crpa})
					
			#return HttpResponseRedirect(reverse('pallevelugu:home'))
	else:
		form = HomeForm()
	return render(request,'clientapp/detail/name.html',{'form':form,})
		
def medi(request):
	data1=[]
	data2=[]
	if request.method=='POST':
		form=VillForm(request.POST)
		if form.is_valid(): 
			P=form.cleaned_data['Village']
			form=VillForm()
			for k in s8:
				if (k['Village']==P):
					request.session.D_id=k['D_id']
					for d in s8:
						if d['D_id']==request.session.D_id:
							data1.append(d)
					for j in s6:
						if j['Did']==request.session.D_id:
							data2.append(j)
					return render(request,'clientapp/main/medi.html',context={'data1':data1 , 'data2':data2,'data':s7 })
			
	else:
		form = VillForm()
	return render(request,'clientapp/main/vill.html',{'form':form,})
	
	
def deal(request):
		data1=[]
		data2=[]
		data3=[]
		if request.method=='POST':
			form=DealForm(request.POST)
			if form.is_valid(): 
				P=form.cleaned_data['Aadhar']
				q=form.cleaned_data['passwd']
				form=DealForm()
				for k in s2:
					if (k['AadharNo']==P and k['passwd']==q):
						request.session.Hid=k['id']
						for d in s9:
							if d['H_id']==request.session.Hid:
								data1.append(d)
						for j in s2:
							if j['Hid']==request.session.Hid:
								data2.append(j)
						for k in s3:
							if k['H_id']==request.session.Hid:
								data3.append(k)
						return render(request,'clientapp/detail/dealer.html',context={'data1':data1 , 'data2':data2, 'data3':data3})
					
			#return HttpResponseRedirect(reverse('pallevelugu:home'))
		else:
			form = DealForm()
		return render(request,'clientapp/detail/deal.html',{'form':form,})
	
	
	
		
		
		

