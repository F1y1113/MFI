# SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions

[Paper](https://arxiv.org/pdf/2408.05357)

[Project Homepage](https://f1y1113.github.io/MFI/)

[Dataset](https://drive.google.com/drive/folders/12kH2S9Rr7ev_XejRZ3HNPhKfk01-dSEv?usp=sharing)

## Paper Abstract

The electric vehicle (EV) battery supply chain's vulnerability to disruptions necessitates advanced predictive analytics. We present SHIELD (Schema-based Hierarchical Induction for EV supply chain Disruption), a system integrating Large Language Models (LLMs) with domain expertise for EV battery supply chain risk assessment. SHIELD combines: (1) LLM-driven schema learning to construct a comprehensive knowledge library,(2) a disruption analysis system utilizing fine-tuned language models for event extraction, multi-dimensional similarity matching for schema matching, and Graph Convolutional Networks (GCNs) with logical constraints for prediction, and (3) an interactive interface for visualizing results and incorporating expert feedback to enhance decision-making. Evaluated on 12,070 paragraphs from 365 sources (2022-2023), SHIELD outperforms baseline GCNs and LLM+prompt method (e.g. GPT-4o) in disruption prediction.These results demonstrate SHIELD's effectiveness in combining LLM capabilities with domain expertise for enhanced supply chain risk assessment.

## Citation

If you found the provided code with our paper useful in your work, please **star** this repo and **cite** our paper!

```
@misc{cheng2024shieldllmdrivenschemainduction,
      title={SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions}, 
      author={Zhi-Qi Cheng and Yifei Dong and Aike Shi and Wei Liu and Yuzhi Hu and Jason O'Connor and Alexander Hauptmann and Kate Whitefoot},
      year={2024},
      eprint={2408.05357},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2408.05357}, 
}
```
