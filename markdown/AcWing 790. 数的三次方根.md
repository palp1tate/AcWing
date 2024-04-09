# [AcWing 790. 数的三次方根](https://www.acwing.com/problem/content/792/)

## 题目描述

给定一个浮点数 n，求它的三次方根。

**输入格式**

共一行，包含一个浮点数 n。

**输出格式**

共一行，包含一个浮点数，表示问题的解。

注意，结果保留 6 位小数。

**数据范围**

−10000≤n≤10000

**输入样例**：

```cpp
1000.00
```

**输出样例**：

```cpp
10.000000
```

## C++

```cpp
#include <iostream>

using namespace std;

int main() {
    double x;
    cin >> x;
    double l = -22, r = 22;
    while ((r - l) > 1e-8) {
        double mid = (l + r) / 2;
        if (mid * mid * mid >= x) r = mid;
        else l = mid;
    }
    printf("%.6lf", l);
    return 0;
}
```

## Go

```go
package main

import (
	"fmt"
)

func main() {
	var x float64
	fmt.Scan(&x)
	l, r := -22.0, 22.0
	for (r - l) > 1e-8 {
		mid := (l + r) / 2
		if mid*mid*mid >= x {
			r = mid
		} else {
			l = mid
		}
	}
	fmt.Printf("%.6f", l)
}
```

## 思路

这里使用 `1e-8`，是因为题目要求保留小数点后 6 位，如果使用`1e-7`, 那么这个因为四舍五入第八位到第七位，已经产生误差，输出六位时候误差会积累。如果使用`-8`，那么四舍五入第九位到第八位，取前六位时候，第七位会被`truncate`掉，但是第七位是准确值。

假设实际结果是`0.123456 4555555555`

直接保留六位小数为`0.123456`

精确到 7 位后变成`0.123456 5`，再保留六位小数为`0.123457`

精确到 8 位后变成`0.123456 46`，再保留六位小数为`0.123456`

由此可见，想要保留出正确的六位小数，需要保证第七位是精准的，不能被进位

## 模板

```cpp
bool check(double x) {/* ... */} // 检查x是否满足某种性质

double bsearch_3(double l, double r)
{
    const double eps = 1e-6;   // eps 表示精度，取决于题目对精度的要求
    while (r - l > eps)
    {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    return l;
}
```
