from django.views.generic import ListView  ,DetailView
from django.shortcuts import render , HttpResponse , Http404
from django.http import JsonResponse
from .models import Dataset
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as ex
from .serializers import SciSerializer
from rest_framework import generics


class ListViewPage(ListView):
    model = Dataset
    template_name = 'list.html'
    def get_context_data(self, **kwargs):
        context = super(ListViewPage, self).get_context_data(**kwargs)
        context['Data'] = Dataset.objects.all()
        print(context) 
        return context
class DetailViewPage(DetailView):
    model = Dataset
    template_name = 'detail.html'
    def get_context_data(self , *args, **kwargs):
        dic_of_dataset = Dataset.objects.mk_ready_dataset(self.kwargs['slug'])
        fig = go.Figure()
        scatter = go.Scatter(x= [0 ,3 ,4 ,5],  y =[1 ,3 ,4 ,5]  , opacity = 0.9)
        # sec_scatter = ex.Scatter(x= [0 ,3 ,4 ,5],  y =[1 ,3 ,4 ,5]  , opacity = 0.9)
        fig.add_trace(scatter)
        plot_div = plot(fig , output_type= 'div')
        # print(dic_of_me)
        # request = self.request
        # print(self.kwargs['slug'])
        # print(self.kwargs)
        # print(type(dic_of_me['describe']))
        # dataset_id=request.session.get('dataset_id' , None)
        # first = Dataset.objects.get(slug = self.kwargs['slug'])
        context = super(DetailViewPage,self).get_context_data(*args, **kwargs)
        # Csv_file = context['object'].file
        # data_set = pd.read_csv(Csv_file).head(20)
        df = dic_of_dataset['data_frame']
        head_df=df.head().to_html(classes = 'mystyle')
        # dict_of_data = data_set.to_dict()
        # # keys_of_dict = dict_of_data.keys()
        # array_of_keys =  np.array(keys_of_dict)
        # print(type(array_of_keys))
        context={
            'head_df':head_df,
            'df' : df, 
            'dic_of_dataset':dic_of_dataset, 
            'plot_div' : plot_div ,        
        }
        
        return context

def first_view(request):
    print('this is my request',request)
    print("this is the slug:",DatasetModel.slug)
    return render(request , 'test.html', context = {})

class ListApiView(generics.ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = SciSerializer

class DetailApiView(generics.RetrieveAPIView):
    queryset = Dataset.objects.all()
    serializer_class = SciSerializer
        
