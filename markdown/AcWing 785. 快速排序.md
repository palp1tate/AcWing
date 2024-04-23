# [AcWing 785. 快速排序](https://www.acwing.com/problem/content/787/)

## 题目描述

给定你一个长度为 n 的整数数列。

请你使用快速排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

**输入格式**

输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在 1∼10^9 范围内），表示整个数列。

**输出格式**

输出共一行，包含 n 个整数，表示排好序的数列。

**数据范围**

1≤n≤100000

**输入样例：**

```cpp
5
3 1 2 4 5
```

**输出样例**：

```cpp
1 2 3 4 5
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

void quick_sort(int q[], int l, int r) {
    if (l >= r) {
        return;
    }
    int i = l - 1, j = r + 1, x = q[(l + r) >> 1];
    while (i < j) {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}


int main() {
    int n;
    int q[N];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> q[i];
    quick_sort(q, 0, n - 1);
    for (int i = 0; i < n; i++) cout << q[i] << " ";
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010;

void quick_sort(int q[], int l, int r) {
    if (l >= r) return;

    int i = l - 1, j = r + 1, x = q[(l + r) >> 1];
    while (i < j) {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }

    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}

int main() {
    int n;
    int q[N];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) scanf("%d", &q[i]);

    quick_sort(q, 0, n - 1);

    for (int i = 0; i < n; i++) printf("%d ", q[i]);

    return 0;
}
```

```cpp
#include <iostream>
#include <vector>

using namespace std;

void quick_sort(vector<int> &q, int l, int r) {
    if (l >= r) {
        return;
    }
    int i = l - 1, j = r + 1, x = q[(l + r) >> 1];
    while (i < j) {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}

int main() {
    int n;
    cin >> n;
    vector<int> q(n);
    for (int i = 0; i < n; i++) cin >> q[i];
    quick_sort(q, 0, n - 1);
    for (int i = 0; i < n; i++) cout << q[i] << " ";
    return 0;
}
```

## Go

```go
package main

import "fmt"

func quickSort(arr []int, left int, right int) {
	if left >= right {
		return
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
	quickSort(arr, left, j)
	quickSort(arr, j+1, right)
	return
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &arr[i])
	}
	quickSort(arr, 0, n-1)
	for i := 0; i < n; i++ {
		fmt.Printf("%d ", arr[i])
	}
}
```

## 模板

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
