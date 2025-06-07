from textnode import TextNode, TextType


def main():
    textNode = TextNode("This is some text", TextType.LINK, "https://www.boot.dev")
    print(textNode)

main()