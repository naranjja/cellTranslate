from google.cloud import translate
import pandas as pd

def perform_translation(el):
    result = translate_client.translate(
        el,
        source_language=settings['SOURCE_LANG'],
        target_language=settings['TARGET_LANG'])
    return str(result['translatedText'])


if __name__ == '__main__':
    
    translate_client = translate.Client()
    
    with open('./settings.conf') as f:
        settings = {k:v for k, v in (_.split('=') for _ in [_.strip() for _ in f.readlines()]) }
    
    col = pd.read_excel('./input/{}.xlsx'.format(settings['FILENAME']), use_cols=settings['COLUMN'])
    
    col = col.apply(perform_translation)
    
    print(col)
