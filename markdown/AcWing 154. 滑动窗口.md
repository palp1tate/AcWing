# [AcWing 154. 滑动窗口](https://www.acwing.com/problem/content/156/)

## 题目描述

给定一个大小为 n≤10^6 的数组。

有一个大小为 𝑘 的滑动窗口，它从数组的最左边移动到最右边。

你只能在窗口中看到 𝑘 个数字。

每次滑动窗口向右移动一个位置。

以下是一个例子：

该数组为 `[1 3 -1 -3 5 3 6 7]`，𝑘 为 3。

|      窗口位置       | 最小值 | 最大值 |
| :-----------------: | :----: | :----: |
| [1 3 -1] -3 5 3 6 7 |   -1   |   3    |
| 1 [3 -1 -3] 5 3 6 7 |   -3   |   3    |
| 1 3 [-1 -3 5] 3 6 7 |   -3   |   5    |
| 1 3 -1 [-3 5 3] 6 7 |   -3   |   5    |
| 1 3 -1 -3 [5 3 6] 7 |   3    |   6    |
| 1 3 -1 -3 5 [3 6 7] |   3    |   7    |

你的任务是确定滑动窗口位于每个位置时，窗口中的最大值和最小值。

**输入格式**

输入包含两行。

第一行包含两个整数 𝑛 和 𝑘，分别代表数组长度和滑动窗口的长度。

第二行有 𝑛 个整数，代表数组的具体数值。

同行数据之间用空格隔开。

**输出格式**

输出包含两个。

第一行输出，从左至右，每个位置滑动窗口中的最小值。

第二行输出，从左至右，每个位置滑动窗口中的最大值。

**输入样例**：

```cpp
8 3
1 3 -1 -3 5 3 6 7
```

**输出样例**：

```cpp
-1 -3 -3 -3 3 3
3 3 5 5 6 7
```

## C++

```cpp
#include <iostream>

using namespace std;

const int MAX_SIZE = 1000010;

int nums[MAX_SIZE], deque[MAX_SIZE]; // 定义两个数组，一个存储输入的数值，一个作为双端队列

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> nums[i];

    int head = 0, tail = -1; // 初始化双端队列的头尾指针

    // 计算滑动窗口最小值
    for (int i = 0; i < n; i++) {
        // 移除超出窗口范围的元素
        if (head <= tail && i - k + 1 > deque[head]) head++;

        // 移除队列中比当前元素大的元素，保证队列递增
        while (head <= tail && nums[deque[tail]] >= nums[i]) tail--;
        deque[++tail] = i; // 将当前元素索引加入队列

        // 输出当前窗口的最小值
        if (i >= k - 1) cout << nums[deque[head]] << " ";
    }

    cout << endl;

    head = 0, tail = -1; // 重新初始化头尾指针

    // 计算滑动窗口最大值
    for (int i = 0; i < n; i++) {
        // 移除超出窗口范围的元素
        if (head <= tail && i - k + 1 > deque[head]) head++;

        // 移除队列中比当前元素小的元素，保证队列递减
        while (head <= tail && nums[deque[tail]] <= nums[i]) tail--;
        deque[++tail] = i; // 将当前元素索引加入队列

        // 输出当前窗口的最大值
        if (i >= k - 1) cout << nums[deque[head]] << " ";
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

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n, k int
	fmt.Fscanf(reader, "%d %d\n", &n, &k)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d ", &nums[i])
	}
	deque := make([]int, n)
	head := 0
	tail := -1
	for i := 0; i < n; i++ {
		if head <= tail && deque[head] < i-k+1 {
			head++
		}
		for head <= tail && nums[deque[tail]] >= nums[i] {
			tail--
		}
		tail++
		deque[tail] = i
		if i >= k-1 {
			fmt.Fprintf(writer, "%d ", nums[deque[head]])
		}
	}
	fmt.Fprintln(writer)
	head = 0
	tail = -1
	for i := 0; i < n; i++ {
		if head <= tail && deque[head] < i-k+1 {
			head++
		}
		for head <= tail && nums[deque[tail]] <= nums[i] {
			tail--
		}
		tail++
		deque[tail] = i
		if i >= k-1 {
			fmt.Fprintf(writer, "%d ", nums[deque[head]])
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

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func maxSlidingWindow(nums []int, k int) {
	var q []int // 使用一个队列q来存储元素的索引

	// 定义一个局部函数push，它的功能是向队列中添加元素
	push := func(i int) {
		// 如果队列不为空，且当前元素值大于等于队列尾部元素值
		for len(q) > 0 && nums[i] >= nums[q[len(q)-1]] {
			// 队列尾部元素出队
			q = q[:len(q)-1]
		}
		// 将当前元素的索引入队
		q = append(q, i)
	}

	// 先将前k个元素做处理
	for i := 0; i < k; i++ {
		push(i)
	}
	n := len(nums)

	fmt.Fprintf(writer, "%d ", nums[q[0]])

	// 从k开始遍历，对于每个元素，都将其添加到队列中
	// 并保证队列的头部元素总是当前窗口的最大值
	for i := k; i < n; i++ {
		push(i)
		// 如果队列中的头部元素不在当前窗口中,就将其出队
		for q[0] <= i-k {
			q = q[1:]
		}

		fmt.Fprintf(writer, "%d ", nums[q[0]])
	}

}

func minSlidingWindow(nums []int, k int) {
	var q []int

	push := func(i int) {
		for len(q) > 0 && nums[i] <= nums[q[len(q)-1]] {
			q = q[:len(q)-1]
		}
		q = append(q, i)
	}

	for i := 0; i < k; i++ {
		push(i)
	}
	n := len(nums)

	fmt.Fprintf(writer, "%d ", nums[q[0]])

	for i := k; i < n; i++ {
		push(i)
		for q[0] <= i-k {
			q = q[1:]
		}
		fmt.Fprintf(writer, "%d ", nums[q[0]])
	}
}

func main() {
	defer writer.Flush()
	var n, k int
	fmt.Fscanf(reader, "%d %d\n", &n, &k)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d ", &nums[i])
	}
	minSlidingWindow(nums, k)
	fmt.Fprintln(writer)
	maxSlidingWindow(nums, k)
}

```

## 模板

```cpp
常见模型：找出滑动窗口中的最大值/最小值
int hh = 0, tt = -1;
for (int i = 0; i < n; i ++ )
{
    while (hh <= tt && check_out(q[hh])) hh ++ ;  // 判断队头是否滑出窗口
    while (hh <= tt && check(q[tt], i)) tt -- ;
    q[ ++ tt] = i;
}
```

