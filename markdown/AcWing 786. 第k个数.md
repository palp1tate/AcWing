[AcWing 786. 第k个数](https://www.acwing.com/problem/content/788/)

#### 题目描述

给定一个长度为 n的整数数列，以及一个整数 k，请用快速选择算法求出数列从小到大排序后的第 k 个数。

**输入格式**

第一行包含两个整数 n 和 k。

第二行包含 n 个整数（所有整数均在 1∼10^9 范围内），表示整数数列。

**输出格式**

输出一个整数，表示数列的第 k 小数。

**数据范围**

1≤n≤100000,

1≤k≤n

**输入样例：**

```cpp
5 3
2 4 1 5 3
```

**输出样例：**

```cpp
3
```

#### 思路

![image-20240403110228271](https://cdn.jsdelivr.net/gh/palp1tate/ImgPicGo/img/image-20240403110228271.png)

#### C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

int quick_sort(int q[], int l, int r, int k) {
    if (l == r) return q[l];
    int i = l - 1, j = r + 1, x = q[(l + r) >> 1];
    while (i < j) {
        while (q[++i] < x);
        while (q[--j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    int sl = j - l + 1;
    if (k <= sl) return quick_sort(q, l, j, k);
    else return quick_sort(q, j + 1, r, k - sl);
}

int main() {
    int n, k;
    cin >> n >> k;
    int q[N];
    for (int i = 0; i < n; i++) cin >> q[i];
    cout << quick_sort(q, 0, n - 1, k) << endl;
    return 0;
}
```

#### Go

```go
package main

import "fmt"

func quickSort(arr []int, left int, right int, k int) int {
	if left == right {
		return arr[left]
	}
	i := left - 1
	j := right + 1
	x := arr[(left+right)>>1]
	for i < j {
		for {
			i++
			if arr[i] >= x {
				break
			}
		}
		for {
			j--
			if arr[j] <= x {
				break
			}
		}
		if i < j {
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	sl := j - left + 1
	if sl >= k {
		return quickSort(arr, left, j, k)
	} else {
		return quickSort(arr, j+1, right, k-sl)
	}
}

func main() {
	var n, k int
	fmt.Scanf("%d", &n)
	fmt.Scanf("%d", &k)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &arr[i])
	}
	fmt.Println(quickSort(arr, 0, n-1, k))
}
```

#### 模板

```cpp
void quick_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j)
    {
        do i ++ ; while (q[i] < x);
        do j -- ; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j), quick_sort(q, j + 1, r);
}
```
