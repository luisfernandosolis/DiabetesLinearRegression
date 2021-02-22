from django.shortcuts import render


import pickle
import os


import pandas as pd


from django.views import View
# Create your views here.


class Main(View):
    def get(self,request):
        context={
            "nombre":"Luis fernando"
        }
        return render(request,"index.html",context)
    def post(self,request):
        name=request.POST.get("nombre")
        genero = request.POST.get("genero")
        edad = request.POST.get("edad")
        embarazo = request.POST.get("embarazo")
        insulina = request.POST.get("insulina")
        masa = request.POST.get("masa")
        pedigri = request.POST.get("pedigri")
        glucosa = request.POST.get("glucosa")
        presion = request.POST.get("presion")

        data = [[embarazo, insulina, masa, edad, glucosa, presion, pedigri]]
        df=pd.DataFrame(data,columns = ['pregnant','insulin','bmi','age','glucose','bp','pedigree'])
        file=open(os.path.dirname(os.path.realpath(__file__))+"\modelo\logistic_reg.sav", "rb")
        model=pickle.load(file)
        predict=model.predict(df)
        print(predict)
        contexto={}
        if predict==1:
            contexto["result"]="Positivo"
            contexto["color"] = "#3CFE2E"
        else:
            contexto["result"] = "Negativo"
            contexto["color"] = "#FF0E00"
        print(contexto)
        return render(request,"results.html",context=contexto)


