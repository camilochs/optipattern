# -----------------------------------------------------------------------------
# Author: Camilo Chacón Sartori
# Date: 17-10-2024
#
# This file is part of OptiPattern.
#
# Copyright (c) [2024] Camilo Chacón Sartori

import argparse
from src.probabilities import calculate_probabilities
from src.metrics import calculate_metrics
from src.llm import execute_llm

def main():

    parser = argparse.ArgumentParser(description="OptiPattern. Generator of probabilities.")
    
    parser.add_argument(
        "--evaluation-graph",
        type=str,
        required=True,
        help="Path evaluation graph file"
    )

    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Path prompt"
    )
    
    parser.add_argument(
        "--api-key",
        type=str,
        required=True,
        help="LLM Api key"
    )

    parser.add_argument(
        "--provider",
        type=str,
        required=True,
        default="anthropic",
        help="Provider: anthropic or openai (default: anthropic)"
    )


    parser.add_argument(
        "--model",
        type=str,
        default="claude-3-opus-20240229",
        help="Model name (default by anthropic)"
    )

    args = parser.parse_args()

    metrics = calculate_metrics(args.evaluation_graph)
    output_llm = execute_llm(prompt_file=args.prompt, api_key=args.api_key, provider=args.provider, model=args.model)
    calculate_probabilities(metrics, output_llm)
 

if __name__ == "__main__":
    main()
