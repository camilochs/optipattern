# -----------------------------------------------------------------------------
# Author: Camilo Chacón Sartori
# Date: 17-10-2024
#
# This file is part of OptiPattern.
#
# Copyright (c) [2024] Camilo Chacón Sartori

import argparse
from src.prompt import build_prompt
# Función principal
def main():

    parser = argparse.ArgumentParser(description="OptiPattern. Generator of prompts.")
    
    parser.add_argument(
        "--example-graph",
        type=str,
        required=False,
        help="Path example graph file",
        default=""
    )
    parser.add_argument(
        "--high-quality-solution-example",
        type=str,
        required=False,
        help="Path of high-quality-solution for example graph",
        default=""
    )
    parser.add_argument(
        "--evaluation-graph",
        type=str,
        required=True,
        help="Path evaluation graph file"
    )
    
    args = parser.parse_args()

    if args.example_graph and not args.high_quality_solution_example:
        parser.error("--high-quality-solution-example is required because --example-graph exist.")
    
    build_prompt(args.evaluation_graph, args.example_graph, args.high_quality_solution_example)
 

if __name__ == "__main__":
    main()
