# OptiPattern: *LLM-Powered Pattern Recognition for Combinatorial Optimization*
## Overview
OptiPattern is an innovative tool designed to enhance combinatorial optimization problem-solving. It functions by:

1. Automatically generating prompts based on the metrics of problem instances (e.g., graphs).
2. Feeding these prompts to a Large Language Model (LLM).
3. Obtaining probability values for each node in the instance from the LLM's output.
4. Integrating these probabilities into approximation algorithms, such as metaheuristics.

### Research Findings

Our research, detailed in the paper "Metaheuristics and Large Language Models Join Forces: Towards an Integrated Optimization Approach", demonstrates the effectiveness of this approach. 

Key insight:
- The probabilities provided by the LLM serve as a *pattern recognition mechanism*.
- This mechanism effectively guides metaheuristics towards more promising search spaces in combinatorial optimization problems.

This integration of LLMs with traditional optimization techniques represents a novel approach to tackling complex combinatorial problems, leveraging the pattern recognition capabilities of advanced language models to improve optimization outcomes.

## Installation

Clone this repository and install the required dependencies:
```
git clone https://github.com/camilochs/optipattern.git
cd optipattern
pip install -r requirements.txt
```

## Features 

## Usages

## Examples


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
