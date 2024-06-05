# [AcWing 840. 模拟散列表](https://www.acwing.com/problem/content/842/)

## 题目描述

维护一个集合，支持如下几种操作：

1. `I x`，插入一个整数 𝑥；
2. `Q x`，询问整数 𝑥 是否在集合中出现过；

现在要进行 𝑁 次操作，对于每个询问操作输出对应的结果。

**输入格式**

第一行包含整数 𝑁，表示操作数量。

接下来 𝑁 行，每行包含一个操作指令，操作指令为 `I x`，`Q x` 中的一种。

**输出格式**

对于每个询问指令 `Q x`，输出一个询问结果，如果 𝑥 在集合中出现过，则输出 `Yes`，否则输出 `No`。

每个结果占一行。

**数据范围**

1≤𝑁≤10^5

−10^9≤𝑥≤10^9

**输入样例**：

```cpp
5
I 1
I 2
I 3
Q 2
Q 5
```

**输出样例**：

```cpp
Yes
No
```

## C++

**开放寻址法**：选取 N 的时候一般为大于数据总个数的 2~3 倍的第一个质数。

```cpp
#include <cstring>
#include <iostream>

using namespace std;

const int N = 200003, null = 0x3f3f3f3f;

int h[N];

int find(int x) {
    int t = (x % N + N) % N;
    while (h[t] != null && h[t] != x) {
        t++;
        if (t == N) t = 0;
    }
    return t;
}

int main() {
    //也可以这么书写，memset是按字节操作的
    //memset(h, 0x3f, sizeof h);
    memset(h, null, sizeof(h));

    int n;
    scanf("%d", &n);

    while (n--) {
        char op[2];
        int x;
        scanf("%s%d", op, &x);
        if (*op == 'I') h[find(x)] = x;
        else {
            if (h[find(x)] == null) puts("No");
            else puts("Yes");
        }
    }

    return 0;
}
```

**拉链法**：N 一般为大于数据总个数的第一个质数。

```cpp
#include <cstring>
#include <iostream>

using namespace std;

const int N = 100003;

int h[N], e[N], ne[N], idx;

void insert(int x) {
    int k = (x % N + N) % N;
    e[idx] = x;
    ne[idx] = h[k];
    h[k] = idx++;
}

bool find(int x) {
    int k = (x % N + N) % N;
    for (int i = h[k]; i != -1; i = ne[i])
        if (e[i] == x)
            return true;

    return false;
}

int main() {
    int n;
    scanf("%d", &n);

    memset(h, -1, sizeof h);

    while (n--) {
        char op[2];
        int x;
        scanf("%s%d", op, &x);

        if (*op == 'I') insert(x);
        else {
            if (find(x)) puts("Yes");
            else puts("No");
        }
    }

    return 0;
}
```

## Go

**开放寻址法**

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N = 200003
const null = 0x3f3f3f3f

var h [N]int

func init() {
	for i := range h {
		h[i] = null
	}
}

func find(x int) int {
	t := (x%N + N) % N
	for h[t] != null && h[t] != x {
		t++
		if t == N {
			t = 0
		}
	}
	return t
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, x int
	var op string

	fmt.Fscan(reader, &n)

	for n > 0 {
		n--
		fmt.Fscan(reader, &op, &x)
		if op == "I" {
			h[find(x)] = x
		} else {
			if h[find(x)] == null {
				fmt.Fprintln(writer, "No")
			} else {
				fmt.Fprintln(writer, "Yes")
			}
		}
	}
}
```

**拉链法**

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N = 100003

var (
	h   [N]int
	e   [N]int
	ne  [N]int
	idx int
)

func init() {
	for i := range h {
		h[i] = -1
	}
}

func insert(x int) {
	k := (x%N + N) % N
	e[idx] = x
	ne[idx] = h[k]
	h[k] = idx
	idx++
}

func find(x int) bool {
	k := (x%N + N) % N
	for i := h[k]; i != -1; i = ne[i] {
		if e[i] == x {
			return true
		}
	}
	return false
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, x int
	var op string

	fmt.Fscan(reader, &n)

	for n > 0 {
		n--
		fmt.Fscan(reader, &op, &x)

		if op == "I" {
			insert(x)
		} else {
			if find(x) {
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
(1) 拉链法
    int h[N], e[N], ne[N], idx;

    // 向哈希表中插入一个数
    void insert(int x)
    {
        int k = (x % N + N) % N;
        e[idx] = x;
        ne[idx] = h[k];
        h[k] = idx ++ ;
    }

    // 在哈希表中查询某个数是否存在
    bool find(int x)
    {
        int k = (x % N + N) % N;
        for (int i = h[k]; i != -1; i = ne[i])
            if (e[i] == x)
                return true;

        return false;
    }

(2) 开放寻址法
    int h[N];

    // 如果x在哈希表中，返回x的下标；如果x不在哈希表中，返回x应该插入的位置
    int find(int x)
    {
        int t = (x % N + N) % N;
        while (h[t] != null && h[t] != x)
        {
            t ++ ;
            if (t == N) t = 0;
        }
        return t;
    }
```

