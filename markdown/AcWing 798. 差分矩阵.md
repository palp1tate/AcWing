# [AcWing 798. 差分矩阵](https://www.acwing.com/problem/content/800/)

## 题目描述

输入一个 n 行 m 列的整数矩阵，再输入 q 个操作，每个操作包含五个整数 x1,y1,x2,y2,c，其中 (x1,y1) 和 (x2,y2)表示一个子矩阵的左上角坐标和右下角坐标。

每个操作都要将选中的子矩阵中的每个元素的值加上 c。

请你将进行完所有操作后的矩阵输出。

**输入格式**

第一行包含整数 n,m,q。

接下来 n 行，每行包含 m 个整数，表示整数矩阵。

接下来 q 行，每行包含 5 个整数 x1,y1,x2,y2,c，表示一个操作。

**输出格式**

共 n 行，每行 m 个整数，表示所有操作进行完毕后的最终矩阵。

**数据范围**

1≤n,m≤1000,

1≤q≤100000,

1≤x1≤x2≤n,

1≤y1≤y2≤m,

−1000≤c≤1000,

−1000≤矩阵内元素的值≤1000

**输入样例**：

```cpp
3 4 3
1 2 2 1
3 2 2 1
1 1 1 1
1 1 2 2 1
1 3 2 3 2
3 1 3 4 1
```

**输出样例**：

```cpp
2 3 4 1
4 3 4 1
2 2 2 2
```

## 思路

**差分矩阵的原理**

假设有一个二维矩阵 `mat`，你需要对这个矩阵的某个子矩阵区域多次进行增加操作。直接更新会导致每次操作的时间复杂度和该子矩阵的大小成正比，当操作次数和矩阵大小都很大时，直接更新效率低下。

这时可以使用差分矩阵 `diff` 来优化。差分矩阵同样是二维的，其大小与原矩阵 `mat` 相同。差分矩阵的主要思想是记录变化（增量），而非直接改变矩阵 `mat` 的值。对差分矩阵的操作最终将被应用回原矩阵以反映所有的更新。

**如何操作差分矩阵**

1. **初始化**：
   - 差分矩阵 `diff` 初始化时，所有值都为 0。
2. **执行更新**：
   - 假设你要将子矩阵 `(x1, y1)` 到 `(x2, y2)` 中的所有元素增加值 `v`。
   - 更新 `diff[x1][y1]` 增加 `v` 表示从 `(x1, y1)` 开始，整个矩阵的元素都增加 `v`。
   - 更新 `diff[x1][y2+1]` 减少 `v` 表示从 `(x1, y2+1)` 开始，右侧矩阵列元素恢复原值。
   - 更新 `diff[x2+1][y1]` 减少 `v` 表示从 `(x2+1, y1)` 开始，下方矩阵行元素恢复原值。
   - 更新 `diff[x2+1][y2+1]` 增加 `v` 表示从 `(x2+1, y2+1)` 开始，右下角的重叠部分再次增加 `v`，从而修正过度减少的部分。
3. **构建最终矩阵**：
   - 通过累加 `diff` 矩阵的前缀和来构建最终矩阵 `mat`。这是通过对每一行和每一列分别累加来完成的，确保每个 `mat[i][j]` 反映了所有相关的 `diff` 更新。

## C++

```cpp
#include <iostream>

using namespace std;

const int N = 1010;
int arr[N][N];

void insert(int x1, int y1, int x2, int y2, int c) {
    arr[x1][y1] += c;
    arr[x2 + 1][y1] -= c;
    arr[x1][y2 + 1] -= c;
    arr[x2 + 1][y2 + 1] += c;
}

int main() {
    int n, m, q, tmp;
    scanf("%d%d%d", &n, &m, &q);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%d", &tmp);
            insert(i, j, i, j, tmp);
        }
    }
    while (q--) {
        int x1, y1, x2, y2, c;
        scanf("%d%d%d%d%d", &x1, &y1, &x2, &y2, &c);
        insert(x1, y1, x2, y2, c);
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            arr[i][j] += arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1];
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

```cpp
#include <iostream>

using namespace std;

const int N = 1010;

int n, m, q;
int a[N][N], b[N][N];

void insert(int x1, int y1, int x2, int y2, int c) {
    b[x1][y1] += c;
    b[x2 + 1][y1] -= c;
    b[x1][y2 + 1] -= c;
    b[x2 + 1][y2 + 1] += c;
}

int main() {
    scanf("%d%d%d", &n, &m, &q);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            scanf("%d", &a[i][j]);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            insert(i, j, i, j, a[i][j]);

    while (q--) {
        int x1, y1, x2, y2, c;
        cin >> x1 >> y1 >> x2 >> y2 >> c;
        insert(x1, y1, x2, y2, c);
    }

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            b[i][j] += b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1];

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) printf("%d ", b[i][j]);
        puts("");
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

func insert(arr [][]int, x1, y1, x2, y2, c int) {
	arr[x1][y1] += c
	arr[x1][y2+1] -= c
	arr[x2+1][y1] -= c
	arr[x2+1][y2+1] += c
}

func main() {
	var n, m, q, tmp int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n, &m, &q)
	arr := make([][]int, n+2)
	for i := 0; i <= n+1; i++ {
		arr[i] = make([]int, m+2)
	}
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			fmt.Fscan(reader, &tmp)
			insert(arr, i, j, i, j, tmp)
		}
	}
	for i := 1; i <= q; i++ {
		var x1, y1, x2, y2, c int
		fmt.Fscan(reader, &x1, &y1, &x2, &y2, &c)
		insert(arr, x1, y1, x2, y2, c)
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]
			fmt.Fprint(writer, arr[i][j], " ")
		}
		fmt.Fprintln(writer)
	}
}
```

## 模板

```cpp
给以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵中的所有元素加上c：
S[x1, y1] += c, S[x2 + 1, y1] -= c, S[x1, y2 + 1] -= c, S[x2 + 1, y2 + 1] += c
```

