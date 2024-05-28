# [AcWing 835. Trie 字符串统计](https://www.acwing.com/problem/content/837/)

## 题目描述

维护一个字符串集合，支持两种操作：

1. `I x` 向集合中插入一个字符串 𝑥；
2. `Q x` 询问一个字符串在集合中出现了多少次。

共有 𝑁 个操作，所有输入的字符串总长度不超过 10^5，字符串仅包含小写英文字母。

**输入格式**

第一行包含整数 𝑁，表示操作数。

接下来 𝑁 行，每行包含一个操作指令，指令为 `I x` 或 `Q x` 中的一种。

**输出格式**

对于每个询问指令 `Q x`，都要输出一个整数作为结果，表示 𝑥 在集合中出现的次数。

每个结果占一行。

**数据范围**

1≤𝑁≤2∗10^4

**输入样例**：

```cpp
5
I abc
Q abc
Q ab
I ab
Q ab
```

**输出样例**：

```cpp
1
0
1
```

## C++

```cpp
#include <iostream>
#include <string>

using namespace std;

const int MAX_NODES = 100010; // 定义最大节点数

int trie[MAX_NODES][26], count[MAX_NODES], index; // trie数组用于存储字典树，count数组用于计数，index用于记录节点数量

// 插入单词到字典树中
void insert(const string &word) {
    int node = 0; // 从根节点开始
    for (char letter: word) { // 遍历单词中的每个字母
        int idx = letter - 'a'; // 将字母映射到[0, 25]的范围内
        if (!trie[node][idx]) trie[node][idx] = ++index; // 如果当前节点的子节点不存在，则创建新的节点
        node = trie[node][idx]; // 移动到下一个节点
    }
    ++count[node]; // 单词插入完成，对应节点的计数加一
}

// 查询字典树中某个单词的出现次数
int query(const string &word) {
    int node = 0; // 从根节点开始
    for (char letter: word) { // 遍历单词中的每个字母
        int idx = letter - 'a'; // 将字母映射到[0, 25]的范围内
        if (!trie[node][idx]) return 0; // 如果当前节点的子节点不存在，则说明单词不存在于字典树中，返回0
        node = trie[node][idx]; // 移动到下一个节点
    }
    return count[node]; // 返回单词对应节点的计数值
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    while (n--) {
        char op;
        string word;
        cin >> op >> word;
        if (op == 'I') insert(word);
        else cout << query(word) << endl;
    }

    return 0;
}
```

## Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	AlphabetSize = 26
	MaxNodes     = 100010
)

var (
	trie  [MaxNodes][AlphabetSize]int
	count [MaxNodes]int
	index int
)

// 插入单词到字典树中
func insert(word string) {
	node := 0                        // 从根节点开始
	for i := 0; i < len(word); i++ { // 遍历单词中的每个字母
		letter := word[i]
		idx := letter - 'a'       // 将字母映射到[0, 25]的范围内
		if trie[node][idx] == 0 { // 如果当前节点的子节点不存在，则创建新的节点
			index++
			trie[node][idx] = index
		}
		node = trie[node][idx] // 移动到下一个节点
	}
	count[node]++ // 单词插入完成，对应节点的计数加一
}

// 查询字典树中某个单词的出现次数
func query(word string) int {
	node := 0                        // 从根节点开始
	for i := 0; i < len(word); i++ { // 遍历单词中的每个字母
		letter := word[i]
		idx := letter - 'a'       // 将字母映射到[0, 25]的范围内
		if trie[node][idx] == 0 { // 如果当前节点的子节点不存在，则说明单词不存在于字典树中
			return 0
		}
		node = trie[node][idx] // 移动到下一个节点
	}
	return count[node] // 返回单词对应节点的计数值
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		var op byte
		var word string
		fmt.Fscanf(reader, "%c %s\n", &op, &word)
		if op == 'I' {
			insert(word)
		} else {
			fmt.Fprintln(writer, query(word))
		}
	}
}
```

## 模板

```cpp
int son[N][26], cnt[N], idx;
// 0号点既是根节点，又是空节点
// son[][]存储树中每个节点的子节点
// cnt[]存储以每个节点结尾的单词数量

// 插入一个字符串
void insert(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) son[p][u] = ++ idx;
        p = son[p][u];
    }
    cnt[p] ++ ;
}

// 查询字符串出现的次数
int query(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) return 0;
        p = son[p][u];
    }
    return cnt[p];
}
```

