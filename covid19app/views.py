from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "cb2a339218mshf7eccf5248f0fcfp16c1c8jsn0c7ed8f2f5c0",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()






# Create your views here.
def index(request):
   length = response['results']
   cllist = []
   for x in range(0,length):
       cllist.append(response['response'][x]['country'])

   if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry)
        for x in range(0,length):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)
        context = {'selectedcountry':selectedcountry,'cllist':cllist,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'index.html',context)
      

  

   


