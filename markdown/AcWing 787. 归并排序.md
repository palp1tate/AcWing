# [AcWing 787. 归并排序](https://www.acwing.com/problem/content/789/)

## 题目描述

给定你一个长度为 n 的整数数列。

请你使用归并排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

**输入格式**

输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在 1∼10^9 范围内），表示整个数列。

**输出格式**

输出共一行，包含 n 个整数，表示排好序的数列。

**数据范围**

1≤n≤100000

**输入样例**：

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

int tmp[N];

void merge_sort(int q[], int l, int r) {
    if (l >= r) return;
    int mid = (l + r) >> 1;
    merge_sort(q, l, mid), merge_sort(q, mid + 1, r);
    int k = 0, i = l, j = mid + 1;
    while (i <= mid && j <= r) {
        if (q[i] <= q[j]) tmp[k++] = q[i++];
        else tmp[k++] = q[j++];
    }
    while (i <= mid) tmp[k++] = q[i++];
    while (j <= r) tmp[k++] = q[j++];
    for (i = l; i <= r; i++) q[i] = tmp[i - l];
}

int main() {
    int n;
    cin >> n;
    int q[N];
    for (int i = 0; i < n; i++) cin >> q[i];
    merge_sort(q, 0, n - 1);
    for (int i = 0; i < n; i++) cout << q[i] << " ";
    return 0;
}
```

## Go

```go
package main

import "fmt"

const N = 1e5 + 10

var tmp = make([]int, N)

func mergeSort(arr []int, l, r int) {
	if l >= r {
		return
	}
	mid := (l + r) >> 1
	mergeSort(arr, l, mid)
	mergeSort(arr, mid+1, r)
	k := 0
	i := l
	j := mid + 1
	for i <= mid && j <= r {
		if arr[i] <= arr[j] {
			tmp[k] = arr[i]
			i++
		} else {
			tmp[k] = arr[j]
			j++
		}
		k++
	}
	for i <= mid {
		tmp[k] = arr[i]
		i++
		k++
	}
	for j <= r {
		tmp[k] = arr[j]
		j++
		k++
	}
	for i := l; i <= r; i++ {
		arr[i] = tmp[i-l]
	}
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	arr := make([]int, N)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &arr[i])
	}
	mergeSort(arr, 0, n-1)
	for i := 0; i < n; i++ {
		fmt.Printf("%d ", arr[i])
	}
}
```

## 模板

```cpp
void merge_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int mid = l + r >> 1;
    merge_sort(q, l, mid);
    merge_sort(q, mid + 1, r);

    int k = 0, i = l, j = mid + 1;
    while (i <= mid && j <= r)
        if (q[i] <= q[j]) tmp[k ++ ] = q[i ++ ];
        else tmp[k ++ ] = q[j ++ ];

    while (i <= mid) tmp[k ++ ] = q[i ++ ];
    while (j <= r) tmp[k ++ ] = q[j ++ ];

    for (i = l, j = 0; i <= r; i ++, j ++ ) q[i] = tmp[j];
}
```
