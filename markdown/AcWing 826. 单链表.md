# [AcWing 826. 单链表](https://www.acwing.com/problem/content/828/)

## 题目描述

实现一个单链表，链表初始为空，支持三种操作：

1. 向链表头插入一个数；
2. 删除第 k 个插入的数后面的一个数；
3. 在第 k 个插入的数后插入一个数。

现在要对该链表进行 M 次操作，进行完所有操作后，从头到尾输出整个链表。

**注意**:题目中第 k 个插入的数并不是指当前链表的第 k 个数。例如操作过程中一共插入了 n 个数，则按照插入的时间顺序，这 n 个数依次为：第 1 个插入的数，第 2 个插入的数，……第 n 个插入的数。

**输入格式**

第一行包含整数 M，表示操作次数。

接下来 M 行，每行包含一个操作命令，操作命令可能为以下几种：

1. `H x`，表示向链表头插入一个数 x。
2. `D k`，表示删除第 k 个插入的数后面的数（当 k 为 0 时，表示删除头结点）。
3. `I k x`，表示在第 k 个插入的数后面插入一个数 x（此操作中 k 均大于 0）。

**输出格式**

共一行，将整个链表从头到尾输出。

**数据范围**

1≤M≤100000

所有操作保证合法。

**输入样例**：

```cpp
10
H 9
I 1 1
D 1
D 0
H 6
I 3 6
I 4 5
I 4 5
I 3 4
D 6
```

**输出样例**：

```cpp
6 4 6 5
```

## C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

const int N = 100005;

int head = -1;           // 链表头的索引，初始化为-1表示空链表
int next_index[N];    // 每个节点的下一个节点索引
int value[N];         // 存储节点值的数组
int free_spot = 0;       // 指向下一个空闲位置的指针

vector<int> nodes;       // 用于快速访问第k个插入的节点

void insertAtHead(int x) {
    int new_node = free_spot++;
    value[new_node] = x;
    next_index[new_node] = head;
    head = new_node;
    nodes.push_back(new_node);
}

void deleteAfter(int k) {
    if (k == 0) {
        if (head != -1) {
            head = next_index[head];
        }
    } else {
        int prev_node = nodes[k - 1];
        int to_delete = next_index[prev_node];
        if (to_delete != -1) {
            next_index[prev_node] = next_index[to_delete];
        }
    }
}

void insertAfter(int k, int x) {
    int prev_node = nodes[k - 1];
    int new_node = free_spot++;
    value[new_node] = x;
    next_index[new_node] = next_index[prev_node];
    next_index[prev_node] = new_node;
    nodes.push_back(new_node);
}

void printList() {
    for (int i = head; i != -1; i = next_index[i]) {
        cout << value[i] << " ";
    }
    cout << endl;
}

int main() {
    int M;
    cin >> M;
    string command;
    int k, x;

    for (int i = 0; i < M; i++) {
        cin >> command;
        if (command == "H") {
            cin >> x;
            insertAtHead(x);
        } else if (command == "D") {
            cin >> k;
            deleteAfter(k);
        } else if (command == "I") {
            cin >> k >> x;
            insertAfter(k, x);
        }
    }

    printList();
    return 0;
}
```

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int value;
    Node* next;
    Node(int val) : value(val), next(NULL) {}
};

class LinkedList {
private:
    Node* head;
    vector<Node*> nodes;  // 用于快速访问第 k 个插入的节点

public:
    LinkedList() : head(NULL) {
        nodes.push_back(NULL);  // 0 索引不使用，对应题目中的 k=0
    }

    void insertAtHead(int val) {
        Node* node = new Node(val);
        node->next = head;
        head = node;
        nodes.push_back(node);  // 记录节点
    }

    void deleteAfter(int k) {
        if (k == 0) {  // 特殊处理删除头结点的情况
            Node* temp = head;
            if (head != NULL) {
                head = head->next;
            }
            delete temp;
        } else if (k < static_cast<int>(nodes.size())) {
            Node* prev = nodes[k];
            if (prev && prev->next) {
                Node* toDelete = prev->next;
                prev->next = toDelete->next;
                delete toDelete;
            }
        }
    }

    void insertAfter(int k, int val) {
        if (k < static_cast<int>(nodes.size())) {
            Node* prev = nodes[k];
            if (prev) {
                Node* node = new Node(val);
                node->next = prev->next;
                prev->next = node;
                nodes.push_back(node);  // 记录新插入的节点
            }
        }
    }

    void printList() {
        Node* current = head;
        if (!current) {
            cout << "\n";
            return;
        }
        while (current) {
            cout << current->value << (current->next ? " " : "\n");
            current = current->next;
        }
    }

    ~LinkedList() {
        Node* current = head;
        while (current) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
};

int main() {
    int M;
    cin >> M;
    LinkedList list;
    string command;
    int k, x;

    for (int i = 0; i < M; ++i) {
        cin >> command;
        if (command == "H") {
            cin >> x;
            list.insertAtHead(x);
        } else if (command == "D") {
            cin >> k;
            list.deleteAfter(k);
        } else if (command == "I") {
            cin >> k >> x;
            list.insertAfter(k, x);
        }
    }

    list.printList();

    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 100010;


// head 表示头结点的下标
// e[i] 表示节点i的值
// ne[i] 表示节点i的next指针是多少
// idx 存储当前已经用到了哪个点
int head, e[N], ne[N], idx;

// 初始化
void init() {
    head = -1;
    idx = 0;
}

// 将x插到头结点
void add_to_head(int x) {
    e[idx] = x, ne[idx] = head, head = idx++;
}

// 将x插到下标是k的点后面
void add(int k, int x) {
    e[idx] = x, ne[idx] = ne[k], ne[k] = idx++;
}

// 将下标是k的点后面的点删掉
void remove(int k) {
    ne[k] = ne[ne[k]];
}

int main() {
    int m;
    cin >> m;

    init();

    while (m--) {
        int k, x;
        char op;

        cin >> op;
        if (op == 'H') {
            cin >> x;
            add_to_head(x);
        } else if (op == 'D') {
            cin >> k;
            if (!k) head = ne[head];
            else remove(k - 1);
        } else {
            cin >> k >> x;
            add(k - 1, x);
        }
    }

    for (int i = head; i != -1; i = ne[i]) cout << e[i] << ' ';
    cout << endl;

    return 0;
}
```

## Go

```go
package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
	"strings"
)

const MAXN = 100005  // 假设最多有100000个操作，每个操作最多插入一个元素

var (
	head int
	nextIndex [MAXN]int
	value [MAXN]int
	freeSpot int
	nodes []int
)

func init() {
	head = -1  // 初始化为空链表
	freeSpot = 0
	nodes = make([]int, 0)
}

func insertAtHead(x int) {
	newNode := freeSpot
	freeSpot++
	value[newNode] = x
	nextIndex[newNode] = head
	head = newNode
	nodes = append(nodes, newNode)
}

func deleteAfter(k int) {
	if k == 0 {
		if head != -1 {
			head = nextIndex[head]
		}
	} else {
		prevNode := nodes[k-1]
		toDelete := nextIndex[prevNode]
		if toDelete != -1 {
			nextIndex[prevNode] = nextIndex[toDelete]
		}
	}
}

func insertAfter(k int, x int) {
	prevNode := nodes[k-1]
	newNode := freeSpot
	freeSpot++
	value[newNode] = x
	nextIndex[newNode] = nextIndex[prevNode]
	nextIndex[prevNode] = newNode
	nodes = append(nodes, newNode)
}

func printList() {
	for i := head; i != -1; i = nextIndex[i] {
		fmt.Printf("%d ", value[i])
	}
	fmt.Println()
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	M, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < M; i++ {
		scanner.Scan()
		parts := strings.Fields(scanner.Text())
		command := parts[0]

		switch command {
		case "H":
			x, _ := strconv.Atoi(parts[1])
			insertAtHead(x)
		case "D":
			k, _ := strconv.Atoi(parts[1])
			deleteAfter(k)
		case "I":
			k, _ := strconv.Atoi(parts[1])
			x, _ := strconv.Atoi(parts[2])
			insertAfter(k, x)
		}
	}

	printList()
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

// Node 表示链表中的一个节点
type Node struct {
	Value int   // 节点存储的值
	Next  *Node // 指向下一个节点的指针
}

// LinkedList 表示链表结构
type LinkedList struct {
	Head  *Node   // 链表的头节点
	Nodes []*Node // 用于记录按插入顺序的节点，以便于快速访问
}

// NewLinkedList 创建并返回一个新的空链表
func NewLinkedList() *LinkedList {
	return &LinkedList{
		Head:  nil,
		Nodes: make([]*Node, 0),
	}
}

// InsertAtHead 在链表的头部插入一个新的节点
func (ll *LinkedList) InsertAtHead(x int) {
	newNode := &Node{Value: x, Next: ll.Head}
	ll.Head = newNode
	ll.Nodes = append(ll.Nodes, newNode)
}

// DeleteAfter 删除第 k 个插入的节点后面的节点
func (ll *LinkedList) DeleteAfter(k int) {
	if k == 0 {
		if ll.Head != nil {
			ll.Head = ll.Head.Next
		}
	} else if k-1 < len(ll.Nodes) {
		prevNode := ll.Nodes[k-1]
		if prevNode != nil && prevNode.Next != nil {
			prevNode.Next = prevNode.Next.Next
		}
	}
}

// InsertAfter 在第 k 个插入的节点后面插入一个新的节点
func (ll *LinkedList) InsertAfter(k int, x int) {
	if k-1 < len(ll.Nodes) {
		prevNode := ll.Nodes[k-1]
		if prevNode != nil {
			newNode := &Node{Value: x, Next: prevNode.Next}
			prevNode.Next = newNode
			ll.Nodes = append(ll.Nodes, newNode)
		}
	}
}

// PrintList 从头到尾打印链表中的所有节点值
func (ll *LinkedList) PrintList() {
	for current := ll.Head; current != nil; current = current.Next {
		fmt.Printf("%d ", current.Value)
	}
	fmt.Println()
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	M, _ := strconv.Atoi(scanner.Text())

	ll := NewLinkedList()

	for i := 0; i < M; i++ {
		scanner.Scan()
		parts := strings.Fields(scanner.Text())
		command := parts[0]

		switch command {
		case "H":
			x, _ := strconv.Atoi(parts[1])
			ll.InsertAtHead(x)
		case "D":
			k, _ := strconv.Atoi(parts[1])
			ll.DeleteAfter(k)
		case "I":
			k, _ := strconv.Atoi(parts[1])
			x, _ := strconv.Atoi(parts[2])
			ll.InsertAfter(k, x)
		}
	}

	ll.PrintList()
}

```

## 模板

```cpp
// head存储链表头，e[]存储节点的值，ne[]存储节点的next指针，idx表示当前用到了哪个节点
int head, e[N], ne[N], idx;

// 初始化
void init()
{
    head = -1;
    idx = 0;
}

// 在链表头插入一个数a
void insert(int a)
{
    e[idx] = a, ne[idx] = head, head = idx ++ ;
}

// 将头结点删除，需要保证头结点存在
void remove()
{
    head = ne[head];
}
```

