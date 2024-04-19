# [AcWing 799. 最长连续不重复子序列](https://www.acwing.com/problem/content/801/)

## 题目描述

给定一个长度为 n 的整数序列，请找出最长的不包含重复的数的连续区间，输出它的长度。

**输入格式**

第一行包含整数 n。

第二行包含 n 个整数（均在 0∼10^5 范围内），表示整数序列。

输出格式

共一行，包含一个整数，表示最长的不包含重复的数的连续区间的长度。

**数据范围**

1≤n≤10^5

**输入样例**：

```cpp
5
1 2 2 3 5
```

**输出样例**：

```cpp
3
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

int arr[N], count[N];


int main() {
    int n, res = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    for (int l = 0, r = 0; r < n; r++) {
        count[arr[r]]++;
        while (l < r && count[arr[r]] > 1) count[arr[l++]]--;
        res = max(res, r - l + 1);
    }
    printf("%d", res);
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

int n;
int q[N], s[N];

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &q[i]);

    int res = 0;
    for (int i = 0, j = 0; i < n; i++) {
        s[q[i]]++;
        while (j < i && s[q[i]] > 1) s[q[j++]]--;
        res = max(res, i - j + 1);
    }

    cout << res << endl;

    return 0;
}
```

1. **右指针 `i`**：
   - 右指针 `i` 用于遍历数组 `q` 中的每一个元素。
   - 它从数组的第一个元素开始，逐步向右移动，直到达到数组的最后一个元素。
   - 在每次迭代中，`i` 指向当前正在考虑的数组元素。
2. **左指针 `j`**：
   - 左指针 `j` 表示当前考虑的窗口的左边界。
   - 它的起始位置也是数组的起始位置，但它会根据需要向右移动，以调整窗口的大小，确保窗口内的所有元素都是唯一的（无重复）。
   - 如果右指针 `i` 指向的元素由于重复而需要调整窗口大小，那么 `j` 将向右移动，直到该重复元素的计数恢复为 1 或更少。

## Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n, res int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n)
	arr := make([]int, n)
	count := make(map[int]int)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}
	for l, r := 0, 0; r < n; r++ {
		count[arr[r]]++
		for l < r && count[arr[r]] > 1 {
			count[arr[l]]--
			l++
		}
		res = max(res, r-l+1)
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprint(writer, res)
}
```

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N int = 1e5 + 10

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n, res int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n)
	arr := make([]int, n)
	count := make([]int, N)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}
	for l, r := 0, 0; r < n; r++ {
		count[arr[r]]++
		for l < r && count[arr[r]] > 1 {
			count[arr[l]]--
			l++
		}
		res = max(res, r-l+1)
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprint(writer, res)
}
```

## 模板

```cpp
for (int i = 0, j = 0; i < n; i ++ )
{
    while (j < i && check(i, j)) j ++ ;

    // 具体问题的逻辑
}
常见问题分类：
    (1) 对于一个序列，用两个指针维护一段区间
    (2) 对于两个序列，维护某种次序，比如归并排序中合并两个有序序列的操作
```

