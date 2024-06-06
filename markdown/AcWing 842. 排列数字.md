# [AcWing 842. 排列数字](https://www.acwing.com/problem/content/844/)

## 题目描述

给定一个整数 𝑛，将数字 1∼𝑛 排成一排，将会有很多种排列方法。

现在，请你按照字典序将所有的排列方法输出。

**输入格式**

共一行，包含一个整数 𝑛。

**输出格式**

按字典序输出所有排列方案，每个方案占一行。

**数据范围**

1≤𝑛≤7

**输入样例**：

```cpp
3
```

**输出样例**：

```cpp
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 10;
int n, path[N];
bool st[N]; // 状态数组

void dfs(int u) {
    if (u == n)// 递归到最后一个数字
    {
        for (int i = 0; i < n; i++) printf("%d ", path[i]); // 输出保存的结果
        puts(" ");
    }

    for (int i = 1; i <= n; i++)
        if (!st[i]) // 没有被用过的数
        {
            path[u] = i;
            st[i] = true; // i被用过
            dfs(u + 1);// 走到下一层
            st[i] = false;// 恢复现场
        }
}

int main() {
    scanf("%d", &n);
    dfs(0);
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 10;

int n;
int path[N];

void dfs(int u, int state) {
    if (u == n) {
        for (int i = 0; i < n; i++) printf("%d ", path[i]);
        puts("");

        return;
    }

    for (int i = 0; i < n; i++)
        if (!(state >> i & 1)) {
            path[u] = i + 1;
            dfs(u + 1, state + (1 << i));
        }
}

int main() {
    scanf("%d", &n);

    dfs(0, 0);

    return 0;
}
```

`state`变量通过位运算来跟踪哪些数字已经被使用过。我们可以通过一个简单的例子来详细说明这一过程：

假设我们要找出 1 到 3 的所有排列。

**初始化**

- `state`初始化为 0（二进制表示为`000`），表示没有任何数字被使用。

**第一层递归**

我们从数字 1 开始尝试，直到数字 3。

- 尝试数字 1:
  - 检查数字 1 是否已使用：`state >> 0 & 1` （即`000 >> 0 & 1`）结果为 0，表示数字 1 未使用。
  - 更新`state`：`state + (1 << 0)`（即`000 + 001`），现`state`变为`001`，表示数字 1 已使用。
  - 进入下一层递归。

**第二层递归**

此时，`state`为`001`，表示数字 1 已被使用。

- 尝试数字 1:
  - 检查数字 1 是否已使用：`state >> 0 & 1` （即`001 >> 0 & 1`）结果为 1，跳过。
- 尝试数字 2:
  - 检查数字 2 是否已使用：`state >> 1 & 1` （即`001 >> 1 & 1`）结果为 0，表示数字 2 未使用。
  - 更新`state`：`state + (1 << 1)`（即`001 + 010`），现`state`变为`011`，表示数字 1 和 2 已使用。
  - 进入下一层递归。

**第三层递归**

此时，`state`为`011`。

- 尝试数字 1:
  - 检查数字 1 是否已使用：`state >> 0 & 1` （即`011 >> 0 & 1`）结果为 1，跳过。
- 尝试数字 2:
  - 检查数字 2 是否已使用：`state >> 1 & 1` （即`011 >> 1 & 1`）结果为 1，跳过。
- 尝试数字 3:
  - 检查数字 3 是否已使用：`state >> 2 & 1` （即`011 >> 2 & 1`）结果为 0，表示数字 3 未使用。
  - 更新`state`：`state + (1 << 2)`（即`011 + 100`），现`state`变为`111`，表示数字 1、2 和 3 已使用。
  - 找到排列：1 2 3。

**回溯**

完成当前分支后，递归函数将结束当前层的执行并返回上一层，同时`state`的值也会恢复到进入当前层之前的状态（通过局部变量的作用域自然实现），这样就可以继续尝试其他的数字组合。

## Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N = 10

var (
	n      int
	path   [N]int
	st     [N]bool
	writer = bufio.NewWriter(os.Stdout)
)

func dfs(u int) {
	if u == n {
		for i := 0; i < n; i++ {
			writer.WriteString(fmt.Sprintf("%d ", path[i]))
		}
		writer.WriteString("\n")
		return
	}

	for i := 1; i <= n; i++ {
		if !st[i] {
			path[u] = i
			st[i] = true
			dfs(u + 1)
			st[i] = false
		}
	}
}

func main() {
	defer writer.Flush()
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n)

	dfs(0)
}
```

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N = 10

var (
	n      int
	path   [N]int
	writer = bufio.NewWriter(os.Stdout)
)

func dfs(u int, state int) {
	if u == n {
		for i := 0; i < n; i++ {
			writer.WriteString(fmt.Sprintf("%d ", path[i]))
		}
		writer.WriteString("\n")
		return
	}

	for i := 0; i < n; i++ {
		if (state>>i)&1 == 0 {
			path[u] = i + 1
			dfs(u+1, state|(1<<i))
		}
	}
}

func main() {
	defer writer.Flush()
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n)

	dfs(0, 0)
}
```

