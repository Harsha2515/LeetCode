class Solution {
public:
    struct Result {
        long long score;
        vector<int> indices;
    };

    vector<int> starts;
    vector<vector<Result>> dp;
    vector<vector<bool>> visited;

    Result solve(int i, int k, vector<vector<int>>& intervals) {
        int n = intervals.size();

        if (i >= n || k == 0) {
            return {0, {}};
        }

        if (visited[i][k]) {
            return dp[i][k];
        }

        visited[i][k] = true;

        // Option 1: Don't take this interval
        Result skip = solve(i + 1, k, intervals);

        // Find first interval whose start > current end
        int next = upper_bound(
            starts.begin(),
            starts.end(),
            intervals[i][1]
        ) - starts.begin();

        // Option 2: Take this interval
        Result take = solve(next, k - 1, intervals);

        take.score += (long long)intervals[i][2];
        take.indices.push_back(intervals[i][3]);

        // Indices must be sorted for lexicographical comparison
        sort(take.indices.begin(), take.indices.end());

        // Choose the better result
        if (take.score > skip.score) {
            dp[i][k] = take;
        }
        else if (take.score < skip.score) {
            dp[i][k] = skip;
        }
        else {
            // Same score -> lexicographically smaller indices
            if (take.indices < skip.indices)
                dp[i][k] = take;
            else
                dp[i][k] = skip;
        }

        return dp[i][k];
    }

    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();

        // Add original index
        for (int i = 0; i < n; i++) {
            intervals[i].push_back(i);
        }

        // Sort by left endpoint
        sort(intervals.begin(), intervals.end());

        // Store all left endpoints
        starts.resize(n);

        for (int i = 0; i < n; i++) {
            starts[i] = intervals[i][0];
        }

        // At most 4 intervals
        dp.resize(n, vector<Result>(5));
        visited.resize(n, vector<bool>(5, false));

        return solve(0, 4, intervals).indices;
    }
};