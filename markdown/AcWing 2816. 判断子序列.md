# [AcWing 2816. 判断子序列](https://www.acwing.com/problem/content/2818/)

## 题目叙述

给定一个长度为 n 的整数序列 a1,a2,……,an 以及一个长度为 m 的整数序列 b1,b2,……,bm。

请你判断 a 序列是否为 b 序列的子序列。

子序列指序列的一部分项按**原有次序排列**而得的序列，例如序列 {a1,a3,a5} 是序列 {a1,a2,a3,a4,a5}的一个子序列。

**输入格式**

第一行包含两个整数 n,m。

第二行包含 n 个整数，表示 a1,a2,……,an。

第三行包含 m 个整数，表示 b1,b2,……,bm。

**输出格式**

如果 a 序列是 b 序列的子序列，输出一行 `Yes`。

否则，输出 `No`。

**数据范围**

1≤n≤m≤10^5,

−10^9≤ai,bi≤10^9

**输入样例**：

```cpp
3 5
1 3 5
1 2 3 4 5
```

**输出样例**：

```cpp
Yes
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int n, m;
int a[N], b[N];

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);

    int i = 0, j = 0;
    while (i < n && j < m) {
        if (a[i] == b[j]) i++;
        j++;
    }

    if (i == n) puts("Yes");
    else puts("No");

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

func main() {
	var n, m int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanf(reader, "%d %d\n", &n, &m)
	a, b := make([]int, n), make([]int, m)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d", &a[i])
	}
	fmt.Fscanf(reader, "\n")
	for i := 0; i < m; i++ {
		fmt.Fscanf(reader, "%d", &b[i])
	}
	i, j := 0, 0
	for i < n && j < m {
		if a[i] == b[j] {
			i++
		}
		j++
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if i == n {
		fmt.Fprintln(writer, "Yes")
	} else {
		fmt.Fprintln(writer, "No")
	}
}
```

```go
package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n, m int
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	params := strings.Fields(line)
	n, _ = strconv.Atoi(params[0])
	m, _ = strconv.Atoi(params[1])
	a := make([]int64, n)
	b := make([]int64, m)
	line, _ = reader.ReadString('\n')
	nums := strings.Fields(line)
	for i := 0; i < n; i++ {
		a[i], _ = strconv.ParseInt(nums[i], 10, 64)
	}
	line, _ = reader.ReadString('\n')
	nums = strings.Fields(line)
	for i := 0; i < m; i++ {
		b[i], _ = strconv.ParseInt(nums[i], 10, 64)
	}
	i, j := 0, 0
	for i < n && j < m {
		if a[i] == b[j] {
			i++
		}
		j++
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if i == n {
		writer.WriteString("Yes\n")
	} else {
		writer.WriteString("No\n")
	}
}
```

