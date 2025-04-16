import os
import pandas as pd
from groq import Groq
data = pd.read_csv('./assets/Students_data.csv')
teacher = pd.read_csv('./assets/Teachers_data.csv')
marks = pd.read_csv('./assets/Marks_data.csv')
combined_text = data.apply(lambda row: ' '.join(row.astype(str)), axis=1).str.cat(sep=' ')
combined_teacher = teacher.apply(lambda row: ' '.join(row.astype(str)), axis=1).str.cat(sep=' ')
combined_marks = marks.apply(lambda row: ' '.join(row.astype(str)), axis=1).str.cat(sep=' ')
print(combined_text)
client = Groq(
    api_key="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",
)
print("Ask me a question :\n");
question = input()
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Read very carefully, answer from this text: Student-- {combined_text} ,teacher-- {combined_teacher} and Marks-- {combined_marks}(The First data is having list of students having thier roll no and and teacher id, teacher is having thier name and id, marks is having marks id and marks value and student id).\n my question my question is :{question}",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)