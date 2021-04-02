from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
import pandas as pd
import seaborn as sns
import numpy as np 
# Create your models here.
class DatasetManager(models.Manager):
    def mk_ready_dataset(self,slug, *args , **kwargs):
        # print("this is self", self)
        # print("this is request" , slug)
        # print("this is args" , args)
        # print("this is kwargs" , kwargs.keys())
        df = self.get(slug = slug)
        data = pd.read_csv(df.file)
        print(type(data))
        head_of_dataset = data.head()
        shape_of_dataset = data.shape
        info_of_dataset = self.change_to_dict(data.describe())
        dict_of_dataset = {
            'shape':shape_of_dataset,
            'describe':info_of_dataset,
            'head':head_of_dataset,
            'data_frame':data,
        }
        return dict_of_dataset
        
    def change_to_dict(self,DataFrame):
        dict_of_dataset = DataFrame.to_dict()
        return dict_of_dataset
class Dataset(models.Model):
    name = models.CharField(max_length=120)
    id = models.AutoField(primary_key=True)
    #size = models.CharField(max_length = 120)
    file = models.FileField(blank=True , null = True)
    slug = models.SlugField(max_length=120 , blank=True)
    objects = DatasetManager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "sci/{slug}".format(slug = self.slug)



#def data_file_reciever(sender , instance , *args, **kwargs):






