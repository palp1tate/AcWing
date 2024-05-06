# [AcWing 827. 双链表](https://www.acwing.com/problem/content/829/)

## 题目描述

实现一个双链表，双链表初始为空，支持 5 种操作：

1. 在最左侧插入一个数；
2. 在最右侧插入一个数；
3. 将第 k 个插入的数删除；
4. 在第 k 个插入的数左侧插入一个数；
5. 在第 k 个插入的数右侧插入一个数

现在要对该链表进行 M 次操作，进行完所有操作后，从左到右输出整个链表。

**注意**:题目中第 k 个插入的数并不是指当前链表的第 k 个数。例如操作过程中一共插入了 n 个数，则按照插入的时间顺序，这 n 个数依次为：第 1 个插入的数，第 2 个插入的数，……第 n 个插入的数。

**输入格式**

第一行包含整数 M，表示操作次数。

接下来 M 行，每行包含一个操作命令，操作命令可能为以下几种：

1. `L x`，表示在链表的最左端插入数 x。
2. `R x`，表示在链表的最右端插入数 x。
3. `D k`，表示将第 k 个插入的数删除。
4. `IL k x`，表示在第 k 个插入的数左侧插入一个数。
5. `IR k x`，表示在第 k 个插入的数右侧插入一个数。

**输出格式**

共一行，将整个链表从左到右输出。

**数据范围**

1≤M≤100000
所有操作保证合法。

**输入样例**：

```cpp
10
R 7
D 1
L 3
IL 2 10
D 3
IL 2 7
L 8
R 9
IL 4 7
IR 2 2
```

**输出样例**：

```cpp
8 7 7 3 2 9
```

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

int current, value[N], l[N], r[N];

void insert(int k, int x) {
    value[current] = x;
    l[current] = k, r[current] = r[k];
    l[r[k]] = current, r[k] = current++;
}

void remove(int k) {
    r[l[k]] = r[k];
    l[r[k]] = l[k];
}

int main() {
    int m;
    scanf("%d", &m);
    r[0] = 1, l[1] = 0;
    current = 2;
    while (m--) {
        char command[3];
        int k, x;
        scanf("%s", command);
        if (command[0] == 'L') {
            scanf("%d", &x);
            insert(0, x);
        } else if (command[0] == 'R') {
            scanf("%d", &x);
            insert(l[1], x);
        } else if (command[0] == 'D') {
            scanf("%d", &k);
            remove(k + 1);
        } else if (command[1] == 'L') {
            scanf("%d%d", &k, &x);
            insert(l[k + 1], x);
        } else {
            scanf("%d%d", &k, &x);
            insert(k + 1, x);
        }

    }
    for (int i = r[0]; i != 1; i = r[i]) printf("%d ", value[i]);
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 1e5 + 10;

int current, value[N], l[N], r[N];

void insert(int k, int x) {
    value[current] = x;
    l[current] = k, r[current] = r[k];
    l[r[k]] = current, r[k] = current++;
}

void remove(int k) {
    r[l[k]] = r[k];
    l[r[k]] = l[k];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int m;
    cin >> m;
    r[0] = 1, l[1] = 0;
    current = 2;
    while (m--) {
        string command;
        int k, x;
        cin >> command;
        if (command[0] == 'L') {
            cin >> x;
            insert(0, x);
        } else if (command[0] == 'R') {
            cin >> x;
            insert(l[1], x);
        } else if (command[0] == 'D') {
            cin >> k;
            remove(k + 1);
        } else if (command[1] == 'L') {
            cin >> k >> x;
            insert(l[k + 1], x);
        } else {
            cin >> k >> x;
            insert(k + 1, x);
        }

    }
    for (int i = r[0]; i != 1; i = r[i]) cout << value[i] << ' ';
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

struct Node {
    int value;
    int left;
    int right;
};

const int N = 1e5 + 10;
Node nodes[N];
int current;

void insert(int k, int x) {
    nodes[current].value = x;
    nodes[current].left = k;
    nodes[current].right = nodes[k].right;
    nodes[nodes[k].right].left = current;
    nodes[k].right = current++;
}

void remove(int k) {
    nodes[nodes[k].left].right = nodes[k].right;
    nodes[nodes[k].right].left = nodes[k].left;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int m;
    cin >> m;
    nodes[0].right = 1;
    nodes[1].left = 0;
    current = 2;
    while (m--) {
        string command;
        int k, x;
        cin >> command;
        if (command[0] == 'L') {
            cin >> x;
            insert(0, x);
        } else if (command[0] == 'R') {
            cin >> x;
            insert(nodes[1].left, x);
        } else if (command[0] == 'D') {
            cin >> k;
            remove(k + 1);
        } else if (command[1] == 'L') {
            cin >> k >> x;
            insert(nodes[k + 1].left, x);
        } else {
            cin >> k >> x;
            insert(k + 1, x);
        }

    }
    for (int i = nodes[0].right; i != 1; i = nodes[i].right) cout << nodes[i].value << ' ';
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
	"strconv"
	"strings"
)

const N = 1e5 + 10

var (
	current int
	value   [N]int
	l       [N]int
	r       [N]int
)

func insert(k, x int) {
	value[current] = x
	l[current] = k
	r[current] = r[k]
	l[r[k]] = current
	r[k] = current
	current++
}

func remove(k int) {
	r[l[k]] = r[k]
	l[r[k]] = l[k]
}

func main() {
	reader := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var m int
	fmt.Scanf("%d", &m)

	r[0] = 1
	l[1] = 0
	current = 2

	for i := 0; i < m; i++ {
		reader.Scan()
		line := reader.Text()
		parts := strings.Fields(line)
		command := parts[0]
		switch command {
		case "L":
			x, _ := strconv.Atoi(parts[1])
			insert(0, x)
		case "R":
			x, _ := strconv.Atoi(parts[1])
			insert(l[1], x)
		case "D":
			k, _ := strconv.Atoi(parts[1])
			remove(k + 1)
		case "IL":
			k, _ := strconv.Atoi(parts[1])
			x, _ := strconv.Atoi(parts[2])
			insert(l[k+1], x)
		case "IR":
			k, _ := strconv.Atoi(parts[1])
			x, _ := strconv.Atoi(parts[2])
			insert(k+1, x)
		}
	}

	for i := r[0]; i != 1; i = r[i] {
		fmt.Fprintf(writer, "%d ", value[i])
	}
}
```

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	value int
	left  int
	right int
}

const N = 1e5 + 10

var (
	nodes   [N]Node
	current int
)

func insert(k, x int) {
	nodes[current].value = x
	nodes[current].left = k
	nodes[current].right = nodes[k].right
	nodes[nodes[k].right].left = current
	nodes[k].right = current
	current++
}

func remove(k int) {
	nodes[nodes[k].left].right = nodes[k].right
	nodes[nodes[k].right].left = nodes[k].left
}

func main() {
	reader := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var m int
	fmt.Scanf("%d", &m)

	nodes[0].right = 1
	nodes[1].left = 0
	current = 2

	for i := 0; i < m; i++ {
		reader.Scan()
		line := reader.Text()
		parts := strings.Fields(line)
		switch parts[0] {
		case "L":
			x, _ := strconv.Atoi(parts[1])
			insert(0, x)
		case "R":
			x, _ := strconv.Atoi(parts[1])
			insert(nodes[1].left, x)
		case "D":
			k, _ := strconv.Atoi(parts[1])
			remove(k + 1)
		case "IL":
			k, _ := strconv.Atoi(parts[1])
			x, _ := strconv.Atoi(parts[2])
			insert(nodes[k+1].left, x)
		case "IR":
			k, _ := strconv.Atoi(parts[1])
			x, _ := strconv.Atoi(parts[2])
			insert(k+1, x)
		}
	}

	for i := nodes[0].right; i != 1; i = nodes[i].right {
		fmt.Fprintf(writer, "%d ", nodes[i].value)
	}
}
```

## 模板

```cpp
// e[]表示节点的值，l[]表示节点的左指针，r[]表示节点的右指针，idx表示当前用到了哪个节点
int e[N], l[N], r[N], idx;

// 初始化
void init()
{
    //0是左端点，1是右端点
    r[0] = 1, l[1] = 0;
    idx = 2;
}

// 在节点a的右边插入一个数x
void insert(int a, int x)
{
    e[idx] = x;
    l[idx] = a, r[idx] = r[a];
    l[r[a]] = idx, r[a] = idx ++ ;
}

// 删除节点a
void remove(int a)
{
    l[r[a]] = l[a];
    r[l[a]] = r[a];
}
```

