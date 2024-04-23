# [AcWing 802. 区间和](https://www.acwing.com/problem/content/804/) 

## 题目描述

假定有一个无限长的数轴，数轴上每个坐标上的数都是 0。

现在，我们首先进行 n 次操作，每次操作将某一位置 x 上的数加 c。

接下来，进行 m 次询问，每个询问包含两个整数 l 和 r，你需要求出在区间 [l,r] 之间的所有数的和。

**输入格式**

第一行包含两个整数 n 和 m。

接下来 n 行，每行包含两个整数 x 和 c。

再接下来 m 行，每行包含两个整数 l 和 r。

**输出格式**

共 m 行，每行输出一个询问中所求的区间内数字和。

**数据范围**

−10^9≤x≤10^9,

1≤n,m≤10^5,

−10^9≤l≤r≤10^9,

−10000≤c≤10000

**输入样例**：

```cpp
3 3
1 2
3 6
7 5
1 3
4 6
7 8
```

**输出样例**：

```cpp
8
0
5
```

## C++

```cpp
//C++98版本
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

// 二分搜索函数，用于找到第一个大于或等于x的元素的索引
int getIndex(const vector<long long> &coords, long long x) {
    int l = 0, r = coords.size();
    while (l < r) {
        int mid = (l + r) >> 1;
        if (coords[mid] >= x) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    map<long long, long long> coordsMap;
    long long x, c;

    // 读取坐标和计数
    for (int i = 0; i < n; ++i) {
        scanf("%lld %lld", &x, &c);
        coordsMap[x] += c;
    }

    vector<long long> coords;
    for (map<long long, long long>::iterator it = coordsMap.begin(); it != coordsMap.end(); ++it) {
        coords.push_back(it->first);
    }

    // 对坐标进行排序
    sort(coords.begin(), coords.end());

    // 前缀和数组
    vector<long long> s(coords.size() + 1, 0);
    for (size_t i = 0; i < coords.size(); ++i) {
        s[i + 1] = s[i] + coordsMap[coords[i]];
    }

    // 处理查询
    for (int i = 0; i < m; ++i) {
        long long l, r;
        scanf("%lld %lld", &l, &r);
        int lIdx = getIndex(coords, l);
        int rIdx = getIndex(coords, r);
        if (rIdx == coords.size() || coords[rIdx] > r) {
            rIdx--;
        }
        long long sum = s[rIdx + 1] - s[lIdx];
        printf("%lld\n", sum);
    }

    return 0;
}
```

```cpp
//C++11版本
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

// 二分搜索函数，用于找到第一个大于或等于 x 的元素的索引
int getIndex(const vector<long long> &coords, long long x) {
    int l = 0, r = coords.size();
    while (l < r) {
        int mid = (l + r) >> 1;
        if (coords[mid] >= x) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    map<long long, long long> coordsMap;
    long long x, c;

    // 读取坐标和对应的计数
    for (int i = 0; i < n; ++i) {
        scanf("%lld %lld", &x, &c);
        coordsMap[x] += c;
    }

    vector<long long> coords;
    // 利用 auto 和基于范围的 for 循环简化迭代
    for (const auto &entry: coordsMap) {
        coords.push_back(entry.first);
    }

    // 对坐标进行排序
    sort(coords.begin(), coords.end());

    // 创建前缀和数组
    vector<long long> s(coords.size() + 1);
    for (size_t i = 0; i < coords.size(); ++i) {
        s[i + 1] = s[i] + coordsMap[coords[i]];
    }

    // 处理查询
    for (int i = 0; i < m; ++i) {
        long long l, r;
        scanf("%lld %lld", &l, &r);
        int lIdx = getIndex(coords, l);
        int rIdx = getIndex(coords, r);
        if (rIdx == coords.size() || coords[rIdx] > r) {
            rIdx--;
        }
        long long sum = s[rIdx + 1] - s[lIdx];
        printf("%lld\n", sum);
    }

    return 0;
}
```

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;

const int N = 300010;

int n, m;
int a[N], s[N];

vector<int> alls;
vector<PII> add, query;

int find(int x) {
    int l = 0, r = alls.size() - 1;
    while (l < r) {
        int mid = l + r >> 1;
        if (alls[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return r + 1;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int x, c;
        cin >> x >> c;
        add.push_back({x, c});

        alls.push_back(x);
    }

    for (int i = 0; i < m; i++) {
        int l, r;
        cin >> l >> r;
        query.push_back({l, r});

        alls.push_back(l);
        alls.push_back(r);
    }

    // 去重
    sort(alls.begin(), alls.end());
    alls.erase(unique(alls.begin(), alls.end()), alls.end());

    // 处理插入
    for (auto item: add) {
        int x = find(item.first);
        a[x] += item.second;
    }

    // 预处理前缀和
    for (int i = 1; i <= alls.size(); i++) s[i] = s[i - 1] + a[i];

    // 处理询问
    for (auto item: query) {
        int l = find(item.first), r = find(item.second);
        cout << s[r] - s[l - 1] << endl;
    }

    return 0;
}
```

## Go

```go
package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

func getIndex(coords []int64, x int64) int {
	l, r := 0, len(coords)
	for l < r {
		mid := (l + r) >> 1
		if coords[mid] >= x {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	line, _ := reader.ReadString('\n')
	params := strings.Fields(line)
	n, _ := strconv.Atoi(params[0])
	m, _ := strconv.Atoi(params[1])

	coordsMap := make(map[int64]int64)

	for i := 0; i < n; i++ {
		line, _ = reader.ReadString('\n')
		params = strings.Fields(line)
		x, _ := strconv.ParseInt(params[0], 10, 64)
		c, _ := strconv.ParseInt(params[1], 10, 64)
		coordsMap[x] += c
	}

	coords := make([]int64, 0, len(coordsMap))
	for k := range coordsMap {
		coords = append(coords, k)
	}
	sort.Slice(coords, func(i, j int) bool { return coords[i] < coords[j] })

	s := make([]int64, len(coords)+1)
	for i, x := range coords {
		s[i+1] = s[i] + coordsMap[x]
	}

	for i := 0; i < m; i++ {
		line, _ = reader.ReadString('\n')
		params = strings.Fields(line)
		l, _ := strconv.ParseInt(params[0], 10, 64)
		r, _ := strconv.ParseInt(params[1], 10, 64)
		lIdx := getIndex(coords, l)
		rIdx := getIndex(coords, r)
		if rIdx == len(coords) || coords[rIdx] > r {
			rIdx--
		}
		sum := s[rIdx+1] - s[lIdx]
		writer.WriteString(strconv.FormatInt(sum, 10) + "\n")
	}
}
```

## 模板

```cpp
vector<int> alls; // 存储所有待离散化的值
sort(alls.begin(), alls.end()); // 将所有值排序
alls.erase(unique(alls.begin(), alls.end()), alls.end());   // 去掉重复元素

// 二分求出x对应的离散化的值
int find(int x) // 找到第一个大于等于x的位置
{
    int l = 0, r = alls.size() - 1;
    while (l < r)
    {
        int mid = l + r >> 1;
        if (alls[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return r + 1; // 映射到1, 2, ...n
}
```

