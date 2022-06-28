import os

from pymdocx.common.comment import parse_p_comment

from pymdocx.common.utils import get_doc, print_xml_node
from pymdocx.doc.table import merge_table_comment_revision
from pymdocx.doc.paragraph import merge_paragraph_comment_revision

DIR_PATH = './../data/test_p'


def test_merge_table_comment_revision():
    doc_o_path = os.path.join(DIR_PATH, 'pt0_0.docx')
    doc_a_path = os.path.join(DIR_PATH, 'pt0_a.docx')
    # doc_b_path = os.path.join(DIR_PATH, 'table_b.docx')
    doc_o = get_doc(doc_o_path)
    doc_a = get_doc(doc_a_path)
    # doc_b = get_doc(doc_b_path)
    # merge_paragraph_comment_revision(doc_o, [doc_a])
    # merge_table_comment_revision(doc_o, [doc_a])
    print(1)
    # comment_list = parse_p_comment(doc_a.paragraphs[0])
    # for c in comment_list:data/test_p/xml/new_doc_base.xml
    #     doc_o.paragraphs[0].add_comment(c['comment_text'],
    #                                     author=c['author'],
    #                                     dtime=c['dtime'],
    #                                     rangeStart=1,
    #                                     rangeEnd=2)
    # doc_o.save('table_new.docx')
    doc_o = get_doc('table_new.docx')
    print(1)
    print_xml_node(doc_o._body._element)


def test_table_xml():
    doc_a_path = os.path.join(DIR_PATH, 'a.docx')
    doc_a = get_doc(doc_a_path)
    table = doc_a.tables[0]
    print_xml_node(table._element)