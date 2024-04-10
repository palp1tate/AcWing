# [AcWing 794. 高精度除法](https://www.acwing.com/problem/content/796/)

## 题目描述

给定两个非负整数（不含前导 0） A，B，请你计算 A/B 的商和余数。

**输入格式**

共两行，第一行包含整数 A，第二行包含整数 B。

**输出格式**

共两行，第一行输出所求的商，第二行输出所求余数。

**数据范围**

1≤A 的长度≤100000,

1≤B≤10000,

B 一定不为 0

**输入样例**：

```cpp
7
2
```

**输出样例**：

```cpp
3
1
```

## C++

```cpp
#include <iostream>
#include <string>

using namespace std;

string div(string &a, int b, int &carry) {
    carry = 0;
    string result;
    for (size_t i = 0; i < a.size(); ++i) {
        carry = a[i] - '0' + carry * 10;
        result.push_back(carry / b + '0');
        carry %= b;
    }

    while (result.size() > 1 && result[0] == '0') result.erase(0, 1);
    return result;
}

int main() {
    string a;
    int b, carry;
    cin >> a >> b;
    cout << div(a, b, carry) << endl;
    cout << carry << endl;
    return 0;
}
```

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> div(vector<int> &A, int b, int &r)
{
    vector<int> C;
    r = 0;
    for (int i = A.size() - 1; i >= 0; i -- )
    {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

int main()
{
    string a;
    vector<int> A;

    int B;
    cin >> a >> B;
    for (int i = a.size() - 1; i >= 0; i -- ) A.push_back(a[i] - '0');

    int r;
    auto C = div(A, B, r);

    for (int i = C.size() - 1; i >= 0; i -- ) cout << C[i];

    cout << endl << r << endl;

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

func div(a string, b int) (string, int) {
	carry := 0
	var result strings.Builder
	for i := 0; i < len(a); i++ {
		carry = carry*10 + int(a[i]-'0')
		result.WriteByte(uint8(carry/b) + '0')
		carry %= b
	}
	resStr := result.String()
	for len(resStr) > 1 && resStr[0] == '0' {
		resStr = resStr[1:]
	}
	return resStr, carry
}

func main() {
	var a string
	var b int
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	res, carry := div(a, b)
	fmt.Println(res)
	fmt.Println(carry)
}
```

