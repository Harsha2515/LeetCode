class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> result(k, 0);
        vector<long long> dp(k, 0);

        for (int a : nums) {
            vector<long long> newdp(k, 0);

            // Start a new subarray [a]
            newdp[a % k]++;

            // Extend all previous subarrays
            for (int r = 0; r < k; r++) {
                if (dp[r] > 0) {
                    int newRemainder = (long long)r * (a % k) % k;
                    newdp[newRemainder] += dp[r];
                }
            }

            // Add all subarrays ending at current position
            for (int r = 0; r < k; r++) {
                result[r] += newdp[r];
            }

            dp = newdp;
        }

        return result;
    }
};