from langchain_community.llms import Ollama
import os
import glob
import re
import argparse

def delete_content_before_word(s, word):
    # Split the string by the specific word
    parts = s.split(word, 1)
    if len(parts) > 1:
        return word + parts[1]
    else:
        return s

def delete_files_in_folder(folder_path):
    if os.path.exists(folder_path):
        # List all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                # Check if it's a file and delete it
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # If it's a directory, you can also delete it and its contents (optional)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'The folder {folder_path} does not exist')
    
def main(modelID, raw_dir, iter_dir, prompt_dir, output_dir, promptID):
    
    input_hs = glob.glob(raw_dir + '*.txt')
    
    delete_files_in_folder(iter_dir)
        
    with open('/home/aikes/SDFconversion/hs_txt/paper1.txt', 'r') as tex:
        default_structure = tex.read()
            
    with open(output_dir + 'llama3_final_iter0.txt', 'w', encoding='utf-8') as file:
        file.write(default_structure)
        
    cnt = 0
    for paper_dir in input_hs:
    
        paperID = paper_dir.split('/')[5].replace('.txt', '')
        with open(paper_dir, 'r') as tex:
            text_con = tex.read()
        
        print("start!!!!" + paperID)
        with open(os.path.join(prompt_dir, promptID + '.txt'), 'r') as tex:
            prompt = tex.read()
            
        with open(iter_dir + 'llama3_final_iter' + str(cnt) + '.txt', 'r') as tex:
            current_structure = tex.read()
        
        cnt += 1

        prompt = prompt.replace('{}_Paragraphs_provided', text_con)
        prompt = prompt.replace('{}.format(Current hierarchical structure)', current_structure)
        
        llm = Ollama(model=modelID)

        result = llm.invoke(prompt)
        match = re.search(r'\n(.*)\n', result, re.DOTALL)
        if match:
            result = match.group(1)
        
        result = delete_content_before_word(result, 'Event 1')

        with open(output_dir + 'llama3_final_iter' + str(cnt) + '.txt', 'w', encoding='utf-8') as file:
            file.write(result)
        print(paperID + ' finished!, result saved in' + output_dir + 'llama3_final_iter' + str(cnt) + '.txt')
    
def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_dir", default='/home/aikes/SDFconversion/raw_paragraph/', type=str)
    parser.add_argument("--iter_dir", default='/home/aikes/SDFconversion/hs_final/hs_final_ll3_3b/', type=str)
    parser.add_argument("--prompt_dir", default='/home/aikes/SDFconversion/prompt', type=str)
    parser.add_argument("--output_dir", default='/home/aikes/SDFconversion/hs_final/hs_final_ll3_3b/', type=str)
    parser.add_argument("--promptID", default='prompt_iterations_v3', type=str)
    parser.add_argument("--modelID", default='llama3', type=str) 
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = _parse_args()
    
    main(args.modelID, args.raw_dir, args.iter_dir, args.prompt_dir, args.output_dir, args.promptID)
