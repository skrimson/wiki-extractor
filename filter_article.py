import json
import sys
from xml.etree import ElementTree
import xmltodict

WIKIPEDIA_NAMESPACE = 'http://www.mediawiki.org/xml/export-0.10/'

output = "./wiki.text"


def translate_path(path):
    return '/'.join('{%s}%s' % (WIKIPEDIA_NAMESPACE, tag) for tag in path.split('/'))


if __name__ == "__main__":
    ids = []
    with open(sys.argv[1], mode="r") as f:
        for line in f:
            line = line.strip()
            ids.append(line)
    ids = set(ids)
    page_tag = translate_path('page')
    text_tag = translate_path('revision/text')
    title_tag = translate_path('title')
    page_id_tag = translate_path('id')
    ElementTree.register_namespace('', WIKIPEDIA_NAMESPACE)
    with open(sys.argv[2], mode="rt") as xm2f:
        context = ElementTree.iterparse(xm2f, events=('start', 'end'))
        event, root = next(context)
        with open(output, mode="a") as o:
            for event, element in context:
                if event == 'end' and element.tag == page_tag:
                    if element.findtext(page_id_tag) in ids:
                        ##### to json
                        # print(json.dumps(
                        #     xmltodict.parse(ElementTree.tostring(element, encoding="unicode")),
                        #     ensure_ascii=False))

                        ##### to text
                        temp_dict = xmltodict.parse(ElementTree.tostring(element, encoding="unicode"))
                        o.write(temp_dict['page']['title'] + "\n" + temp_dict['page']['revision']['text']['#text'])

                    root.clear()
