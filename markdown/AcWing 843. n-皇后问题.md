# [AcWing 843. n-皇后问题](https://www.acwing.com/problem/content/845/)

## 题目描述

𝑛−皇后问题是指将 𝑛 个皇后放在 𝑛×𝑛 的国际象棋棋盘上，使得皇后不能相互攻击到，即任意两个皇后都不能处于同一行、同一列或同一斜线上。

![1_597ec77c49-8-queens.png](https://cdn.jsdelivr.net/gh/palp1tate/ImgPicGo/img/19_860e00c489-1_597ec77c49-8-queens.png)

现在给定整数 𝑛，请你输出所有的满足条件的棋子摆法。

**输入格式**

共一行，包含整数 𝑛。

**输出格式**

每个解决方案占 𝑛 行，每行输出一个长度为 𝑛 的字符串，用来表示完整的棋盘状态。

其中 `.` 表示某一个位置的方格状态为空，`Q` 表示某一个位置的方格上摆着皇后。

每个方案输出完成后，输出一个空行。

**注意：行末不能有多余空格。**

输出方案的顺序任意，只要不重复且没有遗漏即可。

**数据范围**

1≤𝑛≤9

**输入样例**：

```cpp
4
```

**输出样例**：

```cpp
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..
    
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 20;

int n;
char g[N][N];
bool col[N], dg[N * 2], udg[N * 2];

void dfs(int u) {
    if (u == n) {
        for (int i = 0; i < n; i++) puts(g[i]);
        puts("");
        return;
    }

    for (int i = 0; i < n; i++)
        if (!col[i] && !dg[n + u - i] && !udg[u + i]) {
            g[u][i] = 'Q';
            col[i] = dg[n + u - i] = udg[u + i] = true;
            dfs(u + 1);
            col[i] = dg[n + u - i] = udg[u + i] = false;
            g[u][i] = '.';
        }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            g[i][j] = '.';

    dfs(0);

    return 0;
}
```

为了实现这一点，我们使用了三个布尔数组：`col`、`dg` 和 `udg` 来分别标记列、主对角线和副对角线上是否有皇后。

具体来说：

- `col[i]` 表示第 `i` 列是否有皇后。
- `dg[i]` 表示主对角线上是否有皇后。
- `udg[i]` 表示副对角线上是否有皇后。

**主对角线（dg）**

主对角线是从左上到右下的对角线。对于一个棋盘上的位置 `(x, y)`，在主对角线上，所有位置 `(x, y)` 满足 `x - y` 是相同的。为了防止负数索引，我们调整这个索引值为 `n + (x - y)`，其中 `n` 是棋盘的大小。

因此，对于位置 `(x, y)`，在主对角线上使用的索引是 `dg[n + x - y]`。例如，对于一个 8x8 的棋盘（即 `n=8`），位置 `(0, 0)` 的 `dg` 索引是 `8 + 0 - 0 = 8`，位置 `(1, 0)` 的 `dg` 索引是 `8 + 1 - 0 = 9`。

**副对角线（udg）**

副对角线是从右上到左下的对角线。对于一个棋盘上的位置 `(x, y)`，在副对角线上，所有位置 `(x, y)` 满足 `x + y` 是相同的。

因此，对于位置 `(x, y)`，在副对角线上使用的索引是 `udg[x + y]`。例如，对于一个 8x8 的棋盘，位置 `(0, 7)` 的 `udg` 索引是 `0 + 7 = 7`，位置 `(1, 6)` 的 `udg` 索引是 `1 + 6 = 7`。

## Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N = 20

var (
	n   int
	g   [N][N]byte
	col [N]bool
	dg  [N * 2]bool
	udg [N * 2]bool
	out *bufio.Writer
)

func dfs(u int) {
	if u == n {
		for i := 0; i < n; i++ {
			out.Write(g[i][:n])
			out.WriteByte('\n')
		}
		out.WriteByte('\n')
		return
	}

	for i := 0; i < n; i++ {
		if !col[i] && !dg[n+u-i] && !udg[u+i] {
			{
				g[u][i] = 'Q'
				col[i] = true
				dg[n+u-i] = true
				udg[u+i] = true
			}
			dfs(u + 1)
			{
				col[i] = false
				dg[n+u-i] = false
				udg[u+i] = false
				g[u][i] = '.'
			}
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			g[i][j] = '.'
		}
	}

	dfs(0)
}
```

