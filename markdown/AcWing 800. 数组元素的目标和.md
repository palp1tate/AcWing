# [AcWing 800. 数组元素的目标和](https://www.acwing.com/problem/content/802/)

## 题目描述

给定两个升序排序的有序数组 A 和 B，以及一个目标值 x。

数组下标从 0 开始。

请你求出满足 A[i]+B[j]=x 的数对 (i,j)。

数据保证有唯一解。

**输入格式**

第一行包含三个整数 n,m,x，分别表示 A 的长度，B 的长度以及目标值 x。

第二行包含 n 个整数，表示数组 A。

第三行包含 m 个整数，表示数组 B。

**输出格式**

共一行，包含两个整数 i 和 j。

**数据范围**

数组长度不超过 10^5。

同一数组内元素各不相同。

1≤数组元素≤10^9

**输入样例**：

```cpp
4 5 6
1 2 4 7
3 4 6 8 9
```

**输出样例**：

```cpp
1 1
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

int n, m;
long long x;
long long a[N], b[N];

int main() {
    scanf("%d%d%d", &n, &m, &x);
    for (int i = 0; i < n; i++) scanf("%lld", &a[i]);
    for (int i = 0; i < m; i++) scanf("%lld", &b[i]);

    for (int i = 0, j = m - 1; i < n; i++) {
        while (j >= 0 && a[i] + b[j] > x) j--;
        if (j >= 0 && a[i] + b[j] == x) cout << i << ' ' << j << endl;
    }

    return 0;
}
```

## Go

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
	var x int64
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	params := strings.Fields(line)
	n, _ = strconv.Atoi(params[0])
	m, _ = strconv.Atoi(params[1])
	x, _ = strconv.ParseInt(params[2], 10, 64)
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
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i, j := 0, m-1; i < n; i++ {
		for j >= 0 && a[i]+b[j] > x {
			j--
		}
		if j >= 0 && a[i]+b[j] == x {
			writer.WriteString(strconv.Itoa(i) + " " + strconv.Itoa(j) + "\n")
			return
		}
	}
}
```

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int
	var tmp, x int64
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanf(reader, "%d %d %d\n", &n, &m, &x)
	a := make(map[int64]int)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d", &tmp)
		a[tmp] = i
	}
	fmt.Fscanf(reader, "\n")
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for j := 0; j < m; j++ {
		fmt.Fscanf(reader, "%d", &tmp)
		if value, ok := a[x-tmp]; ok {
			fmt.Fprintf(writer, "%d %d\n", value, j)
		}
	}
}
```

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	params := strings.Fields(line)
	n, _ := strconv.Atoi(params[0])
	m, _ := strconv.Atoi(params[1])
	x, _ := strconv.ParseInt(params[2], 10, 64)

	a := make(map[int64]int)
	line, _ = reader.ReadString('\n')
	nums := strings.Fields(line)
	for i := 0; i < n; i++ {
		tmp, _ := strconv.ParseInt(nums[i], 10, 64)
		a[tmp] = i
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	line, _ = reader.ReadString('\n')
	nums = strings.Fields(line)
	for j := 0; j < m; j++ {
		tmp, _ := strconv.ParseInt(nums[j], 10, 64)
		if value, ok := a[x-tmp]; ok {
			fmt.Fprintf(writer, "%d %d\n", value, j)
		}
	}
}
```