# [AcWing 836. 合并集合](https://www.acwing.com/problem/content/838/)

## 题目描述

一共有 𝑛 个数，编号是 1∼𝑛，最开始每个数各自在一个集合中。

现在要进行 𝑚 个操作，操作共有两种：

1. `M a b`，将编号为 𝑎 和 𝑏 的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
2. `Q a b`，询问编号为 𝑎 和 𝑏 的两个数是否在同一个集合中；

**输入格式**

第一行输入整数 𝑛 和 𝑚。

接下来 𝑚 行，每行包含一个操作指令，指令为 `M a b` 或 `Q a b` 中的一种。

**输出格式**

对于每个询问指令 `Q a b`，都要输出一个结果，如果 𝑎 和 𝑏 在同一集合内，则输出 `Yes`，否则输出 `No`。

每个结果占一行。

**数据范围**

1≤𝑛,𝑚≤10^5

**输入样例**：

```cpp
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
```

**输出样例**：

```cpp
Yes
No
Yes
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int fa[N]; // 存储每个元素的父节点，用于表示不相交集合中的集合

// 查找元素 x 所在集合的根节点（即代表元素）
int find(int x) {
    // 如果当前元素的父节点不是自身，则递归查找根节点，并进行路径压缩
    if (fa[x] != x) fa[x] = find(fa[x]);
    return fa[x];
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);

    // 初始化不相交集合，每个元素初始时父节点为自身
    for (int i = 1; i <= n; i++) fa[i] = i;

    while (m--) {
        char op[2];
        int a, b;
        scanf("%s%d%d", op, &a, &b);

        // 如果操作是合并 ('M')，将包含元素 'a' 和 'b' 的集合合并
        if (op[0] == 'M') fa[find(a)] = find(b);
        else {
            // 如果操作是查询 ('Q')，检查元素 'a' 和 'b' 是否属于同一个集合
            if (find(a) == find(b)) puts("Yes");
            else puts("No");
        }
    }

    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int fa[N]; // 存储每个元素的父节点，用于表示不相交集合中的集合

// 查找元素 x 所在集合的根节点（即代表元素）
int find(int x) {
    // 如果当前元素的父节点不是自身，则递归查找根节点，并进行路径压缩
    if (fa[x] != x) fa[x] = find(fa[x]);
    return fa[x];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // 初始化不相交集合，每个元素初始时父节点为自身
    for (int i = 1; i <= n; i++) fa[i] = i;

    while (m--) {
        char op;
        int a, b;
        cin >> op >> a >> b;

        // 如果操作是合并 ('M')，将包含元素 'a' 和 'b' 的集合合并
        if (op == 'M') fa[find(a)] = find(b);
        else {
            // 如果操作是查询 ('Q')，检查元素 'a' 和 'b' 是否属于同一个集合
            if (find(a) == find(b)) cout << "Yes" << endl;
            else cout << "No" << endl;;
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

var fa [N]int

func find(x int) int {
	if fa[x] != x {
		fa[x] = find(fa[x])
	}
	return fa[x]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscanf(reader, "%d %d\n", &n, &m)

	for i := 1; i <= n; i++ {
		fa[i] = i
	}

	for ; m > 0; m-- {
		var op byte
		var a, b int
		fmt.Fscanf(reader, "%c %d %d\n", &op, &a, &b)

		if op == 'M' {
			fa[find(a)] = find(b)
		} else {
			if find(a) == find(b) {
				fmt.Fprintln(writer, "Yes")
			} else {
				fmt.Fprintln(writer, "No")
			}
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

