# AAS JSON → Knowledge Graph — README (based only on the notebook)

This README demonstrates how to transform an Asset Administration Shell (AAS) JSON into a valid
OWL/RDF-based Knowledge Graph (KG) representation using a sequential, transparent workflow.

The goal is to provide an educational, easy-to-follow demonstration of how AAS 3.0 metamodel can be mapped to the semantic knowledge using SPARQL, RDF tooling, and the py-aas-rdf library.

## What it does

- Loads an AAS JSON instance (You can replace the existing JSON with your remote API call to download it).
- Validates each submodel using `py-aas-rdf`.
- Converts submodels to RDF (rdflib Graph → Turtle).
- Loads Turtle into an Oxigraph Store and runs a SPARQL CONSTRUCT mapping (mapping file contains a placeholder token).
- Re-parses mapped result into rdflib, binds prefixes, serializes and writes final TTL.

## Pipeline steps (as implemented in the notebook)

1. Load AAS JSON from AAS_JSON_PATH or from external API call.
2. Provide the path to your SPARQL CONSTRUCT mapping file.
3. The mapping file provided for steel inspection document contain the `PLACEHOLDER` token that will be replaced by `UNIQUE_ID` part of your data.
4. For each `submodel` in `aas_json["submodels"]`:
   - Validate with `Submodel.model_validate`.
   - Convert to RDF with `submodel.to_rdf(...)` into an rdflib.Graph.
   - Serialize graph to Turtle (`ttl_output`).
   - Read SPARQL mapping file and replace `PLACEHOLDER` with `UNIQUE_ID`.
   - Load Turtle into `pyoxigraph.Store` and run the mapping query.
5. Serialize mapping result (Turtle), parse into rdflib.Graph, bind namespaces, serialize to final TTL.
6. Print final TTL and write to `OUTPUT_FILE`.

## How to run (notebook)

1. Ensure the Python packages referred to in the notebook are installed (the notebook mentions `requirements.txt` from "https://github.com/MI-FraunhoferIWM/AAS2KG-inspection-documents-of-steel-products" ).
2. Open `AAS2KG_demo.ipynb` in Jupyter or VS Code.
3. Edit the variables above if needed (paths, UNIQUE_ID).
4. Execute the cells top-to-bottom.
5. Final TTL is printed in the notebook and written to `OUTPUT_FILE`.

## Output

- Final RDF/Turtle is saved to the file path given in `OUTPUT_FILE` and printed to the notebook output.
