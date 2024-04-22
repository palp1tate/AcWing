# [AcWing 801. 二进制中 1 的个数](https://www.acwing.com/problem/content/803/)

## 题目描述

给定一个长度为 n 的数列，请你求出数列中每个数的二进制表示中 1 的个数。

**输入格式**

第一行包含整数 n。

第二行包含 n 个整数，表示整个数列。

**输出格式**

共一行，包含 n 个整数，其中的第 i 个数表示数列中的第 i 个数的二进制表示中 1 的个数。

**数据范围**

1≤n≤100000,

0≤数列中元素的值≤10^9

**输入样例**：

```cpp
5
1 2 3 4 5
```

**输出样例**：

```cpp
1 1 2 1 2
```

## C++

```cpp
#include <iostream>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    while (n--) {
        int x, s = 0;
        scanf("%d", &x);

        for (int i = x; i; i -= i & -i) s++;

        printf("%d ", s);
    }

    return 0;
}
```

`i -= i & -i` 这行代码是在计算 `i` 的二进制表示中最低位的 `1`，然后从 `i` 中减去这个值。

首先，`-i` 是 `i` 的二进制补码，它的计算方式是先对 `i` 的二进制表示取反，然后加 `1`。这样，`i & -i` 的结果就是 `i` 的二进制表示中最低位的 `1`。

然后，`i -= i & -i` 就是将 `i` 减去它的二进制表示中最低位的 `1`。这样，`i` 的二进制表示中的最低位的 `1` 就被去掉了。

例如，假设 `i` 的值是 `12`，它的二进制表示是 `1100`。`-i` 的二进制表示是 `0100`，所以 `i & -i` 的结果是 `0100`。然后，`i -= i & -i` 的结果就是 `1000`，也就是 `8`。这样，`i` 的二进制表示中的最低位的 `1` 就被去掉了。

这个操作在计算一个数的二进制表示中 `1` 的个数时非常有用，因为每次循环都会去掉 `i` 的二进制表示中的一个 `1`，直到 `i` 变为 `0` 为止。

在 C++中，`-i` 是通过取 `i` 的二进制补码来计算的。具体步骤如下：

1. 首先，对 `i` 的二进制表示取反。这意味着所有的 `1` 变为 `0`，所有的 `0` 变为 `1`。
2. 然后，将取反后的结果加 `1`。

例如，假设 `i` 的值是 `5`，它的二进制表示是 `0101`。取反后，我们得到 `1010`。然后，我们将这个结果加 `1`，得到 `1011`。所以，`-i` 的二进制表示是 `1011`，对应的十进制值是 `-5`。

这种计算方式是基于二进制补码的原理，它是计算机内部表示和处理负数的一种方式。

## Go

```go
package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	params := strings.Fields(line)
	n, _ := strconv.Atoi(params[0])
	line, _ = reader.ReadString('\n')
	params = strings.Fields(line)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i := 0; i < n; i++ {
		var count int
		num, _ := strconv.Atoi(params[i])
		for num > 0 {
			num -= num & -num
			count++
		}
		writer.WriteString(strconv.Itoa(count) + " ")
	}
}
```

```go
package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d\n", &n)
	for i := 0; i < n; i++ {
		var tmp int64
		var count int
		fmt.Scanf("%d", &tmp)
		for tmp > 0 {
			tmp -= tmp & -tmp
			count++
		}
		fmt.Printf("%d ", count)
	}
}
```

## 模板

```cpp
求n的第k位数字: n >> k & 1
返回n的最后一位1：lowbit(n) = n & -n
```

`n >> k` 这个操作是将 `n` 右移 `k` 位。在二进制表示中，右移一位等同于将这个数除以 2。所以，`n >> k` 就是将 `n` 除以 `2` 的 `k` 次方。这个操作的结果是将 `n` 的第 `k` 位移动到最低位。

然后，`& 1` 这个操作是将上述结果与 `1` 进行按位与操作。在二进制表示中，任何数与 `1` 进行按位与操作，结果都等于这个数的最低位。所以，`n >> k & 1` 的结果就是 `n` 的第 `k` 位。

例如，假设 `n` 的值是 `13`，它的二进制表示是 `1101`。如果我们想获取第 `2` 位，我们可以计算 `n >> 2 & 1`：

1. `n >> 2` 的结果是 `11`（即 `3`），这是将 `n` 的第 `2` 位移动到最低位的结果。
2. `3 & 1` 的结果是 `1`，这就是 `n` 的第 `2` 位。
