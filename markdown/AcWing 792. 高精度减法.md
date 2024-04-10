# [AcWing 792. 高精度减法](https://www.acwing.com/problem/content/description/794/)

## 题目描述

给定两个正整数（不含前导 0），计算它们的差，计算结果可能为负数。

**输入格式**

共两行，每行包含一个整数。

**输出格式**

共一行，包含所求的差。

**数据范围**

1≤整数长度≤10^5

**输入样例**：

```cpp
32
11
```

**输出样例**：

```cpp
21
```

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


bool cmp(string &a, string &b) {
    if (a.size() != b.size()) return a.size() > b.size();

    for (int i = 0; i < a.size(); ++i)
        if (a[i] != b[i])
            return a[i] > b[i];

    return true;
}

string sub(string &a, string &b) {
    reverse(a);
    reverse(b);
    int carry = 0;
    string result;
    for (size_t i = 0; i < a.size(); ++i) {
        carry = a[i] - '0' + carry;
        if (i < b.size()) carry -= b[i] - '0';
        result.push_back((carry + 10) % 10 + '0');
        if (carry >= 0) carry = 0;
        else carry = -1;
    }
    while (result.length() > 1 && result[result.length() - 1] == '0') result.erase(result.length() - 1, 1);
    reverse(result);
    return result;
}

int main() {
    string a, b;
    cin >> a >> b;
    if (cmp(a, b)) cout << sub(a, b);
    else cout << "-" << sub(b, a);
}
```

```cpp
#include <iostream>
#include <vector>

using namespace std;

bool cmp(vector<int> &A, vector<int> &B)
{
    if (A.size() != B.size()) return A.size() > B.size();

    for (int i = A.size() - 1; i >= 0; i -- )
        if (A[i] != B[i])
            return A[i] > B[i];

    return true;
}

vector<int> sub(vector<int> &A, vector<int> &B)
{
    vector<int> C;
    for (int i = 0, t = 0; i < A.size(); i ++ )
    {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1;
        else t = 0;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

int main()
{
    string a, b;
    vector<int> A, B;
    cin >> a >> b;
    for (int i = a.size() - 1; i >= 0; i -- ) A.push_back(a[i] - '0');
    for (int i = b.size() - 1; i >= 0; i -- ) B.push_back(b[i] - '0');

    vector<int> C;

    if (cmp(A, B)) C = sub(A, B);
    else C = sub(B, A), cout << '-';

    for (int i = C.size() - 1; i >= 0; i -- ) cout << C[i];
    cout << endl;

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

func cmp(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return len(s1) > len(s2)
	}
	for i := range s1 {
		if s1[i] != s2[i] {
			return s1[i] > s2[i]
		}
	}
	return true
}

func sub(a, b string) string {
	a = reverse(a)
	b = reverse(b)
	carry := 0
	var result strings.Builder
	for i := 0; i < len(a); i++ {
		if i < len(a) {
			carry += int(a[i] - '0')
		}
		if i < len(b) {
			carry -= int(b[i] - '0')
		}
        result.WriteByte(uint8((carry+10)%10) + '0')
		if carry >= 0 {
			carry = 0
		} else {
			carry = -1
		}
	}
	resStr := reverse(result.String())
	for len(resStr) > 1 && resStr[0] == '0' {
		resStr = resStr[1:]
	}
	return resStr
}

func main() {
	var a, b string
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	if cmp(a, b) {
		fmt.Println(sub(a, b))
	} else {
		fmt.Println("-" + sub(b, a))
	}
}
```

## 模板

```cpp
// C = A - B, 满足A >= B, A >= 0, B >= 0
vector<int> sub(vector<int> &A, vector<int> &B)
{
    vector<int> C;
    for (int i = 0, t = 0; i < A.size(); i ++ )
    {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1;
        else t = 0;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}
```

