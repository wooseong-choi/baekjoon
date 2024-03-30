import Trie_Node
class Trie:
    # Trie 에는 여러가지 함수가 필요합니다.

    # 1. head를 빈노드로 설정
    def __init__(self):
        print('트리(트라이) 생성')
        self.head = Trie_Node.Node(None)

    # 2. insert 함수 - 트리를 생성하기 위한 함수입니다. 입력된 문자열의 문자를 하나씩 children에 확인 후 저장하고 문자열을 다 돌면 마지막 노드의 data에 문자열을 저장합니다.
    def insert(self, string):
        print(f'삽입 실행, 현재 노드 = {self.head}')
        current_node = self.head
        # 문자열 string이 주어질때 해당 문자열의 문자 값이 트리(트라이) 노드에서 연속적으로 존재하는지 확인, 존재하지 않으면 해당 문자값을 노드로 추가하고 현재 노드로 만든다.
        # 문자열의 문자값을 전부 노드로 만든 후, 전체 문자열의 값을 마지막 문자값의 노드에 저장한다. 이는 시작점부터 문자열을 저장한 노드까지의 노드 값을 연결하면 문자열이 된다는 표시이다.
        for char in string:
            if char not in current_node.children:
                print('애만들기')
                current_node.children[char] = Trie_Node.Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    # 3. search 함수 - 문자열이 존재하는지에 대한 여부를 리턴하는 함수입니다. 문자열을 하나씩 돌면서 확인 후 ​마지막 노드가 data가 존재한다면 True를, 그렇지 않거나 애초에 children에 존재하지 않는다면 False를 리턴합니다.
    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
            
        if current_node.data:
            return True
        else:
            return False
      
    # 4. starts_with 함수 - prefix단어로 시작하는 단어를 찾고 배열로 리턴하는 함수입니다. prefix단어까지 tree를 순회 한 이후 그다음부터 data가 존재하는 것들만 배열에 저장​하여 리턴합니다.
    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None
        
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        
        return words

trie = Trie()
word_list = ["frodo", "front", "firefox", "fire"]
for word in word_list:
    trie.insert(word)

print(trie.search("friend"))
# >>False
print(trie.search("frodo"))
# >>True
print(trie.search("fire"))
# >>True
print(trie.starts_with("fire"))
# >>['fire', 'firefox']
print(trie.starts_with("fro"))
# >>['frodo', 'front']
print(trie.starts_with("jimmy"))
# >>None
print(trie.starts_with("f"))
# >>['fire', 'frodo', 'front', 'firefox']