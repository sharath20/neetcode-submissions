public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        var res = new Dictionary<int,int>();

        for(int i =0; i < nums.Length ; i ++) {
            int diff = target - nums[i];
            if(res.ContainsKey(diff)) {
                return new int[]{res[diff],i};
            }
            res.Add(nums[i],i);
        }
        return new int[0];
    }
}
