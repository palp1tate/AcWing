# [AcWing 828. 模拟栈](https://www.acwing.com/problem/content/830/) 

实现一个栈，栈初始为空，支持四种操作：

1. `push x` – 向栈顶插入一个数 𝑥；
2. `pop` – 从栈顶弹出一个数；
3. `empty` – 判断栈是否为空；
4. `query` – 查询栈顶元素。

现在要对栈进行 𝑀 个操作，其中的每个操作 3 和操作 4 都要输出相应的结果。

**输入格式**

第一行包含整数 𝑀，表示操作次数。

接下来 𝑀 行，每行包含一个操作命令，操作命令为 `push x`，`pop`，`empty`，`query` 中的一种。

**输出格式**

对于每个 `empty` 和 `query` 操作都要输出一个查询结果，每个结果占一行。

其中，`empty` 操作的查询结果为 `YES` 或 `NO`，`query` 操作的查询结果为一个整数，表示栈顶元素的值。

**数据范围**

1≤𝑀≤100000,

1≤𝑥≤10^9,

所有操作保证合法。

**输入样例**：

```cpp
10
push 5
query
push 6
pop
query
pop
empty
push 4
query
empty
```

**输出样例**：

```cpp
5
5
YES
4
NO
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

long long stack[N];
long long head = 0;


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
            stack[++head] = k;
        } else if (command == "pop") head--;
        else if (command == "empty") {
            if (head == 0) cout << "YES" << endl;
            else cout << "NO" << endl;
        } else cout << stack[head] << endl;
    }
}
```

## Go

```go
package main

import "fmt"

const N int = 1e5 + 10

func main() {
	stack := make([]int64, N)
	head := 0
	var m int
	fmt.Scanf("%d", &m)
	for i := 0; i < m; i++ {
		var op string
		var x int64
		fmt.Scanf("%s", &op)
		if op == "push" {
			fmt.Scanf("%d", &x)
			head++
			stack[head] = x
		} else if op == "pop" {
			head--
		} else if op == "empty" {
			if head == 0 {
				fmt.Println("YES")
			} else {
				fmt.Println("NO")
			}
		} else if op == "query" {
			fmt.Println(stack[head])
		}
	}
}
```

## 模板

```cpp
// tt表示栈顶
int stk[N], tt = 0;

// 向栈顶插入一个数
stk[ ++ tt] = x;

// 从栈顶弹出一个数
tt -- ;

// 栈顶的值
stk[tt];

// 判断栈是否为空，如果 tt > 0，则表示不为空
if (tt > 0)
{

}
```

