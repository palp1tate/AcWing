# [AcWing 839. 模拟堆](https://www.acwing.com/problem/content/841/)

## 题目描述

维护一个集合，初始时集合为空，支持如下几种操作：

1. `I x`，插入一个数 𝑥；
2. `PM`，输出当前集合中的最小值；
3. `DM`，删除当前集合中的最小值（数据保证此时的最小值唯一）；
4. `D k`，删除第 𝑘 个插入的数；
5. `C k x`，修改第 𝑘 个插入的数，将其变为 𝑥；

现在要进行 𝑁 次操作，对于所有第 2 个操作，输出当前集合的最小值。

**输入格式**

第一行包含整数 𝑁。

接下来 𝑁 行，每行包含一个操作指令，操作指令为 `I x`，`PM`，`DM`，`D k` 或 `C k x` 中的一种。

**输出格式**

对于每个输出指令 `PM`，输出一个结果，表示当前集合中的最小值。

每个结果占一行。

**数据范围**

1≤≤𝑁≤10^5

−10^9≤𝑥≤10^9

数据保证合法。

**输入样例**：

```cpp
8
I -10
PM
I -10
D 1
C 2 8
I 6
PM
DM
```

**输出样例**：

```cpp
-10
6
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

long long h[N];
int ph[N], hp[N], cnt;

// h[N] 是实际堆存储的数组
// ph[N] 是从元素插入次序到堆中位置的映射
// hp[N] 是从堆中位置到元素插入次序的映射
// cnt 是堆中当前的元素数量

void heap_swap(int a, int b) {
    swap(ph[hp[a]], ph[hp[b]]);
    swap(hp[a], hp[b]);
    swap(h[a], h[b]);
}

// heap_swap 函数交换堆中两个元素的位置，包括它们在堆数组 h 和索引映射 ph 和 hp 中的位置

void down(int u) {
    int t = u;
    if (u * 2 <= cnt && h[u * 2] < h[t]) t = u * 2;
    if (u * 2 + 1 <= cnt && h[u * 2 + 1] < h[t]) t = u * 2 + 1;
    if (u != t) {
        heap_swap(u, t);
        down(t);
    }
}

// down 函数用于将元素下沉以维持堆的性质，从节点 u 开始下沉到合适的位置

void up(int u) {
    while (u / 2 && h[u] < h[u / 2]) {
        heap_swap(u, u / 2);
        u >>= 1;
    }
}

// up 函数用于将元素上浮以维持堆的性质，从节点 u 开始上浮到合适的位置

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m = 0;
    cin >> n;
    while (n--) {
        string op;
        int k;
        long long x;
        cin >> op;
        if (op == "I") {
            cin >> x;
            cnt++;
            m++;
            ph[m] = cnt, hp[cnt] = m;
            h[cnt] = x;
            up(cnt);
        } else if (op == "PM") {
            cout << h[1] << endl;
        } else if (op == "DM") {
            heap_swap(1, cnt);
            cnt--;
            down(1);
        } else if (op == "D") {
            cin >> k;
            k = ph[k];
            heap_swap(k, cnt);
            cnt--;
            up(k);
            down(k);
        } else {
            cin >> k >> x;
            k = ph[k];
            h[k] = x;
            up(k);
            down(k);
        }
    }

    return 0;
}
```

```cpp
#include <iostream>
#include <cstring>

using namespace std;

const int N = 100010;

long long h[N];
int ph[N], hp[N], cnt;

void heap_swap(int a, int b) {
    swap(ph[hp[a]], ph[hp[b]]);
    swap(hp[a], hp[b]);
    swap(h[a], h[b]);
}

void down(int u) {
    int t = u;
    if (u * 2 <= cnt && h[u * 2] < h[t]) t = u * 2;
    if (u * 2 + 1 <= cnt && h[u * 2 + 1] < h[t]) t = u * 2 + 1;
    if (u != t) {
        heap_swap(u, t);
        down(t);
    }
}

void up(int u) {
    while (u / 2 && h[u] < h[u / 2]) {
        heap_swap(u, u / 2);
        u >>= 1;
    }
}

int main() {
    int n, m = 0;
    scanf("%d", &n);
    while (n--) {
        char op[5];
        int k;
        long long x;
        scanf("%s", op);
        if (!strcmp(op, "I")) {
            scanf("%lld", &x);
            cnt++;
            m++;
            ph[m] = cnt, hp[cnt] = m;
            h[cnt] = x;
            up(cnt);
        } else if (!strcmp(op, "PM")) printf("%lld\n", h[1]);
        else if (!strcmp(op, "DM")) {
            heap_swap(1, cnt);
            cnt--;
            down(1);
        } else if (!strcmp(op, "D")) {
            scanf("%d", &k);
            k = ph[k];
            heap_swap(k, cnt);
            cnt--;
            up(k);
            down(k);
        } else {
            scanf("%d%lld", &k, &x);
            k = ph[k];
            h[k] = x;
            up(k);
            down(k);
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
	h   [N]int64
	ph  [N]int
	hp  [N]int
	cnt int
)

func heapSwap(a, b int) {
	ph[hp[a]], ph[hp[b]] = ph[hp[b]], ph[hp[a]]
	hp[a], hp[b] = hp[b], hp[a]
	h[a], h[b] = h[b], h[a]
}

func down(u int) {
	t := u
	if u*2 <= cnt && h[u*2] < h[t] {
		t = u * 2
	}
	if u*2+1 <= cnt && h[u*2+1] < h[t] {
		t = u*2 + 1
	}
	if u != t {
		heapSwap(u, t)
		down(t)
	}
}

func up(u int) {
	for u/2 > 0 && h[u] < h[u/2] {
		heapSwap(u, u/2)
		u /= 2
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscan(reader, &n)

	for i := 0; i < n; i++ {
		var op string
		fmt.Fscan(reader, &op)

		switch op {
		case "I":
			var x int64
			fmt.Fscan(reader, &x)
			cnt++
			m++
			ph[m], hp[cnt] = cnt, m
			h[cnt] = x
			up(cnt)
		case "PM":
			fmt.Fprintln(writer, h[1])
		case "DM":
			heapSwap(1, cnt)
			cnt--
			down(1)
		case "D":
			var k int
			fmt.Fscan(reader, &k)
			k = ph[k]
			heapSwap(k, cnt)
			cnt--
			up(k)
			down(k)
		case "C":
			var k int
			var x int64
			fmt.Fscan(reader, &k, &x)
			k = ph[k]
			h[k] = x
			up(k)
			down(k)
		}
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
