from google.cloud import translate
from time import time
import pandas as pd


def perform_translation(string):
    result = translate_client.translate(
        string,
        source_language=settings['SOURCE_LANG'],
        target_language=settings['TARGET_LANG'])
    return result['translatedText']


def main():        
    if settings['FILENAME'].endswith('.xlsx'):
        print('\n- Reading spreadsheet...')
        df = pd.read_excel('./input/{}'.format(settings['FILENAME']))
        print('Succesfully loaded {} by {} matrix!'.format(
            df.shape[0], df.shape[1]
        ))
    else:
        print('The service can only translate spreadsheet files for now!')
        return
    
    print('\n- Translating...')
    df[settings['COLUMN']] = \
        df[settings['COLUMN']].apply(perform_translation)
    print('Finished translating {} strings!'.format(df.shape[0]))
    
    print('\n- Saving changes to output folder...')
    df.to_excel(
        './output/{}'.format(settings['FILENAME']), 
        index=False)
    print('Saved results to ./output/{}!'.format(
        settings['FILENAME']
    ))


if __name__ == '__main__':
    
    start_time = time()
    
    print('\n- Initializing translation service...')
    translate_client = translate.Client()
    print('Service initialized correctly!')
    
    with open('./settings.conf') as f:
        settings = {
            k: v for k, v in (
                _.split('=') for _ in [
                    _.strip() for _ in f.readlines()
                ]
            ) 
        }
    f.close()
    
    try:
        main()
    except Exception as e:
        raise e

    print('\nProcess finished in {} seconds!'.format(
        round(time() - start_time, 2)
    ))
