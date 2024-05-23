# [AcWing 831. KMP 字符串](https://www.acwing.com/problem/content/833/)

## 题目描述

给定一个字符串 𝑆，以及一个模式串 𝑃，所有字符串中只包含大小写英文字母以及阿拉伯数字。

模式串 𝑃 在字符串 𝑆 中多次作为子串出现。

求出模式串 𝑃 在字符串 𝑆 中所有出现的位置的起始下标。

**输入格式**

第一行输入整数 𝑁，表示字符串 𝑃 的长度。

第二行输入字符串 𝑃。

第三行输入整数 𝑀，表示字符串 𝑆 的长度。

第四行输入字符串 𝑆。

**输出格式**

共一行，输出所有出现位置的起始下标（下标从 0 开始计数），整数之间用空格隔开。

**数据范围**

1≤𝑁≤10^5
1≤𝑀≤10^6

**输入样例**：

```cpp
3
aba
5
ababa
```

**输出样例**：

```cpp
0 2
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 100010, M = 1000010;

int n, m;
int nextArr[N];
char text[M], pattern[N];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    // 输入模式串长度n和模式串，从索引1开始存储模式串
    cin >> n >> (pattern + 1) >> m >> (text + 1); // 输入文本串长度m和文本串，从索引1开始存储文本串

    // 计算 next 数组
    for (int i = 2, j = 0; i <= n; i++) {
        // 当字符不匹配时，跳转到前一位置的 next 数组位置
        while (j && pattern[i] != pattern[j + 1]) j = nextArr[j];
        // 如果字符匹配，j加1
        if (pattern[i] == pattern[j + 1]) j++;
        // 记录 next 数组当前位置的值
        nextArr[i] = j;
    }

    // KMP 匹配过程
    for (int i = 1, j = 0; i <= m; i++) {
        // 当字符不匹配时，跳转到前一位置的 next 数组位置
        while (j && text[i] != pattern[j + 1]) j = nextArr[j];
        // 如果字符匹配，j加1
        if (text[i] == pattern[j + 1]) j++;
        // 如果匹配到整个模式串，输出匹配起始位置
        if (j == n) {
            cout << i - n << " ";
            // 继续查找下一个可能的匹配位置
            j = nextArr[j];
        }
    }

    return 0;
}
```

`next` 数组在 KMP（Knuth-Morris-Pratt）字符串匹配算法中起到关键作用。它的主要目的是在模式匹配过程中，当遇到字符不匹配的情况时，提供一种快速跳转的方法，从而避免重复比较已经匹配过的字符。

具体来说，`next` 数组的作用有以下几点：

1. **跳过不必要的比较**：当在文本中匹配模式串的过程中遇到字符不匹配时，`next` 数组可以帮助我们快速确定下一个匹配的起始位置，而不是回退到上一个字符再重新开始匹配。
2. **提高匹配效率**：通过利用`next` 数组的信息，可以将原本可能需要重复比较的操作优化为线性时间复杂度，从而使得 KMP 算法能够在 O(n + m) 时间内完成匹配任务，其中 n 是文本长度，m 是模式串长度。
3. **记录部分匹配信息**：`next` 数组记录了每个位置之前的最长相同前缀和后缀的长度，这些信息用于在匹配失败时快速确定新的匹配位置。

举例说明`next` 数组的构建和作用：

假设我们有一个模式串 `pattern` = "ABABC"。

- 计算`next` 数组的步骤如下：

1. `pattern[1]` = 'A'，没有前缀和后缀，所以 `next[1]` = 0。
2. `pattern[2]` = 'B'，没有前缀和后缀，所以 `next[2]` = 0。
3. `pattern[3]` = 'A'，前缀"A"和后缀"A"匹配，所以 `next[3]` = 1。
4. `pattern[4]` = 'B'，前缀"AB"和后缀"AB"匹配，所以 `next[4]` = 2。
5. `pattern[5]` = 'C'，没有前缀和后缀匹配，所以 `next[5]` = 0。

构建的 `next` 数组为 `[0, 0, 1, 2, 0]`。

- 使用`next` 数组进行匹配：

当我们在文本中匹配模式串时，如果在某个位置字符不匹配，可以使用`next` 数组跳转到上一个可能的匹配位置，避免重新比较已经匹配的部分。

## Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const N = 100010
const M = 1000010

var (
	n, m    int
	nextArr [N]int
	text    [M]byte
	pattern [N]byte
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	// 读取模式串长度和模式串
	fmt.Fscanf(reader, "%d\n", &n)
	patternLine, _ := reader.ReadString('\n')
	copy(pattern[1:], patternLine)

	// 读取文本串长度和文本串
	fmt.Fscanf(reader, "%d\n", &m)
	textLine, _ := reader.ReadString('\n')
	copy(text[1:], textLine)

	// 计算 next 数组
	for i, j := 2, 0; i <= n; i++ {
		for j > 0 && pattern[i] != pattern[j+1] {
			j = nextArr[j]
		}
		if pattern[i] == pattern[j+1] {
			j++
		}
		nextArr[i] = j
	}

	// KMP 匹配过程
	for i, j := 1, 0; i <= m; i++ {
		for j > 0 && text[i] != pattern[j+1] {
			j = nextArr[j]
		}
		if text[i] == pattern[j+1] {
			j++
		}
		if j == n {
			fmt.Fprintf(writer, "%d ", i-n)
			j = nextArr[j]
		}
	}
}
```

## 模板

```cpp
// s[]是长文本，p[]是模式串，n是s的长度，m是p的长度
求模式串的Next数组：
for (int i = 2, j = 0; i <= m; i ++ )
{
    while (j && p[i] != p[j + 1]) j = ne[j];
    if (p[i] == p[j + 1]) j ++ ;
    ne[i] = j;
}

// 匹配
for (int i = 1, j = 0; i <= n; i ++ )
{
    while (j && s[i] != p[j + 1]) j = ne[j];
    if (s[i] == p[j + 1]) j ++ ;
    if (j == m)
    {
        j = ne[j];
        // 匹配成功后的逻辑
    }
}
```

