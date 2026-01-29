# AAS JSON  to Knowledge Graph Conversion Pipeline

This repository demonstrates how to transform an **Asset Administration Shell (AAS) JSON** into a valid  
**OWL/RDF-based Knowledge Graph (KG)** representation using a sequential, transparent workflow.

The goal is to provide an educational, easy-to-follow demonstration of how AAS 3.0 metamodel can be
mapped to the semantic knowledge using SPARQL, RDF tooling, and the `py-aas-rdf` library.

---

## 🚀 Overview

This project shows how to:

1. Load AAS instance
2. Validate JSON against AAS Meta-Model schema
3. Convert AAS JSON -> RDF (using `py-aas-rdf`)
4. Apply SPARQL mapping → AAS RDF
5. Save output RDF

The notebook uses a **fully sequential approach** (no abstractions, no functions) for maximum clarity.

---

## 📁 Repository Structure

```plaintext
AAS2KG-usage/
├── input/
│   ├── mapping.sparql # SPARQL CONSTRUCT file for semantic transformation
├── output/
│   └── ... # Generated RDF files
├── AAS2KG_demo.ipynb # Main sequential demonstration notebook
├── .env_template # Environment variables required to access DSMS instance(HOST_URL, credentials, etc.)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## 🔧 Requirements

Install all dependencies via:

```bash
pip install -r requirements.txt

## ⚙️ Configuration

Environment variables must be defined in a .env file in the working directory:

````plaintxt
DSMS_HOST_URL=https://pmdx.materials-data.space/
DSMS_USERNAME=<username>
DSMS_PASSWORD=<password>
```
