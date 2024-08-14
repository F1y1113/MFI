from langchain_community.llms import Ollama
import os
import glob
import re
import argparse

def main(input_dir, prompt_dir, output_dir, promptID, mode, ID):
    if mode == 'single':
        paper_dir = input_dir + ID + '.txt'
        paperID = ID
        test_dir = '/home/aikes/SDFconversion/test'
        with open(paper_dir, 'r') as tex:
            text_con = tex.read()
                
        with open(os.path.join(prompt_dir, promptID + '.txt'), 'r') as tex:
            prompt = tex.read()

        prompt = prompt.replace('{}_Paragraphs_provided', text_con) 
        llm = Ollama(model="llama3")
        
        result = llm.invoke(prompt)
        match = re.search(r'\n(.*)\n', result, re.DOTALL)
        if match:
            result = match.group(1)

        with open(os.path.join(test_dir, paperID + '_l3.txt'), 'w', encoding='utf-8') as file:
            file.write(result)
        print(paperID + ' finished!')
        
    else:
        input_hs = glob.glob(input_dir + '*.txt')
        for paper_dir in input_hs:
            paperID = paper_dir.split('/')[5].replace('.txt', '')
            with open(paper_dir, 'r') as tex:
                text_con = tex.read()
                    
            with open(os.path.join(prompt_dir, promptID + '.txt'), 'r') as tex:
                prompt = tex.read()

            prompt = prompt.replace('{}_Paragraphs_provided', text_con) 
            llm = Ollama(model="llama3")
            
            result = llm.invoke(prompt)
            match = re.search(r'\n(.*)\n', result, re.DOTALL)
            if match:
                result = match.group(1)

            with open(os.path.join(output_dir, paperID + '_l3.txt'), 'w', encoding='utf-8') as file:
                file.write(result)
            print(paperID + ' finished!')
    
def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default='/home/aikes/SDFconversion/raw_paragraph/', type=str)
    parser.add_argument("--prompt_dir", default='/home/aikes/SDFconversion/prompt', type=str)
    parser.add_argument("--output_dir", default='/home/aikes/SDFconversion/hs_txt_llama3_3b', type=str)
    parser.add_argument("--promptID", default='prompt_4', type=str)
    parser.add_argument("--mode", default='multi', type=str)
    parser.add_argument("--ID", default='paper1', type=str) 
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = _parse_args()
    
    main(args.input_dir, args.prompt_dir, args.output_dir, args.promptID, args.mode, args.ID)
