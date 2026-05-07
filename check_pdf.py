import fitz
try:
    doc = fitz.open(r'C:\Users\Admin\Downloads\LSD\file1.pdf')
    page = doc[0]
    blocks = page.get_text('dict')['blocks']
    text_blocks = [b for b in blocks if b['type'] == 0]
    if len(text_blocks) > 0:
        print('PDF has text. Example of first text block spans:')
        for l in text_blocks[0]['lines']:
            for s in l['spans']:
                print(f"Text: '{s['text']}', Font: {s['font']}, Size: {s['size']}, Color: {s['color']}")
    else:
        print('PDF does NOT have text. It might be scanned images.')
except Exception as e:
    print('Error:', e)
