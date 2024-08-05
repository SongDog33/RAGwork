from initialize_pinecone import pc
from docs_quickstart_index import index_name
from pinecone import ServerlessSpec

index = pc.Index(index_name)

index.upsert(
    vectors=[
        {"id": "vec1", "values": [1.0, 1.5]},
        {"id": "vec2", "values": [2.0, 1.0]},
        {"id": "vec3", "values": [0.1, 3.0]},
    ],
    namespace="ns1"
)

index.upsert(
    vectors=[
        {"id": "vec1", "values": [1.0, -2.5]},
        {"id": "vec2", "values": [3.0, -2.0]},
        {"id": "vec3", "values": [0.5, -1.5]},
    ],
    namespace="ns2"
)
