
class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        parent = [-1] * n
        timer = 0

        # Iterative DFS: Euler tour and parent information
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))
                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting table
        up = [parent[:]] + [[-1] * n for _ in range(LOG - 1)]

        for j in range(1, LOG):
            prev = up[j - 1]
            cur = up[j]
            for u in range(n):
                p = prev[u]
                if p != -1:
                    cur[u] = prev[p]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0
            while diff:
                if diff & 1:
                    u = up[j][u]
                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick tree supporting point updates and prefix XOR
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            # XOR over Euler positions [0, i]
            if i < 0:
                return 0
            i += 1
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        chars = [1 << (ord(c) - 97) for c in s]

        # Root-to-node character parity at each Euler position.
        # Range XOR update on subtree [tin[u], tout[u]].
        for u in range(n):
            add(tin[u], chars[u])
            add(tout[u] + 1, chars[u])

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)

                delta = chars[u] ^ new_mask
                if delta:
                    add(tin[u], delta)
                    add(tout[u] + 1, delta)
                    chars[u] = new_mask

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                # Root-to-node prefix XOR masks
                pu = prefix(tin[u])
                pv = prefix(tin[v])

                # LCA is included once
                path_mask = pu ^ pv ^ chars[w]

                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans
