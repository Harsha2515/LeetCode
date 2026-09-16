class Solution {
public:
    int numberOfSets(int n, int k) {
        const long long MOD = 1e9 + 7;

        vector<vector<long long>> dp(n, vector<long long>(k + 1, 0));

        // dp[i][j] = number of ways to make j segments
        // using points 0...i
        //
        // Initially, choosing 0 segments is always possible.
        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
        }

        for (int j = 1; j <= k; j++) {
            long long prefix = 0;

            for (int i = 1; i < n; i++) {

                // dp[i-1][j] :
                // don't use point i as the endpoint of a new segment
                //
                // prefix contains possibilities for starting
                // the last segment.
                prefix = (prefix + dp[i - 1][j - 1]) % MOD;

                dp[i][j] = (dp[i - 1][j] + prefix) % MOD;
            }
        }

        return dp[n - 1][k];
    }
};