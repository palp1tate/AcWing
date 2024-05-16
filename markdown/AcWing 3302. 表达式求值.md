# [AcWing 3302. 表达式求值](https://www.acwing.com/problem/content/3305/)

## 题目描述

给定一个表达式，其中运算符仅包含 `+,-,*,/`（加 减 乘 整除），可能包含括号，请你求出表达式的最终值。

**注意：**

- 数据保证给定的表达式合法。
- 题目保证符号 `-` 只作为减号出现，不会作为负号出现，例如，`-1+2`,`(2+2)*(-(1+1)+2)` 之类表达式均不会出现。
- 题目保证表达式中所有数字均为正整数。
- 题目保证表达式在中间计算过程以及结果中，均不超过 2^31−1。
- 题目中的整除是指向 0 取整，也就是说对于大于 0 的结果向下取整，例如 5/3=1，对于小于 0 的结果向上取整，例如 5/(1−4)=−1。
- C++和 Java 中的整除默认是向零取整；Python 中的整除`//`默认向下取整，因此 Python 的`eval()`函数中的整除也是向下取整，在本题中不能直接使用。

**输入格式**

共一行，为给定表达式。

**输出格式**

共一行，为表达式的结果。

**数据范围**

表达式的长度不超过 10^5。

**输入样例**：

```cpp
(2+2)*(1+1)
```

**输出样例**：

```cpp
8
```

## C++

```cpp
#include <iostream>
#include <algorithm>
#include <stack>
#include <unordered_map>

using namespace std;

// 用于存储操作数的栈
stack<int> num;
// 用于存储操作符的栈
stack<char> op;

// 执行一次计算操作
void eval() {
    // 获取并弹出栈顶的两个操作数
    auto b = num.top();
    num.pop();
    auto a = num.top();
    num.pop();

    // 获取并弹出栈顶的操作符
    auto c = op.top();
    op.pop();

    int x;
    // 根据操作符进行相应的计算
    if (c == '+') x = a + b;
    else if (c == '-') x = a - b;
    else if (c == '*') x = a * b;
    else x = a / b;

    // 将计算结果压回操作数栈
    num.push(x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    // 定义操作符优先级的映射
    unordered_map<char, int> pr{{'+', 1},
                                {'-', 1},
                                {'*', 2},
                                {'/', 2}};
    string str;
    // 读取输入的表达式
    cin >> str;

    // 遍历输入的表达式
    for (int i = 0; i < str.size(); i++) {
        auto c = str[i];

        // 如果当前字符是数字
        if (isdigit(c)) {
            int x = 0, j = i;
            // 提取完整的数字
            while (j < str.size() && isdigit(str[j]))
                x = x * 10 + str[j++] - '0';
            // 更新索引i
            i = j - 1;
            // 将数字压入操作数栈
            num.push(x);
        }
            // 如果当前字符是左括号
        else if (c == '(') op.push(c);
            // 如果当前字符是右括号
        else if (c == ')') {
            // 处理所有括号内的操作符
            while (op.top() != '(') eval();
            // 弹出左括号
            op.pop();
        }
            // 如果当前字符是操作符
        else {
            // 处理优先级高于或等于当前操作符的操作符
            while (!op.empty() && op.top() != '(' && pr[op.top()] >= pr[c]) eval();
            // 将当前操作符压入操作符栈
            op.push(c);
        }
    }

    // 处理栈中剩余的操作符
    while (!op.empty()) eval();

    // 输出最终结果
    cout << num.top() << endl;
    return 0;
}
```

## Go

```go
package main

import (
	"container/list"
	"fmt"
)

// 用于存储操作数的栈
var num *list.List

// 用于存储操作符的栈
var op *list.List

// 执行一次计算操作
func eval() {
	// 获取并弹出栈顶的两个操作数
	b := num.Remove(num.Back()).(int)
	a := num.Remove(num.Back()).(int)

	// 获取并弹出栈顶的操作符
	c := op.Remove(op.Back()).(rune)

	var x int
	// 根据操作符进行相应的计算
	switch c {
	case '+':
		x = a + b
	case '-':
		x = a - b
	case '*':
		x = a * b
	case '/':
		x = a / b
	}

	// 将计算结果压回操作数栈
	num.PushBack(x)
}

func main() {
	// 定义操作符优先级的映射
	pr := map[rune]int{'+': 1,
		'-': 1,
		'*': 2,
		'/': 2}

	num = list.New()
	op = list.New()

	var str string
	fmt.Scan(&str)

	// 遍历输入的表达式
	for i := 0; i < len(str); i++ {
		c := rune(str[i])

		// 如果当前字符是数字
		if '0' <= c && c <= '9' {
			x := 0
			j := i
			// 提取完整的数字
			for j < len(str) && '0' <= rune(str[j]) && rune(str[j]) <= '9' {
				digit := int(str[j] - '0')
				x = x*10 + digit
				j++
			}
			// 更新索引i
			i = j - 1
			// 将数字压入操作数栈
			num.PushBack(x)
		} else if c == '(' { // 如果当前字符是左括号
			op.PushBack(c)
		} else if c == ')' { // 如果当前字符是右括号
			// 处理所有括号内的操作符
			for op.Back().Value.(rune) != '(' {
				eval()
			}
			// 弹出左括号
			op.Remove(op.Back())
		} else { // 如果当前字符是操作符
			// 处理优先级高于或等于当前操作符的操作符
			for op.Len() > 0 && op.Back().Value.(rune) != '(' && pr[op.Back().Value.(rune)] >= pr[c] {
				eval()
			}
			// 将当前操作符压入操作符栈
			op.PushBack(c)
		}
	}

	// 处理栈中剩余的操作符
	for op.Len() > 0 {
		eval()
	}

	// 输出最终结果
	fmt.Println(num.Back().Value.(int))
}
```

