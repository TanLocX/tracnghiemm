
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\vscode\code\TN_MMT\lichsudang\file3_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Total questions:', len(data))
for i in [0, 1, 2, 9, 49, 99, 139]:
    if i < len(data):
        q = data[i]
        print(f'--- Cau {i+1} ---')
        print('Q:', q['question'])
        for opt in q['options']:
            print(' ', opt)
        print('Answer:', repr(q['answer']))
        print()
