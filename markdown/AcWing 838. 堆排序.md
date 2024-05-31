# [AcWing 838. 堆排序](https://www.acwing.com/problem/content/840/)

## 题目描述

输入一个长度为 𝑛 的整数数列，从小到大输出前 𝑚 小的数。

**输入格式**

第一行包含整数 𝑛 和 𝑚。

第二行包含 𝑛 个整数，表示整数数列。

**输出格式**

共一行，包含 𝑚 个整数，表示整数数列中前 𝑚 小的数。

**数据范围**

1≤𝑚≤𝑛≤10^5，

1≤数列中元素≤10^9

**输入样例**：

```cpp
5 3
4 5 1 3 2
```

**输出样例**：

```cpp
1 2 3
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int n, m;
int h[N], cnt;

void down(int u) {
    int t = u;
    if (u * 2 <= cnt && h[u * 2] < h[t]) t = u * 2;
    if (u * 2 + 1 <= cnt && h[u * 2 + 1] < h[t]) t = u * 2 + 1;
    if (u != t) {
        swap(h[u], h[t]);
        down(t);
    }
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) scanf("%d", &h[i]);
    cnt = n;

    for (int i = n / 2; i; i--) down(i);

    while (m--) {
        printf("%d ", h[1]);
        h[1] = h[cnt--];
        down(1);
    }

    puts("");

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
	n, m, cnt int
	h         [N]int
)

func down(u int) {
	t := u
	if u*2 <= cnt && h[u*2] < h[t] {
		t = u * 2
	}
	if u*2+1 <= cnt && h[u*2+1] < h[t] {
		t = u*2 + 1
	}
	if u != t {
		h[u], h[t] = h[t], h[u]
		down(t)
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscan(reader, &n, &m)
	for i := 1; i <= n; i++ {
		fmt.Fscan(reader, &h[i])
	}
	cnt = n

	for i := n / 2; i > 0; i-- {
		down(i)
	}

	for m > 0 {
		fmt.Fprintf(writer, "%d ", h[1])
		h[1] = h[cnt]
		cnt--
		down(1)
		m--
	}
}
```

## 模板

```cpp
// h[N]存储堆中的值, h[1]是堆顶，x的左儿子是2x, 右儿子是2x + 1
// ph[k]存储第k个插入的点在堆中的位置
// hp[k]存储堆中下标是k的点是第几个插入的
int h[N], ph[N], hp[N], size;

// 交换两个点，及其映射关系
void heap_swap(int a, int b)
{
    swap(ph[hp[a]],ph[hp[b]]);
    swap(hp[a], hp[b]);
    swap(h[a], h[b]);
}

void down(int u)
{
    int t = u;
    if (u * 2 <= size && h[u * 2] < h[t]) t = u * 2;
    if (u * 2 + 1 <= size && h[u * 2 + 1] < h[t]) t = u * 2 + 1;
    if (u != t)
    {
        heap_swap(u, t);
        down(t);
    }
}

void up(int u)
{
    while (u / 2 && h[u] < h[u / 2])
    {
        heap_swap(u, u / 2);
        u >>= 1;
    }
}

// O(n)建堆
for (int i = n / 2; i; i -- ) down(i);
```

