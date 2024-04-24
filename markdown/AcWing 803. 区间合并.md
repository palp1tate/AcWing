# [AcWing 803. 区间合并](https://www.acwing.com/problem/content/805/)

## 题目描述

给定 n 个区间 [li,ri]，要求合并所有有交集的区间。

注意如果在端点处相交，也算有交集。

输出合并完成后的区间个数。

例如：\[1,3\]和 \[2,6\] 可以合并为一个区间\[1,6\]。

**输入格式**

第一行包含整数 n。

接下来 n 行，每行包含两个整数 l 和 r。

**输出格式**

共一行，包含一个整数，表示合并区间完成后的区间个数。

**数据范围**

1≤n≤100000,

−10^9≤li≤ri≤10^9

**输入样例**：

```cpp
5
1 2
2 4
5 6
7 8
7 9
```

**输出样例**：

```cpp
3
```

## C++

```cpp
//C++11版本

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Interval {
    long long Start;
    long long End;

    Interval(long long start, long long end) : Start(start), End(end) {};
};

bool compareIntervals(Interval &a, Interval &b) {
    return a.Start < b.Start;
};

vector<Interval> mergeIntervals(vector<Interval> &intervals) {
    if (intervals.empty()) return intervals;
    sort(intervals.begin(), intervals.end(), compareIntervals);
    vector<Interval> merged;
    Interval current = intervals[0];
    for (auto &interval: intervals) {
        if (interval.Start > current.End) {
            merged.push_back(current);
            current = interval;
        } else if (interval.End > current.End) current.End = interval.End;
    }
    merged.push_back(current);
    return merged;
}

int main() {
    int n, l, r;
    scanf("%d", &n);
    vector<Interval> intervals;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &l, &r);
        intervals.push_back(Interval(l, r));
    }
    vector<Interval> merged = mergeIntervals(intervals);
    printf("%d", merged.size());
}
```

```cpp
//C++98版本

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Interval {
    long long Start;
    long long End;

    Interval(long long start, long long end) : Start(start), End(end) {};
};

bool compareIntervals(Interval &a, Interval &b) {
    return a.Start < b.Start;
};

vector<Interval> mergeIntervals(vector<Interval> &intervals) {
    if (intervals.empty()) return intervals;
    sort(intervals.begin(), intervals.end(), compareIntervals);
    vector<Interval> merged;
    Interval current = intervals[0];
    for (size_t i = 0; i < intervals.size(); i++) {
        if (intervals[i].Start > current.End) {
            merged.push_back(current);
            current = intervals[i];
        } else if (intervals[i].End > current.End) current.End = intervals[i].End;
    }
    merged.push_back(current);
    return merged;
}

int main() {
    int n, l, r;
    scanf("%d", &n);
    vector<Interval> intervals;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &l, &r);
        Interval interval(l, r);
        intervals.push_back(interval);
    }
    vector<Interval> merged = mergeIntervals(intervals);
    printf("%d", merged.size());
}
```

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;

void merge(vector<PII> &segs) {
    vector<PII> res;

    sort(segs.begin(), segs.end());

    int st = -2e9, ed = -2e9;
    for (auto seg: segs)
        if (ed < seg.first) {
            if (st != -2e9) res.push_back({st, ed});
            st = seg.first, ed = seg.second;
        } else ed = max(ed, seg.second);

    if (st != -2e9) res.push_back({st, ed});

    segs = res;
}

int main() {
    int n;
    scanf("%d", &n);

    vector<PII> segs;
    for (int i = 0; i < n; i++) {
        int l, r;
        scanf("%d%d", &l, &r);
        segs.push_back({l, r});
    }

    merge(segs);

    cout << segs.size() << endl;

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

// Interval 定义了一个区间结构
type Interval struct {
	Start int64
	End   int64
}

// mergeIntervals 合并给定的区间列表
func mergeIntervals(intervals []Interval) []Interval {
	if len(intervals) == 0 {
		return intervals
	}

	// 按照区间的起始位置进行排序
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})

	var merged []Interval
	current := intervals[0]

	for _, interval := range intervals {
		if interval.Start > current.End {
			// 如果当前区间的起始位置在前一个区间的结束位置之后，没有重叠
			merged = append(merged, current)
			current = interval
		} else if interval.End > current.End {
			// 如果有重叠，合并区间
			current.End = interval.End
		}
	}
	// 添加最后一个区间
	merged = append(merged, current)
	return merged
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(line))

	intervals := make([]Interval, n)
	for i := 0; i < n; i++ {
		line, _ = reader.ReadString('\n')
		parts := strings.Fields(line)
		start, _ := strconv.ParseInt(parts[0], 10, 64)
		end, _ := strconv.ParseInt(parts[1], 10, 64)
		intervals[i] = Interval{Start: start, End: end}
	}

	mergedIntervals := mergeIntervals(intervals)
	writer.WriteString(strconv.Itoa(len(mergedIntervals)))
}
```

## 模板

```cpp
// 将所有存在交集的区间合并
void merge(vector<PII> &segs)
{
    vector<PII> res;

    sort(segs.begin(), segs.end());

    int st = -2e9, ed = -2e9;
    for (auto seg : segs)
        if (ed < seg.first)
        {
            if (st != -2e9) res.push_back({st, ed});
            st = seg.first, ed = seg.second;
        }
        else ed = max(ed, seg.second);

    if (st != -2e9) res.push_back({st, ed});

    segs = res;
}
```

