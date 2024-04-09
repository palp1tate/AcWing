[AcWing 791. 高精度加法](https://www.acwing.com/problem/content/description/793/)

#### 题目描述

给定两个正整数（不含前导 0），计算它们的和。

**输入格式**

共两行，每行包含一个整数。

**输出格式**

共一行，包含所求的和。

**数据范围**

1≤整数长度≤100000

**输入样例**：

```cpp
12
23
```

**输出样例**：

```cpp
35
```

#### C++

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

string add(string &a, string &b) {
    reverse(a);
    reverse(b);
    size_t n = max(a.size(), b.size()), carry = 0;
    string result;
    for (size_t i = 0; i < n; ++i) {
        if (i < a.size()) carry += a[i] - '0';
        if (i < b.size()) carry += b[i] - '0';
        result.push_back(carry % 10 + '0');
        carry /= 10;
    }
    if (carry) result.push_back(carry + '0');
    reverse(result);
    return result;
}

int main() {
    string a, b;
    cin >> a >> b;
    cout << add(a, b) << endl;
    return 0;
}
```

```cpp
#include <iostream>
#include <string>
#include <algorithm> // std::reverse

using namespace std;

// 实现大整数相加的函数
string add(string &a, string &b) {
    // 反转字符串，使得从最低位开始相加
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    size_t n = max(a.size(), b.size()), carry = 0;
    string result;

    for (size_t i = 0; i < n; i++) {
        if (i < a.size()) carry += a[i] - '0';
        if (i < b.size()) carry += b[i] - '0';
        result.push_back(static_cast<char>(carry % 10 + '0'));
        carry /= 10;
    }

    // 处理最高位的进位
    if (carry) result.push_back(static_cast<char>(carry + '0'));

    // 将结果反转回正确的顺序
    reverse(result.begin(), result.end());

    return result;
}

int main() {
    string a, b;
    cin >> a >> b;
    cout << add(a, b) << endl;
    return 0;
}
```

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> add(vector<int> &A, vector<int> &B) {
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (size_t i = 0; i < A.size(); i++) {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }

    if (t) C.push_back(t);
    return C;
}

int main() {
    string a, b;
    vector<int> A, B;
    cin >> a >> b;
    for (size_t i = a.size(); i > 0; i--) A.push_back(a[i - 1] - '0');
    for (size_t i = b.size(); i > 0; i--) B.push_back(b[i - 1] - '0');

    auto C = add(A, B);

    for (size_t i = C.size(); i > 0; i--) cout << C[i - 1];
    cout << endl;

    return 0;
}
```

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> add(vector<int> &A, vector<int> &B)
{
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i ++ )
    {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }

    if (t) C.push_back(t);
    return C;
}

int main()
{
    string a, b;
    vector<int> A, B;
    cin >> a >> b;
    for (int i = a.size() - 1; i >= 0; i -- ) A.push_back(a[i] - '0');
    for (int i = b.size() - 1; i >= 0; i -- ) B.push_back(b[i] - '0');

    auto C = add(A, B);

    for (int i = C.size() - 1; i >= 0; i -- ) cout << C[i];
    cout << endl;

    return 0;
}
```

#### Go

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

func max(i int, j int) int {
	if i > j {
		return i
	}
	return j
}

func add(a, b string) string {
	a = reverse(a)
	b = reverse(b)
	n := max(len(a), len(b))
	var carry uint8 = 0
	var res strings.Builder
	for i := 0; i < n; i++ {
		if i < len(a) {
			carry += a[i] - '0'
		}
		if i < len(b) {
			carry += b[i] - '0'
		}
		res.WriteByte(carry%10 + '0')
		carry /= 10
	}
	if carry > 0 {
		res.WriteByte(carry + '0')
	}
	return reverse(res.String())
}

func main() {
	var a, b string
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	fmt.Println(add(a, b))
}
```

#### 模板

```cpp
// C = A + B, A >= 0, B >= 0
vector<int> add(vector<int> &A, vector<int> &B)
{
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i ++ )
    {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }

    if (t) C.push_back(t);
    return C;
}
```

