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

- Generate a prompt that from graph instances that extracts the metrics and adds our special requests.
- Execute a prompt in an LLM extract the values of its response and generate a file of probabilities associated to each node of the instance.

Important: Only Anthropic Claude (LLM) is available.

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

```
>> python3.11 -m generate-probabilities --evaluation-graph instances-graphs/evaluation/social-networks/500-3000-0.2-0.0-0.3-0.5 \
  --prompt outputs/prompts/prompt_20241017_132904.txt \
  --api-key <YOU ANTHROPIC API KEY>
Probabilities generated: outputs/probabilities/probabilities_20241019_142504.txt
```

## Cite
```
@article{Sartori2024MetaheuristicsAL,
  title={Metaheuristics and Large Language Models Join Forces: Towards an Integrated Optimization Approach},
  author={Camilo Chac{\'o}n Sartori and Christian Blum and Filippo Bistaffa and Guillem Rodr{\'i}guez Corominas},
  journal={ArXiv},
  year={2024},
  volume={abs/2405.18272},
  url={https://api.semanticscholar.org/CorpusID:270068396}
}
```

## Contributing
We welcome contributions! Please follow these steps to contribute:

- Fork this repository.
- Create a new branch (`git checkout -b feature-xyz`).
- Commit your changes (`git commit -m 'Add new feature`').
- Push to the branch (`git push origin feature-xyz`).
- Open a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or suggestions, feel free to open an issue or contact the repository owner at cchacon@iiia.csic.es
