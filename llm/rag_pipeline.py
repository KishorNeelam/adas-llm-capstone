"""
Illustrative RAG pipeline for automotive internal use.
Focus: safety, governance, and controlled knowledge access.
"""

def retrieve_documents(query):
    """
    Retrieve information only from approved internal sources.
    """
    approved_docs = [
        "ADAS requirements document",
        "Safety concept description",
        "Test strategy overview"
    ]
    return approved_docs

def generate_answer(context, query):
    """
    Generate answer strictly based on retrieved context.
    """
    if not context:
        return "Insufficient approved information to answer this query."
    return f"Answer generated using approved context: {context}"

query = "Explain AEB failure scenarios"
context = retrieve_documents(query)
answer = generate_answer(context, query)

print(answer)
