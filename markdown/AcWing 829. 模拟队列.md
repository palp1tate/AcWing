# [AcWing 829. 模拟队列](https://www.acwing.com/problem/content/831/)

## 题目描述

实现一个队列，队列初始为空，支持四种操作：

1. `push x` – 向队尾插入一个数 𝑥；
2. `pop` – 从队头弹出一个数；
3. `empty` – 判断队列是否为空；
4. `query` – 查询队头元素。

现在要对队列进行 𝑀 个操作，其中的每个操作 3 和操作 4 都要输出相应的结果。

**输入格式**

第一行包含整数 𝑀，表示操作次数。

接下来 𝑀 行，每行包含一个操作命令，操作命令为 `push x`，`pop`，`empty`，`query` 中的一种。

**输出格式**

对于每个 `empty` 和 `query` 操作都要输出一个查询结果，每个结果占一行。

其中，`empty` 操作的查询结果为 `YES` 或 `NO`，`query` 操作的查询结果为一个整数，表示队头元素的值。

**数据范围**

1≤𝑀≤100000,

1≤𝑥≤10^9,

所有操作保证合法。

**输入样例**：

```cpp
10
push 6
empty
query
pop
empty
push 3
push 4
pop
query
push 6
```

**输出样例**：

```cpp
NO
6
YES
4
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

long long queue[N];
long long head = 0, tail = -1;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int m;
    cin >> m;
    while (m--) {
        string command;
        cin >> command;
        if (command == "push") {
            int k;
            cin >> k;
            queue[++tail] = k;
        } else if (command == "pop") {
            head++;
        } else if (command == "empty") {
            cout << (head <= tail ? "NO" : "YES") << endl;
        } else cout << queue[head] << endl;
    }
    return 0;
}
```

## Go

```go
package main

import "fmt"

const N int = 1e5 + 10

func main() {
	queue := make([]int64, N)
	head := 0
	tail := -1
	var m int
	fmt.Scanf("%d", &m)
	for i := 0; i < m; i++ {
		var op string
		var x int64
		fmt.Scanf("%s", &op)
		if op == "push" {
			fmt.Scanf("%d", &x)
			tail++
			queue[tail] = x
		} else if op == "pop" {
			head++
		} else if op == "empty" {
			if head <= tail {
				fmt.Println("NO")
			} else {
				fmt.Println("YES")
			}
		} else if op == "query" {
			fmt.Println(queue[head])
		}
	}
}
```

## 模板

### 普通队列

```cpp
// hh 表示队头，tt表示队尾
int q[N], hh = 0, tt = -1;

// 向队尾插入一个数
q[ ++ tt] = x;

// 从队头弹出一个数
hh ++ ;

// 队头的值
q[hh];

// 判断队列是否为空，如果 hh <= tt，则表示不为空
if (hh <= tt)
{

}
```

### 循环队列

```cpp
// hh 表示队头，tt表示队尾的后一个位置
int q[N], hh = 0, tt = 0;

// 向队尾插入一个数
q[tt ++ ] = x;
if (tt == N) tt = 0;

// 从队头弹出一个数
hh ++ ;
if (hh == N) hh = 0;

// 队头的值
q[hh];

// 判断队列是否为空，如果hh != tt，则表示不为空
if (hh != tt)
{

}
```

