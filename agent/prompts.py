from langchain_core.prompts import ChatPromptTemplate

classify_prompt = ChatPromptTemplate.from_messages([
    ("user", "I have a piece of text: {text}. Tell me whether it is a question or compliment. Respond with only the word 'question' or 'compliment'.")
])

beautify_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant that will beautify answers given to you. Please provide a more professional and polished version of this answer. Also use the tag for directing the query to the concerned department."),
    ("user", "answer: {answer}"),
    ("user", "tag: {tag}")
])
