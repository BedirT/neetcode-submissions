class Node:
    def __init__(self, char, is_complete=False):
        self.char = char
        self.is_complete = is_complete
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        node = self.root
        for idx, ch in enumerate(word):
            if ch in node.children:
                node = node.children[ch]
                if idx == len(word)-1:
                    node.is_complete = True
            else:
                # create the node
                child_node = Node(ch, idx==len(word)-1)
                node.children[ch] = child_node
                node = child_node

    def _look_up_w_end(self, prefix: str) -> tuple:
        node = self.root
        for idx, ch in enumerate(prefix):
            if ch not in node.children:
                return (False, False)
            node = node.children[ch]
        return (True, node.is_complete)
                
    def search(self, word: str) -> bool:
        res = self._look_up_w_end(word)
        return res[0] and res[1]

    def startsWith(self, prefix: str) -> bool:
        return self._look_up_w_end(prefix)[0]
        
        