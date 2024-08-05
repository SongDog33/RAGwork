from first_upsert import index
from pinecone import ServerlessSpec

print(index.describe_index_stats())
