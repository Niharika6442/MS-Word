import openai
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM



def t5_summerizer(content):
    
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    input_ids = tokenizer(content, max_length=2048, truncation=True, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_length=500)
    output_text = tokenizer.decode(output_ids[0],
                                skip_special_tokens=True)
    print(f"Summarized Text: {output_text}")
    return output_text


def openai_summerizer(content):
    openai.api_key = "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"

    prompt_content = "Can you provide a comprehensive summary of the given text? The summary should cover all the key points and main ideas presented in the original text, while also condensing the information into a concise and easy-to-understand format. Please ensure that the summary includes relevant details and examples that support the main ideas, while avoiding any unnecessary information or repetition. The length of the summary should be appropriate for the length and complexity of the original text, providing a clear and accurate overview without omitting any important information. Please find the text here:" + content

    response = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = prompt_content,
                        max_tokens = 150,
                        temperature = 0.2)

    summerized_content = response['choices'][0]['text']

    print(summerized_content)
    
    return summerized_content

if __name__=='__main__':
    with open('content.txt', 'r', encoding='utf-8') as infile:
        data = infile.read()
        
    openai_summerizer(data)


    
    