from initialize_pinecone import pc
from pinecone import ServerlessSpec

index_name = "docs-quickstart-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=2,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
