from django.shortcuts import render
from django.http import HttpResponse
import jsonify
import os
import yaml
import joblib
import pickle
import numpy as np


params_path = "../params.yaml"


def home(request):
    return HttpResponse("Hello")