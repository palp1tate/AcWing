# [AcWing 837. 连通块中点的数量](https://www.acwing.com/problem/content/839/)

## 题目描述

给定一个包含 𝑛 个点（编号为 1∼𝑛）的无向图，初始时图中没有边。

现在要进行 𝑚 个操作，操作共有三种：

1. `C a b`，在点 𝑎 和点 𝑏 之间连一条边，𝑎 和 𝑏 可能相等；
2. `Q1 a b`，询问点 𝑎 和点 𝑏 是否在同一个连通块中，𝑎 和 𝑏 可能相等；
3. `Q2 a`，询问点 𝑎 所在连通块中点的数量；

**输入格式**

第一行输入整数 𝑛 和 𝑚。

接下来 𝑚 行，每行包含一个操作指令，指令为 `C a b`，`Q1 a b` 或 `Q2 a` 中的一种。

**输出格式**

对于每个询问指令 `Q1 a b`，如果 𝑎 和 𝑏 在同一个连通块中，则输出 `Yes`，否则输出 `No`。

对于每个询问指令 `Q2 a`，输出一个整数表示点 𝑎 所在连通块中点的数量

每个结果占一行。

**数据范围**

1≤𝑛,𝑚≤10^5

**输入样例**：

```cpp
5 5
C 1 2
Q1 1 2
Q2 1
C 2 5
Q2 5
```

**输出样例**：

```cpp
Yes
2
3
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int n, m;
int p[N], cnt[N];

int find(int x) {
    if (p[x] != x) p[x] = find(p[x]);
    return p[x];
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        p[i] = i;
        cnt[i] = 1;
    }

    while (m--) {
        char op[3];
        int a, b;
        scanf("%s", op);

        if (op[0] == 'C') {
            scanf("%d%d", &a, &b);
            if (find(a) == find(b)) continue;
            cnt[find(b)] += cnt[find(a)];
            p[find(a)] = find(b);
        } else if (op[1] == '1') {
            scanf("%d%d", &a, &b);
            if (find(a) == find(b)) puts("Yes");
            else puts("No");
        } else {
            scanf("%d", &a);
            printf("%d\n", cnt[find(a)]);
        }
    }

    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int n, m;
int p[N], cnt[N];

int find(int x) {
    if (p[x] != x) p[x] = find(p[x]);
    return p[x];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        p[i] = i;
        cnt[i] = 1;
    }

    while (m--) {
        string op;
        int a, b;
        cin >> op;

        if (op == "C") {
            cin >> a >> b;
            a = find(a), b = find(b);
            if (a != b) {
                p[a] = b;
                cnt[b] += cnt[a];
            }
        } else if (op == "Q1") {
            cin >> a >> b;
            if (find(a) == find(b)) cout << "Yes" << endl;
            else cout << "No" << endl;;
        } else {
            cin >> a;
            cout << cnt[find(a)] << endl;
        }
    }

    return 0;
}
```

## Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N = 100010

var (
	n, m int
	p    [N]int
	cnt  [N]int
)

func find(x int) int {
	if p[x] != x {
		p[x] = find(p[x])
	}
	return p[x]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscan(reader, &n, &m)

	for i := 1; i <= n; i++ {
		p[i] = i
		cnt[i] = 1
	}

	for m > 0 {
		m--
		var op string
		var a, b int
		fmt.Fscan(reader, &op)

		if op == "C" {
			fmt.Fscan(reader, &a, &b)
			a = find(a)
			b = find(b)
			if a != b {
				p[a] = b
				cnt[b] += cnt[a]
			}
		} else if op == "Q1" {
			fmt.Fscan(reader, &a, &b)
			if find(a) == find(b) {
				fmt.Fprintln(writer, "Yes")
			} else {
				fmt.Fprintln(writer, "No")
			}
		} else if op == "Q2" {
			fmt.Fscan(reader, &a)
			fmt.Fprintln(writer, cnt[find(a)])
		}
	}
}
```

## 模板

```cpp
(1)朴素并查集：

    int p[N]; //存储每个点的祖宗节点

    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }

    // 初始化，假定节点编号是1~n
    for (int i = 1; i <= n; i ++ ) p[i] = i;

    // 合并a和b所在的两个集合：
    p[find(a)] = find(b);


(2)维护size的并查集：

    int p[N], size[N];
    //p[]存储每个点的祖宗节点, size[]只有祖宗节点的有意义，表示祖宗节点所在集合中的点的数量

    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }

    // 初始化，假定节点编号是1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        size[i] = 1;
    }

    // 合并a和b所在的两个集合：
    size[find(b)] += size[find(a)];
    p[find(a)] = find(b);


(3)维护到祖宗节点距离的并查集：

    int p[N], d[N];
    //p[]存储每个点的祖宗节点, d[x]存储x到p[x]的距离

    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x)
        {
            int u = find(p[x]);
            d[x] += d[p[x]];
            p[x] = u;
        }
        return p[x];
    }

    // 初始化，假定节点编号是1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        d[i] = 0;
    }

    // 合并a和b所在的两个集合：
    p[find(a)] = find(b);
    d[find(a)] = distance; // 根据具体问题，初始化find(a)的偏移量
```

