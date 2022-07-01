import os

from pymdocx.common.utils import get_doc, print_xml_node
from pymdocx.doc.table import merge_table_comment_revision

DIR_PATH = './../data/test_table'
OUTPUT_PATH = './../data/output'


def test_merge_table_comment_revision():
    doc_o_path = os.path.join(DIR_PATH, 't_base.docx')
    doc_a_path = os.path.join(DIR_PATH, 't_base_1.docx')
    doc_b_path = os.path.join(DIR_PATH, 't_base_2.docx')
    output_file_path = os.path.join(DIR_PATH, "t_base_new.docx")

    doc_o = get_doc(doc_o_path)
    doc_a = get_doc(doc_a_path)
    doc_b = get_doc(doc_b_path)
    merge_table_comment_revision(doc_o, [doc_a, doc_b])
    doc_o.save(output_file_path)


def test_table_xml():
    doc_a_path = os.path.join(DIR_PATH, 'a.docx')
    doc_a = get_doc(doc_a_path)
    table = doc_a.tables[0]
    print_xml_node(table._element)