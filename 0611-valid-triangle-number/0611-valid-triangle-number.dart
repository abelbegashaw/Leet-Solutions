class Solution {
  int triangleNumber(List<int> nums) {

    int result = 0;
    nums.sort();
    for(int i = 0; i < nums.length; i++) {
        for(int j = i + 1; j < nums.length; j++) {
            for(int k = j + 1; k < nums.length; k++) {
                if(nums[i] + nums[j] > nums[k]) {
                    result++;
                }
            }
        }
    }
    return result;
  }
}