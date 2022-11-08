# -*- coding: utf-8 -*-
from recbole.quick_start import run_recbole

parameter_dict = {
   'neg_sampling': None,
   'train_neg_sample_args': None
}
config_file_list = ['/kaggle/working/mycode/RecBole/sas.yaml']
run_recbole(model='SASRec', dataset='ml-1m', config_dict=parameter_dict,config_file_list=config_file_list)
