# [AcWing 795. 前缀和](https://www.acwing.com/problem/content/797/)

## 题目描述

输入一个长度为 n 的整数序列。

接下来再输入 m 个询问，每个询问输入一对 l,r,。

对于每个询问，输出原序列中从第 l 个数到第 r 个数的和。

**输入格式**

第一行包含两个整数 n 和 m。

第二行包含 n 个整数，表示整数数列。

接下来 m 行，每行包含两个整数 l 和 r，表示一个询问的区间范围。

**输出格式**

共 m 行，每行输出一个询问的结果。

**数据范围**

1≤l≤r≤n1,

1≤n,m≤100000，

−1000≤数列中元素的值≤1000

**输入样例：**

```cpp
5 3
2 1 3 6 4
1 2
1 3
2 4
```

**输出样例：**

```cpp
3
6
10
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;
int s[N];

int main() {
    int n, m, tmp;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        s[i + 1] = s[i] + tmp;
    }
    while (m--) {
        int l, r;
        scanf("%d%d", &l, &r);
        printf("%d\n", s[r] - s[l - 1]);
    }
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int n, m;
int a[N], s[N];

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i ++ ) scanf("%d", &a[i]);

    for (int i = 1; i <= n; i ++ ) s[i] = s[i - 1] + a[i]; // 前缀和的初始化

    while (m -- )
    {
        int l, r;
        scanf("%d%d", &l, &r);
        printf("%d\n", s[r] - s[l - 1]); // 区间和的计算
    }

    return 0;
}
```

## Go

```go
package main

import "fmt"

func main() {
	var n, m, tmp int
	fmt.Scanf("%d %d", &n, &m)
	s := make([]int, n+1)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &tmp)
		s[i+1] = s[i] + tmp
	}
	for i := 0; i < m; i++ {
		var l, r int
		fmt.Scanf("%d %d", &l, &r)
		fmt.Println(s[r] - s[l-1])
	}
}
```

## 模板

```cpp
S[i] = a[1] + a[2] + ... a[i]
a[l] + ... + a[r] = S[r] - S[l - 1]
```

