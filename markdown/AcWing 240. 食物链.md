# [AcWing 240. 食物链](https://www.acwing.com/problem/content/242/)

## 题目描述

动物王国中有三类动物 𝐴,𝐵,𝐶，这三类动物的食物链构成了有趣的环形。

𝐴 吃 𝐵，𝐵 吃 𝐶，𝐶 吃 𝐴。

现有 𝑁 个动物，以 1∼𝑁 编号。

每个动物都是 𝐴,𝐵,𝐶 中的一种，但是我们并不知道它到底是哪一种。

有人用两种说法对这 𝑁 个动物所构成的食物链关系进行描述：

第一种说法是 `1 X Y`，表示 𝑋 和 𝑌 是同类。

第二种说法是 `2 X Y`，表示 𝑋 吃 𝑌。

此人对 𝑁 个动物，用上述两种说法，一句接一句地说出 𝐾 句话，这 𝐾 句话有的是真的，有的是假的。

当一句话满足下列三条之一时，这句话就是假话，否则就是真话。

1. 当前的话与前面的某些真的话冲突，就是假话；
2. 当前的话中 𝑋 或 𝑌 比 𝑁 大，就是假话；
3. 当前的话表示 𝑋 吃 𝑋，就是假话。

你的任务是根据给定的 𝑁 和 𝐾 句话，输出假话的总数。

**输入格式**

第一行是两个整数 𝑁 和 𝐾，以一个空格分隔。

以下 K𝐾 行每行是三个正整数 𝐷，𝑋，𝑌，两数之间用一个空格隔开，其中 𝐷 表示说法的种类。

若 𝐷=1，则表示 𝑋 和 𝑌 是同类。

若 𝐷=2，则表示 𝑋 吃 𝑌。

**输出格式**

只有一个整数，表示假话的数目。

**数据范围**

1≤𝑁≤50000,

0≤𝐾≤100000

**输入样例**：

```cpp
100 7
1 101 1 
2 1 2
2 2 3 
2 3 3 
1 1 3 
2 3 1 
1 5 5
```

**输出样例**：

```cpp
3
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 50010;

int n, m;
int p[N], d[N];

int find(int x) {
    if (p[x] != x) {
        int t = find(p[x]);
        d[x] += d[p[x]];
        p[x] = t;
    }
    return p[x];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (int i = 1; i <= n; i++) p[i] = i;

    int res = 0;
    while (m--) {
        int t, x, y;
        cin >> t >> x >> y;

        if (x > n || y > n) res++;
        else {
            int px = find(x), py = find(y);
            if (t == 1) {
                if (px == py && (d[x] - d[y]) % 3) res++;
                else if (px != py) {
                    p[px] = py;
                    d[px] = d[y] - d[x];
                }
            } else {
                if (px == py && (d[x] - d[y] - 1) % 3) res++;
                else if (px != py) {
                    p[px] = py;
                    d[px] = d[y] + 1 - d[x];
                }
            }
        }
    }

    cout << res;

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

const N = 50010

var (
	n, m int
	p    [N]int
	d    [N]int
)

func find(x int) int {
	if p[x] != x {
		t := find(p[x])
		d[x] += d[p[x]]
		p[x] = t
	}
	return p[x]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanf(reader, "%d %d\n", &n, &m)

	for i := 1; i <= n; i++ {
		p[i] = i
	}

	res := 0
	for i := 0; i < m; i++ {
		var t, x, y int

		fmt.Fscanf(reader, "%d %d %d\n", &t, &x, &y)

		if x > n || y > n {
			res++
		} else {
			px := find(x)
			py := find(y)
			if t == 1 {
				if px == py && (d[x]-d[y])%3 != 0 {
					res++
				} else if px != py {
					p[px] = py
					d[px] = d[y] - d[x]
				}
			} else {
				if px == py && (d[x]-d[y]-1)%3 != 0 {
					res++
				} else if px != py {
					p[px] = py
					d[px] = d[y] + 1 - d[x]
				}
			}
		}
	}

	fmt.Fprintln(writer, res)
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

