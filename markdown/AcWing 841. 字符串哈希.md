# [AcWing 841. 字符串哈希](https://www.acwing.com/problem/content/843/)

## 题目描述

给定一个长度为 𝑛 的字符串，再给定 𝑚 个询问，每个询问包含四个整数 𝑙1,𝑟1,𝑙2,𝑟2，请你判断\[𝑙1,𝑟1] 和\[𝑙2,𝑟2] 这两个区间所包含的字符串子串是否完全相同。

字符串中只包含大小写英文字母和数字。

**输入格式**

第一行包含整数 𝑛 和 𝑚，表示字符串长度和询问次数。

第二行包含一个长度为 𝑛 的字符串，字符串中只包含大小写英文字母和数字。

接下来 𝑚 行，每行包含四个整数 𝑙1,𝑟1,𝑙2,𝑟2，表示一次询问所涉及的两个区间。

注意，字符串的位置从 1 开始编号。

**输出格式**

对于每个询问输出一个结果，如果两个字符串子串完全相同则输出 `Yes`，否则输出 `No`。

每个结果占一行。

**数据范围**

1≤𝑛,𝑚≤10^5

**输入样例**：

```cpp
8 3
aabbaabb
1 3 5 7
1 3 6 8
1 2 1 2
```

**输出样例**：

```cpp
Yes
No
Yes
```

## C++

```cpp
#include <iostream>

using namespace std;

typedef unsigned long long ULL;

const int N = 100010, P = 131;

int n, m;
char str[N];
ULL h[N], p[N];// p数组存放幂，h数组表示前缀和哈希值

ULL get(int l, int r) {
    return h[r] - h[l - 1] * p[r - l + 1];
}

int main() {
    scanf("%d%d", &n, &m);
    scanf("%s", str + 1);

    p[0] = 1;
    for (int i = 1; i <= n; i++) {
        h[i] = h[i - 1] * P + str[i];
        p[i] = p[i - 1] * P;
    }

    while (m--) {
        int l1, r1, l2, r2;
        scanf("%d%d%d%d", &l1, &r1, &l2, &r2);

        if (get(l1, r1) == get(l2, r2)) puts("Yes");
        else puts("No");
    }

    return 0;
}
```

**思路**

* 把字符串看成是一个 P 进制数，每个字符的 ASCII 码对应数的一位
* ASCII 范围 0 - 127，最少 128 进制，经验上取 131 或 13331 冲突率低
* 字符串很长，对应的数太大，通过模 2^64 把它映射到 [0, 2^64 - 1]
* 用 unsigned long long 存储，溢出相当于对 2^64 取模，省略了手动运算
* 该方法的好处是，可以利用前缀哈希直接求出子串哈希（减去高位）

```cpp
hash(DEF) = hash(ABCDEF) - hash(ABC) x P^3
    1       2       3       4       5       6
    A       B       C       D       E       F  
  1xP^5 + 2xP^4 + 3xP^3 + 4xP^2 + 5xP^1 + 6xP^0

                            D       E       F
                          4xP^2 + 5xP^1 + 6xP^0

    A       B       C  
  1xP^2 + 2xP^1 + 3xP^0
```

* 不要把某一位映射成 P 进制 0，例如，A 如果是 0，则 AA 也是 0，就会出现冲突
* `\0` 的 ASCII 是 0，本题不出现该字符，不用担心上一点
* 使用这种方法就假定了人品足够好，不出现冲突

## Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	N = 100010
	P = 131
)

var (
	n, m int
	str  string
	h    [N]uint64
	p    [N]uint64
)

func get(l, r int) uint64 {
	return h[r] - h[l-1]*p[r-l+1]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanf(reader, "%d%d\n", &n, &m)
	str, _ = reader.ReadString('\n')
	str = " " + str[:len(str)-1] // 加空格使索引从1开始，同时去除末尾的换行符

	p[0] = 1
	for i := 1; i <= n; i++ {
		h[i] = h[i-1]*P + uint64(str[i])
		p[i] = p[i-1] * P
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	for m > 0 {
		var l1, r1, l2, r2 int
		fmt.Fscanf(reader, "%d%d%d%d\n", &l1, &r1, &l2, &r2)

		if get(l1, r1) == get(l2, r2) {
			writer.WriteString("Yes\n")
		} else {
			writer.WriteString("No\n")
		}
		m--
	}
}
```

## 模板

```cpp
核心思想：将字符串看成P进制数，P的经验值是131或13331，取这两个值的冲突概率低
小技巧：取模的数用2^64，这样直接用unsigned long long存储，溢出的结果就是取模的结果

typedef unsigned long long ULL;
ULL h[N], p[N]; // h[k]存储字符串前k个字母的哈希值, p[k]存储 P^k mod 2^64

// 初始化
p[0] = 1;
for (int i = 1; i <= n; i ++ )
{
    h[i] = h[i - 1] * P + str[i];
    p[i] = p[i - 1] * P;
}

// 计算子串 str[l ~ r] 的哈希值
ULL get(int l, int r)
{
    return h[r] - h[l - 1] * p[r - l + 1];
}
```

