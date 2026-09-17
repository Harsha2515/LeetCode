class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        const int INF = 1e9;

        vector<int> best(n, INF);

        int left = 0;
        int sum = 0;
        int ans = INF;

        for (int right = 0; right < n; right++) {
            sum += arr[right];

            // Shrink window if sum becomes greater than target
            while (sum > target && left <= right) {
                sum -= arr[left++];
            }

            // Found a subarray [left ... right]
            if (sum == target) {
                int len = right - left + 1;

                // Combine with the best subarray before 'left'
                if (left > 0 && best[left - 1] != INF) {
                    ans = min(ans, best[left - 1] + len);
                }

                // This is the best single subarray ending at/before right
                if (right == 0)
                    best[right] = len;
                else
                    best[right] = min(best[right - 1], len);
            } 
            else {
                // No new valid subarray ending at right
                if (right > 0)
                    best[right] = best[right - 1];
            }
        }

        return ans == INF ? -1 : ans;
    }
};