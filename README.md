# OptiPattern: *LLM-Powered Pattern Recognition for Combinatorial Optimization*
## Overview
OptiPattern is an innovative tool designed to enhance combinatorial optimization problem-solving. It functions by:

1. Automatically generating prompts based on the metrics of problem instances (e.g., graphs).
2. Feeding these prompts to a Large Language Model (LLM).
3. Obtaining probability values for each node in the instance from the LLM's output.
4. Integrating these probabilities into approximation algorithms, such as metaheuristics.

### Research Findings

Our research, detailed in the paper ["Metaheuristics and Large Language Models Join Forces: Towards an Integrated Optimization Approach"](https://arxiv.org/abs/2405.18272), demonstrates the effectiveness of this approach. 

Key insight:
- The probabilities provided by the LLM serve as a *pattern recognition mechanism*.
- This mechanism effectively guides metaheuristics towards more promising search spaces in combinatorial optimization problems.

This integration of LLMs with traditional optimization techniques represents a novel approach to tackling complex combinatorial problems, leveraging the pattern recognition capabilities of advanced language models to improve optimization outcomes.

## Installation

Clone this repository and install the required dependencies:
```
git clone https://github.com/camilochs/optipattern.git
cd optipattern
pip3.11 install -r requirements.txt
```

## Features 

- Create a prompt that extracts metrics from graph instances and incorporates our specific requests.
- Run a prompt in the LLM to extract values from its response and generate a file containing probabilities for each node in the instance.

**Note:** Only Anthropic Claude (LLM) is available (should be extended shortly).
## Examples
### Generating prompt
1. Without example graph
   ```
   >> python3.11 -m generate-prompt --evaluation-graph instances-graphs/evaluation/social-networks/500-3000-0.2-0.0-0.3-0.5
   Prompt generated: outputs/prompts/prompt_20241017_132802.txt
   ```
2. With example graph
   ```
   >> python3.11 -m generate-prompt --evaluation-graph instances-graphs/evaluation/social-networks/500-3000-0.2-0.0-0.3-0.5 \
       --example-graph instances-graphs/examples/graph-100-1.txt \
       --high-quality-solution-example instances-graphs/examples/high_quality_solution_nodes-graph-100-1.txt
   Prompt generated: outputs/prompts/prompt_20241017_132904.txt
   ```

### Generating probabilities

This function only works to run an Anthropic model, in particular, in the paper we use Claude-3-Sonnet. If you want to use GPT-x (OpenAI), you can either email me or create your own implementation for integration.

```
>> python3.11 -m generate-probabilities --evaluation-graph instances-graphs/evaluation/social-networks/500-3000-0.2-0.0-0.3-0.5 \
  --prompt outputs/prompts/prompt_20241017_132904.txt \
  --api-key <YOU ANTHROPIC API KEY>
Probabilities generated: outputs/probabilities/probabilities_20241019_142504.txt
```
Once you obtain the fixed probabilities for each node, you can incorporate them into the functioning of a metaheuristic to influence or guide their search. This process is explained in Section “USING LLM OUTPUT TO GUIDE A METAHEURISTIC” of our paper.

## Supplementary Material

All the results of the experiments presented in our paper can be found in the [supplementary material](<supplementary material/>) folder.

## Cite
```
@ARTICLE{10818476,
  author={Sartori, Camilo Chacón and Blum, Christian and Bistaffa, Filippo and Corominas, Guillem Rodríguez},
  journal={IEEE Access}, 
  title={Metaheuristics and Large Language Models Join Forces: Towards an Integrated Optimization Approach}, 
  year={2024},
  volume={},
  number={},
  pages={1-1},
  keywords={Optimization;Metaheuristics;Pattern recognition;Large language models;Transformers;Machine learning algorithms;Graph neural networks;Data models;Approximation algorithms;Vectors;combinatorial optimization;hybrid algorithm;metaheuristics;large languages models},
  doi={10.1109/ACCESS.2024.3524176}}
```
