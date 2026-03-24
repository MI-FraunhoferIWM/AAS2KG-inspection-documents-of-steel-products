
import json

import rdflib
from rdflib import Graph, Namespace
from pathlib import Path
from py_aas_rdf.models.submodel import Submodel, Property

def main(argv):
    UNIQUE_ID = "316-4401"

    AAS_NS = Namespace("https://admin-shell.io/aas/3/0/")
    BASE_URI = "https://example.org/aas/"
    AAS_JSON_PATH = "../input/inspectiondocument_316_4401_alloy.json"  # Path()
    CONSTRUCT = "../input/inspectiondocument_aas2kg_mapping_v2.sparql"
    RESULT_TTL_PATH = "../output/inspectiondocument_316_4401_alloy_pmdco.ttl"
    #PLACEHOLDER = "PLACEHOLDER"

    # Load AAS JSON
    with open(AAS_JSON_PATH, "r", encoding="utf-8") as f:
        aas_json = json.load(f)

    # Run for each submodel in inspection document
    for sm_json in aas_json.get("submodels", []):
        rdf_graph = Graph()
        rdf_graph.bind("aas", "https://admin-shell.io/aas/3/0/")

        # Validate submodel using py-aas-rdf library
        submodel = Submodel.model_validate(sm_json)
        # Convert submodel to RDF
        submodel.to_rdf(rdf_graph, base_uri="https://example.org/aas/", id_strategy="base64-url-encode")
        ttl_output = rdf_graph.serialize(format="turtle")

        out_path = (AAS_JSON_PATH + ".ttl").replace("/input","/output")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ttl_output)

        print("Result written to: {}".format(out_path))

        # Apply SPARQL construct for specific submodels
        if sm_json.get("idShort") == "InspectionDocumentsOfSteelProducts":
            with open(CONSTRUCT, "r", encoding="utf-8") as f:

                mapping_query = f.read() #.replace(PLACEHOLDER, UNIQUE_ID)
                #store = Store()
                #store.load(ttl_output, format=RdfFormat.TURTLE)
                #mapping_result = store.query(mapping_query)
                ## Serialize the result from Oxigraph (returns bytes)
                #mapped_bytes = mapping_result.serialize(format=RdfFormat.TURTLE)

                # --- Parse into rdflib.Graph for prefix binding ---
                g1 = rdflib.Graph()
                g2 = rdflib.Graph()
                #g.parse(data=mapped_bytes, format="turtle")
                g1.parse(out_path, format="turtle")

                g1.bind("aas", "https://admin-shell.io/aas/3/0/")
                g1.bind("pmd", "https://w3id.org/pmd/co/")
                g2.bind("pmd", "https://w3id.org/pmd/co/")
                g1.bind("tto", "https://w3id.org/pmd/tto/")
                g2.bind("tto", "https://w3id.org/pmd/tto/")
                g1.bind("obo", "http://purl.obolibrary.org/obo/")
                g2.bind("obo", "http://purl.obolibrary.org/obo/")
                g2.bind("qudt", "http://qudt.org/schema/qudt/")

                qres = g1.query(mapping_query)

                # Add all constructed triples into g2
                for triple in qres:
                    g2.add(triple)

                # Serialize with prefixes applied
                final_ttl = g2.serialize(format="turtle")

                # Write to file
                with open(RESULT_TTL_PATH, "w", encoding="utf-8") as f:
                    f.write(final_ttl)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
