from common.models import *
from common.datasets import *
from functools import partial
import torch
import torch.optim
import torch.nn as nn

p = lambda func, args: partial(func, args)
session = {
    "train":
    {
        "model":NVIDIA_ConvNet,
        "modelname":'nvidia_model',
        "lr":1e-3,
        "loss_func":nn.functional.mse_loss,
        "optimizer":torch.optim.Adam,
        "num_epochs":5,
        "batch_size":5,
        "sess_id": 0,
        "vsplit":0.0,
        "dataset":SteerDataset_ONLINE,
	    "root":'/home/dhruvkar/datasets/avfone/'
    },
    "online":
    {
        "sess_id": 0,
	    "models_dir":'/home/nvidia/datasets/avfone/models/'
        ,"funclist":[]
    }
}