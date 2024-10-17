# -----------------------------------------------------------------------------
# Author: Camilo Chacón Sartori
# Date: 17-10-2024
#
# This file is part of OptiPattern.
#
# Copyright (c) [2024] Camilo Chacón Sartori

from src.metrics import calculate_metrics
from src.utils import write_file

def build_prompt(path_evaluation_graph, path_example_graph, path_high_quality_nodes_example):

    template = ""
    if path_example_graph != "":
        with open("prompts/k-dDSP problem/template.txt", "r") as f:
            template = f.read()

        with open(path_high_quality_nodes_example, "r") as f:
            high_quality_solutions = f.read()
            template = template.replace("{{high_quality_solution}}", high_quality_solutions)
        
        metrics_example_graph = calculate_metrics(path_example_graph)
        template = template.replace("{{graph_data_example}}", metrics_example_graph)
    else:
        with open("prompts/k-dDSP problem/template-without-example.txt", "r") as f:
            template = f.read()

    metrics_evaluate_graph = calculate_metrics(path_evaluation_graph)
    template = template.replace("{{graph_data_evalution}}", metrics_evaluate_graph)
    write_file(template, "prompts")