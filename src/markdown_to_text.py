from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    def is_odd(num):
        if num % 2 == 1:
            return True
        return False
    
    new_nodes = []

    for node in old_nodes:
    
        if node.text_type is not TextType.TEXT:
           new_nodes.append(node)
           continue

        new_node_list = node.text.split(delimiter)

        if len(new_node_list) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        for i in new_node_list:
            if i == "":
                continue

            if not is_odd(new_node_list.index(i)):
                new_nodes.append(TextNode(i, TextType.TEXT, None))

            else:
                new_nodes.append(TextNode(i, text_type, None))
            
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return matches
