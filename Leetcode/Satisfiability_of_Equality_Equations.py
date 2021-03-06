# Solution1 : DFS
# Time : O(N), Space: O(N)

# Solution2 : Union-find. 'a == b'에 해당되는 각 노드들을 일렬(a가 parent)로 연결. 
# 그 이후, 'a != b'를 체크할때 a의 root와 b의 root가 같으면 False를 리턴.
# Time : O(N), Space : O(N)

from collections import defaultdict
import string

class Solution:
    def equationsPossible_2(self, equations: List[str]) -> bool:
        def find(c: str) -> str:
            if colors[c] != c:
                return find(colors[c])
            return c
            
        colors = {c : c for c in string.ascii_lowercase}
        for e in equations:
            if e[1] == "=":
                colors[find(e[0])] = find(e[3])         
        return not any(e[1] == "!" and find(e[0]) == find(e[3]) for e in equations)
    
    def equationsPossible_1(self, equations: List[str]) -> bool:
        def canMeet(src, dst, visited):
            if src == dst:
                return True            
            visited[src] = True
            for a in graph[src]:
                if visited[a]:
                    continue
                if canMeet(a, dst, visited):
                    return True
            return False
        
        graph = defaultdict(list)
        for e in equations:
            if e[1] == "=":
                graph[e[0]].append(e[3])
                graph[e[3]].append(e[0])
                
        for e in equations:
            if e[1] == "!":
                if canMeet(e[0], e[3], defaultdict(lambda: False)):
                    return False
        return True
