# [AcWing 143. 最大异或对](https://www.acwing.com/problem/content/145/)

## 题目描述

在给定的 𝑁 个整数 𝐴1，𝐴2……𝐴𝑁 中选出两个进行 𝑥𝑜𝑟（异或）运算，得到的结果最大是多少？

**输入格式**

第一行输入一个整数 𝑁。

第二行输入 𝑁 个整数 𝐴1～𝐴𝑁。

**输出格式**

输出一个整数表示答案。

**数据范围**

1≤𝑁≤10^5,

0≤𝐴𝑖<2^31

**输入样例**：

```cpp
3
1 2 3
```

**输出样例**：

```cpp
3
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 100010, M = N * 31;

int n;
int a[N];
int son[M][2], idx;

void insert(int x) {
    int p = 0;
    for (int i = 30; i >= 0; i--) {
        int u = x >> i & 1;
        if (!son[p][u]) son[p][u] = ++idx;
        p = son[p][u];
    }
}

int query(int x) {
    int p = 0, res = 0;
    for (int i = 30; i >= 0; i--) {
        int u = x >> i & 1;
        if (son[p][!u]) {
            res += 1 << i;
            p = son[p][!u];
        } else {
            p = son[p][u];
        }
    }

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i], insert(a[i]);

    int res = 0;
    for (int i = 0; i < n; i++) {
        int t = query(a[i]);
        res = max(res, t);
    }

    cout << res << endl;
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010, M = N * 31;

int n;
int a[N];
int son[M][2], idx;

void insert(int x) {
    int p = 0;
    for (int i = 30; i >= 0; i--) {
        int u = x >> i & 1;
        if (!son[p][u]) son[p][u] = ++idx;
        p = son[p][u];
    }
}

int query(int x) {
    int p = 0, res = 0;
    for (int i = 30; i >= 0; i--) {
        int u = x >> i & 1;
        if (son[p][!u]) {
            p = son[p][!u];
            res = res * 2 + !u;
        } else {
            p = son[p][u];
            res = res * 2 + u;
        }
    }

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i], insert(a[i]);

    int res = 0;
    for (int i = 0; i < n; i++) {
        int t = query(a[i]);
        res = max(res, a[i] ^ t);
    }

    cout << res << endl;
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

const (
	N = 100010
	M = N * 31
)

var (
	n   int
	a   [N]int
	son [M][2]int
	idx int
)

func insert(x int) {
	p := 0
	for i := 30; i >= 0; i-- {
		u := x >> i & 1
		if son[p][u] == 0 {
			idx++
			son[p][u] = idx
		}
		p = son[p][u]
	}
}

func query(x int) int {
	p := 0
	res := 0
	for i := 30; i >= 0; i-- {
		u := x >> i & 1
		if son[p][1-u] != 0 {
			res += 1 << i
			p = son[p][1-u]
		} else {
			p = son[p][u]
		}
	}
	return res
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	fmt.Fscan(reader, &n)

	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &a[i])
	}

	res := 0
	for i := 0; i < n; i++ {
		insert(a[i])
		t := query(a[i])
		if t > res {
			res = t
		}
	}

	fmt.Fprintln(writer, res)
}
```

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	N = 100010
	M = N * 31
)

var (
	n   int
	a   [N]int
	son [M][2]int
	idx int
)

func insert(x int) {
	p := 0
	for i := 30; i >= 0; i-- {
		u := x >> i & 1
		if son[p][u] == 0 {
			idx++
			son[p][u] = idx
		}
		p = son[p][u]
	}
}

func query(x int) int {
	p := 0
	res := 0
	for i := 30; i >= 0; i-- {
		u := x >> i & 1
		if son[p][1-u] != 0 {
			res = res*2 + 1 - u
			p = son[p][1-u]
		} else {
			res = res*2 + u
			p = son[p][u]
		}
	}
	return res
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	fmt.Fscan(reader, &n)

	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &a[i])
		insert(a[i])
	}

	res := 0
	for i := 0; i < n; i++ {
		t := a[i] ^ query(a[i])
		if t > res {
			res = t
		}
	}

	fmt.Fprintln(writer, res)
}
```

