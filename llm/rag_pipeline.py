"""
Simple RAG pipeline example for automotive internal use.
This code is illustrative and focuses on architecture, not performance.
"""

def retrieve_documents(query):
    return ["Relevant internal ADAS document section"]

def generate_answer(context, query):
    return f"Answer based only on provided context: {context}"

query = "Explain AEB failure scenarios"
docs = retrieve_documents(query)
answer = generate_answer(docs, query)

print(answer)
