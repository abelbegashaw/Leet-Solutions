/**
 * @param {string} s
 * @return {number}
 */
var distinctSubseqII = function(s) {
    const MOD = 10**9 + 7
    let dp = Array.from({length: s.length}, () => 1);
    let last = new Map([[s[0], 0]]);
    for(let i = 1; i < s.length; i++) {
        if (last.has(s[i])) {
            let index = last.get(s[i]);
            let decrement = index == 0 ? 0 : dp[index - 1];
            dp[i] = (dp[i - 1] * 2 - decrement) % MOD;
        } else {
            dp[i] = (dp[i - 1] * 2 + 1) % MOD
        }
        last.set(s[i], i)
    };
    return (dp.at(-1) % MOD + MOD) % MOD; 

};