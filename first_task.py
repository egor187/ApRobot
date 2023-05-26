import spacy
from itertools import chain
from collections import Counter

nlp = spacy.load('en_core_web_sm')


def main(text):
    nlp_text = nlp(text)
    is_digit_token_count = list(chain.from_iterable([token.text.split('/') for token in nlp_text if token.is_digit or '/' in token.text]))
    is_propn_token_count = [token for token in nlp_text if token.pos_ == 'PROPN']
    result = Counter(is_digit_token_count) | Counter(is_propn_token_count)
    start_table = f"""<html>
                <head>
                <title>output</title>
                </head>
                <body>
                    <table>
                        <tr><th>Entry</th><th>Count</th></tr>
                """

    end_table = """
                    </table>
                    </body>
                    </html>
                """
    for k, v in result.items():
        start_table += f'<tr><td>{k}</td><td>{v}</td></tr>'

    with open('output.html', mode='w') as output:
        output.write(
            start_table + end_table
        )


if __name__ == '__main__':
    main(input())
