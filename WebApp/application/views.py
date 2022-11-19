from django.shortcuts import render
from django.http import HttpResponse
from prediction_service import prediction
import numpy as np
# import jsonify
# import os
# import yaml
# import joblib
import pickle
import numpy as np
import pandas as pd

params_path = "../params.yaml"


# def home(request):
#     res = render(request,'index.html')
#     return res 

def home(request):
    if request.method == "POST":
        item_identifier = request.POST["item_identifier"]

        item_weight = request.POST["item_weight"]

        item_fat_content = request.POST["item_fat_content"]

        item_visibility  = request.POST["item_visibility"]

        item_type = request.POST["item_type"]

        item_mrp = request.POST["item_mrp"]

        outlet_indentifier = request.POST["outlet_identifier"]

        outlet_establishment = request.POST["outlet_establishment"]

        outlet_size = request.POST["outlet_size"]

        outlet_location_type = request.POST["outlet_location_type"]

        outlet_type = request.POST["outlet_type"]


        # print(item_identifier)
        # print(item_weight)
        # print(item_fat_content)
        # print(item_visibility )
        # print(item_type)
        # print(item_mrp)
        # print(outlet_indentifier)
        # print(outlet_establishment)
        # print(outlet_size)
        # print(outlet_location_type)
        # print(outlet_type)

        lis=[item_identifier,item_weight,item_fat_content,item_visibility,
        item_type,item_mrp,outlet_indentifier,outlet_establishment,
        outlet_size,outlet_location_type,outlet_type]
        print(lis)

        transformer = pickle.load(open('../column_transformer/transformer_model_.pickle','rb'))
        print("------------File Loading is Done------------")

        # create in such a way so that it can be transformed
        k=['item_identifier', 'item_weight', 'item_fat_content', 'item_visibility',
       'item_type', 'item_mrp', 'outlet_identifier',
       'outlet_establishment_year', 'outlet_size', 'outlet_location_type',
       'outlet_type']

        
        v = [item_identifier,float(item_weight),item_fat_content,float(item_visibility),
        item_type,float(item_mrp),outlet_indentifier,float(outlet_establishment),
        outlet_size,outlet_location_type,outlet_type]
        print(v)


        dic = dict(list(zip(k,v)))
        print("---------DICTIONARY READY--------------")
        print(dic)
        df = pd.DataFrame(dic,index=[0])
        print("--------------DF IS READY-------------")
        # print(df.iloc[0])
        # print(value)
        print(df.to_numpy())

        # df = df.reset_index(drop=True,inplace=True)-
        # value = df.loc[:,:]
        # print("check type",type(df['item_weight'][0]))
        print(df.to_numpy())
        # print(arr)
        # arr1  = arr.reshape(1,-1)
        # print(arr1)
        op = transformer.transform(df.to_numpy())
        print(op)
        # result = prediction.predict(data)
        
        # return HttpResponse(result)
    res = render(request,'index.html')
    return res