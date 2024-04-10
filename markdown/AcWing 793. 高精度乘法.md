# [AcWing 793. 高精度乘法](https://www.acwing.com/problem/content/description/795/)

## 题目描述

给定两个非负整数（不含前导 00） A 和 B，请你计算 A×B 的值。

**输入格式**

共两行，第一行包含整数 A，第二行包含整数 B。

**输出格式**

共一行，包含 A×B 的值。

**数据范围**

1≤A 的长度≤100000,

0≤B≤100000

**输入样例**：

```cpp
2
3
```

**输出样例**：

```cpp
6
```

## 思路

将 B 看成一个整体再相乘，不要一位一位的乘！注意结果的前导 0！

## C++

```cpp
#include <iostream>
#include <string>

using namespace std;

void reverse(string &s) {
    size_t n = s.length();
    for (int i = 0; i < n / 2; ++i) {
        swap(s[i], s[n - i - 1]);
    }
}

string mul(string &a, int b) {
    reverse(a);
    int carry = 0;
    string result;
    for (size_t i = 0; i < a.size() || carry; ++i) {
        if (i < a.size()) carry += (a[i] - '0') * b;
        result.push_back(carry % 10 + '0');
        carry /= 10;
    }
    reverse(result);
    if (result[0] == '0') return "0";
    return result;
}

int main() {
    string a;
    int b;
    cin >> a >> b;
    cout << mul(a, b);
    return 0;
}
```

```cpp
#include <iostream>
#include <vector>

using namespace std;


vector<int> mul(vector<int> &A, int b)
{
    vector<int> C;

    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();

    return C;
}


int main()
{
    string a;
    int b;

    cin >> a >> b;

    vector<int> A;
    for (int i = a.size() - 1; i >= 0; i -- ) A.push_back(a[i] - '0');

    auto C = mul(A, b);

    for (int i = C.size() - 1; i >= 0; i -- ) printf("%d", C[i]);

    return 0;
}
```

## Go

```go
package main

import (
	"fmt"
	"strings"
)

func reverse(s string) string {
	r := []rune(s)
	l := len(r)
	for i := 0; i < l/2; i++ {
		r[i], r[l-i-1] = r[l-i-1], r[i]
	}
	return string(r)
}

func mul(a string, b int) string {
	a = reverse(a)
	carry := 0
	var result strings.Builder
	for i := 0; i < len(a) || carry > 0; i++ {
		if i < len(a) {
			carry += int(a[i]-'0') * b
		}
		result.WriteByte(uint8(carry%10) + '0')
		carry /= 10
	}
	resStr := reverse(result.String())
	if resStr[0] == '0' {
		return "0"
	}
	return resStr
}

func main() {
	var a string
	var b int
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	fmt.Println(mul(a, b))
}
```

## 模板

```cpp
// C = A * b, A >= 0, b >= 0
vector<int> mul(vector<int> &A, int b)
{
    vector<int> C;

    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();

    return C;
}
```

