# [AcWing 830. 单调栈](https://www.acwing.com/problem/content/832/)

## 题目描述

给定一个长度为 𝑁 的整数数列，输出每个数左边第一个比它小的数，如果不存在则输出 −1。

**输入格式**

第一行包含整数 𝑁，表示数列长度。

第二行包含 𝑁 个整数，表示整数数列。

**输出格式**

共一行，包含 𝑁 个整数，其中第 𝑖 个数表示第 𝑖 个数的左边第一个比它小的数，如果不存在则输出 −1。

**数据范围**

1≤𝑁≤10^5,

1≤数列中元素≤10^9

**输入样例**：

```cpp
5
3 4 2 7 5
```

**输出样例**：

```cpp
-1 3 -1 2 2
```

## C++

```cpp
#include <iostream>

using namespace std;

const int MAX_SIZE = 100010;

long long stack[MAX_SIZE], top;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int num_elements;
    cin >> num_elements;
    while (num_elements--) {
        int current_element;
        cin >> current_element;
        while (top && stack[top] >= current_element)
            top--;
        if (!top)
            cout << "-1 ";
        else
            cout << stack[top] << " ";
        stack[++top] = current_element;
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

const N int = 1e5 + 10

func main() {
	stack := make([]int64, N)
	top := 0

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscanf(reader, "%d\n", &n)
	for i := 0; i < n; i++ {
		var x int64
		fmt.Fscanf(reader, "%d", &x)
		for top > 0 && stack[top] >= x {
			top--
		}
		if top > 0 {
			fmt.Fprintf(writer, "%d ", stack[top])
		} else {
			fmt.Fprintf(writer, "-1 ")
		}
		top++
		stack[top] = x
	}
}
```

## 模板

```cpp
常见模型：找出每个数左边离它最近的比它大/小的数
int tt = 0;
for (int i = 1; i <= n; i ++ )
{
    while (tt && check(stk[tt], i)) tt -- ;
    stk[ ++ tt] = i;
}
```

