# -----------------------------------------------------------------------------
# Author: Camilo Chacón Sartori
# Date: 17-10-2024
#
# This file is part of OptiPattern.
#
# Copyright (c) [2024] Camilo Chacón Sartori

import pandas as pd
import numpy as np
import io
import re
from pydantic import BaseModel, Field
from typing import List
from src.utils import write_file

class AlphaBetaModel(BaseModel):
    alpha: List[float] = Field(..., description="values alpha")
    beta: List[float] = Field(..., description="values beta")

def extract_values(data_str: str) -> AlphaBetaModel:
    alpha_values = re.findall(r'alpha_\d+=(\d\.\d+)', data_str)
    beta_values = re.findall(r'beta_\d+=(\d\.\d+)', data_str)

    alpha_floats = [float(value) for value in alpha_values]
    beta_floats = [float(value) for value in beta_values]

    return AlphaBetaModel(alpha=alpha_floats, beta=beta_floats)

def extract_alpha_beta_values(output_llm) -> AlphaBetaModel:
    model = extract_values(output_llm)
    alpha_total = sum(model.alpha) 
    model.alpha = [v / alpha_total for v in model.alpha]
    return model

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def calculate_probabilities(metric_evaluation_graph, output_llm):

    data_io = io.StringIO(metric_evaluation_graph)
    df = pd.read_csv(data_io, names=["node", "idc", "odc", "closeness", "betweenness", "pagerank"])
    
    model = extract_alpha_beta_values(output_llm)
    df['influence'] = sigmoid(
                    (model.alpha[0] * (1 - (model.beta[0] - df['idc']))) +
                    (model.alpha[1] * (1 - (model.beta[1] - df['odc']))) +
                    (model.alpha[2] * (1 - (model.beta[2] - df['closeness']))) +
                    (model.alpha[3] * (1 - (model.beta[3] - df['betweenness']))) + 
                    (model.alpha[4] * (1 - (model.beta[4] - df['pagerank'])))   
                 ) 

    data = df['influence'][df['node']]
    write_file(data.to_string(index=False, header=False), "probabilities")
