from unittest import TestCase
from htmlnode import HTMLNode, LeafNode

test_prop = {
    "href": "https://www.google.com",
    "target": "_blank",
}

test_prop_2 = {
    "href": "https://www.github.com",
    "target": "_blank",
}

class TestHtmlNode(TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_props_to_html_eq(self):
        node1 = HTMLNode(props=test_prop)
        node2 = HTMLNode(props=test_prop)
        self.assertEqual(node1.props_to_html(), node2.props_to_html())
    
    def test_props_to_html_not_eq(self):
        node1 = HTMLNode(props = test_prop)
        node2 = HTMLNode(props = test_prop_2)
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_rep(self):
        node = HTMLNode('p', 'This is a paragraph', None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(
            "tag - p\nvalue - This is a paragraph\nchildren - None\nprops - {'class': 'greeting', 'href': 'https://boot.dev'}",
            repr(node)
            )
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_no_tag(self):
        node = LeafNode(None, "Just a text")
        self.assertEqual(node.to_html(), "Just a text")
