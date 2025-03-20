from transformers import pipeline

def query_tables_with_llm(question, table_data):
    llm = pipeline('text-generation', model='gpt2')
    context = " ".join([str(row) for row in table_data])
    prompt = f"Question: {question}\nContext: {context}\nAnswer:"
    result = llm(prompt, max_length=100)
    return result[0]['generated_text']
