# [AcWing 797. 差分](https://www.acwing.com/problem/content/799/)

## 题目描述

输入一个长度为 n 的整数序列。

接下来输入 m 个操作，每个操作包含三个整数 l,r,c，表示将序列中 [l,r]之间的每个数加上 c。

请你输出进行完所有操作后的序列。

**输入格式**

第一行包含两个整数 n 和 m。

第二行包含 n 个整数，表示整数序列。

接下来 m 行，每行包含三个整数 l，r，c，表示一个操作。

**输出格式**

共一行，包含 n 个整数，表示最终序列。

**数据范围**

1≤n,m≤100000,

1≤l≤r≤n1,

−1000≤c≤1000,

−1000≤整数序列中元素的值≤1000

**输入样例**：

```cpp
6 3
1 2 2 1 2 1
1 3 1
3 5 1
1 6 1
```

**输出样例**：

```cpp
3 4 5 3 4 2
```

## 思路

**差分数组的基本概念**

差分数组 `diff` 是对原数组 `arr` 的一个变换，用于记录每个元素与前一个元素的差值。差分数组的主要优点是能够将区间增加或减少操作降低到常数时间复杂度。

**差分数组的构建**

对于原始数组 `arr`，其差分数组 `diff` 的构建方式如下：

```cpp
diff[i] = arr[i] - arr[i - 1];
```

其中，`arr[0]` 假设为 `0`（如果数组索引从 `1` 开始）。因此，`diff[1] = arr[1] - arr[0]`，以此类推。

**区间更新操作**

- 要对原数组 `arr` 中的一个子区间 `[l, r]` 的所有元素加上一个值 `x`，你只需要：
  - `diff[l] += x`
  - `diff[r + 1] -= x`（如果 `r + 1` 在数组边界内）

**代码示例**

以下是一个 C++ 示例代码，用于演示如何使用差分数组：

```cpp
#include <iostream>
#include <vector>

using namespace std;

void add_range(vector<int>& diff, int l, int r, int x) {
    diff[l] += x;
    if (r + 1 < diff.size()) {
        diff[r + 1] -= x;
    }
}

int main() {
    int n;  // 数组长度
    cin >> n;
    vector<int> arr(n + 1, 0), diff(n + 2, 0);

    // 假设进行操作
    add_range(diff, 2, 5, 10);  // 在区间 [2, 5] 上加 10
    add_range(diff, 3, 7, 5);   // 在区间 [3, 7] 上加 5

    // 构建最终数组
    for (int i = 1; i <= n; i++) {
        arr[i] = arr[i - 1] + diff[i];
        cout << arr[i] << " ";
    }

    return 0;
}
```

这样，你就可以高效地对数组进行多次区间操作，并最终快速得到结果数组。

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;
int arr[N];

void insert(int l, int r, int num) {
    arr[l] += num;
    arr[r + 1] -= num;
}

int main() {
    int n, m, tmp;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &tmp);
        insert(i, i, tmp);
    }
    while (m--) {
        int l, r, c;
        scanf("%d%d%d", &l, &r, &c);
        insert(l, r, c);
    }
    for (int i = 1; i <= n; i++) {
        arr[i] += arr[i - 1];
        printf("%d ", arr[i]);
    }
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int n, m;
int a[N], b[N];

void insert(int l, int r, int c) {
    b[l] += c;
    b[r + 1] -= c;
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);

    for (int i = 1; i <= n; i++) insert(i, i, a[i]);

    while (m--) {
        int l, r, c;
        scanf("%d%d%d", &l, &r, &c);
        insert(l, r, c);
    }

    for (int i = 1; i <= n; i++) b[i] += b[i - 1];

    for (int i = 1; i <= n; i++) printf("%d ", b[i]);

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

func insert(arr []int, l int, r int, c int) {
	arr[l] += c
	arr[r+1] -= c
}

func main() {
	var n, m, tmp int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n, &m)
	arr := make([]int, n+10)
	for i := 1; i <= n; i++ {
		fmt.Fscan(reader, &tmp)
		insert(arr, i, i, tmp)
	}
	for i := 1; i <= m; i++ {
		var l, r, c int
		fmt.Fscan(reader, &l, &r, &c)
		insert(arr, l, r, c)
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i := 1; i <= n; i++ {
		arr[i] += arr[i-1]
		fmt.Fprintf(writer, "%d ", arr[i])
	}
}
```

## 模板

```cpp
给区间[l, r]中的每个数加上c：B[l] += c, B[r + 1] -= c
```

