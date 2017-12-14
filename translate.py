from google.cloud import translate
import pandas as pd


def perform_translation(string):
    result = translate_client.translate(
        string,
        source_language=settings['SOURCE_LANG'],
        target_language=settings['TARGET_LANG'])
    return result['translatedText']


if __name__ == '__main__':
    
    try:
        print('\n- Initializing translation service...')
        translate_client = translate.Client()
        
        with open('./settings.conf') as f:
            settings = {
                k: v for k, v in (
                    _.split('=') for _ in [
                        _.strip() for _ in f.readlines()
                    ]
                ) 
            }
        
        print('- Reading spreadsheet...')
        df = pd.read_excel('./input/{}.xlsx'.format(settings['FILENAME']))
        
        print('- Translating...')
        df[settings['COLUMN']] = \
            df[settings['COLUMN']].apply(perform_translation)
        
        print('- Saving changes to output folder...')
        df.to_excel(
            './output/{}.xlsx'.format(settings['FILENAME']), 
            index=False)
        
    except Exception as e:
        raise e

    print('Done!')
