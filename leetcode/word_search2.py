class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True # mark end of word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        if not board or not words:
            return result

        rows = len(board)
        cols = len(board[0])

        # add words to new trie
        trie = Trie()
        for word in words:
            trie.add(word)

        def dfs(i,j,node,word):
            # need 'node' to check if prefix exists in tree
            # no need to carry copy of board since we're using only 1 version of the board
            # word to carry sub-string
            if node.is_word:
                result.append(word)
                node.is_word = False # for future searches with similar prefixes eg. 'at', 'atop'

            if i not in range(rows) or j not in range(cols) or board[i][j] == '0':
                return # exceeds bounds or already visiting

            char = board[i][j]
            # check if current char exists in children of node
            # if it doesn't there's no prefix with the current char included in the word and there's no point of continuing
            node = node.children.get(char)
            if not node:
                return

            # add current char to substring
            word += char
            board[i][j] = '0' # mark as visiting

            # explore neighbors
            dfs(i,j+1,node,word)
            dfs(i,j-1,node,word)
            dfs(i+1,j,node,word)
            dfs(i-1,j,node,word)

            # put original value back after visiting
            board[i][j] = char

        # do a dfs on every node
        node = trie.root
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,node,'')
        return result
